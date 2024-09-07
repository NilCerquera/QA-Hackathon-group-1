# Pruebas Exploratorias en BugBank.

Este proyecto tiene como objetivo interactuar y validar la plataforma **BugBank** para la gestión de crear un usuario, iniciar sesión y realizar transferencias bancarias, con un enfoque principal en la búsqueda de fallos críticos relacionados con la validación de campos y el correcto funcionamiento de la información recibida del Front.

## Descripción del Proyecto
Realizamos una **prueba exploratoriay funcionalidad** basada en la metodología de **caja negra y puntos grises**, sin acceso al código fuente, simulando diversos escenarios y evaluando la robustez de la aplicación. Nos enfocamos en validar aspectos clave como la creación de un usuario, iniciar la sesión y realizar transferencia a otras cuentas digitales.

## Tecnologías Utilizadas
- **Selenium**: Para realizar y gestionar los script de automatización de la plataforma.
- **Python**: Para realizar y ejecutar las pruebas correspondientes.
- **Google Spreadsheet**: Creación de listas de verificación, clases de equivalencia y casos de prueba.
- **JIRA**: Seguimiento y reporte de bugs.
- **Xmind**: Estructuración de pruebas mediante mapas mentales.

## Objetivo
Identificar errores críticos y evaluar la validez de los datos a través de los diferentes formularios de la aplicación (Creación de usuarios, iniciar sesión y ejecutar transferencias). Nos centramos en la validación de campos y en asegurar la funcionalidad de las respuestas y comportamiento de la aplicación a través del Front.

## Cómo Ejecutar las Pruebas
1. Importamos la colección de información y datos del repositorio principal disponible en este repositorio ("Proyecto clonado").
2. Analizar los requisitos iniciales y realizar listas de comprobación y casos de pruebas, adicional realizar test con pruebas automatizadas para la ejecución de scripts y confirmación de la prueba a través de **Selenium** utilizando el lenguaje de programación y **Python** y los requisitos proporcionados en la [Requisitos aplicación BugBank](https://bugbank.netlify.app/requirements).
3. Verificar los resultados cumplan con los requisitos de validación y a pesar de que no contamos con criterios de los requisitos iniciales, ejecutamos las pruebas que generan mayor impacto a la aplicación y reportamos cualquier error detectado en **JIRA**.

## Equipo de Trabajo
Este proyecto fue desarrollado por un equipo de QA Engineers comprometidos con la calidad del software y meticulosos en la validación de la aplicación:
- **Juan Pablo Silva Martínez**
- **Mario Guillermo Pastrana Gómez**
- **Jorge Michell Guerrero Herrera**
- **Jahaziel Kolansinsky**
- **Nilton Fdo. Cerquera**
- **Jeisson Steve Ortiz Peñaloza**

## Fallas criticas de la aplicación**

luego de ejecutar las pruebas correspondientes y validar el comportamiento de la aplicación **BugBank**, encontramos las siguientes novedades de la aplicación

**Formulario Registro usuario**

- **Campo email**
La unica restricción que permite es que el correo debe contar con el caracter @, de resto permite crear correos con cualquier parametro incluso sin dominio (gmail.com. hotmail.com etc)

- **Campo nombre**
No tiene establecido los parametros, lo que permite nombres con números, caracteres especiales y nombres en otro idioma

- **Campo contraseña**
No tiene establecido los parametros, lo que permite contraseñas con números, caracteres especiales y nombres en otro idioma 
  
- **Campo confirmar contraseña**
No presenta fallas graves, a pesar de que no cuenta con parametros establecidos, cumple la condicion de que debe ser similar a la contraseña
  
- **Selector crear cuenta con saldo**
No presenta fallas al seleccionar sin saldo (registra cuenta con 0 reales) y al seleccionar con saldo (registra con 1.000 reales)

- **Funcionalidad registro**
Permite crear una cuenta con los mismos datos (email, nombre, contraseña y confirmación contraseña)
Crea cuentas con solo dos digitos de la cuenta y el digito de verificación

**Formulario iniciar sesión**
- **Campo email**
- No tiene establecido los parametros, lo que permite nombres con números, caracteres especiales y nombres en otro idioma

- **Campo contraseña**
- No tiene establecido los parametros, lo que permite contraseñas con números, caracteres especiales y nombres en otro idioma 
  
- **Funcionalidad Iniciar sesión**
No presenta fallas al iniciar sesión, se requiere diligenciar los dos parametros (email y contraseña) y presenta buen funcionamiento de la aplicación en este sentido.

- **Funcionalidad Aplicación cuando la sesión se encuentra activa con el usuario**

Se valida la interfaz, y a pesar que se encuentra en idioma portuges, y no contamos con diseños de la aplicación, es útil y sencillo el funcionamiento para el usuario 

- **Sección Transferencia**
Permite realizar una transferencia solo con el valor a transferir, es critico ya que realiza transferencia sin número de cuenta y digito de verificación
Al crear dos cuentas para interactuar las transferencias, no permite realizar la transferencia a pesar de que la cuenta esta activa y el número de cuenta digital correspondiente

  
- **Sección pagos**
No realizamos pruebas exploratorias o validación de esta sección ya que se encuentra en desarollo
- 
- **Sección extractos**
En esta sección no presenta fallas o errores criticos, nuestra la creación de la cuenta y los movimientos realizados de la aplicación

- **Sección beneficios**
  No realizamos pruebas exploratorias o validación de esta sección ya que se encuentra en desarollo

  
