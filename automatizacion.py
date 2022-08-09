import pandas as pd
import numpy as np

df = pd.read_csv('prueba.csv')

telefono = df[df.duplicated(['telefono'], keep = False)]
titular = df[df.duplicated(['titular'], keep = False)]
noPoliza =df[df.duplicated(['noPoliza'], keep = False)]
placa = df[df.duplicated(['placa'], keep = False)]
final = pd.concat([telefono,titular,noPoliza,placa])

with pd.ExcelWriter('duplicados_script.xlsx') as writer:
    final.to_excel(writer, sheet_name = 'Duplicados', index = False)
    telefono.to_excel(writer, sheet_name = 'Telefono', index = False)
    titular.to_excel(writer, sheet_name = 'Titular', index = False)
    noPoliza.to_excel(writer, sheet_name = 'NoPoliza', index = False)
    placa.to_excel(writer, sheet_name = 'Placa', index = False)