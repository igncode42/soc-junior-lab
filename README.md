# SOC Junior Lab

Laboratorio defensivo orientado a practicar fundamentos de Security Operations mediante análisis de logs, detección de actividad sospechosa, correlación básica, clasificación de severidad y documentación técnica.

El proyecto utiliza exclusivamente escenarios y datos simulados con fines educativos.

---

## Navegación rápida

| Área | Recurso |
|---|---|
| 🐍 Analizador principal | [`scripts/soc_log_analyzer.py`](scripts/soc_log_analyzer.py) |
| 🐍 Baseline Python | [`scripts/detectar_login_fallidos.py`](scripts/detectar_login_fallidos.py) |
| 📄 Log sintético | [`logs/auth_sample.log`](logs/auth_sample.log) |
| 📊 Reporte automático | [`reports/soc-analysis-report.md`](reports/soc-analysis-report.md) |
| 🔐 Caso SSH | [`cases/02-fuerza-bruta-ssh.md`](cases/02-fuerza-bruta-ssh.md) |
| 🎣 Caso Phishing | [`cases/01-phishing.md`](cases/01-phishing.md) |
| 📘 Runbook SSH | [`docs/03-runbook-analisis-alerta.md`](docs/03-runbook-analisis-alerta.md) |
| 📘 Runbook Phishing | [`docs/04-runbook-phishing.md`](docs/04-runbook-phishing.md) |
| 📚 Glosario SOC | [`docs/02-glosario-soc-junior.md`](docs/02-glosario-soc-junior.md) |

---

## Objetivo

Aplicar un flujo básico y reproducible de análisis defensivo:

```text
evidencia
↓
parsing
↓
análisis
↓
detección
↓
correlación
↓
clasificación
↓
priorización
↓
documentación
```

El laboratorio busca desarrollar habilidades prácticas relacionadas con roles iniciales de SOC y operaciones de seguridad.

---

## Habilidades trabajadas

- Análisis manual de logs.
- Autenticación SSH.
- Identificación de actividad sospechosa.
- Detección de múltiples fallos de autenticación.
- Correlación básica de eventos.
- Análisis inicial de phishing.
- Clasificación de severidad.
- Distinción entre evento, alerta, posible incidente e incidente confirmado.
- Automatización con Python.
- Generación automática de reportes.
- Creación de runbooks.
- Documentación técnica.
- Priorización de hallazgos.
- Pensamiento operacional defensivo.

---

# Casos prácticos

## Caso 01 - Phishing

Análisis de un correo sospechoso simulado orientado al robo de credenciales.

Se revisan:

- remitente;
- dominio;
- asunto;
- urgencia artificial;
- solicitud de credenciales;
- enlace incluido;
- interacción del usuario;
- riesgo potencial;
- acciones recomendadas.

### Archivos relacionados

- 📄 [Caso completo de phishing](cases/01-phishing.md)
- 📊 [Reporte técnico de phishing](reports/reporte-phishing.md)
- 📘 [Runbook de respuesta ante phishing](docs/04-runbook-phishing.md)

---

## Caso 02 - Autenticación SSH

Análisis de logs simulados de autenticación SSH para identificar:

- accesos exitosos;
- intentos fallidos;
- múltiples usuarios objetivo;
- actividad repetida desde una misma IP;
- intentos contra cuentas privilegiadas;
- autenticaciones exitosas posteriores a múltiples fallos;
- posibles señales de compromiso.

### Archivos relacionados

- 📄 [Dataset sintético `auth_sample.log`](logs/auth_sample.log)
- 🔐 [Caso completo de fuerza bruta SSH](cases/02-fuerza-bruta-ssh.md)
- 📊 [Reporte técnico de fuerza bruta SSH](reports/reporte-fuerza-bruta-ssh.md)
- 📘 [Runbook de análisis de alerta SSH](docs/03-runbook-analisis-alerta.md)

---

# Automatización con Python

El proyecto contiene dos niveles de automatización.

## 1. Baseline

### [`scripts/detectar_login_fallidos.py`](scripts/detectar_login_fallidos.py)

Primera capa de análisis automatizado.

Permite:

- leer el log SSH simulado;
- detectar eventos `Failed password`;
- extraer IP y usuario;
- contar intentos fallidos por IP;
- identificar usuarios objetivo;
- asignar una severidad básica.

Flujo:

```text
log
↓
Failed password
↓
IP + usuario
↓
conteo
↓
severidad
```

Esta versión funciona como baseline y no intenta confirmar posibles compromisos.

➡️ [Ver código del baseline](scripts/detectar_login_fallidos.py)

---

## 2. Analizador principal

### [`scripts/soc_log_analyzer.py`](scripts/soc_log_analyzer.py)

Versión principal del laboratorio.

Implementa:

- lectura del archivo de logs;
- parsing de eventos SSH;
- normalización de eventos;
- identificación de autenticaciones fallidas y exitosas;
- conteo por IP;
- conteo por IP y usuario;
- identificación de usuarios objetivo;
- clasificación de severidad;
- priorización de hallazgos;
- correlación de eventos;
- detección de posibles compromisos;
- cálculo de riesgo general;
- generación automática de reporte Markdown.

