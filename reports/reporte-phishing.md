# Reporte técnico - Análisis de phishing

## 1. Resumen ejecutivo

Durante el análisis de un correo sospechoso simulado, se identificaron múltiples indicadores compatibles con phishing orientado al robo de credenciales corporativas.

El mensaje aparenta provenir de un área de soporte o seguridad interna, pero utiliza un dominio no validado, aplica presión mediante urgencia artificial y solicita al usuario validar sus credenciales a través de un enlace sospechoso.

Debido a que no existe evidencia de que el usuario haya interactuado con el enlace ni entregado credenciales, el caso se clasifica como una alerta de phishing de severidad Media.

---

## 2. Fuente de información

| Elemento | Detalle |
|---|---|
| Caso relacionado | `cases/01-phishing.md` |
| Tipo de análisis | Correo sospechoso |
| Vector | Correo electrónico |
| Tipo de amenaza | Phishing |
| Riesgo principal | Robo de credenciales |
| Entorno | Laboratorio simulado |

---

## 3. Alcance del análisis

El análisis se enfocó en revisar:

- Remitente.
- Asunto.
- Cuerpo del mensaje.
- Enlace incluido.
- Urgencia del mensaje.
- Solicitud de credenciales.
- Riesgo para la cuenta corporativa.
- Posible interacción del usuario.
- Acciones recomendadas.

Este reporte corresponde a un laboratorio simulado y no incluye análisis técnico real de cabeceras, reputación del dominio, sandboxing, inteligencia de amenazas ni revisión de infraestructura externa.

---

## 4. Correo analizado

| Campo | Valor |
|---|---|
| Remitente | `soporte-seguridad@empresa-validacion.test` |
| Destinatario | `usuario@empresa.test` |
| Asunto | `Acción requerida: valide su cuenta antes del cierre del día` |
| URL observada | `https://empresa-validacion.test/login-seguro` |

Resumen del mensaje:

El correo informa una supuesta actividad inusual en la cuenta del usuario y solicita validar credenciales antes del cierre del día para evitar la suspensión del acceso.

El mensaje utiliza presión y urgencia para inducir una acción rápida.

---

## 5. Indicadores observados

| Indicador | Observación | Riesgo |
|---|---|---|
| Dominio sospechoso | El remitente utiliza `empresa-validacion.test`, dominio no validado como oficial | Medio / Alto |
| Urgencia artificial | El mensaje exige acción antes del cierre del día | Medio |
| Solicitud de credenciales | El usuario es dirigido a validar información sensible | Alto |
| Enlace externo | El enlace apunta a un dominio no confirmado como legítimo | Alto |
| Amenaza de bloqueo | Se presiona al usuario indicando que su cuenta será suspendida | Medio |
| Mensaje genérico | No incluye nombre real ni contexto específico verificable | Medio |

La combinación de estos indicadores aumenta la probabilidad de que el mensaje corresponda a phishing.

---

## 6. Análisis del enlace

URL observada:

`https://empresa-validacion.test/login-seguro`

Observaciones:

- El dominio debe validarse antes de interactuar.
- El uso de HTTPS no confirma legitimidad.
- El nombre del dominio puede intentar aparentar una relación con la organización.
- El enlace podría conducir a una página destinada a capturar credenciales.
- La URL no debe abrirse directamente desde el correo durante un análisis básico.
- En este laboratorio, el dominio `.test` se utiliza exclusivamente como parte del escenario simulado.

Conclusión:

El enlace debe considerarse sospechoso hasta validar su legitimidad mediante canales oficiales o herramientas de análisis seguras.

---

## 7. Evaluación de riesgo

El principal riesgo identificado es la exposición de credenciales corporativas.

Si un usuario ingresara sus datos en un sitio fraudulento, un atacante podría intentar:

- Acceder al correo corporativo.
- Consultar información interna.
- Enviar nuevos mensajes de phishing desde una cuenta legítima.
- Acceder a otros servicios asociados a la identidad.
- Aprovechar permisos disponibles en la cuenta.
- Realizar nuevas acciones utilizando una identidad comprometida.

Estos escenarios representan impactos potenciales y no indican que hayan ocurrido dentro de este caso simulado.

---

## 8. Clasificación del caso

| Campo | Valor |
|---|---|
| Tipo | Alerta de phishing |
| Severidad | Media |
| Vector | Correo electrónico |
| Activo afectado | Cuenta corporativa |
| Impacto potencial | Exposición de credenciales |
| Estado | Requiere revisión |

### Justificación

El mensaje presenta múltiples indicadores compatibles con phishing:

- urgencia artificial;
- solicitud de credenciales;
- dominio no validado;
- enlace externo;
- amenaza de bloqueo.

Sin embargo, no existe evidencia de interacción del usuario, exposición de credenciales o compromiso de cuenta.

Por este motivo, el caso permanece clasificado como alerta de severidad Media.

---

## 9. Evolución de la clasificación

La clasificación puede cambiar según la interacción del usuario y la evidencia disponible.

| Situación | Clasificación | Severidad sugerida |
|---|---|---|
| Usuario recibe el correo y no interactúa | Alerta | Media |
| Usuario hace clic en el enlace | Alerta | Alta |
| Usuario ingresa credenciales | Posible incidente | Crítica |
| Cuenta es utilizada por un tercero no autorizado | Incidente confirmado | Crítica |

