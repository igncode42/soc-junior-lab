import argparse
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


FAILED_PATTERN = re.compile(
    r"Failed password for (?P<user>\S+) "
    r"from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)

ACCEPTED_PATTERN = re.compile(
    r"Accepted password for (?P<user>\S+) "
    r"from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def display_path(file_path):
    """Devuelve una ruta segura para mostrar sin exponer rutas locales."""
    path = Path(file_path)
    resolved = path.resolve()

    try:
        return resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return path.name


def positive_integer(value):
    try:
        number = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(
            "El umbral debe ser un número entero."
        ) from error

    if number < 1:
        raise argparse.ArgumentTypeError(
            "El umbral debe ser mayor o igual a 1."
        )

    return number


def markdown_path(value):
    file_path = Path(value)

    if file_path.suffix.lower() != ".md":
        raise argparse.ArgumentTypeError(
            "El reporte debe utilizar la extensión .md."
        )

    return file_path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analiza logs SSH simulados."
    )

    parser.add_argument(
        "log_file",
        type=Path,
        help="Ruta del archivo de log que se analizará."
    )

    parser.add_argument(
        "--threshold",
        type=positive_integer,
        default=3,
        metavar="N",
        help=(
            "Cantidad mínima de fallos utilizada como umbral para "
            "priorización y correlación. Valor predeterminado: 3."
        )
    )

    parser.add_argument(
        "--report",
        type=markdown_path,
        default=Path("reports/soc-analysis-report.md"),
        metavar="RUTA",
        help=(
            "Ruta del reporte Markdown que se generará. "
            "Valor predeterminado: reports/soc-analysis-report.md."
        )
    )

    return parser.parse_args()


def read_log_file(file_path):
    if not file_path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {display_path(file_path)}"
        )

    if not file_path.is_file():
        raise IsADirectoryError(
            "La ruta no corresponde a un archivo: "
            f"{display_path(file_path)}"
        )

    with file_path.open("r", encoding="utf-8") as log_file:
        return log_file.readlines()


def parse_log_line(line):
    failed_match = FAILED_PATTERN.search(line)

    if failed_match:
        return {
            "event_type": "failed",
            "user": failed_match.group("user"),
            "ip": failed_match.group("ip"),
        }

    accepted_match = ACCEPTED_PATTERN.search(line)

    if accepted_match:
        return {
            "event_type": "accepted",
            "user": accepted_match.group("user"),
            "ip": accepted_match.group("ip"),
        }

    return None


def parse_log_lines(lines):
    events = []

    for line_number, line in enumerate(lines, start=1):
        event = parse_log_line(line)

        if event is None:
            continue

        event["line_number"] = line_number
        events.append(event)

    return events


def summarize_failed_attempts(events):
    failed_attempts_by_ip = defaultdict(int)
    targeted_users_by_ip = defaultdict(set)
    failed_attempts_by_ip_and_user = defaultdict(int)

    for event in events:
        if event["event_type"] != "failed":
            continue

        ip = event["ip"]
        user = event["user"]

        failed_attempts_by_ip[ip] += 1
        targeted_users_by_ip[ip].add(user)
        failed_attempts_by_ip_and_user[(ip, user)] += 1

    return (
        failed_attempts_by_ip,
        targeted_users_by_ip,
        failed_attempts_by_ip_and_user,
    )


def detect_possible_compromises(events, threshold):
    pending_failures = {}
    possible_incidents = []

    for event in events:
        pair = (event["ip"], event["user"])

        if event["event_type"] == "failed":
            state = pending_failures.setdefault(
                pair,
                {
                    "count": 0,
                    "first_failed_line": event["line_number"],
                },
            )

            state["count"] += 1
            continue

        state = pending_failures.pop(pair, None)

        if state is None or state["count"] < threshold:
            continue

        possible_incidents.append(
            {
                "ip": event["ip"],
                "user": event["user"],
                "failed_attempts_before_success": state["count"],
                "first_failed_line": state["first_failed_line"],
                "success_line": event["line_number"],
            }
        )

    return possible_incidents


def classify_severity(
    attempts,
    threshold,
    has_possible_compromise=False,
):
    if has_possible_compromise or attempts >= threshold * 2:
        return "Alta"

    if attempts >= threshold:
        return "Media"

    return "Baja"


def build_ip_findings(
    failed_attempts_by_ip,
    targeted_users_by_ip,
    failed_attempts_by_ip_and_user,
    threshold,
    possible_incidents,
):
    incident_ips = {
        incident["ip"]
        for incident in possible_incidents
    }

    findings = []

    for ip, attempts in sorted(
        failed_attempts_by_ip.items(),
        key=lambda item: (-item[1], item[0]),
    ):
        targeted_users = sorted(
            targeted_users_by_ip[ip]
        )

        has_possible_compromise = (
            ip in incident_ips
        )

        findings.append(
            {
                "ip": ip,
                "failed_attempts": attempts,
                "severity": classify_severity(
                    attempts,
                    threshold,
                    has_possible_compromise,
                ),
                "targeted_users": targeted_users,
                "attempts_by_user": {
                    user: failed_attempts_by_ip_and_user[
                        (ip, user)
                    ]
                    for user in targeted_users
                },
                "has_possible_compromise": (
                    has_possible_compromise
                ),
            }
        )

    return findings