La correlación de posibles compromisos utiliza:

```text
IP + usuario
↓
múltiples fallos
↓
login exitoso posterior
↓
posible compromiso
```

Esto evita asociar un login exitoso con intentos fallidos dirigidos a una cuenta diferente.

➡️ [Ver código del analizador principal](scripts/soc_log_analyzer.py)

➡️ [Ver reporte generado por el analizador](reports/soc-analysis-report.md)

---

# Política de severidad

El laboratorio utiliza una política simplificada de priorización.

Con el umbral predeterminado de `3`:

| Condición | Severidad |
|---|---|
| Menos de 3 intentos fallidos | Baja |
| 3 a 5 intentos fallidos | Media |
| 6 o más intentos fallidos | Alta |
| Posible compromiso correlacionado | Alta |
| Compromiso confirmado o impacto grave | Crítica |

La severidad se utiliza para priorizar el análisis.

Una detección de posible compromiso no representa por sí sola la confirmación de un acceso no autorizado.

➡️ [Ver documentación sobre evento, alerta e incidente](docs/01-evento-alerta-incidente.md)

---

# Evento, alerta e incidente

El laboratorio diferencia cuatro estados:

```text
EVENTO
↓
actividad registrada

ALERTA
↓
actividad sospechosa que requiere revisión

POSIBLE INCIDENTE
↓
señales relevantes de posible compromiso

INCIDENTE CONFIRMADO
↓
evidencia suficiente de compromiso o impacto
```

La clasificación puede cambiar a medida que aparece nueva evidencia.

Para profundizar:

- 📘 [Evento, alerta e incidente](docs/01-evento-alerta-incidente.md)
- 📚 [Glosario SOC Junior](docs/02-glosario-soc-junior.md)

---

# Ejecución

Desde la raíz del proyecto.

## Baseline

```powershell
py scripts/detectar_login_fallidos.py
```

También puede utilizarse:

```powershell
python scripts/detectar_login_fallidos.py
```

---

## Analizador principal

```powershell
py scripts/soc_log_analyzer.py logs/auth_sample.log
```

O:

```powershell
python scripts/soc_log_analyzer.py logs/auth_sample.log
```

También puede configurarse explícitamente el umbral y el archivo de reporte:

```powershell
py scripts/soc_log_analyzer.py logs/auth_sample.log --threshold 3 --report reports/soc-analysis-report.md
```

Archivos utilizados:

- [Dataset `logs/auth_sample.log`](logs/auth_sample.log)
- [Analizador `scripts/soc_log_analyzer.py`](scripts/soc_log_analyzer.py)
- [Reporte `reports/soc-analysis-report.md`](reports/soc-analysis-report.md)

---

# Resultado esperado

Utilizando el dataset:

[`logs/auth_sample.log`](logs/auth_sample.log)

con:

```text
threshold = 3
```

el analizador produce:

```text
Líneas procesadas: 23
Eventos reconocidos: 23
Líneas ignoradas: 0
Intentos fallidos: 17
Accesos exitosos: 6
IPs observadas: 7
Alertas priorizadas: 3
Posibles compromisos: 1
Riesgo general estimado: ALTO
```

➡️ [Ver reporte completo generado](reports/soc-analysis-report.md)

---

# Hallazgos principales del dataset

## `203.0.113.45`

```text
7 intentos fallidos
→ severidad Alta
```

Usuarios objetivo:

- `root`
- `test`
- `soporte`

---

## `198.51.100.23`

```text
4 intentos fallidos contra admin
→ severidad Media
```

---

## `192.0.2.15`

```text
5 fallos contra root
↓
login exitoso posterior
↓
misma IP + mismo usuario
↓
posible incidente
↓
severidad Alta
```

La correlación requiere investigación adicional y no confirma automáticamente un compromiso.

### Evidencia relacionada

- [Ver log utilizado](logs/auth_sample.log)
- [Ver análisis manual SSH](cases/02-fuerza-bruta-ssh.md)
- [Ver reporte manual SSH](reports/reporte-fuerza-bruta-ssh.md)
- [Ver reporte automático](reports/soc-analysis-report.md)

---

# Reporte automático

El analizador genera:

[`reports/soc-analysis-report.md`](reports/soc-analysis-report.md)

El reporte contiene:

- metadatos del análisis;
- resumen ejecutivo;
- métricas;
- riesgo general;
- hallazgos priorizados;
- detalle por usuario;
- posibles compromisos;
- recomendaciones operativas;
- limitaciones;
- conclusión.

➡️ [Abrir reporte automático](reports/soc-analysis-report.md)

---

# Estructura del proyecto

