from pathlib import Path
import re
from collections import defaultdict


BASE_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = BASE_DIR / "logs" / "auth_sample.log"

ALERT_THRESHOLD = 3
HIGH_SEVERITY_THRESHOLD = 6


FAILED_PATTERN = re.compile(
    r"Failed password for (?P<user>\S+) "
    r"from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)


def read_log_file(file_path):
    if not file_path.exists():
        raise FileNotFoundError("No se encontró logs/auth_sample.log.")

    with file_path.open("r", encoding="utf-8") as log_file:
        return log_file.readlines()


def analyze_failed_logins(lines):
    failed_attempts_by_ip = defaultdict(int)
    targeted_users_by_ip = defaultdict(set)

    for line in lines:
        match = FAILED_PATTERN.search(line)

        if match is None:
            continue

        ip = match.group("ip")
        user = match.group("user")

        failed_attempts_by_ip[ip] += 1
        targeted_users_by_ip[ip].add(user)

    return failed_attempts_by_ip, targeted_users_by_ip


def classify_severity(attempts):
    if attempts >= HIGH_SEVERITY_THRESHOLD:
        return "Alta"

    if attempts >= ALERT_THRESHOLD:
        return "Media"

    return "Baja"


def print_summary(failed_attempts_by_ip, targeted_users_by_ip):
    print("\n=== BASELINE: INTENTOS FALLIDOS POR IP ===\n")

    if not failed_attempts_by_ip:
        print("No se detectaron intentos fallidos.")
        return

    ordered_results = sorted(
        failed_attempts_by_ip.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    for ip, attempts in ordered_results:
        users = ", ".join(sorted(targeted_users_by_ip[ip]))
        severity = classify_severity(attempts)

        print(f"IP origen: {ip}")
        print(f"Intentos fallidos: {attempts}")
        print(f"Usuarios objetivo: {users}")
        print(f"Severidad: {severity}")

        if attempts >= ALERT_THRESHOLD:
            print("Clasificación: Posible alerta de fuerza bruta")
        else:
            print("Clasificación: Evento de autenticación fallida")

        print("-" * 50)


def main():
    print("SOC Junior Lab - Baseline de autenticación SSH")

    try:
        lines = read_log_file(LOG_FILE)
    except (OSError, UnicodeError):
        print("[ERROR] No fue posible leer logs/auth_sample.log.")
        return

    failed_attempts_by_ip, targeted_users_by_ip = analyze_failed_logins(lines)

    print_summary(
        failed_attempts_by_ip,
        targeted_users_by_ip,
    )


if __name__ == "__main__":
    main()