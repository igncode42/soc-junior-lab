# Plantilla general - Reporte de incidente de seguridad

## 1. Resumen ejecutivo

Describir de forma breve qué ocurrió, cuál fue el hallazgo principal, qué activo fue afectado y cuál es la clasificación y severidad del caso.

Ejemplo:

Durante el análisis de logs, correos o alertas, se identificó actividad sospechosa relacionada con `[describir actividad]`. El caso afecta a `[usuario / sistema / cuenta / servicio]` y se clasifica como `[evento / alerta / posible incidente / incidente confirmado]` con severidad `[Baja / Media / Alta / Crítica]` debido a `[motivo principal]`.

---

## 2. Datos generales del caso

| Campo | Detalle |
|---|---|
| ID del caso | `INC-YYYY-MM-DD-001` |
| Fecha de detección | `YYYY-MM-DD` |
| Hora de detección | `HH:MM` |
| Analista / Equipo | `[Analista o equipo responsable]` |
| Tipo de caso | `Phishing / Fuerza bruta / Malware / Acceso sospechoso / Otro` |
| Estado | `Abierto / En revisión / Escalado / Cerrado` |
| Severidad inicial | `Baja / Media / Alta / Crítica` |
| Severidad final | `Baja / Media / Alta / Crítica` |

---

## 3. Fuente de información

Indicar desde dónde proviene la evidencia analizada.

| Fuente | Detalle |
|---|---|
| Log | `ruta/del/log.log` |
| Correo | `[correo sospechoso]` |
| Alerta | `[nombre de alerta]` |
| Sistema | `[nombre del sistema]` |
| Usuario reportante | `usuario@empresa.test` |
| Herramienta | `SIEM / EDR / Antivirus / Firewall / Mesa de ayuda / Otro` |

---

## 4. Alcance del análisis

Indicar claramente qué información fue revisada y cuáles fueron las limitaciones.

### Elementos revisados

- Logs relacionados.
- Usuario afectado.
- IP de origen.
- Remitente o dominio.
- Enlaces o adjuntos.
- Eventos anteriores y posteriores.
- Accesos exitosos o fallidos.
- Actividad sospechosa relacionada.
- Acciones realizadas después del evento.

### Limitaciones del análisis

Ejemplos:

- No se revisaron logs históricos completos.
- No se realizó análisis forense profundo.
- No se ejecutó sandboxing.
- No se consultó inteligencia de amenazas.
- No se confirmó compromiso.
- El análisis corresponde a una revisión inicial.

Las limitaciones deben documentarse para evitar conclusiones que la evidencia disponible no permita confirmar.

---

## 5. Descripción del evento

Describir qué ocurrió de manera clara, cronológica y basada en evidencia.

### Ejemplo - Autenticación

Se detectaron múltiples intentos fallidos de autenticación contra el usuario `[usuario]` desde la IP `[IP]`.

Posteriormente, se observó un acceso exitoso desde la misma IP contra el mismo usuario.

Esta secuencia representa una señal de posible compromiso, pero debe validarse con evidencia adicional antes de confirmar un acceso no autorizado.

### Ejemplo - Phishing

Se recibió un correo sospechoso que solicita al usuario validar credenciales mediante un enlace externo.

El mensaje presenta indicadores compatibles con phishing, como urgencia artificial, dominio no validado y solicitud de información sensible.

---

## 6. Línea de tiempo

| Fecha | Hora | Evento |
|---|---|---|
| `YYYY-MM-DD` | `HH:MM` | Se detecta la alerta |
| `YYYY-MM-DD` | `HH:MM` | Se revisa evidencia inicial |
| `YYYY-MM-DD` | `HH:MM` | Se identifica el activo afectado |
| `YYYY-MM-DD` | `HH:MM` | Se identifica actividad relacionada |
| `YYYY-MM-DD` | `HH:MM` | Se aplican acciones autorizadas |
| `YYYY-MM-DD` | `HH:MM` | Se escala o cierra el caso |

---

## 7. Evidencia observada

Registrar los elementos que respaldan el análisis.

### Evidencia posible

- IP de origen.
- Usuario afectado.
- Sistema afectado.
- Remitente.
- Dominio.
- URL.
- Adjuntos.
- Logs relevantes.
- Capturas, si aplica.
- Fecha y hora de eventos.
- Resultado de autenticación.
- Acciones realizadas por el usuario.
- Actividad posterior al evento.