```text
soc-junior-lab/
│
├── README.md
├── .gitignore
│
├── cases/
│   ├── 01-phishing.md
│   └── 02-fuerza-bruta-ssh.md
│
├── docs/
│   ├── 01-evento-alerta-incidente.md
│   ├── 02-glosario-soc-junior.md
│   ├── 03-runbook-analisis-alerta.md
│   └── 04-runbook-phishing.md
│
├── logs/
│   └── auth_sample.log
│
├── reports/
│   ├── reporte-fuerza-bruta-ssh.md
│   ├── reporte-phishing.md
│   ├── reporte-template.md
│   └── soc-analysis-report.md
│
└── scripts/
    ├── detectar_login_fallidos.py
    └── soc_log_analyzer.py
```

---

# Documentación

| Archivo | Propósito |
|---|---|
| [`docs/01-evento-alerta-incidente.md`](docs/01-evento-alerta-incidente.md) | Diferencia entre evento, alerta, posible incidente e incidente confirmado |
| [`docs/02-glosario-soc-junior.md`](docs/02-glosario-soc-junior.md) | Conceptos fundamentales utilizados en el laboratorio |
| [`docs/03-runbook-analisis-alerta.md`](docs/03-runbook-analisis-alerta.md) | Procedimiento de análisis de autenticación SSH |
| [`docs/04-runbook-phishing.md`](docs/04-runbook-phishing.md) | Procedimiento inicial de respuesta ante phishing |
| [`cases/01-phishing.md`](cases/01-phishing.md) | Caso práctico de análisis de phishing |
| [`cases/02-fuerza-bruta-ssh.md`](cases/02-fuerza-bruta-ssh.md) | Caso práctico de autenticación SSH |
| [`reports/reporte-fuerza-bruta-ssh.md`](reports/reporte-fuerza-bruta-ssh.md) | Reporte manual del escenario SSH |
| [`reports/reporte-phishing.md`](reports/reporte-phishing.md) | Reporte manual del escenario de phishing |
| [`reports/reporte-template.md`](reports/reporte-template.md) | Plantilla reutilizable para documentación |
| [`reports/soc-analysis-report.md`](reports/soc-analysis-report.md) | Reporte generado automáticamente por Python |
| [`scripts/detectar_login_fallidos.py`](scripts/detectar_login_fallidos.py) | Baseline de análisis automatizado |
| [`scripts/soc_log_analyzer.py`](scripts/soc_log_analyzer.py) | Analizador principal del laboratorio |

---

# Metodología

El proyecto combina análisis manual y automatización.

```text
1. observar evidencia
2. identificar eventos
3. detectar patrones
4. correlacionar actividad
5. clasificar
6. priorizar
7. recomendar acciones
8. documentar
```

El objetivo no es únicamente producir una alerta, sino poder explicar:

- qué ocurrió;
- qué evidencia existe;
- por qué resulta relevante;
- qué todavía no puede confirmarse;
- qué debería revisarse después.

---

# Limitaciones

Este proyecto es un laboratorio educativo y no representa un sistema de detección de producción.

El analizador:

- trabaja con logs SSH simulados;
- reconoce un conjunto limitado de formatos;
- utiliza una política simplificada de severidad;
- no construye ventanas temporales;
- no consulta reputación de IP;
- no utiliza geolocalización;
- no consume inteligencia de amenazas;
- no considera criticidad real de activos;
- no analiza completamente la actividad posterior a una sesión;
- no confirma automáticamente compromisos.

Las detecciones deben interpretarse como señales para investigación.

---

# Seguridad y privacidad

El repositorio utiliza exclusivamente datos simulados o preparados para demostración.

No deben publicarse:

- credenciales reales;
- tokens;
- claves privadas;
- logs de producción;
- archivos EVTX reales;
- capturas PCAP reales;
- información personal;
- evidencia sin sanitizar.

El archivo [`logs/auth_sample.log`](logs/auth_sample.log) es un dataset sintético incluido deliberadamente para permitir la reproducción del análisis.

---

# Estado del proyecto

**Completo para el alcance actual del laboratorio.**

El proyecto demuestra un flujo defensivo básico y reproducible:

```text
logs
↓
eventos
↓
detecciones
↓
correlación
↓
hallazgos
↓
severidad
↓
priorización
↓
reporte
```

Posibles extensiones futuras podrían incluir integración con un SIEM, nuevas fuentes de logs o escenarios adicionales, sin formar parte del alcance actual.

---

## Resumen

SOC Junior Lab reúne análisis manual, automatización con Python y documentación técnica aplicada a escenarios simulados de autenticación SSH y phishing.

El objetivo es construir una base práctica y defendible de operaciones de seguridad, demostrando la capacidad de transformar evidencia técnica en hallazgos estructurados y documentados.

### Explorar el laboratorio

- 🐍 [Analizador principal](scripts/soc_log_analyzer.py)
- 📊 [Reporte automático](reports/soc-analysis-report.md)
- 🔐 [Caso SSH](cases/02-fuerza-bruta-ssh.md)
- 🎣 [Caso Phishing](cases/01-phishing.md)
- 📘 [Runbook SSH](docs/03-runbook-analisis-alerta.md)
- 📘 [Runbook Phishing](docs/04-runbook-phishing.md)
- 📚 [Glosario SOC](docs/02-glosario-soc-junior.md)