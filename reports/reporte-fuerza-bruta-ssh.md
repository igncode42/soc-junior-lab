# Reporte técnico - Posible fuerza bruta SSH

## 1. Resumen ejecutivo

Durante el análisis de logs simulados de autenticación SSH en el servidor `server01`, se identificaron múltiples intentos fallidos de inicio de sesión desde distintas direcciones IP.

El hallazgo más relevante corresponde a la IP `192.0.2.15`, desde donde se observaron cinco intentos fallidos contra el usuario `root`, seguidos posteriormente por un inicio de sesión exitoso desde la misma IP hacia la misma cuenta.

Esta secuencia representa una señal relevante de posible compromiso y requiere investigación prioritaria.

Sin embargo, el patrón por sí solo no confirma que el acceso haya sido realizado por un atacante. La legitimidad del login debe validarse mediante evidencia adicional.

---

## 2. Fuente de información

| Elemento | Detalle |
|---|---|
| Archivo analizado | `logs/auth_sample.log` |
| Tipo de log | Autenticación SSH |
| Servidor | `server01` |
| Tipo de laboratorio | Simulado |
| Caso relacionado | `cases/02-fuerza-bruta-ssh.md` |

Los datos utilizados en este análisis son simulados y tienen fines exclusivamente educativos.

---

## 3. Alcance del análisis

El análisis se centró en identificar:

- Intentos fallidos de autenticación.
- Direcciones IP con múltiples fallos.
- Usuarios objetivo.
- Actividad repetida desde una misma IP.
- Inicios de sesión exitosos posteriores a fallos.
- Correlación entre IP y usuario.
- Posibles alertas de fuerza bruta.
- Señales de posible compromiso.

El análisis no busca confirmar automáticamente un incidente, sino identificar patrones que requieran investigación adicional.

---

## 4. Hallazgos principales

### Hallazgo 1 - IP `203.0.113.45`

Se detectaron siete intentos fallidos desde la IP `203.0.113.45`.

Usuarios objetivo:

- `root`
- `test`
- `soporte`

Distribución:

- `root`: 5 intentos fallidos.
- `test`: 1 intento fallido.
- `soporte`: 1 intento fallido.

### Interpretación

La IP intentó autenticarse contra distintos usuarios, incluyendo una cuenta privilegiada como `root`.

La repetición de intentos y la presencia de múltiples usuarios objetivo puede ser compatible con actividad de fuerza bruta o intentos de identificar credenciales válidas.

Clasificación:

| Campo | Valor |
|---|---|
| Tipo | Alerta |
| Severidad | Alta |
| Intentos fallidos | 7 |
| IP origen | `203.0.113.45` |
| Usuarios afectados | `root`, `test`, `soporte` |
| Estado | Requiere revisión |

---

### Hallazgo 2 - IP `198.51.100.23`

Se detectaron cuatro intentos fallidos contra el usuario `admin` desde la IP `198.51.100.23`.

### Interpretación

El usuario `admin` representa una cuenta sensible dentro del escenario simulado.

Los cuatro intentos fallidos superan el umbral básico de alerta utilizado en este laboratorio, por lo que la actividad requiere revisión.

No existe un login exitoso posterior relacionado con esta combinación de IP y usuario dentro de la evidencia disponible.

Clasificación:

| Campo | Valor |
|---|---|
| Tipo | Alerta |
| Severidad | Media |
| Intentos fallidos | 4 |
| IP origen | `198.51.100.23` |
| Usuario afectado | `admin` |
| Estado | Requiere monitoreo |

---

### Hallazgo 3 - IP `192.0.2.15`

Se detectaron cinco intentos fallidos contra el usuario `root` desde la IP `192.0.2.15`.

Posteriormente, se observó un inicio de sesión exitoso desde la misma IP hacia el mismo usuario.

Secuencia:

```text
192.0.2.15 + root
↓
5 intentos fallidos
↓
Accepted password para root
↓
misma IP + mismo usuario
↓
posible compromiso
```

### Interpretación

Este es el hallazgo de mayor prioridad del análisis.

La existencia de múltiples intentos fallidos seguida por una autenticación exitosa desde la misma IP contra el mismo usuario representa una correlación relevante.

El patrón puede ser compatible con un acceso exitoso posterior a intentos de fuerza bruta.

Sin embargo, esta evidencia no confirma por sí sola que el acceso haya sido realizado por un atacante.

Clasificación:

| Campo | Valor |
|---|---|
| Tipo | Posible incidente |
| Severidad | Alta |
| Intentos fallidos previos | 5 |
| IP origen | `192.0.2.15` |
| Usuario afectado | `root` |
| Estado | Requiere análisis prioritario |

---

## 5. Evidencia relevante

La evidencia principal corresponde a la siguiente secuencia:

- Cinco eventos `Failed password for root from 192.0.2.15`.
- Posterior evento `Accepted password for root from 192.0.2.15`.
- La IP de origen permanece igual.
- El usuario objetivo permanece igual.
- El usuario afectado es `root`, una cuenta privilegiada.

La correlación puede representarse como:

```text
IP + usuario
↓
múltiples fallos
↓
login exitoso posterior
↓
posible compromiso para investigar
```

---

## 6. Política de severidad

Este laboratorio utiliza una política simplificada para priorizar hallazgos.

Con el umbral predeterminado de `3`:

