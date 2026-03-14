## 1) Descripción del problema
*Contexto:* Consiste en un sistema de entrega de medicaments de una farmacia hospitalaria, donde el objetivo es administrar el flujo de pacientes que reclaman recetas mediantres unas pautas de prioridad. El sistema deber ser capaz de organizar a los pacientes en dos categorias distintas, asegurando que la atención se asigne primero a quienes tienen una condición medica prioritaria, sin perder el orden de llegada dentro de cada grupo. Pautas: 
- 1. Los pacientes normales se atienden en orden de llegada. 
- 2. Los pacientes críticos tienen prioridad sobre los normales.
- 3. Entre pacientes críticos también se respeta el orden de llegada. 
- 4. Solo puede haber un paciente en atención.
- 5. Cuando se atiende a un paciente, este se elimina del sistema.

## 2) Requerimientos
Lista requerimientos **funcionales** y **no funcionales**.
### *Requerimientos funcionales*
- *R01:* Registro de recetas prioritarias: El sistema debe permitir el ingreso de pacientes con condiciones de salud críticas o recetas de urgencia, clasificándolos automáticamente como usuarios de alta prioridad.
- *R03:* Protocolo de atención jerarquizada: Al momento de llamar a un paciente a ventanilla, el sistema debe dar preferencia obligatoria a los pacientes en la fila de prioridad. Solo se podrá atender a un paciente de la fila normal si no hay nadie esperando en la fila de prioridad.
- *RF04:*Preservación del orden de llegada: El sistema debe asegurar que, dentro de una misma categoría (prioritaria o normal), los pacientes sean atendidos estrictamente en el orden en que llegaron.
-*RF5:* Gestión de disponibilidad: El sistema debe notificar al personal cuando se intente realizar una entrega de medicamentos y no existan solicitudes pendientes en ninguna de las áreas del dispensario.
### *Requerimientos no funcionales*
- *R01:* Integridad del proceso: El sistema debe garantizar que un paciente atendido sea retirado inmediatamente de los registros activos para evitar duplicidad en la entrega de medicamentos.
- *R02:* Escalabilidad: El sistema debe ser capaz de gestionar un aumento repentino en el volumen de recetas (por ejemplo, en horas pico) sin degradar la lógica de prioridad establecida.*

## 3) Historias de usuario
### *H01-Registro de usuarios y clasificación.*
- *Descripción:* El sistema permite el ingreso de pacientes o usuarios mediante un comando que especifica su nivel de prioridad (Crítico/Prioritario o Normal/General) seguido de su nombre.
- *Caso exitoso:* Se ingresa un comando válido (ej. C Juan o N Marta). El sistema identifica el tipo de prioridad y almacena el nombre en la cola correspondiente, confirmando el registro de forma exitosa.
- *Caso no exitoso:* El usuario ingresa una cadena vacía o un comando con un formato que el sistema no reconoce. El sistema no realiza ninguna acción y queda a la espera de un dato válido.
- *Entrada:* [Clasificación, Nombre]
- *Salida:* No hay salida, el sistema procesa los datos.
### *H02-Atención por clasificación de prioridad*
- *Descripción:* El sistema procesa la atención de los usuarios en ventanilla cada vez que se solicita la acción de "atender". Debe garantizar que ningún usuario de tipo Normal sea atendido mientras exista alguien en la fila de prioritarios.
- *Caso exitoso:* Existen pacientes en espera. Al solicitar atención, el sistema extrae al primer usuario de la cola de prioritarios. Si esta está vacía, extrae al primero de la cola de normales.
- *Caso no exitoso:* El usuario solicita atención cuando ambas colas están vacías. El sistema identifica la ausencia de datos y notifica que no hay pendientes.
- *Entrada:* Se pide atención.
- *Salida:* Se atiendde al usuario que solicito atención, deacuerdo a la prioridad y si hay mas usuarios.

## 4) Diagramas de flujo
Este diagrama de flujo muestra el proceso en el cual se debe desarrollar el codigo, Teniendo un solo for y varios if donde se determinan el tipo de paciente que es (prioritario, normal o si es para dar salida).


## 5) Diagramas de secuencia
En este diagrama de secuencia representamos los función básica del código, donde el usuario identifica al paciente y lo categoriza como paciente critico o normal, donde estos nombres y según la categorización lo archivamosen una lista, vamos a tener como prioridad a los pacientes críticos, y cuando termina de atender a los pacientes críticos pasa a los pacientes normales, eliminando a cada paciente atendido. Por ultimo, imprimir a los pacientes según el orden de llamada.

## 6) Diagramas de casos de uso
En este diagrama se muestra lo que ve el usuario y tiene que hacer y lo que tiene que hacer el sistema. Primero el usuario ingresa su nombre y su prioridad, luego el sistema toma los datos ingresados y determina deacuerdo a la prioridad el orden de atencion. Cuando el usuario ve el orden de los pacientes y a medida que los va atendiendo el sistema elimina a estos.

## 7) Análisis de complejidad
Al solo tener un solo for la funcion tendria una complejidad de $O(n^2)$ los if no interfieren en la complejidad. 

## 8) Tests
- *Test 1:* Validar si hay una fila larga de pacientes normales y llega una urgencia de último minuto.
- *Test 2:* Validar que entre personas del mismo tipo se respete el orden.
- *Test 3:* Validar que el sistema no falle si se pide atender y no hay datos.
