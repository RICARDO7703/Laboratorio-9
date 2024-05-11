import serial
import time

# Configuración del puerto serial
puerto_serial = 'COM3'
baudios = 9600
arduino = serial.Serial(puerto_serial, baudios)
time.sleep(2)  # Esperar a que Arduino se inicialice

# Bucle principal
while True:
    # Encender el LED
    arduino.write(b'H')  # Envía el comando 'H' a Arduino para encender el LED
    print("LED encendido")
    time.sleep(2)  # Esperar 2 segundos
    
    # Apagar el LED
    arduino.write(b'L')  # Envía el comando 'L' a Arduino para apagar el LED
    print("LED apagado")
    time.sleep(3)  # Esperar 3 segundos antes de repetir el ciclo
