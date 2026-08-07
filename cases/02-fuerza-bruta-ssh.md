# Caso 02 - Análisis manual de fuerza bruta SSH

## Objetivo

Analizar manualmente logs simulados de autenticación SSH para identificar actividad normal, intentos fallidos, posibles alertas de fuerza bruta y señales de un posible compromiso de cuenta.

---

## Fuente de datos

Archivo analizado:

- `logs/auth_sample.log`

Tipo de log:

- Autenticación SSH simulada.

Importante:

- Los datos de este laboratorio son simulados.
- Las IPs utilizadas son de ejemplo o pertenecen al entorno interno simulado.
- No se utilizan credenciales, sistemas ni infraestructura productiva real.
- El objetivo es practicar análisis básico de logs, clasificación de hallazgos y documentación técnica.

---

## Contexto

El archivo contiene registros simulados de autenticación SSH en un servidor denominado `server01`.

Los eventos incluyen:

- Inicios de sesión exitosos.
- Intentos fallidos de autenticación.
- Distintos usuarios objetivo.
- Distintas IPs de origen.
- Actividad repetida desde una misma IP.
- Un caso donde múltiples fallos contra un usuario son seguidos por un inicio de sesión exitoso desde el mismo origen.

---

## Metodología de análisis

Para revisar el log se observaron los siguientes elementos:

1. Fecha y hora del evento.
2. Servidor afectado.
3. Resultado de autenticación.
4. Usuario objetivo.
5. IP de origen.
6. Cantidad de intentos fallidos.
7. Usuarios objetivo por IP.
8. Existencia de logins exitosos posteriores.
9. Relación entre IP y usuario.
10. Clasificación y severidad del hallazgo.

El análisis manual busca identificar patrones y priorizar actividad sospechosa sin asumir automáticamente que existe un compromiso.

---

## Actividad normal observada

Se observan inicios de sesión exitosos desde IPs internas del laboratorio hacia usuarios normales.

Ejemplos:

- `usuario1` desde `192.168.1.20`
- `usuario2` desde `192.168.1.22`
- `usuario3` desde `192.168.1.24`

Dentro del escenario simulado, estos eventos se consideran actividad normal porque corresponden a usuarios no privilegiados y direcciones internas del laboratorio sin actividad sospechosa previa relevante.

Clasificación:

| Elemento | Valor |
|---|---|
| Tipo | Evento |
| Severidad | Baja |
| Acción | Registrar y monitorear |

---

## Hallazgo 1 - Múltiples intentos fallidos contra root

Se detectan múltiples intentos fallidos contra el usuario `root` desde la IP `203.0.113.45`.

Eventos observados:

```text
Failed password for root from 203.0.113.45
Failed password for root from 203.0.113.45
Failed password for root from 203.0.113.45
Failed password for root from 203.0.113.45
Failed password for root from 203.0.113.45
```

Además, la misma IP registra intentos contra otros usuarios:

- `test`
- `soporte`

En total, esta IP acumula siete intentos fallidos contra distintos usuarios.

### Interpretación

La repetición de intentos y el uso de varios usuarios objetivo puede ser compatible con actividad de fuerza bruta o intentos de identificar credenciales válidas.

El usuario `root` aumenta la relevancia del hallazgo por tratarse de una cuenta privilegiada.

Clasificación:

| Elemento | Valor |
|---|---|
| Tipo | Alerta |
| Severidad | Alta |
| Intentos fallidos | 7 |
| Usuarios objetivo | `root`, `test`, `soporte` |
| IP origen | `203.0.113.45` |
| Acción recomendada | Investigar origen, revisar actividad relacionada y aplicar controles si corresponde |

---

## Hallazgo 2 - Intentos fallidos contra admin

Se detectan cuatro intentos fallidos contra el usuario `admin` desde la IP `198.51.100.23`.

Eventos observados:

```text
Failed password for admin from 198.51.100.23
Failed password for admin from 198.51.100.23
Failed password for admin from 198.51.100.23
Failed password for admin from 198.51.100.23
```

### Interpretación

La actividad representa un patrón sospechoso contra una cuenta administrativa y supera el umbral básico de alerta utilizado en este laboratorio.

No existe un login exitoso posterior asociado a esta IP y usuario dentro de la evidencia disponible.

Clasificación:

| Elemento | Valor |
|---|---|
| Tipo | Alerta |
| Severidad | Media |
| Intentos fallidos | 4 |
| Usuario objetivo | `admin` |
| IP origen | `198.51.100.23` |
| Acción recomendada | Revisar origen, historial del usuario y nuevos intentos relacionados |

---

## Hallazgo 3 - Intentos fallidos seguidos de acceso exitoso

Se detectan cinco intentos fallidos contra el usuario `root` desde la IP `192.0.2.15`.

Posteriormente, se observa un inicio de sesión exitoso desde la misma IP hacia el mismo usuario.

Secuencia observada:

```text
192.0.2.15 + root
↓
5 intentos fallidos
↓
Accepted password for root from 192.0.2.15
```

### Interpretación

