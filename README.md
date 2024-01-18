# villa_fc
Software para la generacion de alertas de pagos gestionada mediante un archivo de excel.

`python src/vila_fc.py`

1. Unificación de Datos
El primer paso del programa consiste en unificar la información dispersa en varios archivos Excel en uno solo. Esto facilita la gestión y análisis de los datos.

2. Verificación de Datos
Luego, el programa lee el Excel generado y verifica la validez de la información proporcionada. Detecta posibles errores en los campos de nombre, apellido, número de celular y última fecha de pago. Indica cuáles deben corregirse para garantizar la precisión de los datos.

3. Creación de Diccionario de Deudores
Con la información corregida, se crea un diccionario que contiene los nombres y números de teléfono de las personas que tienen cuentas pendientes por pagar.

4. Envío de Recordatorios por WhatsApp
El programa utiliza la API de WhatsApp para enviar recordatorios automáticos a las personas que tienen cuentas pendientes. Se les insta a acercarse a la escuela de fútbol para regularizar sus deudas.

5. Generación de Histograma
Finalmente, se genera un histograma utilizando la biblioteca de visualización de datos en Python. Este histograma proporciona una representación gráfica del estado actual de los pagos en la escuela de fútbol, mostrando la proporción de personas al día y aquellas con cuentas pendientes.

[Grafica de la comparacion de los pagos](./Imagen/Figure_1.png)
