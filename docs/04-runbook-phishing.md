# Runbook - Respuesta básica ante phishing

## Objetivo

Definir un procedimiento básico para analizar y responder ante un correo sospechoso o posible phishing.

Este runbook está orientado a un contexto junior de operaciones de seguridad, soporte TI, monitoreo o gestión inicial de incidentes.

---

## 1. Contexto del runbook

El phishing es una técnica de engaño utilizada para obtener información sensible, como credenciales, datos personales o acceso a sistemas.

Normalmente llega por correo electrónico, aunque también puede aparecer mediante mensajería, SMS, redes sociales o plataformas colaborativas.

Este runbook usa como referencia el caso:

- `cases/01-phishing.md`

Y el reporte:

- `reports/reporte-phishing.md`

---

## 2. Tipo de alerta

| Campo | Detalle |
|---|---|
| Nombre de alerta | Correo sospechoso / posible phishing |
| Vector | Correo electrónico |
| Posible amenaza | Robo de credenciales |
| Activo afectado | Cuenta corporativa |
| Severidad inicial | Media |
| Estado inicial | Requiere revisión |

---

## 3. Objetivo del análisis

El objetivo es determinar si el correo corresponde a:

| Clasificación | Descripción |
|---|---|
| Correo legítimo | Mensaje esperado y confiable |
| Correo sospechoso | Presenta señales dudosas que requieren revisión |
| Alerta de phishing | Presenta indicadores claros compatibles con phishing |
| Posible incidente | Existe interacción del usuario o exposición potencial |
| Incidente confirmado | Existe evidencia suficiente de compromiso o impacto |

La clasificación puede cambiar a medida que aparece nueva evidencia durante el análisis.

---

## 4. Procedimiento de análisis

### Paso 1 - Registrar información básica

Antes de tomar acciones, registrar los datos principales del correo.

Datos mínimos:

- Remitente.
- Destinatario.
- Asunto.
- Fecha y hora de recepción.
- Cuerpo del mensaje.
- Enlaces incluidos.
- Adjuntos, si existen.
- Usuario que reporta el correo.

Preguntas clave:

- ¿Quién envió el correo?
- ¿Quién lo recibió?
- ¿Qué solicita el mensaje?
- ¿Incluye enlaces o adjuntos?
- ¿Pide credenciales, dinero, datos o una acción urgente?

---

### Paso 2 - Revisar el remitente

Analizar la dirección del remitente.

Elementos a revisar:

- Dominio del correo.
- Errores sutiles en el nombre del dominio.
- Remitente externo haciéndose pasar por interno.
- Nombre visible distinto al correo real.
- Dominio parecido al oficial, pero no igual.

Ejemplo:

| Remitente | Observación |
|---|---|
| `soporte@empresa.test` | Podría ser legítimo si pertenece al dominio oficial |
| `soporte-seguridad@empresa-validacion.test` | Sospechoso si no pertenece a la empresa |
| `soporte@empresaa.test` | Sospechoso por posible typosquatting |

Conclusión:

Un nombre visible confiable no basta. Se debe revisar la dirección real del remitente y validar el dominio.

---

### Paso 3 - Revisar el asunto y tono del mensaje

Identificar señales de presión, manipulación o ingeniería social.

Indicadores comunes:

- Urgencia artificial.
- Amenaza de bloqueo.
- Premios o beneficios inesperados.
- Solicitud de acción inmediata.
- Mensaje genérico.
- Errores de redacción.
- Lenguaje que busca generar miedo o apuro.

Ejemplos:

| Señal | Riesgo |
|---|---|
| “Su cuenta será suspendida hoy” | Presión mediante miedo |
| “Valide sus credenciales ahora” | Posible robo de credenciales |
| “Última advertencia” | Urgencia artificial |
| “Ha ganado un premio” | Engaño mediante recompensa |

---

### Paso 4 - Revisar enlaces

No se debe hacer clic directamente en enlaces sospechosos.

Elementos a revisar:

- Dominio real del enlace.
- Coincidencia con el dominio oficial.
- Enlaces acortados.
- Redirecciones sospechosas.
- Páginas que solicitan credenciales.
- Uso de nombres parecidos al dominio legítimo.