| Condición | Severidad |
|---|---|
| Menos de 3 intentos fallidos | Baja |
| 3 a 5 intentos fallidos | Media |
| 6 o más intentos fallidos | Alta |
| Posible compromiso correlacionado | Alta |
| Compromiso confirmado o impacto grave | Crítica |

La severidad no depende únicamente de la cantidad de intentos.

También se considera:

- Usuario afectado.
- Repetición de actividad.
- Existencia de autenticaciones exitosas posteriores.
- Correlación entre IP y usuario.
- Contexto disponible.
- Evidencia adicional de posible compromiso.

---

## 7. Evaluación del hallazgo prioritario

La IP `192.0.2.15` presenta cinco fallos contra `root` seguidos por una autenticación exitosa desde el mismo origen contra la misma cuenta.

Aunque cinco fallos normalmente corresponden a severidad Media según el volumen, la correlación con una autenticación exitosa posterior eleva el hallazgo a severidad Alta.

| Campo | Valor |
|---|---|
| Clasificación | Posible incidente |
| Severidad | Alta |
| Cuenta | `root` |
| IP | `192.0.2.15` |
| Compromiso confirmado | No |
| Requiere investigación | Sí |

La severidad Crítica queda reservada para situaciones donde exista evidencia suficiente de compromiso confirmado o impacto grave.

---

## 8. Acciones recomendadas

Acciones iniciales sugeridas para un entorno real:

1. Validar si el acceso desde `192.0.2.15` estaba autorizado.
2. Revisar actividad posterior del usuario `root`.
3. Revisar otros logs relacionados.
4. Revisar comandos o acciones realizadas durante la sesión.
5. Verificar cambios recientes en archivos, usuarios o configuraciones.
6. Cambiar credenciales si existe riesgo de compromiso.
7. Bloquear temporalmente la IP sospechosa si el procedimiento lo autoriza.
8. Deshabilitar acceso SSH directo para `root` si está habilitado y la política lo permite.
9. Aplicar MFA si corresponde.
10. Configurar controles contra intentos repetidos de autenticación.
11. Escalar el caso a un analista senior o equipo responsable.
12. Documentar los hallazgos y acciones realizadas.

Importante:

Las acciones de contención deben ejecutarse según procedimientos internos, permisos y autorización del equipo responsable.

---

## 9. Evidencia adicional necesaria

Para confirmar o descartar un compromiso sería necesario revisar evidencia adicional, como:

- Historial de accesos del usuario `root`.
- Actividad posterior al login.
- Comandos ejecutados.
- Cambios de configuración.
- Modificaciones de archivos.
- Creación o modificación de usuarios.
- Uso de privilegios.
- Otros registros de autenticación.
- Origen esperado de la conexión.
- Actividad relacionada en otros sistemas.

Sin esta evidencia adicional, el caso debe permanecer clasificado como posible incidente.

---

## 10. Recomendaciones preventivas

Para reducir el riesgo de eventos similares:

- Deshabilitar login directo como `root` cuando sea posible.
- Utilizar cuentas nominales con privilegios controlados.
- Aplicar autenticación multifactor cuando corresponda.
- Configurar políticas contra intentos repetidos de autenticación.
- Monitorear accesos SSH.
- Revisar periódicamente usuarios y permisos.
- Aplicar principio de mínimo privilegio.
- Mantener logs centralizados.
- Crear alertas para múltiples fallos de autenticación.
- Mantener procedimientos de respuesta documentados.

---

## 11. Limitaciones

Este reporte corresponde a un laboratorio educativo basado en logs simulados.

El análisis no incluye:

- ventanas temporales avanzadas;
- reputación de IP;
- geolocalización;
- inteligencia de amenazas;
- criticidad real de activos;
- análisis forense;
- contexto histórico completo;
- validación automática de legitimidad;
- confirmación automática de compromiso.

Por este motivo, las detecciones deben interpretarse como señales para investigación y no como conclusiones definitivas.

---

## 12. Conclusión

El análisis permitió identificar actividad sospechosa asociada a múltiples intentos fallidos de autenticación SSH desde distintas IPs.

La IP `203.0.113.45` generó siete intentos fallidos contra varios usuarios y fue clasificada como alerta de severidad Alta.

La IP `198.51.100.23` generó cuatro intentos fallidos contra `admin` y fue clasificada como alerta de severidad Media.

El hallazgo de mayor prioridad corresponde a `192.0.2.15`, donde cinco intentos fallidos contra `root` fueron seguidos por un login exitoso desde la misma IP contra el mismo usuario.

Esta correlación se clasifica como posible incidente de severidad Alta y requiere investigación adicional para determinar si el acceso fue legítimo o si existió un compromiso real.

---

## 13. Resumen técnico

Se analizaron logs simulados de autenticación SSH y se identificaron patrones compatibles con actividad de fuerza bruta.

El análisis produjo una alerta Alta asociada a siete intentos fallidos desde `203.0.113.45`, una alerta Media asociada a cuatro intentos contra `admin` desde `198.51.100.23` y un posible incidente de severidad Alta asociado a cinco fallos contra `root` desde `192.0.2.15` seguidos por una autenticación exitosa desde la misma IP contra el mismo usuario.

El patrón correlacionado requiere investigación, pero no se considera compromiso confirmado sin evidencia adicional.