def calculate_overall_risk(
    findings,
    possible_incidents,
):
    if possible_incidents:
        return "ALTO"

    if any(
        finding["severity"] == "Alta"
        for finding in findings
    ):
        return "ALTO"

    if any(
        finding["severity"] == "Media"
        for finding in findings
    ):
        return "MEDIO"

    return "BAJO"


def build_analysis_summary(
    total_lines,
    events,
    findings,
    possible_incidents,
):
    recognized_events = len(events)

    return {
        "processed_lines": total_lines,
        "recognized_events": recognized_events,
        "ignored_lines": (
            total_lines - recognized_events
        ),
        "failed_events": sum(
            event["event_type"] == "failed"
            for event in events
        ),
        "accepted_events": sum(
            event["event_type"] == "accepted"
            for event in events
        ),
        "observed_ips": len(
            {
                event["ip"]
                for event in events
            }
        ),
        "prioritized_alerts": sum(
            finding["severity"]
            in {"Media", "Alta"}
            for finding in findings
        ),
        "possible_compromises": len(
            possible_incidents
        ),
    }


def build_operational_recommendation(
    overall_risk,
    possible_incidents,
):
    if possible_incidents:
        return (
            "Prioridad alta: validar la legitimidad "
            "de los accesos correlacionados, revisar "
            "la actividad posterior y considerar "
            "medidas de contención si aparece "
            "evidencia adicional."
        )

    if overall_risk == "ALTO":
        return (
            "Prioridad alta: investigar las IP con "
            "mayor volumen, revisar las cuentas "
            "objetivo y evaluar controles adicionales "
            "contra intentos repetidos de autenticación."
        )

    if overall_risk == "MEDIO":
        return (
            "Prioridad media: revisar los orígenes "
            "que alcanzaron el umbral y mantener "
            "seguimiento de nueva actividad."
        )

    return (
        "Prioridad baja: mantener monitoreo y "
        "conservar la evidencia para detectar "
        "cambios en el comportamiento."
    )


