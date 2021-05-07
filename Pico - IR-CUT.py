# "RP2-Pico" LDR kontrol + LB1838 motor driver + IR-CUT + IR-LED / kod = 1,*2,*3 & TEST
import time
from machine import Pin, ADC
#[][][][][][][][][][][][][][][][][ W1 ][][][][][][][][][][][][][][][][][

LED = Pin(25, Pin.OUT) 			# IR-LED Start Voltajı için Transistörü aç
LB1838 = Pin(14, Pin.OUT)		# LB1838 Start Voltajı için Transistörü aç
LB1838İNP1 = Pin(15, Pin.OUT)	# LB1838-İNP1 sağ >< sol '+' yada '-' ,ayarı
LDR = ADC(26) 					# LDR sinyal ANALOG giriş Pin'i

lightlevel = LDR.read_u16() # LDR sinyalini sayıya çevir "LDR.read_u16()"
LED.off()					# IR-LED kapalı
LB1838.off()				# LB1838 kapalı

#[][][][][][][][][][][][][][][][][][][][][][][]][][][][][][][][][]][][][-(*2)

def gunduz(): # IR-CUT-filtre GUNDUZ " lightlevel < 61611 " çalışır
	
	LED.off() 			# IR-LED kapalı
	LB1838İNP1.low() 	# Motor SOL < dönüyor LB1838-İNP1 " - " low
	LB1838.on() 		# LB1838 açık
	time.sleep(0.7)		# Filtre " gunduz " tarafına döndü
	LB1838.off() 		# LB1838 kapalı
	
	while True:				# "LDR sinyali > 61611 gece" olana kadar dön[][-(*3)
		if(LDR.read_u16() > 61611): # LDR sinyali ADC(26) okunuyor..
			machine.reset() 		# HELLO WORLD.../\/\/\/\/\/\/\/\/\/\
			#gece()
		else:
			time.sleep(2)
#[][][][][][][][][][][][][][][][][][][][][][][]][][][][][][][][][]][][][-(*2)

def gece(): # IR-CUT-filtre GECE " lightlevel > 61611 " çalışır
	
	LED.off() 			# IR-LED kapalı
	LB1838İNP1.high() 	# Motor SAG > dönüyor - LB1838-İNP1 " + "high
	LB1838.on() 		# LB1838 açık
	time.sleep(0.7)		# Filtre " gece " tarafına döndü
	LB1838.off() 		# LB1838 kapalı
	LED.on() 			# IR-LED Start Voltajı için Transistörü aç
	
	while True:				# "LDR sinyali < 61611 gündüz"olana kadar dön][-(*3)
		if(LDR.read_u16() < 61611): # LDR sinyali ADC(26) okunuyor..
			machine.reset() 		# HELLO WORLD.../\/\/\/\/\/\/\/\/\/\
			#gunduz()
		else:
			time.sleep(2)
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\-START-/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\-(1)

def start():# 65535  ‘full voltage ADC’.
	
	while True:	# LDR kontrol ADC(26) - " GECE / GUNDUZ " kontrol ediliyor.
		if(LDR.read_u16() > 61611): # LDR.read_u16() > 61611 "den büyükse".
			gece()					# " gece " dir.
		else:						# Deilse
			gunduz()				# " gunduz " dür.
		
#[T]\\\\\\\\\\\\\\\\\\\\\\\\\\\\[]-TEST-[]////////////////////////////[T]

def test():
	for i in range(5):
		LED.off()
		LB1838İNP1.low()
		LB1838.on()
		time.sleep(2)
		
		lightlevel = LDR.read_u16()
		print(lightlevel)
		
		LED.on()
		LB1838İNP1.high()
		time.sleep(2)
#[T]////////////////////////////[]-TEST-[]\\\\\\\\\\\\\\\\\\\\\\\\\\\\[T]

test()

# start()
