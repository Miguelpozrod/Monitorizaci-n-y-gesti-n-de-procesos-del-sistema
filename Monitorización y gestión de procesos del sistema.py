import psutil


def listar_procesos():
    print("Procesos activos:")
    for proceso in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        pid = proceso.info['pid']
        nombre = proceso.info['name']
        cpu = proceso.info['cpu_percent']
        memoria = proceso.info['memory_percent']

        print(f"PID: {pid}, Nombre: {nombre}, CPU: {cpu}%, Memoria: {memoria}%")

        if nombre.lower() == "notepad.exe":
            print("El Bloc de notas está en ejecución")


def finalizar_proceso(pid):
    try:
        proceso = psutil.Process(pid)
        proceso.terminate()
        print(f"Proceso con PID {pid} finalizado exitosamente.")
    except psutil.NoSuchProcess:
        print(f"No se encontró ningún proceso con PID {pid}.")
    except psutil.AccessDenied:
        print(f"No tienes permisos para finalizar el proceso con PID {pid}.")


# Programa principal
while True:
    listar_procesos()

    pid_a_finalizar = input("\nIngresa el PID del proceso que desea finalizar (o 'q' para salir): ")

    if pid_a_finalizar.lower() == 'q':
        break

    if pid_a_finalizar:
        try:
            pid_a_finalizar = int(pid_a_finalizar)
            finalizar_proceso(pid_a_finalizar)
        except ValueError:
            print("Por favor, ingresa un número válido para el PID.")

    input("\nPresiona Enter para continuar")

print("Programa finalizado.")