Ejemplo:

| URL | Observación |
|---|---|
| `https://empresa.test/login` | Podría ser legítima si corresponde al dominio oficial |
| `https://empresa-validacion.test/login-seguro` | Sospechosa si no pertenece a la organización |
| `https://short.example/validar-cuenta` | Ejemplo simulado de enlace acortado o redirección sospechosa |

Importante:

Que una página utilice HTTPS no significa que sea legítima. HTTPS indica que la comunicación está cifrada, pero no demuestra que el sitio pertenezca realmente a la organización.

---

### Paso 5 - Revisar adjuntos

Si el correo incluye archivos adjuntos, deben tratarse con precaución.

Extensiones o formatos que requieren mayor atención:

- `.exe`
- `.scr`
- `.bat`
- `.cmd`
- `.js`
- `.vbs`
- `.zip`
- `.rar`
- documentos con macros

Preguntas clave:

- ¿El adjunto era esperado?
- ¿El remitente es confiable?
- ¿El archivo tiene doble extensión?
- ¿El nombre busca generar urgencia?
- ¿Solicita habilitar macros o contenido?
- ¿El archivo corresponde al contexto del mensaje?

Ejemplos sospechosos:

| Archivo | Riesgo |
|---|---|
| `Factura.exe` | Archivo ejecutable inesperado |
| `Documento.pdf.exe` | Doble extensión |
| `Liquidacion.zip` | Archivo comprimido que requiere revisión |
| `Informe.docm` | Documento con macros |

---

### Paso 6 - Identificar solicitud del mensaje

Determinar qué busca conseguir el correo.

Solicitudes comunes en phishing:

- Validar credenciales.
- Cambiar contraseña mediante un enlace.
- Descargar un archivo.
- Habilitar macros.
- Transferir dinero.
- Confirmar datos personales.
- Aprobar una operación urgente.
- Escanear un código QR.
- Contactar mediante un canal externo.
- Aprobar una solicitud MFA o entregar un código.

Mayor riesgo:

| Solicitud | Riesgo |
|---|---|
| Ingresar usuario y contraseña | Robo de credenciales |
| Abrir adjunto ejecutable | Ejecución de malware |
| Habilitar macros | Ejecución de código |
| Transferir dinero | Fraude |
| Confirmar MFA o entregar código | Toma de cuenta |

---

### Paso 7 - Consultar interacción del usuario

Este paso es fundamental para determinar la clasificación y severidad del caso.

Preguntar o revisar:

- ¿El usuario abrió el correo?
- ¿Hizo clic en el enlace?
- ¿Ingresó credenciales?
- ¿Descargó algún archivo?
- ¿Ejecutó algún adjunto?
- ¿Aprobó una solicitud MFA?
- ¿Ingresó algún código de autenticación?
- ¿Reportó actividad extraña después?

Clasificación inicial:

| Acción del usuario | Clasificación | Severidad sugerida |
|---|---|---|
| Solo recibió el correo | Alerta | Media |
| Abrió el correo sin interactuar | Alerta | Media |
| Hizo clic en el enlace | Alerta | Alta |
| Descargó un archivo sin ejecutarlo | Alerta | Alta |
| Ingresó credenciales | Posible incidente | Crítica |
| Ejecutó un adjunto sospechoso | Posible incidente | Crítica |
| Cuenta utilizada por un tercero no autorizado | Incidente confirmado | Crítica |

Importante:

La interacción del usuario aumenta el riesgo, pero la clasificación final debe basarse en toda la evidencia disponible.

---

### Paso 8 - Clasificar severidad

Asignar severidad según evidencia, interacción e impacto.

| Severidad | Criterio |
|---|---|
| Baja | Correo sospechoso aislado con indicadores limitados y sin interacción |
| Media | Indicadores claros de phishing sin interacción relevante del usuario |
| Alta | Usuario hizo clic, descargó contenido o existen múltiples usuarios afectados |
| Crítica | Credenciales expuestas, ejecución de contenido malicioso, compromiso confirmado o impacto grave |

Ejemplos:

