# Caso 01 - Análisis básico de phishing

## Objetivo

Analizar un correo sospechoso simulado para identificar señales de phishing, evaluar el riesgo y documentar acciones recomendadas.

---

## 1. Contexto del caso

Se recibe un correo que aparenta provenir del área de soporte interno de una empresa.

El mensaje solicita al usuario validar sus credenciales mediante un enlace externo debido a una supuesta actualización urgente de seguridad.

Este caso es simulado y tiene fines educativos dentro del laboratorio SOC Junior Lab.

---

## 2. Correo analizado

### Remitente

`soporte-seguridad@empresa-validacion.test`

### Destinatario

`usuario@empresa.test`

### Asunto

`Acción requerida: valide su cuenta antes del cierre del día`

### Cuerpo del mensaje

Estimado usuario,

Hemos detectado actividad inusual en su cuenta corporativa. Para evitar la suspensión del acceso, debe validar sus credenciales antes del cierre del día.

Ingrese al siguiente enlace para confirmar su información:

`https://empresa-validacion.test/login-seguro`

Si no realiza esta acción, su cuenta será bloqueada temporalmente.

Atentamente,  
Equipo de Soporte TI

---

## 3. Indicadores sospechosos

| Indicador | Observación |
|---|---|
| Remitente sospechoso | El dominio `empresa-validacion.test` no corresponde necesariamente al dominio oficial de la organización |
| Urgencia artificial | El correo presiona al usuario indicando que debe actuar antes del cierre del día |
| Solicitud de credenciales | El mensaje solicita validar información sensible mediante un enlace |
| Enlace externo | El enlace no apunta a un dominio corporativo confirmado como legítimo |
| Amenaza de bloqueo | Se utiliza presión para inducir una acción rápida |
| Mensaje genérico | No menciona el nombre real del usuario ni información específica que permita validar el contexto |

---

## 4. Análisis del enlace

URL observada:

`https://empresa-validacion.test/login-seguro`

Elementos a revisar:

- Dominio del enlace.
- Coincidencia con el dominio oficial.
- Uso de HTTPS.
- Similitud con dominios legítimos.
- Posibles redirecciones.
- Solicitud de credenciales.
- Reputación del dominio.

Importante:

Que un sitio utilice HTTPS no significa que sea legítimo. HTTPS indica que la comunicación está cifrada, pero no demuestra que el sitio pertenezca realmente a la organización.

En este laboratorio, el dominio utilizado termina en `.test` y corresponde exclusivamente a un escenario simulado.

---

## 5. Clasificación del caso

| Campo | Valor |
|---|---|
| Tipo | Alerta de phishing |
| Severidad | Media |
| Vector | Correo electrónico |
| Activo afectado | Cuenta corporativa del usuario |
| Riesgo principal | Robo de credenciales |
| Estado | Requiere revisión |

Justificación:

El mensaje presenta varios indicadores compatibles con phishing, incluyendo urgencia artificial, solicitud de credenciales y un enlace hacia un dominio no validado.

Sin embargo, en este escenario no existe evidencia de que el usuario haya interactuado con el enlace ni entregado credenciales. Por este motivo, el caso permanece clasificado como alerta de severidad Media.

---

## 6. Riesgo asociado

El principal riesgo es que el usuario ingrese sus credenciales en un sitio fraudulento.

Si esto ocurriera, un atacante podría:

- Acceder a la cuenta corporativa.
- Leer información interna.
- Enviar nuevos correos de phishing desde una cuenta legítima.
- Intentar acceder a otros sistemas.
- Obtener información sensible.
- Aprovechar permisos asociados a la cuenta.
- Realizar nuevas acciones utilizando la identidad comprometida.

Estos impactos representan riesgos potenciales y no significan que hayan ocurrido dentro de este caso simulado.

---

## 7. Acciones recomendadas

Acciones iniciales sugeridas:

