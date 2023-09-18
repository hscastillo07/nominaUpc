# Definición de constantes
SMMMLV = 1160000  # Valor constante del SMMMLV

# Función para calcular el salario de un docente
def calcular_salario_docente():
    # Capturar datos del usuario
    horas_catedra = float(input("Ingrese las horas de cátedra: "))
    valor_hora = float(input("Ingrese el valor por hora: "))
    
    # Capturar el título de posgrado (si tiene)
    titulo_posgrado = input("Ingrese el título de posgrado (especializacion/maestria/doctorado) o 'ninguno': ").lower()
    
    # Capturar el nivel de investigación (si tiene)
    nivel_semillero = input("Ingrese el nivel del semillero (A1/A/B/C) o 'ninguno': ").upper()
    
    # Verificar si el docente es reconocido por Colciencias
    reconocido_colciencias = input("¿Es reconocido por Colciencias? (Si/No): ").lower()
    
    # Verificar si el docente pertenece a un semillero
    pertenece_semillero = input("¿Pertenece a un semillero? (Si/No): ").lower()

    # Calcular la bonificación por título de posgrado
    if titulo_posgrado == "especializacion":
        bonificacion_titulo = 0.10 * SMMMLV
    elif titulo_posgrado == "maestria":
        bonificacion_titulo = 0.45 * SMMMLV
    elif titulo_posgrado == "doctorado":
        bonificacion_titulo = 0.90 * SMMMLV
    elif titulo_posgrado == "ninguno":
        bonificacion_titulo = 0
    else:
        print("Opción de título de posgrado no válida. No se aplicará bonificación.")
        bonificacion_titulo = 0

    # Calcular la bonificación por nivel de semillero
    if nivel_semillero == "A1":
        bonificacion_semillero = 0.56 * SMMMLV
    elif nivel_semillero == "A":
        bonificacion_semillero = 0.47 * SMMMLV
    elif nivel_semillero == "B":
        bonificacion_semillero = 0.42 * SMMMLV
    elif nivel_semillero == "C":
        bonificacion_semillero = 0.38 * SMMMLV
    elif nivel_semillero == "ninguno":
        bonificacion_semillero = 0
    else:
        print("Opción de nivel de semillero no válida. No se aplicará bonificación.")
        bonificacion_semillero = 0

    # Calcular la bonificación por reconocimiento de Colciencias
    bonificacion_colciencias = 0.33 * SMMMLV if reconocido_colciencias == "si" else 0

    # Calcular la bonificación por pertenecer a un semillero
    bonificacion_semillero = 0.19 * SMMMLV if pertenece_semillero == "si" else 0

    # Calcular el salario total
    salario = (horas_catedra * valor_hora) + bonificacion_titulo + bonificacion_semillero + bonificacion_colciencias + bonificacion_semillero

    # Imprimir el salario
    print(f"El salario del docente es: ${salario}")

# Llamar a la función para calcular el salario
calcular_salario_docente()