Si el usuario recibió un correo con indicadores claros de phishing pero no interactuó, el caso puede clasificarse como una alerta de severidad Media.

Si el usuario hizo clic en el enlace pero no ingresó información, la severidad aumenta a Alta y se requiere revisar actividad posterior.

Si el usuario ingresó credenciales en el sitio sospechoso, el caso debe tratarse como posible incidente de severidad Crítica debido a la exposición de credenciales.

Si posteriormente se confirma que un tercero utilizó esas credenciales, el caso pasa a incidente confirmado.

---

## 5. Acciones según escenario

Importante:

En un entorno real, acciones como bloqueo de dominios, revocación de sesiones, aislamiento de equipos o cambios de contraseña deben ejecutarse según procedimientos internos, permisos y autorización del equipo responsable.

### Escenario A - Usuario no interactuó

Acciones recomendadas:

1. Indicar al usuario que no haga clic ni responda.
2. Reportar el correo al equipo de seguridad o soporte TI.
3. Marcar el correo como phishing o sospechoso.
4. Buscar mensajes similares.
5. Bloquear o filtrar remitente, dominio o URL si corresponde.
6. Documentar el caso.

---

### Escenario B - Usuario hizo clic en el enlace

Acciones recomendadas:

1. Confirmar la URL visitada.
2. Revisar fecha y hora de interacción.
3. Validar si se ingresaron credenciales.
4. Revisar accesos recientes de la cuenta.
5. Revisar sesiones activas.
6. Buscar actividad anómala posterior.
7. Aplicar un cambio preventivo de contraseña si el contexto lo justifica.
8. Escalar si aparecen señales de posible compromiso.
9. Documentar las acciones realizadas.

---

### Escenario C - Usuario ingresó credenciales

Acciones recomendadas:

1. Cambiar la contraseña inmediatamente según procedimiento.
2. Revocar sesiones activas.
3. Validar o restablecer MFA si corresponde.
4. Revisar accesos recientes.
5. Revisar ubicaciones y dispositivos utilizados.
6. Revisar reglas de correo sospechosas.
7. Revisar reenvíos automáticos.
8. Buscar actividad anómala posterior.
9. Bloquear dominio o URL si corresponde.
10. Buscar correos similares en la organización.
11. Preservar evidencia relevante.
12. Escalar como posible incidente.

---

### Escenario D - Usuario descargó o ejecutó un adjunto

Acciones recomendadas:

1. Determinar si el archivo fue únicamente descargado o también ejecutado.
2. Aislar el equipo si existe sospecha de malware y el procedimiento lo autoriza.
3. No borrar evidencia sin autorización.
4. Registrar nombre, ruta y características del archivo.
5. Revisar alertas del antivirus o EDR.
6. Revisar procesos sospechosos.
7. Revisar conexiones de red relacionadas.
8. Revisar actividad posterior del sistema.
9. Escalar al equipo correspondiente.
10. Documentar las acciones realizadas.

---

### Escenario E - Compromiso confirmado

Si existe evidencia suficiente de que una cuenta o sistema fue comprometido:

1. Escalar inmediatamente según el procedimiento interno.
2. Aplicar las acciones de contención autorizadas.
3. Preservar evidencia.
4. Determinar el alcance del compromiso.
5. Revisar actividad posterior.
6. Identificar otros usuarios o sistemas afectados.
7. Documentar una línea de tiempo.
8. Mantener seguimiento hasta el cierre del incidente.

---

## 6. Evidencia a recopilar

Evidencia mínima:

- Correo original.
- Remitente real.
- Destinatario.
- Asunto.
- Fecha y hora.
- Cuerpo del mensaje.
- URL incluida.
- Adjuntos.
- Cabeceras del correo, si están disponibles.
- Captura del correo, si aplica.
- Usuarios afectados.
- Acción realizada por el usuario.
- Logs de acceso posteriores.
- Sesiones o accesos sospechosos.
- Medidas de contención aplicadas.
- Evidencia de escalamiento, si corresponde.

La evidencia debe conservarse de acuerdo con los procedimientos de la organización y sin modificar innecesariamente los artefactos originales.

