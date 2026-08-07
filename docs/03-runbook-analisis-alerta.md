# Runbook - Análisis básico de alerta de seguridad

## Objetivo

Definir un procedimiento básico para analizar una alerta de seguridad relacionada con múltiples intentos fallidos de autenticación.

Este runbook está orientado a un contexto junior de operaciones de seguridad, monitoreo, SOC o gestión de incidencias TI.

---

## 1. Contexto del runbook

Una alerta puede generarse cuando un sistema detecta actividad sospechosa o cuando uno o varios eventos cumplen una condición relevante para seguridad.

Ejemplos:

- Múltiples intentos fallidos de inicio de sesión.
- Intentos contra usuarios privilegiados.
- Accesos desde IPs desconocidas.
- Login exitoso después de varios fallos.
- Actividad fuera de horario habitual.

Este runbook usa como referencia el archivo:

- `logs/auth_sample.log`

Y el caso documentado:

- `cases/02-fuerza-bruta-ssh.md`

---

## 2. Tipo de alerta

| Campo | Detalle |
|---|---|
| Nombre de alerta | Múltiples intentos fallidos de autenticación SSH |
| Fuente | Logs de autenticación |
| Servicio afectado | SSH |
| Sistema | `server01` |
| Posible amenaza | Fuerza bruta / acceso no autorizado |
| Severidad inicial | Media |

---

## 3. Objetivo del análisis

El objetivo del análisis es determinar si la actividad corresponde a:

| Clasificación | Descripción |
|---|---|
| Evento | Actividad esperada, aislada o por debajo del umbral |
| Alerta | Actividad sospechosa que requiere revisión |
| Falso positivo | Actividad legítima que inicialmente parece sospechosa |
| Posible incidente | Existen señales relevantes de posible compromiso |
| Incidente confirmado | Existe evidencia suficiente de compromiso o impacto |

La clasificación puede cambiar a medida que aparece nueva evidencia durante la investigación.

---

## 4. Procedimiento de análisis

### Paso 1 - Revisar la alerta inicial

Identificar los datos básicos de la alerta:

- Fecha y hora.
- Sistema afectado.
- Usuario objetivo.
- IP de origen.
- Cantidad de intentos.
- Resultado de autenticación.
- Severidad inicial.

Preguntas clave:

- ¿Qué ocurrió?
- ¿Cuándo ocurrió?
- ¿Desde dónde ocurrió?
- ¿Qué usuario fue afectado?
- ¿Fue un intento fallido o exitoso?
- ¿Existe actividad relacionada antes o después?

---

### Paso 2 - Revisar la fuente de logs

Consultar los logs relacionados con la alerta.

En este laboratorio, la fuente es:

- `logs/auth_sample.log`

Buscar eventos como:

- `Failed password`
- `Accepted password`
- Intentos repetidos desde la misma IP.
- Intentos contra usuarios privilegiados.
- Login exitoso posterior a fallos.
- Actividad repetida contra un mismo usuario.

---

### Paso 3 - Identificar IP de origen

Registrar la IP o IPs involucradas.

Ejemplo:

| IP origen | Observación |
|---|---|
| `203.0.113.45` | Múltiples intentos fallidos contra varios usuarios |
| `198.51.100.23` | Intentos fallidos contra `admin` |
| `192.0.2.15` | Fallos contra `root` seguidos de login exitoso |

Preguntas clave:

- ¿La IP es interna o externa?
- ¿La IP aparece varias veces?
- ¿La IP intenta acceder a varios usuarios?
- ¿La IP tuvo un login exitoso?
- ¿La actividad desde esa IP es esperada?

---

### Paso 4 - Identificar usuario afectado

Revisar qué usuario fue objetivo de la actividad.

Usuarios sensibles:

- `root`
- `admin`
- cuentas de soporte
- cuentas de servicio
- cuentas con privilegios elevados

Factores que aumentan el riesgo:

