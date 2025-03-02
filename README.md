#  Generador de contraseñas seguras
## Introducción

En la actualidad, la seguridad de la información es un aspecto fundamental en el uso de tecnología. Uno de los principales factores que garantizan la protección de datos personales y corporativos es el uso de contraseñas seguras. Sin embargo, muchas veces los usuarios generan contraseñas fáciles de vulnerar, poniendo en riesgo su información.

Este proyecto busca desarrollar un generador de contraseñas aleatorias que garantice la seguridad de los datos mediante la creación de claves robustas. Además, el sistema validará la fortaleza de la contraseña y permitirá su almacenamiento de manera segura en una base de datos.

## Objetivos

- Desarrollar un generador de contraseñas seguras que permita la creación de claves aleatorias con diferentes tipos de caracteres.
- Implementar una validación de seguridad para determinar la fortaleza de la contraseña generada.
- Permitir la selección de criterios personalizados como la longitud de la contraseña y los tipos de caracteres a incluir.
- Brindar opciones para almacenar o descartar la contraseña, asegurando su protección en una base de datos si el usuario decide guardarla.
- Facilitar la iteración en la generación de contraseñas para garantizar la satisfacción del usuario con la clave creada.

## Descripción del diagráma de flujo

1. Generar contraseñas seguras:
- Solicitar al usuario la longitud de la contraseña y los tipos de caracteres a incluir (mayúsculas, minúsculas, números y caracteres especiales).
- Validar que el usuario haya seleccionado al menos un tipo de carácter. Si no, mostrar un mensaje de error y volver a solicitar las preferencias.
- Generar la contraseña de manera aleatoria según las preferencias del usuario.
- Mostrar la contraseña generada.
  
2. Comprobar la fuerza de una contraseña ingresada por el usuario:
- Evaluar la fortaleza de la contraseña basándose en criterios como longitud, uso de mayúsculas, minúsculas, números, caracteres especiales y diversidad de caracteres.
- Mostrar un mensaje indicando si la contraseña es débil, media o fuerte.
  
3. Guardar la contraseña en una base de datos (opcional):
- Preguntar al usuario si desea guardar la contraseña generada.
- Si el usuario acepta, almacenar la contraseña en una base de datos junto con un identificador único (por ejemplo, un nombre de usuario o servicio asociado).
- Mostrar un mensaje de confirmación si la contraseña se guardó correctamente.

4. Flujo general:
- Permitir al usuario generar una contraseña, comprobar la fuerza de una contraseña o salir del programa.
- Preguntar al usuario si desea realizar otra acción después de completar una operación. Si la respuesta es afirmativa, volver al menú principal; de lo contrario, finalizar el programa.

<img src="https://github.com/easalazarp/secure-password-genetator/blob/5660dd92ad1b1ee1a2240be7cf37e7f3158805eb/Diagrama%20de%20flujo.jpg" alt="Diagrama de flujo" />

## Descripción del diagráma de aplicación

Este diagrama representa la arquitectura de una aplicación de generación y validación de contraseñas, organizada en cuatro capas principales:

1. Capa de Presentación (Frontend/UI)
- Interfaz de Usuario (UI): Es la parte visual e interactiva con la que el usuario interactúa. Aquí se ingresan las configuraciones para la generación de contraseñas.
- Controlador (Frontend Controller): Gestiona la lógica de la interfaz, comunicándose con el backend para enviar solicitudes y recibir respuestas.
2. Capa de Servicios (Backend Services)
- API Gateway: Actúa como intermediario entre el frontend y los servicios backend, canalizando las solicitudes hacia los servicios correspondientes.
- Servicio de Generación de Contraseñas: Se encarga de crear contraseñas aleatorias basadas en los criterios definidos por el usuario (longitud, tipos de caracteres, etc.).
- Servicio de Validación de Contraseñas: Evalúa la seguridad de las contraseñas generadas según criterios como longitud, variedad de caracteres y patrones predecibles.
3. Capa de Datos (Data Layer)
- Base de Datos (Opcional): Permite almacenar las contraseñas generadas (si el usuario elige guardarlas) y otros datos relevantes, como registros de actividad.
4. Capa de Gestión y Monitoreo (Management & Monitoring)
- Sistema de Registro y Monitoreo: Supervisa el funcionamiento de la aplicación, registrando eventos relevantes para seguridad, auditoría y optimización del sistema.
<img src="https://github.com/easalazarp/secure-password-genetator/blob/main/Diagrama%20de%20arquitectura%20de%20aplicacio%CC%81n.png" alt="Diagrama de aplicación" />