El hecho de hacer clic o ingresar credenciales aumenta el riesgo.

La confirmación de un incidente requiere evidencia suficiente de compromiso o impacto.

---

## 10. Acciones recomendadas

Importante:

En un entorno real, acciones como bloqueo de dominios, revocación de sesiones o cambios de contraseña deben ejecutarse según procedimientos internos y autorización correspondiente.

Acciones iniciales:

1. No hacer clic en el enlace.
2. No ingresar credenciales.
3. Reportar el correo al equipo de seguridad o soporte TI.
4. Validar el dominio oficial de la organización mediante un canal confiable.
5. Buscar mensajes similares en otros buzones.
6. Bloquear o filtrar remitente, dominio o URL si corresponde.
7. Revisar si algún usuario interactuó con el enlace.
8. Revisar accesos recientes si existió interacción.
9. Cambiar credenciales si existe evidencia de que fueron ingresadas en el sitio sospechoso.
10. Revocar sesiones activas si existe riesgo de compromiso.
11. Validar o restablecer MFA si corresponde.
12. Escalar el caso si aparecen señales adicionales de posible compromiso.
13. Documentar el análisis y las acciones realizadas.

---

## 11. Evidencia que se debería recopilar

Para completar el análisis en un entorno real, se debería recopilar:

- Remitente completo.
- Destinatario.
- Asunto.
- Fecha y hora de recepción.
- Cuerpo completo del mensaje.
- URL incluida.
- Cabeceras del correo.
- Adjuntos, si existen.
- Usuarios que recibieron el mensaje.
- Usuarios que hicieron clic.
- Usuarios que ingresaron credenciales.
- Registros de acceso posteriores.
- Sesiones activas o accesos sospechosos.
- Evidencia de reglas de bloqueo o contención aplicadas.

La evidencia debe preservarse según los procedimientos establecidos por la organización.

---

## 12. Acciones según interacción del usuario

### Usuario no interactuó

- Mantener el caso como alerta.
- Reportar y documentar el mensaje.
- Buscar correos similares.
- Aplicar bloqueo o filtrado si corresponde.

### Usuario hizo clic

- Aumentar la severidad a Alta.
- Revisar la URL visitada.
- Validar si se ingresaron credenciales.
- Revisar accesos y sesiones posteriores.
- Escalar si aparece actividad anómala.

### Usuario ingresó credenciales

- Clasificar como posible incidente.
- Cambiar credenciales según procedimiento.
- Revocar sesiones activas.
- Revisar MFA.
- Revisar accesos posteriores.
- Escalar para investigación adicional.

### Compromiso confirmado

Si existe evidencia suficiente de uso no autorizado de la cuenta:

- Clasificar como incidente confirmado.
- Ejecutar acciones de contención autorizadas.
- Determinar alcance e impacto.
- Preservar evidencia.
- Escalar según procedimiento.
- Documentar la investigación.

---

## 13. Recomendaciones preventivas

Para reducir el riesgo de phishing, se recomienda:

- Activar MFA en cuentas corporativas.
- Capacitar a usuarios en detección de correos sospechosos.
- Implementar filtros antiphishing.
- Bloquear dominios maliciosos o sospechosos cuando corresponda.
- Crear canales claros para reportar mensajes sospechosos.
- Revisar reglas de correo y reenvío automático.
- Monitorear accesos desde ubicaciones o dispositivos inusuales.
- Aplicar principio de mínimo privilegio.
- Definir procedimientos de respuesta ante phishing.
- Realizar simulaciones internas de concientización.

---

## 14. Limitaciones

Este reporte corresponde a un laboratorio educativo basado en un correo completamente simulado.

El análisis no incluye:

- cabeceras reales del mensaje;
- reputación real del dominio;
- sandboxing;
- inteligencia de amenazas;
- análisis de malware;
- logs reales de identidad;
- información real de usuarios;
- análisis forense;
- validación mediante SIEM o EDR.

Por este motivo, la clasificación representa un ejercicio de análisis inicial y documentación y no una investigación completa de producción.

---

## 15. Conclusión

El correo analizado presenta múltiples señales compatibles con phishing, incluyendo urgencia artificial, solicitud de credenciales, amenaza de bloqueo y uso de un enlace hacia un dominio no validado.

Debido a que no existe evidencia de interacción del usuario ni exposición de credenciales, el caso se mantiene como una alerta de phishing de severidad Media.

La prioridad consiste en evitar la interacción con el mensaje, reportarlo, revisar si existen otros usuarios afectados y escalar el análisis si aparece evidencia de exposición de credenciales o actividad anómala posterior.

---

## 16. Resumen técnico

Se analizó un correo sospechoso simulado orientado al robo de credenciales corporativas.

El mensaje utiliza urgencia artificial, solicitud de información sensible, un dominio no validado y un enlace externo para inducir al usuario a realizar una acción.

El caso fue clasificado como alerta de phishing de severidad Media debido a que no existe evidencia de interacción del usuario ni compromiso confirmado.

Se documentaron indicadores, riesgo potencial, acciones de respuesta, evidencia necesaria, criterios de evolución del caso y medidas preventivas.