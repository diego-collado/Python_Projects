import shodan

# Conexión con la aplicativa
api = shodan.Shodan("noevTLPxVFdDWTTd8WOTA3vOjeG53noF")

try:
    # Búsqueda
    resultados = api.search("búsqueda_a_realizar")
    total_resultados = resultados['total']

    # Impresión de resultados
    print(f"Total resultados encontrados: {total_resultados}")

    coincidencias = resultados['coincidencias']
    for resultado in coincidencias:
        print(f"IP: {resultado['ip_str']}")
        print(resultado['data'])
        print("")

except shodan.APIError as errorShodan:
    print(f"Error: {errorShodan}") # Si hay error, nos permite saber qué error es