print("Bienvenido al calculador de factura. Aquí calcularemos cuanto tiene que pagar cada uno")

factura_inicial = float(input("¿De cuanto es la factura? Usa punto en lugar de  coma para los decimales."))

propina = float(input("¿Qué porcentaje de la factura quieres dejar como propina? Escribe solo el número, sin el porcentaje."))

factura_total = float(factura_inicial + (factura_inicial * propina / 100))

personas = int(input("¿Cuántos sois?"))

resultado = float(factura_total / personas)

resultado_redondeo = round(resultado, 2)

mensaje = f"Cada uno debe pagar {resultado_redondeo}€"

print(mensaje)

