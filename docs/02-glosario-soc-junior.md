# Glosario SOC Junior

## Objetivo

Definir conceptos básicos utilizados en operaciones de seguridad, monitoreo, análisis de logs e investigación inicial de incidentes.

Este glosario funciona como base de estudio y referencia para roles junior relacionados con SOC, ciberseguridad, monitoreo e incidencias TI.

---

## SOC

Un SOC, Security Operations Center, es un equipo encargado de monitorear, detectar, analizar y responder a eventos, alertas e incidentes de seguridad.

- Ejemplo: un SOC puede revisar alertas de intentos de acceso sospechosos, actividad anómala en servidores, phishing o malware detectado en endpoints.

---

## SIEM

Un SIEM, Security Information and Event Management, es una plataforma que centraliza, almacena y analiza logs de distintos sistemas para detectar eventos relevantes y generar alertas de seguridad.

- Ejemplo: un SIEM puede recibir logs desde servidores, firewalls, aplicaciones, endpoints y servicios cloud para correlacionar actividad y generar alertas.

---

## Log

Un log es un registro generado por un sistema, aplicación, dispositivo o servicio. Sirve para saber qué ocurrió, cuándo ocurrió, dónde ocurrió y qué usuario o sistema estuvo involucrado.

Ejemplo:

```text
Jul 17 09:15:22 server01 sshd[1201]: Failed password for root from 203.0.113.45 port 50221 ssh2
```

---

## Evento

Un evento es cualquier actividad registrada por un sistema.

No todos los eventos son maliciosos ni requieren una respuesta de seguridad.

- Ejemplo: un usuario inicia sesión correctamente en un servidor.

---

## Alerta

Una alerta es una señal generada cuando uno o varios eventos cumplen una condición sospechosa o relevante para seguridad.

Una alerta debe revisarse, pero no confirma automáticamente que exista un incidente.

- Ejemplo: múltiples intentos fallidos de inicio de sesión desde la misma IP.

---

## Posible incidente

Un posible incidente existe cuando la evidencia muestra señales relevantes de posible compromiso, pero todavía no es suficiente para confirmar que ocurrió un acceso no autorizado o un impacto real.

- Ejemplo: múltiples intentos fallidos contra una cuenta sensible seguidos por un inicio de sesión exitoso desde la misma IP contra el mismo usuario.

Este patrón requiere investigación adicional antes de confirmar un incidente.

---

## Incidente confirmado

Un incidente confirmado es una situación en la que existe evidencia suficiente de compromiso o impacto sobre la confidencialidad, integridad o disponibilidad de un sistema.

- Ejemplo: se valida que un inicio de sesión fue realizado por un tercero no autorizado y que posteriormente se ejecutaron acciones dentro de la cuenta comprometida.

---

## Confidencialidad, integridad y disponibilidad

La confidencialidad, integridad y disponibilidad son tres principios básicos de seguridad de la información.

- Confidencialidad: proteger la información para que solo accedan personas autorizadas.
- Integridad: asegurar que la información no sea modificada de forma indebida.
- Disponibilidad: asegurar que los sistemas o datos estén accesibles cuando se necesitan.

Ejemplos:

- Un acceso no autorizado puede afectar la confidencialidad.
- Una modificación no autorizada de archivos puede afectar la integridad.
- Un ataque que deja un servicio fuera de línea puede afectar la disponibilidad.

---

## IP

Una IP es una dirección utilizada para identificar un equipo o servicio dentro de una red.

Ejemplos:

- `192.168.1.10`
- `203.0.113.45`

---

## Usuario

Un usuario es una identidad que accede a un sistema, aplicación o servicio.

Ejemplos:

- `root`
- `admin`
- `usuario1`
- `soporte`

---

## Severidad

La severidad indica la importancia o criticidad de un evento, alerta o incidente según la evidencia disponible, el contexto y el impacto potencial o confirmado.

| Severidad | Significado |
|---|---|
| Baja | Actividad normal o por debajo del umbral de alerta |
| Media | Actividad sospechosa que requiere revisión |
| Alta | Posible compromiso, actividad relevante o impacto significativo |
| Crítica | Compromiso confirmado o impacto grave |

En este laboratorio, la severidad se utiliza como mecanismo simplificado de priorización y no sustituye una evaluación de riesgo completa.

---

## Falso positivo

Un falso positivo es una alerta que inicialmente parece sospechosa, pero después del análisis se determina que corresponde a actividad legítima o que no representa una amenaza real.

- Ejemplo: un usuario falla varias veces su contraseña porque la olvidó, pero el acceso posterior es validado como legítimo.

---

## Phishing

El phishing es una técnica de engaño mediante la cual un atacante intenta obtener credenciales, información sensible o acceso a sistemas utilizando correos, mensajes, sitios web u otros medios fraudulentos.

Señales comunes:

