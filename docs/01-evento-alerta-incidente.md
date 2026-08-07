# Evento, Alerta e Incidente

## Objetivo

Comprender la diferencia entre evento, alerta, posible incidente e incidente confirmado dentro de un contexto básico de operaciones de seguridad.

---

## 1. Evento

Un evento es cualquier acción o registro que ocurre dentro de un sistema, aplicación, red o dispositivo.

Un evento no necesariamente representa actividad maliciosa. Simplemente indica que algo ocurrió.

### Ejemplos

- Un usuario inicia sesión correctamente.
- Un usuario falla su contraseña una vez.
- Un servidor recibe una conexión.
- Un archivo es modificado.
- Una aplicación genera un registro de actividad.

### Ejemplo simple

```text
Jul 16 10:15:22 server01 sshd[1234]: Accepted password for usuario1 from 192.168.1.20 port 55221 ssh2
```

Este registro indica que un usuario inició sesión correctamente mediante SSH.

Clasificación:

- Tipo: Evento
- Severidad: Baja
- Acción: Registrar y monitorear

---

## 2. Alerta

Una alerta es una señal generada cuando uno o varios eventos cumplen una condición sospechosa o relevante para seguridad.

Una alerta requiere revisión, pero no significa automáticamente que exista un incidente.

### Ejemplos

- Múltiples intentos fallidos de inicio de sesión.
- Conexión desde una ubicación inusual.
- Detección de un archivo sospechoso.
- Tráfico anómalo.
- Acceso fuera de horario habitual.

### Ejemplo simple

```text
Jul 16 10:20:11 server01 sshd[1234]: Failed password for root from 203.0.113.45 port 49822 ssh2
Jul 16 10:20:15 server01 sshd[1235]: Failed password for root from 203.0.113.45 port 49823 ssh2
Jul 16 10:20:18 server01 sshd[1236]: Failed password for root from 203.0.113.45 port 49824 ssh2
```

Este patrón puede indicar un intento de acceso no autorizado y requiere análisis adicional.

Clasificación:

- Tipo: Alerta
- Severidad: Media
- Acción: Revisar IP, usuario afectado, cantidad de intentos y contexto

---

## 3. Posible incidente

Un posible incidente existe cuando la evidencia muestra señales relevantes de posible compromiso, pero todavía no es suficiente para confirmar que ocurrió un acceso no autorizado o un impacto real.

Debe investigarse hasta determinar si la actividad fue legítima o maliciosa.

### Ejemplo simple

```text
Múltiples intentos fallidos contra root desde una misma IP
→
Inicio de sesión exitoso posterior desde la misma IP contra root
```

Este patrón aumenta el riesgo porque existe una autenticación exitosa después de varios intentos fallidos contra la misma cuenta.

Sin embargo, este comportamiento por sí solo no confirma que el acceso haya sido realizado por un atacante.

Clasificación:

- Tipo: Posible incidente
- Severidad: Alta
- Acción: Validar la legitimidad del acceso, revisar actividad posterior, analizar evidencia adicional y aplicar contención si corresponde

---

## 4. Incidente confirmado

Un incidente confirmado es una situación en la que existe evidencia suficiente de compromiso o impacto sobre la confidencialidad, integridad o disponibilidad de un sistema.

Un incidente confirmado requiere análisis, contención, respuesta, documentación y seguimiento.

### Ejemplos

- Cuenta comprometida confirmada.
- Acceso no autorizado confirmado.
- Malware ejecutado en un equipo.
- Exfiltración de información.
- Ransomware.
- Modificación no autorizada de información.
- Interrupción de un servicio causada por un ataque.

### Ejemplo simple

Después de detectar un inicio de sesión sospechoso en una cuenta privilegiada, se confirma mediante evidencia adicional que el acceso no fue autorizado y que posteriormente se realizaron acciones dentro del sistema.

Clasificación:

- Tipo: Incidente confirmado
- Severidad: Crítica
- Acción: Contener, preservar evidencia, revisar alcance, responder, escalar y documentar

---

## Diferencia rápida

| Concepto | Qué significa | Ejemplo | Acción |
|---|---|---|---|
| Evento | Algo ocurrió | Login exitoso normal | Registrar |
| Alerta | Algo parece sospechoso | Múltiples logins fallidos | Revisar |
| Posible incidente | Existen señales de posible compromiso | Fallos seguidos de login exitoso | Investigar |
| Incidente confirmado | Existe evidencia suficiente de compromiso o impacto | Acceso no autorizado confirmado | Contener y responder |

---

## Flujo de clasificación

La clasificación puede evolucionar a medida que aparece nueva evidencia:

```text
EVENTO
↓
Actividad registrada

ALERTA
↓
Actividad sospechosa que requiere revisión

POSIBLE INCIDENTE
↓
Señales relevantes de posible compromiso

INCIDENTE CONFIRMADO
↓
Evidencia suficiente de compromiso o impacto
```

No todos los eventos generan alertas, no todas las alertas se convierten en posibles incidentes y no todos los posibles incidentes terminan siendo incidentes confirmados.

La clasificación debe basarse en la evidencia disponible y puede cambiar durante la investigación.

---

## Resumen técnico

Un evento es cualquier registro de actividad dentro de un sistema. Una alerta aparece cuando uno o varios eventos cumplen una condición sospechosa o relevante para seguridad. Un posible incidente presenta señales que requieren investigación adicional, pero todavía no confirma un compromiso. Un incidente confirmado cuenta con evidencia suficiente de acceso no autorizado, compromiso o impacto y requiere contención, respuesta, documentación y seguimiento.