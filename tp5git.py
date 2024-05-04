# Funcion para agregar alumnos
def agregar_alumno(datos, alumno):
    datos["Alumnos"].append(alumno)
    print("Alumno agregado con éxito.")


datos = {"Alumnos": []}
alumno1 = {
    "Nombre": "Juan",
    "Apellido": "Saravia",
    "DNI": "12345678",
    "Fecha de nacimiento": "26/11/2004",
    "Tutor": "Claudia Santoiemma",
    "Notas": [8, 7, 6],
    "Faltas": 2,
    "amonestaciones": 0
}
agregar_alumno(datos, alumno1)
print(datos)

# Funcion para mostrar los datos de los alumnos
def mostrar_alumno(alumno):
    print("Nombre:", alumno["Nombre"])
    print("Apellido:", alumno["Apellido"])
    print("DNI:", alumno["DNI"])
    print("Fecha de nacimiento:", alumno["Fecha de nacimiento"])
    print("Tutor:", alumno["Tutor"])
    print("Notas:", alumno["Notas"])
    print("Faltas:", alumno["Faltas"])
    print("Amonestaciones:", alumno["amonestaciones"])

alumno2 = {
    "Nombre": "Camila",
    "Apellido": "Aleman",
    "DNI": "87654321",
    "Fecha de nacimiento": "02/02/2004",
    "Tutor": "Pedro Aleman",
    "Notas": [9, 8, 7],
    "Faltas": 1,
    "amonestaciones": 1
}
mostrar_alumno(alumno2)

# Funcion para modificar los datos de los alumnos
def modificar_alumno(alumno, campo, nuevo_valor):
    if campo in alumno:
        alumno[campo] = nuevo_valor
        print("Datos modificados con éxito.")
    else:
        print("Campo no válido.")


modificar_alumno(alumno1, "Notas", [9, 8, 7, 10])
print(alumno1)

#Funcion para expulsar alumnos
def expulsar_alumno(datos, dni):
    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni:
            datos["Alumnos"].remove(alumno)
            print("Alumno expulsado con éxito.")
            return
    print("Alumno no encontrado.")

expulsar_alumno(datos, "12345678")
print(datos)
