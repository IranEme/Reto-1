def buscar_password(password, archivo='10-million-password-list-top-1000000.txt'):
    password = password.strip()
    if not (5 <= len(password) <= 8):
        return "El password debe tener entre 5 y 8 caracteres."
    with open(archivo, 'r') as f:
        for linea in f:
            pw = linea.strip()
            if pw == password or pw[::-1] == password:
                return f'Password encontrada: {pw if pw == password else pw[::-1]}'
    return "Password no encontrada"

if __name__ == "__main__":
    password = input('contraseña: ')
    print(buscar_password(password))