### Tabla de evidencia

| Evidencia | Detalle | Observación |
|---|---|---|
| IP origen | `[IP]` | `[Descripción]` |
| Usuario | `[usuario]` | `[Descripción]` |
| Dominio | `[dominio.test]` | `[Descripción]` |
| URL | `[URL]` | `[Descripción]` |
| Log | `[línea o archivo]` | `[Descripción]` |
| Archivo adjunto | `[nombre]` | `[Descripción]` |

---

## 8. Indicadores relevantes

Listar indicadores técnicos o señales sospechosas identificadas durante el análisis.

| Indicador | Tipo | Observación |
|---|---|---|
| `[IP]` | IP | Dirección involucrada en la actividad |
| `[dominio.test]` | Dominio | Dominio sospechoso o no validado |
| `[URL]` | URL | Enlace observado |
| `[usuario]` | Cuenta | Usuario afectado |
| `[hash]` | Hash | Hash de archivo, si aplica |
| `[archivo]` | Archivo | Adjunto o archivo sospechoso |

Importante:

Un indicador aislado no confirma necesariamente que exista un compromiso. Debe analizarse dentro del contexto del caso y junto con el resto de la evidencia.

---

## 9. Análisis técnico

Explicar la interpretación de la evidencia.

Preguntas a responder:

- ¿Qué patrón se observa?
- ¿La actividad parece normal o sospechosa?
- ¿Existe repetición?
- ¿Qué IP y usuario están relacionados?
- ¿Afecta a una cuenta privilegiada?
- ¿Existe acceso exitoso posterior?
- ¿Existe correlación entre distintos eventos?
- ¿El usuario interactuó con un correo o enlace?
- ¿Se ingresaron credenciales?
- ¿Se ejecutó algún archivo?
- ¿Existe impacto confirmado?
- ¿Se requiere contención?
- ¿Se debe escalar?
- ¿Qué evidencia adicional sería necesaria?

### Resumen del análisis

La evidencia observada indica `[describir interpretación]`.

El caso se considera `[evento / alerta / posible incidente / incidente confirmado]` debido a `[motivo]`.

La evidencia disponible `[permite / no permite]` confirmar un compromiso.

---

## 10. Clasificación del caso

| Campo | Valor |
|---|---|
| Tipo | `Evento / Alerta / Posible incidente / Incidente confirmado` |
| Categoría | `Phishing / Fuerza bruta / Malware / Acceso no autorizado / Otro` |
| Severidad | `Baja / Media / Alta / Crítica` |
| Activo afectado | `Usuario / Cuenta / Servidor / Correo / Sistema` |
| Impacto | `Sin impacto / Bajo / Medio / Alto / Crítico` |
| Estado | `Abierto / En revisión / Escalado / Cerrado` |

---

## 11. Evaluación de severidad

Justificar por qué se asignó una determinada severidad.

| Severidad | Criterio |
|---|---|
| Baja | Actividad aislada o por debajo del umbral, sin evidencia relevante de compromiso |
| Media | Actividad sospechosa que requiere revisión |
| Alta | Posible compromiso, actividad relevante o interacción que aumenta significativamente el riesgo |
| Crítica | Credenciales expuestas, ejecución de malware, compromiso confirmado o impacto grave |

Severidad asignada:

`[Baja / Media / Alta / Crítica]`

Justificación:

La severidad se asigna como `[nivel]` debido a `[motivo principal]`.

Importante:

La severidad puede cambiar durante la investigación si aparece nueva evidencia.

---

## 12. Impacto potencial y observado

### Impacto potencial

Describir qué podría ocurrir si la amenaza se confirma.

Posibles impactos:

- Compromiso de credenciales.
- Acceso no autorizado.
- Exposición de información.
- Movimiento lateral.
- Envío de correos maliciosos.
- Instalación o ejecución de malware.
- Interrupción de servicio.
- Escalamiento de privilegios.
- Afectación de sistemas críticos.

### Impacto observado

`[Describir el impacto confirmado o indicar explícitamente que no existe impacto confirmado]`

Ejemplo:

`No existe impacto confirmado con la evidencia actualmente disponible.`

---

## 13. Acciones realizadas

Registrar únicamente acciones que realmente hayan sido ejecutadas.

