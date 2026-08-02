import base64
user_input = input("Introduce un nombre: ")
# Esto es un ejemplo muy básico de vulnerabilidad que CodeQL detectará
exec("print('Hola ' + user_input)")
