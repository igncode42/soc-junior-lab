# SOC Log Analyzer — Reporte de análisis SSH

## Metadatos

- **Fecha de generación:** 2026-08-07 18:59:12 -0400
- **Archivo analizado:** `logs/auth_sample.log`
- **Umbral configurado:** 3
- **Estado del análisis:** Completado

## Resumen ejecutivo

| Métrica | Resultado |
|---|---:|
| Líneas procesadas | 23 |
| Eventos reconocidos | 23 |
| Líneas ignoradas | 0 |
| Intentos fallidos | 17 |
| Accesos exitosos | 6 |
| IPs observadas | 7 |
| Alertas priorizadas | 3 |
| Posibles compromisos | 1 |

## Evaluación general

**Riesgo general estimado:** `ALTO`

Política aplicada: severidad Media desde 3 fallos y Alta desde 6 fallos o cuando existe un posible compromiso correlacionado. La severidad Crítica queda reservada para compromiso confirmado o impacto grave.

## Hallazgos priorizados por IP

### 1. [ALTA] `203.0.113.45`

- **Intentos fallidos:** 7
- **Usuarios objetivo:** `root`, `soporte`, `test`
- **Posible compromiso relacionado:** No

#### Detalle por usuario

| Usuario | Intentos fallidos |
|---|---:|
| `root` | 5 |
| `soporte` | 1 |
| `test` | 1 |

### 2. [ALTA] `192.0.2.15`

- **Intentos fallidos:** 5
- **Usuarios objetivo:** `root`
- **Posible compromiso relacionado:** Sí

#### Detalle por usuario

| Usuario | Intentos fallidos |
|---|---:|
| `root` | 5 |

### 3. [MEDIA] `198.51.100.23`

- **Intentos fallidos:** 4
- **Usuarios objetivo:** `admin`
- **Posible compromiso relacionado:** No

#### Detalle por usuario

| Usuario | Intentos fallidos |
|---|---:|
| `admin` | 4 |

### 4. [BAJA] `192.168.1.35`

- **Intentos fallidos:** 1
- **Usuarios objetivo:** `admin`
- **Posible compromiso relacionado:** No

#### Detalle por usuario

| Usuario | Intentos fallidos |
|---|---:|
| `admin` | 1 |

## Posibles compromisos de cuenta

### 1. [ALTA] Posible compromiso

- **IP de origen:** `192.0.2.15`
- **Usuario:** `root`
- **Fallos previos al acceso:** 5
- **Secuencia de líneas:** 17 → 22
- **Compromiso confirmado:** No
- **Evaluación:** acceso exitoso posterior a múltiples fallos desde la misma IP contra el mismo usuario.

## Recomendación operativa

Prioridad alta: validar la legitimidad de los accesos correlacionados, revisar la actividad posterior y considerar medidas de contención si aparece evidencia adicional.

## Limitaciones

- La severidad y el riesgo se basan en una política simplificada para este laboratorio.
- El análisis trabaja con logs SSH simulados.
- El análisis no utiliza timestamps para construir ventanas temporales.
- No se considera la criticidad real del activo o de la cuenta.
- No se consulta reputación, geolocalización ni inteligencia de amenazas.
- No se analiza actividad posterior dentro de una sesión.
- Un posible compromiso representa una señal para investigar, no una confirmación definitiva.

## Conclusión

El análisis convirtió eventos SSH simulados en hallazgos estructurados, priorizó actividad por severidad y correlacionó intentos fallidos con accesos exitosos posteriores utilizando la combinación de IP y usuario.

Las detecciones representan señales para investigación y no confirman automáticamente un compromiso.