| Acción | Responsable | Estado |
|---|---|---|
| Revisión de evidencia inicial | `[analista/equipo]` | `Completado` |
| Validación de usuario afectado | `[analista/equipo]` | `Pendiente / Completado` |
| Bloqueo de IP o dominio | `[analista/equipo]` | `No aplica / Pendiente / Completado` |
| Cambio de contraseña | `[analista/equipo]` | `No aplica / Pendiente / Completado` |
| Revocación de sesiones | `[analista/equipo]` | `No aplica / Pendiente / Completado` |
| Escalamiento | `[analista/equipo]` | `No aplica / Pendiente / Completado` |

Importante:

No registrar como realizada una acción que únicamente haya sido recomendada.

---

## 14. Acciones recomendadas

Listar acciones sugeridas para investigar, contener o prevenir.

Acciones posibles:

1. Validar si la actividad fue autorizada.
2. Revisar logs adicionales.
3. Revisar actividad anterior y posterior al evento.
4. Bloquear una IP, dominio o URL sospechosa si corresponde.
5. Cambiar credenciales si existe riesgo de exposición.
6. Revocar sesiones activas cuando corresponda.
7. Validar o restablecer MFA.
8. Revisar reglas de correo y reenvío.
9. Revisar actividad posterior del usuario.
10. Aislar un equipo si existe sospecha de malware.
11. Preservar evidencia relevante.
12. Escalar al equipo responsable.
13. Documentar el cierre del caso.
14. Aplicar mejoras preventivas.

En un entorno real, las acciones de contención deben ejecutarse según procedimientos internos, permisos y autorización correspondiente.

---

## 15. Criterios de escalamiento

Escalar el caso si ocurre alguna de estas condiciones:

- Usuario privilegiado afectado.
- Login exitoso posterior a múltiples intentos fallidos.
- Credenciales ingresadas en un sitio sospechoso.
- Ejecución de un archivo sospechoso.
- Múltiples usuarios afectados.
- Actividad repetida desde una misma IP.
- Dominio o URL confirmado como malicioso.
- Evidencia de acceso no autorizado.
- Evidencia de compromiso de cuenta o sistema.
- Actividad posterior sospechosa.
- Impacto en sistemas críticos.
- Falta de evidencia suficiente para determinar la legitimidad de una actividad de alto riesgo.

---

## 16. Evidencia adicional necesaria

Indicar qué información sería necesaria para confirmar o descartar las hipótesis del análisis.

Ejemplos:

- Logs adicionales.
- Historial de accesos.
- Actividad posterior del usuario.
- Sesiones activas.
- Cabeceras completas de correo.
- Alertas SIEM o EDR.
- Registros de endpoint.
- Cambios de archivos o configuraciones.
- Acciones realizadas durante una sesión.
- Información sobre legitimidad del acceso.
- Evidencia de otros sistemas afectados.

---

## 17. Estado del caso

| Campo | Estado |
|---|---|
| Caso abierto | `Sí / No` |
| Caso escalado | `Sí / No` |
| Contención aplicada | `Sí / No / No aplica` |
| Compromiso confirmado | `Sí / No / En revisión` |
| Impacto confirmado | `Sí / No / En revisión` |
| Requiere seguimiento | `Sí / No` |
| Estado final | `Abierto / En revisión / Escalado / Cerrado` |

---

## 18. Conclusión

Redactar una conclusión clara, basada exclusivamente en la evidencia disponible.

Ejemplo:

El análisis permitió identificar actividad sospechosa relacionada con `[tipo de amenaza]`.

Según la evidencia observada, el caso se clasifica como `[evento / alerta / posible incidente / incidente confirmado]` con severidad `[nivel]`.

Actualmente `[existe / no existe]` evidencia suficiente para confirmar un compromiso.

Se recomiendan acciones de `[investigación / contención / prevención / escalamiento]` para reducir el riesgo y determinar el alcance real del caso.

---

## 19. Resumen técnico

Redactar una versión breve y profesional del análisis.

Ejemplo:

Se analizó evidencia asociada a `[tipo de caso]` y se identificaron `[indicadores principales]`.

El caso fue clasificado como `[evento / alerta / posible incidente / incidente confirmado]` con severidad `[nivel]` debido a `[motivo principal]`.

La evidencia disponible `[permite / no permite]` confirmar un compromiso.

Se documentaron acciones realizadas, recomendaciones, evidencia adicional necesaria y criterios de escalamiento.