- Remitente extraño.
- Urgencia artificial.
- Enlaces sospechosos.
- Archivos adjuntos inesperados.
- Errores de redacción.
- Solicitud de contraseñas o datos sensibles.
- Dominios similares al legítimo.

---

## Fuerza bruta

La fuerza bruta es un intento repetido de obtener acceso mediante múltiples combinaciones de usuario y contraseña.

- Ejemplo: numerosos intentos fallidos de autenticación contra el usuario `root` desde una misma IP.

La existencia de múltiples fallos puede generar una alerta, pero no confirma por sí sola que exista un compromiso.

---

## IAM

IAM, Identity and Access Management, es la disciplina encargada de gestionar identidades, usuarios, permisos y accesos dentro de una organización.

- Ejemplo: crear usuarios, asignar permisos, revisar accesos y eliminar cuentas que ya no deberían existir.

---

## EDR

Un EDR, Endpoint Detection and Response, es una herramienta que monitorea actividad en endpoints y permite detectar, investigar y responder ante amenazas en equipos como estaciones de trabajo o servidores.

- Ejemplo: detectar una ejecución sospechosa de malware en un equipo corporativo.

---

## Runbook

Un runbook es una guía documentada que define pasos para analizar o responder ante una situación específica.

- Ejemplo: un runbook para analizar una alerta de múltiples intentos fallidos de autenticación SSH.

---

## Escalamiento

El escalamiento ocurre cuando un analista deriva una alerta, posible incidente o incidente a un nivel superior o equipo especializado debido a su severidad, impacto o necesidad de análisis adicional.

- Ejemplo: un analista SOC junior identifica un posible compromiso de una cuenta privilegiada y escala el caso a un analista senior.

---

## IOC

Un IOC, Indicator of Compromise, es un dato o señal técnica que puede estar asociado con actividad maliciosa o con un compromiso.

Ejemplos:

- IP sospechosa.
- Hash de archivo malicioso.
- Dominio malicioso.
- URL de phishing.
- Archivo sospechoso.

Un IOC debe interpretarse dentro de su contexto y no siempre confirma por sí solo que exista un compromiso.

---

## Contención

La contención es una acción orientada a limitar la propagación, impacto o continuidad de un incidente.

- Ejemplo: bloquear temporalmente una IP, deshabilitar una cuenta comprometida o aislar un equipo infectado.

---

## Mitigación

La mitigación consiste en reducir el riesgo, probabilidad o impacto asociado a una amenaza.

- Ejemplo: aplicar parches, fortalecer controles de acceso o endurecer configuraciones.

---

## Hardening

El hardening es el proceso de fortalecer la configuración de un sistema para reducir su superficie de ataque y limitar riesgos.

- Ejemplo: deshabilitar servicios innecesarios, aplicar actualizaciones, restringir accesos y utilizar configuraciones seguras.

---

## Correlación

La correlación consiste en relacionar varios eventos para identificar patrones que pueden no ser relevantes de forma aislada.

Ejemplo:

```text
Múltiples fallos desde una IP contra un usuario
→
Login exitoso posterior
→
Misma IP + mismo usuario
→
Posible compromiso para investigar
```

En este laboratorio, el analizador principal utiliza la combinación de IP y usuario para correlacionar intentos fallidos con accesos exitosos posteriores.

---

## Parsing

El parsing es el proceso de interpretar información en texto para extraer campos estructurados que puedan ser analizados por un programa.

Ejemplo:

```text
Failed password for root from 203.0.113.45
```

Puede convertirse en:

```text
event_type = failed
user = root
ip = 203.0.113.45
```

---

## Priorización

La priorización consiste en ordenar hallazgos según su relevancia o severidad para decidir cuáles deben analizarse primero.

- Ejemplo: una IP con múltiples fallos contra una cuenta privilegiada puede tener mayor prioridad que un único intento fallido contra un usuario común.

---

## Diferencia rápida

| Concepto | Qué representa |
|---|---|
| Evento | Actividad registrada |
| Alerta | Actividad sospechosa que requiere revisión |
| Posible incidente | Señales relevantes de posible compromiso |
| Incidente confirmado | Evidencia suficiente de compromiso o impacto |
| IOC | Indicador técnico que puede aportar evidencia |
| Correlación | Relación entre eventos para identificar patrones |
| Runbook | Procedimiento documentado de análisis o respuesta |

---

## Resumen técnico

Un analista junior de seguridad debe comprender conceptos como SOC, SIEM, logs, eventos, alertas, posibles incidentes, incidentes confirmados, severidad, phishing, fuerza bruta, IAM, EDR, IOC, correlación, parsing, priorización, runbooks y escalamiento.

Estos conceptos permiten transformar evidencia técnica en hallazgos estructurados, distinguir actividad normal de comportamiento sospechoso, priorizar señales relevantes y apoyar una investigación o respuesta documentada.