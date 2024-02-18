def calcular_factura(cantidad_sin_iva, porcentaje_iva=21):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total_factura = cantidad_sin_iva + iva
    return total_factura

     
factura_sin_iva = float(input("Por favor ingrese la cantidad de la factura sin IVA: "))
porcentaje_iva = float(input("Por favor ingrese el porcentaje de IVA (si ingresa 0 , se usará el 21% por defecto): "))

if porcentaje_iva != 0:
    total_con_iva = calcular_factura(factura_sin_iva, porcentaje_iva)
    print(f"Total con {porcentaje_iva}% de IVA: {total_con_iva}")
else:
    total_con_iva_21 = calcular_factura(factura_sin_iva)
    print(f"Total con 21% de IVA (por defecto): {total_con_iva_21}")