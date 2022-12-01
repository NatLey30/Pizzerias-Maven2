# Pizzerias-Maven2

Repositorio en el que se limpian los datos de los dataframes orders.csv y order_details.csv, para realizar un predicción 

En los dos archivos eliminamos los nans, copiando la fila de depués y ordenamos el dataset.

Para orders.csv creamos una nueva columna con todas las fechas en el mismo formato.

Para order_details.csv con reyex cambiamos las @ por a, los 3 por e, los 0 por o, ...

Una vez limpios los datos, se hace una predicción de los ingredientes a comprar para la siguiente semana, para lo cual cogemos la última semana del dataset y miramos cuantos ingredientes hacen falta.

Los ficheros de entrada son:
- orders.csv
- order_details.csv
- pizza_types.csv
- pizzas.csv
- data_dictionary

Los ficheros de salida son:
- reporte.html
- reporteCOO.pdf

Los archivos de transformación son:
- compra.py
- limpiar_datos.py
