'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

Enunciat:
Implementa la funció 'fibonacci(fibonacci_number)' que contingui l'algorisme
de Fibonacci i rebi com a paràmetre un valor numèric enter anomenat
'fibonacci_number' i torneu el valor de la sèrie Fibonacci en aquesta posició.
Així mateix, si el valor no és numèric, o és menor a zero, cal llançar
una excepció ValueError("missatge"), la qual pot incloure un missatge que hi hauria de
correspondre amb el tipus d'error durant la validació.

Paràmetres:
- fibonacci_number: Nombre enter positiu superior a 0 que representa la
posició a la sèrie Fibonacci.

Exemple:
     Entrada:
     fibonacci(10)

     Sortida:
     55

'''

def fibonacci(fibonacci_number):
    # 1. Validar que sigui un numero enter
    if type (fibonacci_number) is not int: 
        raise ValueError ("El valor introduït ah de ser un numero enter")

    #2. Validar que no sigui menor a cero
    if fibonacci_number < 0:
        raise ValueError ("El numero no pot ser emnor a cero")

    # 3. Valors d'inic: si demanem la posició 0 dona 0, i si demanem la posició 1 dona 1
    if fibonacci_number == 0:
        return 0
    elif fibonacci_number == 1:
        return 1

    # Càlcul per a posicions majors que 1
    a, b = 0, 1
    for _ in  range (2, fibonacci_number +1):
        a, b = b, a + b
    return b
    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(fibonacci(10))