- Intentos contra `root`.
- Intentos contra `admin`.
- Login exitoso en una cuenta privilegiada.
- Actividad repetida contra una misma cuenta.
- Usuario afectado fuera de horario habitual.

---

### Paso 5 - Contar intentos fallidos

Registrar la cantidad de intentos fallidos por IP y, cuando sea posible, por combinación de IP y usuario.

Criterio simplificado utilizado en este laboratorio con el umbral predeterminado de `3`:

| Cantidad / condición | Severidad |
|---|---|
| Menos de 3 intentos | Baja |
| 3 a 5 intentos | Media |
| 6 o más intentos | Alta |
| Posible compromiso correlacionado | Alta |
| Compromiso confirmado o impacto grave | Crítica |

Importante:

La cantidad de intentos no es el único criterio. También deben considerarse el usuario afectado, la IP de origen, el contexto y la existencia de un acceso exitoso posterior.

La política de severidad utilizada aquí es simplificada y específica para este laboratorio.

---

### Paso 6 - Buscar login exitoso posterior

Este paso es especialmente relevante para detectar una posible correlación.

Revisar si después de varios intentos fallidos aparece un login exitoso desde la misma IP contra el mismo usuario.

Ejemplo de patrón:

| Secuencia | Significado |
|---|---|
| Varios `Failed password` contra `root` | Posible fuerza bruta |
| Luego `Accepted password` para `root` | Autenticación exitosa posterior |
| Misma IP y mismo usuario | Correlación relevante |

Representación simplificada:

```text
IP + usuario
↓
múltiples fallos
↓
login exitoso posterior
↓
posible incidente
```

Interpretación:

Si una misma combinación de IP y usuario registra múltiples fallos y posteriormente una autenticación exitosa, el caso debe tratarse como posible incidente hasta validar la legitimidad del acceso.

Este patrón por sí solo no confirma que exista un compromiso.

---

### Paso 7 - Clasificar el caso

Clasificar según la evidencia observada.

| Caso | Clasificación |
|---|---|
| Fallo aislado | Evento |
| Múltiples fallos | Alerta |
| Múltiples fallos contra cuenta privilegiada | Alerta |
| Múltiples fallos seguidos de login exitoso para la misma cuenta | Posible incidente |
| Acceso validado como no autorizado | Incidente confirmado |

La clasificación debe basarse en la evidencia disponible y puede cambiar durante la investigación.

---

### Paso 8 - Definir severidad

Asignar una severidad según la evidencia, contexto e impacto.

| Severidad | Criterio |
|---|---|
| Baja | Actividad aislada o por debajo del umbral |
| Media | Actividad sospechosa que alcanza el umbral de revisión |
| Alta | Volumen elevado de intentos o posible compromiso correlacionado |
| Crítica | Compromiso confirmado o impacto grave |

Ejemplo:

La IP `192.0.2.15` registra múltiples intentos fallidos contra `root` y posteriormente un login exitoso desde la misma IP contra el mismo usuario.

Clasificación:

- Tipo: Posible incidente
- Severidad: Alta

La severidad es Alta porque existe una correlación relevante entre múltiples fallos y una autenticación exitosa posterior. Sin embargo, el acceso todavía debe validarse antes de considerarlo un incidente confirmado.

---

### Paso 9 - Acciones recomendadas

Según la severidad y la evidencia disponible, recomendar acciones.

Importante:

En un entorno real, las acciones de contención deben ejecutarse según permisos, procedimientos internos y autorización del equipo responsable.

Acciones básicas:

1. Validar si el acceso fue autorizado.
2. Revisar actividad posterior del usuario afectado.
3. Revisar otros logs relacionados.
4. Bloquear temporalmente una IP sospechosa si corresponde.
5. Cambiar credenciales si existe riesgo de compromiso.
6. Revisar la configuración de SSH.
7. Deshabilitar login directo como `root` si está habilitado.
8. Configurar controles contra intentos repetidos de autenticación.
9. Aplicar MFA si está disponible.
10. Escalar a un analista senior o equipo responsable cuando corresponda.
11. Documentar hallazgos y acciones.