---

## 7. Criterios de escalamiento

Escalar el caso si se cumple alguna de estas condiciones:

- Usuario ingresó credenciales.
- Usuario ejecutó un archivo sospechoso.
- Hay múltiples usuarios afectados.
- La cuenta presenta accesos anómalos.
- Se detectan reglas de correo sospechosas.
- Hay reenvíos automáticos no autorizados.
- Existe una aprobación MFA sospechosa.
- Hay sospecha de malware.
- El correo suplanta a un área crítica.
- El caso afecta cuentas privilegiadas.
- Existe evidencia de acceso no autorizado.
- El impacto o alcance no puede determinarse con la evidencia disponible.

El escalamiento permite que un analista o equipo con mayor capacidad de investigación continúe el análisis cuando el riesgo o la incertidumbre lo justifican.

---

## 8. Cierre del caso

Antes de cerrar, documentar:

- Qué ocurrió.
- Qué indicadores se observaron.
- Qué usuario o usuarios fueron afectados.
- Si hubo interacción.
- Qué clasificación se asignó.
- Qué severidad se asignó.
- Qué evidencia se revisó.
- Qué acciones se realizaron.
- Qué acciones quedaron pendientes.
- Si se escaló o no.
- Qué limitaciones tuvo el análisis.
- Recomendaciones preventivas.

Ejemplo de cierre:

El correo fue clasificado como alerta de phishing debido a un dominio no validado, solicitud de credenciales y urgencia artificial. El usuario no interactuó con el enlace, por lo que no existe evidencia de exposición de credenciales ni compromiso de cuenta. Se recomendó reportar el mensaje, buscar correos similares y mantener monitoreo.

---

## 9. Recomendaciones preventivas

Para reducir el riesgo de phishing:

- Activar MFA.
- Capacitar a los usuarios.
- Crear un canal claro de reporte.
- Implementar filtros antiphishing.
- Bloquear dominios o URLs maliciosas cuando corresponda.
- Revisar accesos anómalos.
- Revisar reglas de correo y reenvío.
- Mantener procedimientos documentados.
- Realizar simulaciones controladas.
- Fomentar una cultura de reporte temprano.
- Aplicar principios de mínimo privilegio.
- Mantener sistemas y herramientas de seguridad actualizados.

---

## 10. Resumen del procedimiento

1. Registrar información básica del correo.
2. Revisar remitente.
3. Revisar asunto y tono.
4. Revisar enlaces.
5. Revisar adjuntos.
6. Identificar qué solicita el mensaje.
7. Confirmar si el usuario interactuó.
8. Clasificar el caso.
9. Asignar severidad.
10. Aplicar acciones según el escenario.
11. Recopilar evidencia.
12. Escalar si corresponde.
13. Documentar el cierre.

Flujo simplificado:

```text
correo sospechoso
↓
indicadores
↓
interacción del usuario
↓
clasificación
↓
severidad
↓
acciones
↓
evidencia
↓
escalamiento
↓
cierre
```

---

## 11. Limitaciones

Este runbook corresponde a un laboratorio educativo y representa una guía básica de análisis inicial.

No sustituye:

- procedimientos internos de una organización;
- análisis forense;
- herramientas de seguridad empresariales;
- análisis completo de cabeceras;
- sandboxing;
- inteligencia de amenazas;
- análisis de malware;
- investigación de identidad completa.

Las decisiones de bloqueo, aislamiento, revocación de sesiones o modificación de credenciales deben realizarse según autorización y procedimientos internos.

---

## 12. Resumen técnico

Este runbook define un procedimiento básico para analizar y responder ante correos sospechosos o posibles casos de phishing.

El flujo incluye revisión del remitente, contenido, enlaces, adjuntos, solicitud del mensaje e interacción del usuario. A partir de la evidencia disponible, el caso se clasifica como alerta, posible incidente o incidente confirmado y se asigna una severidad según el riesgo e impacto.

La respuesta incluye acciones según escenario, recopilación de evidencia, criterios de escalamiento y cierre documentado, evitando considerar un compromiso como confirmado hasta disponer de evidencia suficiente.