import RPi.GPIO as GPIO
from time import strftime

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#pin_lampu = 15 		#ruko cipamokolan, pindahin aja ke 11 biar gampang sinkron ama pintu peraga
pin_lampu = 11		#definisi pin GPIO yg terhubung ke relay lampu
GPIO.setup(pin_lampu, GPIO.OUT)

def lampu_on(pin):		#fungsi untuk menyalakan lampu (NC)
	GPIO.output(pin, 0)

def lampu_off(pin):		#fungsi untuk mematikan lampu (NC)
	GPIO.output(pin, 1)




#Coded by Faisal Candrasyah H, CTO of Indisbuilding
