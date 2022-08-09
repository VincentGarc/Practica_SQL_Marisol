import pandas as pd
import openpyxl

excel1 = 'archivos/BaseDatos.csv'
excel2 = 'archivos/NuevoArchivo.csv'

df1 = pd.read_csv(excel1)
df2 = pd.read_csv(excel2)

values1 = df1[['fechaOc','servicio','nombreCliente','titular','noPoliza','assistant','origen','importe','telefono','placa']]
values2 = df2[['fechaOc','servicio','nombreCliente','titular','noPoliza','assistant','origen','importe','telefono','placa']]
dataframes = [values1,values2]

join = pd.concat(dataframes, ignore_index=True, sort=False)
join.to_csv('archivos/BaseDatos.csv')