def build_markdown_report(
    source_path,
    threshold,
    summary,
    findings,
    possible_incidents,
    overall_risk,
    recommendation,
):
    generated_at = (
        datetime.now()
        .astimezone()
        .strftime("%Y-%m-%d %H:%M:%S %z")
    )

    lines = [
        "# SOC Log Analyzer — Reporte de análisis SSH",
        "",
        "## Metadatos",
        "",
        f"- **Fecha de generación:** {generated_at}",
        (
            "- **Archivo analizado:** "
            f"`{display_path(source_path)}`"
        ),
        f"- **Umbral configurado:** {threshold}",
        "- **Estado del análisis:** Completado",
        "",
        "## Resumen ejecutivo",
        "",
        "| Métrica | Resultado |",
        "|---|---:|",
        (
            "| Líneas procesadas | "
            f"{summary['processed_lines']} |"
        ),
        (
            "| Eventos reconocidos | "
            f"{summary['recognized_events']} |"
        ),
        (
            "| Líneas ignoradas | "
            f"{summary['ignored_lines']} |"
        ),
        (
            "| Intentos fallidos | "
            f"{summary['failed_events']} |"
        ),
        (
            "| Accesos exitosos | "
            f"{summary['accepted_events']} |"
        ),
        (
            "| IPs observadas | "
            f"{summary['observed_ips']} |"
        ),
        (
            "| Alertas priorizadas | "
            f"{summary['prioritized_alerts']} |"
        ),
        (
            "| Posibles compromisos | "
            f"{summary['possible_compromises']} |"
        ),
        "",
        "## Evaluación general",
        "",
        (
            "**Riesgo general estimado:** "
            f"`{overall_risk}`"
        ),
        "",
        (
            f"Política aplicada: severidad Media "
            f"desde {threshold} fallos y Alta desde "
            f"{threshold * 2} fallos o cuando existe "
            "un posible compromiso correlacionado. "
            "La severidad Crítica queda reservada "
            "para compromiso confirmado o impacto grave."
        ),
        "",
        "## Hallazgos priorizados por IP",
        "",
    ]

    if not findings:
        lines.extend(
            [
                "No se detectaron intentos fallidos.",
                "",
            ]
        )

    for position, finding in enumerate(
        findings,
        start=1,
    ):
        compromise_status = (
            "Sí"
            if finding["has_possible_compromise"]
            else "No"
        )

        lines.extend(
            [
                (
                    f"### {position}. "
                    f"[{finding['severity'].upper()}] "
                    f"`{finding['ip']}`"
                ),
                "",
                (
                    "- **Intentos fallidos:** "
                    f"{finding['failed_attempts']}"
                ),
                (
                    "- **Usuarios objetivo:** "
                    + ", ".join(
                        f"`{user}`"
                        for user
                        in finding["targeted_users"]
                    )
                ),
                (
                    "- **Posible compromiso "
                    "relacionado:** "
                    f"{compromise_status}"
                ),
                "",
                "#### Detalle por usuario",
                "",
                "| Usuario | Intentos fallidos |",
                "|---|---:|",
            ]
        )

        for user, attempts in (
            finding["attempts_by_user"].items()
        ):
            lines.append(
                f"| `{user}` | {attempts} |"
            )

        lines.append("")

    lines.extend(
        [
            "## Posibles compromisos de cuenta",
            "",
        ]
    )

    if not possible_incidents:
        lines.extend(
            [
                (
                    "No se detectaron accesos exitosos "
                    "posteriores a un número de fallos "
                    "igual o superior al umbral para "
                    "la misma combinación de IP y usuario."
                ),
                "",
            ]
        )

    for position, incident in enumerate(
        possible_incidents,
        start=1,
    ):
        lines.extend(
            [
                (
                    f"### {position}. "
                    "[ALTA] Posible compromiso"
                ),
                "",
                (
                    "- **IP de origen:** "
                    f"`{incident['ip']}`"
                ),
                (
                    "- **Usuario:** "
                    f"`{incident['user']}`"
                ),
                (
                    "- **Fallos previos al acceso:** "
                    f"{incident[
                        'failed_attempts_before_success'
                    ]}"
                ),
                (
                    "- **Secuencia de líneas:** "
                    f"{incident['first_failed_line']} "
                    f"→ {incident['success_line']}"
                ),
                "- **Compromiso confirmado:** No",
                (
                    "- **Evaluación:** acceso exitoso "
                    "posterior a múltiples fallos desde "
                    "la misma IP contra el mismo usuario."
                ),
                "",
            ]
        )

    lines.extend(
        [
            "## Recomendación operativa",
            "",
            recommendation,
            "",
            "## Limitaciones",
            "",
            (
                "- La severidad y el riesgo se basan "
                "en una política simplificada para "
                "este laboratorio."
            ),
            (
                "- El análisis trabaja con logs "
                "SSH simulados."
            ),
            (
                "- El análisis no utiliza timestamps "
                "para construir ventanas temporales."
            ),
            (
                "- No se considera la criticidad real "
                "del activo o de la cuenta."
            ),
            (
                "- No se consulta reputación, "
                "geolocalización ni inteligencia "
                "de amenazas."
            ),
            (
                "- No se analiza actividad posterior "
                "dentro de una sesión."
            ),
            (
                "- Un posible compromiso representa "
                "una señal para investigar, no una "
                "confirmación definitiva."
            ),
            "",
            "## Conclusión",
            "",
            (
                "El análisis convirtió eventos SSH "
                "simulados en hallazgos estructurados, "
                "priorizó actividad por severidad y "
                "correlacionó intentos fallidos con "
                "accesos exitosos posteriores utilizando "
                "la combinación de IP y usuario."
            ),
            "",
            (
                "Las detecciones representan señales "
                "para investigación y no confirman "
                "automáticamente un compromiso."
            ),
            "",
        ]
    )

    return "\n".join(lines)


def write_markdown_report(
    report_path,
    report_content,
):
    report_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with report_path.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as report_file:
        report_file.write(report_content)


def print_analysis_header(
    file_path,
    threshold,
    report_path,
):
    print("\n" + "=" * 60)
    print("SOC LOG ANALYZER")
    print("=" * 60)
    print(
        f"Archivo: {display_path(file_path)}"
    )
    print(
        f"Umbral configurado: {threshold}"
    )
    print(
        "Reporte Markdown: "
        f"{display_path(report_path)}"
    )
    print("Estado del análisis: COMPLETADO")


def print_executive_summary(
    summary,
    overall_risk,
):
    print("\n=== RESUMEN EJECUTIVO ===")

    print(
        "Líneas procesadas: "
        f"{summary['processed_lines']}"
    )

    print(
        "Eventos reconocidos: "
        f"{summary['recognized_events']}"
    )

    print(
        "Líneas ignoradas: "
        f"{summary['ignored_lines']}"
    )

    print(
        "Intentos fallidos: "
        f"{summary['failed_events']}"
    )

    print(
        "Accesos exitosos: "
        f"{summary['accepted_events']}"
    )

    print(
        "IPs observadas: "
        f"{summary['observed_ips']}"
    )

    print(
        "Alertas priorizadas: "
        f"{summary['prioritized_alerts']}"
    )

    print(
        "Posibles compromisos: "
        f"{summary['possible_compromises']}"
    )

    print(
        f"Riesgo general estimado: {overall_risk}"
    )


