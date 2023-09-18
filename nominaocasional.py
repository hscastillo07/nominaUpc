# Definición de constantes
SMMMLV = 1160000  # Valor constante del SMMMLV

# Función para calcular el salario de un profesor ocasional
def calcular_salario_profesor_ocasional():
    # Define las opciones de categoría
    opciones_categoria = {
        1: "auxiliar de tiempo completo",
        2: "auxiliar de medio tiempo",
        3: "asistente de tiempo completo",
        4: "asistente de medio tiempo",
        5: "asociado de tiempo completo",
        6: "asociado de medio tiempo",
        7: "titular de tiempo completo",
        8: "titular de medio tiempo",
    }

    # Define las opciones de salario base
    opciones_salario_base = {
        "auxiliar de tiempo completo": 2.645 * SMMMLV,
        "auxiliar de medio tiempo": 1.509 * SMMMLV,
        "asistente de tiempo completo": 3.125 * SMMMLV,
        "asistente de medio tiempo": 1.749 * SMMMLV,
        "asociado de tiempo completo": 3.606 * SMMMLV,
        "asociado de medio tiempo": 1.990 * SMMMLV,
        "titular de tiempo completo": 3.918 * SMMMLV,
        "titular de medio tiempo": 2.146 * SMMMLV,
    }

    # Imprime las opciones de categoría
    print("Opciones de categoría:")
    for num, categoria in opciones_categoria.items():
        print(f"{num}: {categoria}")

    # Solicita al usuario que elija una opción de categoría
    while True:
        try:
            opcion_numero = int(input("Elija el número de la categoría: "))
            categoria = opciones_categoria.get(opcion_numero)
            if categoria:
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Obtener el salario base según la categoría
    salario_base = opciones_salario_base[categoria]

    # Solicitar otros datos al usuario
    titulo_posgrado = input("Ingrese el título de posgrado (especializacion/maestria/doctorado) o 'ninguno': ").lower()
    reconocido_colciencias = input("¿Es reconocido por Colciencias? (Si/No): ").lower()
    pertenece_semillero = input("¿Pertenece a un semillero? (Si/No): ").lower()

    # Define funciones para calcular bonificaciones
    def bonificacion_titulo_especializacion():
        return 0.10 * salario_base

    def bonificacion_titulo_maestria():
        return 0.45 * salario_base

    def bonificacion_titulo_doctorado():
        return 0.90 * salario_base

    def bonificacion_titulo_ninguno():
        return 0

    def bonificacion_colciencias_si():
        return 0.33 * salario_base

    def bonificacion_colciencias_no():
        return 0

    # Define un diccionario para mapear opciones a funciones
    opciones_titulo = {
        "especializacion": bonificacion_titulo_especializacion,
        "maestria": bonificacion_titulo_maestria,
        "doctorado": bonificacion_titulo_doctorado,
        "ninguno": bonificacion_titulo_ninguno,
    }

    opciones_colciencias = {
        "si": bonificacion_colciencias_si,
        "no": bonificacion_colciencias_no,
    }

    # Utiliza las funciones mapeadas para calcular bonificaciones
    bonificacion_titulo = opciones_titulo.get(titulo_posgrado, bonificacion_titulo_ninguno)()
    
    bonificacion_colciencias = opciones_colciencias.get(reconocido_colciencias, bonificacion_colciencias_no)()
    
    bonificacion_semillero_pertenece = 0.19 * salario_base if pertenece_semillero == "si" else 0

    # Calcular el salario total
    salario_total = salario_base + bonificacion_titulo + bonificacion_colciencias + bonificacion_semillero_pertenece

    # Imprimir el salario
    print(f"El salario del profesor ocasional es: ${salario_total:.2f}")

# Llamar a la función para calcular el salario de un profesor ocasional
calcular_salario_profesor_ocasional()
