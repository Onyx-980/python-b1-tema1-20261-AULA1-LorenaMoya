def count_vowels(text_chain:str):
    # 1. Verificar que el paràmetre sigui un string
    if not isinstance(text_chain, str):
        raise ValueError("El parámetro debe ser una cadena de texto (string).")
    
    # 2. Definir les vocals a comptar
    vowels = "aeiouAEIOUáéíóúÁÉÍÓÚàèòÀÈÒäëïöüÄËÏÖÜ"

    
    # 3. Comptar les vocals a la cadena de text
    count = sum(1 for char in text_chain if char in vowels)
    
    return count

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(count_vowels("Hello world, this is an example."))