---

### Paso 10 - Documentar el cierre

Todo análisis debe dejar un registro claro de lo observado.

Elementos mínimos:

- Qué ocurrió.
- Qué evidencia se revisó.
- Qué IP estuvo involucrada.
- Qué usuario fue afectado.
- Qué patrón se observó.
- Cómo se clasificó el caso.
- Qué severidad se asignó.
- Qué acciones se recomendaron.
- Qué limitaciones tuvo el análisis.
- Si se escaló o no el caso.

Si todavía no existe evidencia suficiente para confirmar un compromiso, el cierre debe indicarlo explícitamente.

---

## 5. Ejemplo aplicado

Caso observado:

- IP origen: `192.0.2.15`
- Usuario afectado: `root`
- Actividad: múltiples intentos fallidos
- Evento posterior: login exitoso
- Correlación: misma IP y mismo usuario
- Clasificación: Posible incidente
- Severidad: Alta

Interpretación:

La actividad muestra una secuencia de múltiples intentos fallidos contra una cuenta privilegiada seguidos por una autenticación exitosa desde el mismo origen.

Este comportamiento representa una señal relevante de posible compromiso, pero no demuestra por sí solo que el acceso haya sido realizado por un atacante.

Se recomienda validar si el acceso fue legítimo, revisar la actividad posterior de la cuenta, analizar evidencia adicional y aplicar medidas de contención si corresponde.

---

## 6. Criterios de escalamiento

El caso debe escalarse si ocurre alguna de estas condiciones:

- Login exitoso posterior a múltiples fallos.
- Usuario afectado con privilegios elevados.
- IP externa o desconocida.
- Actividad repetida en un corto periodo.
- Múltiples usuarios objetivo.
- Evidencia de cambios posteriores en el sistema.
- Sospecha de compromiso de credenciales.
- Evidencia de acceso no autorizado.
- Impacto en sistemas críticos.
- Falta de claridad sobre la legitimidad del acceso.

El escalamiento permite que un analista o equipo con mayor capacidad de investigación continúe el análisis cuando el riesgo o la incertidumbre lo justifican.

---

## 7. Resumen del procedimiento

1. Revisar la alerta.
2. Confirmar la fuente de logs.
3. Identificar IP de origen.
4. Identificar usuario afectado.
5. Contar intentos fallidos.
6. Buscar login exitoso posterior.
7. Correlacionar IP y usuario.
8. Clasificar el caso.
9. Asignar severidad.
10. Recomendar acciones.
11. Documentar y escalar si corresponde.

Flujo simplificado:

```text
logs
↓
eventos
↓
actividad sospechosa
↓
correlación
↓
clasificación
↓
severidad
↓
acciones
↓
documentación
```

---

## 8. Limitaciones

Este runbook corresponde a un laboratorio educativo y utiliza una política simplificada de análisis.

No contempla:

- ventanas temporales avanzadas;
- criticidad real de activos;
- reputación de IP;
- geolocalización;
- inteligencia de amenazas;
- contexto histórico completo;
- validación automática de legitimidad;
- análisis forense profundo.

Por este motivo, una detección debe interpretarse como una señal para investigar y no como confirmación automática de compromiso.

---

## 9. Resumen técnico

Este runbook define un procedimiento básico para analizar alertas relacionadas con múltiples intentos fallidos de autenticación SSH.

El flujo permite revisar logs, identificar IPs y usuarios afectados, contar intentos, correlacionar fallos con accesos exitosos posteriores para la misma combinación de IP y usuario, clasificar la actividad, asignar severidad, recomendar acciones y definir criterios de escalamiento.

La distinción entre alerta, posible incidente e incidente confirmado permite priorizar actividad sospechosa sin afirmar un compromiso hasta disponer de evidencia suficiente.