Este patrón es el hallazgo más relevante del análisis porque existe una autenticación exitosa posterior a múltiples intentos fallidos contra la misma cuenta desde el mismo origen.

La correlación entre:

```text
IP + usuario + fallos previos + login exitoso posterior
```

representa una señal relevante de posible compromiso.

Sin embargo, el patrón por sí solo no confirma que el acceso haya sido realizado por un atacante. Es necesario validar la legitimidad del login y revisar evidencia adicional.

Clasificación:

| Elemento | Valor |
|---|---|
| Tipo | Posible incidente |
| Severidad | Alta |
| Intentos fallidos previos | 5 |
| Usuario objetivo | `root` |
| IP origen | `192.0.2.15` |
| Acción recomendada | Validar legitimidad, revisar actividad posterior, analizar evidencia adicional y contener si corresponde |

---

## Política de severidad utilizada

Este laboratorio utiliza una política simplificada para priorizar hallazgos.

Con el umbral predeterminado de `3`:

| Condición | Severidad |
|---|---|
| Menos de 3 intentos fallidos | Baja |
| 3 a 5 intentos fallidos | Media |
| 6 o más intentos fallidos | Alta |
| Posible compromiso correlacionado | Alta |
| Compromiso confirmado o impacto grave | Crítica |

La cantidad de intentos no es el único criterio. También se consideran el usuario afectado, el contexto y la existencia de una autenticación exitosa correlacionada.

---

## Resumen de hallazgos

| Hallazgo | IP origen | Usuario objetivo | Tipo | Severidad |
|---|---|---|---|---|
| Múltiples fallos contra varios usuarios | `203.0.113.45` | `root`, `test`, `soporte` | Alerta | Alta |
| Múltiples fallos contra admin | `198.51.100.23` | `admin` | Alerta | Media |
| Fallos seguidos de login exitoso correlacionado | `192.0.2.15` | `root` | Posible incidente | Alta |

---

## Acciones recomendadas

Para un entorno real, las acciones iniciales podrían incluir:

1. Validar si las IPs involucradas pertenecen a orígenes esperados.
2. Revisar si los accesos observados estaban autorizados.
3. Revisar actividad posterior de las cuentas afectadas.
4. Consultar logs adicionales del sistema.
5. Bloquear temporalmente una IP sospechosa si el procedimiento lo autoriza.
6. Cambiar credenciales si existe riesgo de compromiso.
7. Revisar la configuración de SSH.
8. Deshabilitar el acceso directo como `root` si está habilitado y la política lo permite.
9. Aplicar controles contra intentos repetidos de autenticación.
10. Utilizar MFA cuando sea compatible con el entorno.
11. Escalar el caso si existe sospecha relevante de compromiso.
12. Documentar los hallazgos y acciones realizadas.

Importante:

Las acciones de contención deben ejecutarse según los permisos, procedimientos y autorizaciones establecidos por la organización.

---

## Evidencia adicional necesaria

Para confirmar o descartar un posible compromiso sería necesario revisar información adicional, como:

- Actividad posterior del usuario.
- Comandos o acciones realizadas durante la sesión.
- Otros registros de autenticación.
- Historial de accesos del usuario.
- Origen esperado de la conexión.
- Cambios recientes en archivos o configuraciones.
- Creación o modificación de usuarios.
- Uso de privilegios.
- Otros sistemas relacionados.

Sin esta evidencia adicional, el hallazgo debe permanecer clasificado como posible incidente.

---

## Limitaciones

Este análisis corresponde a un laboratorio educativo y utiliza logs simulados.

El análisis manual no incluye:

- ventanas temporales avanzadas;
- reputación de IP;
- geolocalización;
- inteligencia de amenazas;
- criticidad real de activos;
- contexto histórico completo;
- análisis forense;
- confirmación automática de compromiso.

Las detecciones representan señales para investigar y no conclusiones definitivas sobre actividad maliciosa.

---

## Conclusión

El análisis manual permitió identificar actividad normal, alertas asociadas a múltiples intentos fallidos y un posible incidente relacionado con una autenticación exitosa posterior a varios fallos.

El hallazgo más relevante corresponde a `192.0.2.15`, donde se observan cinco intentos fallidos contra `root` seguidos por un login exitoso desde la misma IP contra el mismo usuario.

Esta correlación requiere investigación prioritaria, pero no confirma por sí sola un compromiso. La legitimidad del acceso debe validarse mediante evidencia adicional.

---

## Resumen técnico

Se analizaron logs simulados de autenticación SSH para identificar actividad normal y patrones sospechosos.

Se detectó una alerta de severidad Alta asociada a siete intentos fallidos desde `203.0.113.45`, una alerta de severidad Media asociada a cuatro fallos contra `admin` desde `198.51.100.23` y un posible incidente de severidad Alta asociado a cinco fallos contra `root` desde `192.0.2.15` seguidos por un login exitoso desde la misma IP contra el mismo usuario.

El análisis permitió aplicar un flujo de evidencia, identificación de patrones, correlación, clasificación, severidad y acciones recomendadas sin considerar un compromiso como confirmado hasta disponer de evidencia suficiente.