import os
import sqlite3
import subprocess

# --- VULNERABILIDAD 1: Inyección SQL ---
def get_user_sql(user_id):
    # CodeQL detectará esto como "py/sql-injection"
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)

# --- VULNERABILIDAD 2: Inyección de comandos (Command Injection) ---
def ping_host(target_host):
    # CodeQL detectará esto como "py/command-injection"
    os.system(f"ping -c 4 {target_host}")

# --- VULNERABILIDAD 3: Credenciales codificadas (Hardcoded Secret) ---
# CodeQL detectará esto como "py/hardcoded-credentials" o "hardcoded-api-key"
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"

# --- VULNERABILIDAD 4: Ataque de ruta (Path Traversal) ---
def read_log_file(filename):
    # CodeQL detectará esto como "py/path-injection"
    with open(f"/var/log/{filename}", "r") as file:
        return file.read()

# --- VULNERABILIDAD 5: Uso peligroso de eval() ---
def process_data(user_data):
    # CodeQL detectará esto como "py/unsafe-eval" o "py/unsafe-exec"
    result = eval(user_data) 
    return result

if __name__ == "__main__":
    user_input = input("Introduce un ID de usuario: ")
    get_user_sql(user_input)
    ping_host(input("Introduce una IP: "))
    print(read_log_file(input("Introduce un archivo de log: ")))
    process_data(input("Introduce código Python: "))
