import serial
import time

porta = "COM6"
arduino = serial.Serial(porta, 9600, timeout=1)
time.sleep(2)

while True:
    comando = input("Digite 1 para ligar o LED ou 0 para desligar: ")
    if comando == '1':
        arduino.write(b'1')
        print("LED 1 ligado")
    elif comando == '2':
        arduino.write(b'2')
        print("LED 2 ligado")
    elif comando == '3':
        arduino.write(b'3')
        print("LEDs ligados!")
    elif comando == '4':
        arduino.write(b'4')
        print("LED 1 desligado")
    elif comando =='5':
        arduino.write(b'5')
        print("LED 2 desligado")
    elif comando == '0':
        arduino.write(b'0')
        print("LEDs desligado")
    elif comando.lower() == 'sair':
        print("Encerrando Comunicação com Arduino")
        break
    else:
        print("Digite um número válido!")

arduino.close()