1. No hacer clic en el enlace.
2. No ingresar credenciales.
3. Reportar el correo al equipo de seguridad o soporte TI.
4. Verificar el dominio oficial de la organización mediante un canal confiable.
5. Revisar si otros usuarios recibieron mensajes similares.
6. Bloquear o filtrar remitente, dominio o URL si corresponde.
7. Revisar logs de acceso si algún usuario interactuó con el enlace.
8. Cambiar credenciales si existe evidencia de que fueron ingresadas en el sitio sospechoso.
9. Revocar sesiones activas si existe riesgo de compromiso.
10. Validar o restablecer MFA si corresponde.
11. Documentar los hallazgos y las acciones realizadas.

Importante:

En un entorno real, acciones como bloqueo de dominios, cambio de credenciales o revocación de sesiones deben ejecutarse de acuerdo con procedimientos internos y autorización correspondiente.

---

## 8. Evidencia a recopilar

Para documentar correctamente el caso, se debería recopilar:

- Remitente.
- Destinatario.
- Asunto.
- Fecha y hora de recepción.
- Cuerpo completo del mensaje.
- URL incluida.
- Archivos adjuntos, si existen.
- Cabeceras del correo, si están disponibles.
- Usuarios que recibieron el mensaje.
- Usuarios que hicieron clic, si existe esa información.
- Usuarios que ingresaron credenciales, si corresponde.
- Logs de acceso posteriores.
- Acciones de contención realizadas.

---

## 9. Posible respuesta del equipo SOC

El equipo SOC o seguridad podría realizar las siguientes acciones:

- Analizar el dominio sospechoso.
- Revisar el enlace mediante procedimientos o herramientas seguras.
- Buscar correos similares en otros buzones.
- Crear una regla de bloqueo o filtrado si corresponde.
- Notificar a usuarios afectados.
- Revisar accesos anómalos.
- Revisar sesiones activas.
- Escalar el caso si existen señales de posible compromiso.
- Documentar el análisis y las acciones realizadas.

---

## 10. Evolución de la clasificación

La clasificación puede cambiar según la interacción del usuario y la evidencia disponible.

| Situación | Clasificación | Severidad sugerida |
|---|---|---|
| Usuario recibe el correo y no interactúa | Alerta | Media |
| Usuario hace clic en el enlace | Alerta | Alta |
| Usuario ingresa credenciales | Posible incidente | Crítica |
| Cuenta es utilizada por un tercero no autorizado | Incidente confirmado | Crítica |

El hecho de hacer clic o ingresar credenciales aumenta el riesgo, pero la confirmación de un incidente requiere evidencia adicional de compromiso o impacto.

---

## 11. Limitaciones del análisis

Este caso corresponde a un laboratorio educativo y utiliza información completamente simulada.

No se realizó:

- análisis técnico real de cabeceras;
- consulta de reputación del dominio;
- sandboxing;
- análisis de infraestructura externa;
- análisis forense;
- revisión de actividad real de una cuenta;
- validación mediante herramientas SIEM o EDR.

Por este motivo, el caso representa una práctica de análisis inicial y documentación, no una investigación completa de producción.

---

## 12. Conclusión

El correo analizado presenta múltiples señales compatibles con phishing, incluyendo urgencia artificial, solicitud de credenciales, dominio no validado, enlace externo y amenaza de bloqueo de cuenta.

Debido a que no existe evidencia de interacción del usuario ni exposición de credenciales, el caso se mantiene como una alerta de severidad Media.

La respuesta recomendada consiste en evitar la interacción con el mensaje, reportarlo, revisar si existen usuarios adicionales afectados y escalar el análisis si aparece evidencia de exposición de credenciales o actividad anómala posterior.

---

## 13. Resumen técnico

Se analizó un correo sospechoso simulado orientado al robo de credenciales. Se identificaron indicadores compatibles con phishing, como urgencia artificial, solicitud de información sensible y uso de un dominio no validado.

El caso fue clasificado como alerta de severidad Media debido a que no existe evidencia de interacción del usuario ni compromiso confirmado. Se propusieron acciones de revisión, prevención, recopilación de evidencia y escalamiento en caso de aparecer señales adicionales de posible compromiso.