def print_ip_findings(
    findings,
    threshold,
):
    print(
        "\n=== HALLAZGOS PRIORIZADOS POR IP ==="
    )

    print(
        f"Política: Media desde {threshold} fallos; "
        f"Alta desde {threshold * 2} o por "
        "posible compromiso.\n"
    )

    if not findings:
        print(
            "No se detectaron intentos fallidos."
        )
        return

    for position, finding in enumerate(
        findings,
        start=1,
    ):
        print(
            f"{position}. "
            f"[{finding['severity'].upper()}] "
            f"{finding['ip']}"
        )

        print(
            "   Intentos fallidos: "
            f"{finding['failed_attempts']}"
        )

        print(
            "   Usuarios objetivo: "
            f"{', '.join(finding['targeted_users'])}"
        )

        print("   Detalle por usuario:")

        for user, attempts in (
            finding["attempts_by_user"].items()
        ):
            print(
                f"      - {user}: {attempts}"
            )

        compromise_status = (
            "Sí"
            if finding["has_possible_compromise"]
            else "No"
        )

        print(
            "   Posible compromiso relacionado: "
            f"{compromise_status}"
        )

        print("-" * 60)


def print_possible_compromises(
    possible_incidents,
    threshold,
):
    print(
        "\n=== POSIBLES COMPROMISOS DE CUENTA ==="
    )

    print(
        f"Umbral aplicado: {threshold}\n"
    )

    if not possible_incidents:
        print(
            "No se detectaron accesos exitosos "
            "posteriores a un número de fallos "
            "igual o superior al umbral para "
            "la misma IP y usuario."
        )
        return

    for position, incident in enumerate(
        possible_incidents,
        start=1,
    ):
        print(
            f"{position}. [ALTA] Posible compromiso"
        )

        print(
            f"   IP origen: {incident['ip']}"
        )

        print(
            f"   Usuario: {incident['user']}"
        )

        print(
            "   Fallos previos al acceso: "
            f"{incident[
                'failed_attempts_before_success'
            ]}"
        )

        print(
            "   Secuencia de líneas: "
            f"{incident['first_failed_line']} "
            f"→ {incident['success_line']}"
        )

        print(
            "   Evaluación: acceso exitoso posterior "
            "a múltiples fallos desde la misma IP "
            "contra el mismo usuario."
        )

        print(
            "   Compromiso confirmado: No"
        )

        print("-" * 60)


def print_operational_recommendation(
    recommendation,
):
    print(
        "\n=== RECOMENDACIÓN OPERATIVA ==="
    )

    print(recommendation)


def main():
    args = parse_arguments()

    try:
        lines = read_log_file(
            args.log_file
        )
    except (OSError, UnicodeError) as error:
        print(
            f"[ERROR] {error}"
        )
        return

    events = parse_log_lines(lines)

    (
        failed_attempts_by_ip,
        targeted_users_by_ip,
        failed_attempts_by_ip_and_user,
    ) = summarize_failed_attempts(events)

    possible_incidents = (
        detect_possible_compromises(
            events,
            args.threshold,
        )
    )

    findings = build_ip_findings(
        failed_attempts_by_ip,
        targeted_users_by_ip,
        failed_attempts_by_ip_and_user,
        args.threshold,
        possible_incidents,
    )

    overall_risk = calculate_overall_risk(
        findings,
        possible_incidents,
    )

    summary = build_analysis_summary(
        len(lines),
        events,
        findings,
        possible_incidents,
    )

    recommendation = (
        build_operational_recommendation(
            overall_risk,
            possible_incidents,
        )
    )

    report_content = build_markdown_report(
        args.log_file,
        args.threshold,
        summary,
        findings,
        possible_incidents,
        overall_risk,
        recommendation,
    )

    try:
        write_markdown_report(
            args.report,
            report_content,
        )
    except OSError as error:
        print(
            "[ERROR] No se pudo escribir "
            f"el reporte: {error}"
        )
        return

    print_analysis_header(
        args.log_file,
        args.threshold,
        args.report,
    )

    print_executive_summary(
        summary,
        overall_risk,
    )

    print_ip_findings(
        findings,
        args.threshold,
    )

    print_possible_compromises(
        possible_incidents,
        args.threshold,
    )

    print_operational_recommendation(
        recommendation
    )

    print(
        "\nReporte generado correctamente en: "
        f"{display_path(args.report)}"
    )

    print(
        "Análisis finalizado correctamente.\n"
    )


if __name__ == "__main__":
    main()