import pandas as pd
from datetime import datetime
import re

orders = pd.read_csv("orders_ordenado.csv", sep=',')

semana = []
pedidos_semana = []
contador = 0
h = len(orders.axes[0])-1
fecha = ""
while contador <= 7:
    dia = str(orders.loc[h, 'dates_std']).split(' ')[0]
    if dia != fecha:
        fecha = dia        
        semana.append(fecha)
        contador += 1
    pedidos_semana.append(orders.loc[h, 'order_id'])
    h -= 1
pedidos_semana.pop(len(pedidos_semana)-1)
semana.pop(len(semana)-1)

print(semana)
for day in pedidos_semana:
    print(day)
