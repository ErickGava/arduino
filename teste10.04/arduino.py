import serial
import time
from banco import Banco


PORTA = "COM3"
ARDUINO  = serial.Serial(PORTA,9600,timeout=1)
time.sleep(2)

ALUNO = "Chicken Lille"
ULTRASSOM = 1
banco = Banco()


while True:
    
    distancia = ARDUINO.readline().decode('utf-8').strip()  
    print(distancia)  
    banco.inserir_ou_atualizar_estado(ALUNO,ULTRASSOM,distancia)