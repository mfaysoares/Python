import RPi.GPIO as GPIO
from Tkinter import *
import tkFont
import Adafruit_DHT
from PIL import ImageTk, Image

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup();
GPIO.setup(38,GPIO.OUT)

#Pinos PWM - Fan
pwmFan = GPIO.PWM(38,100)
pwmFan.start(0)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25

root = Tk() #Cria a Janela
root.wm_title("T3_DISP_MOVEIS") #Título da Janela
#root.wm_attributes('-transparentcolor',root['bg'])
#root.config(background = "green") #Cor de fundo

#img = ImageTk.PhotoImage(Image.open("pucrs.png"))
#imglabel = Label(root, image=img).grid(row=6, column=5)
img = ImageTk.PhotoImage(Image.open("background.png"))
background_label = Label(image=img)
background_label.place(x=0,y=0,relwidth=1,relheight=1)


def LAMP_ON():
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    return

def LAMP_OFF():
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.HIGH)
    return

def ATUALIZA():
    Text1.delete('1.0', END)
    Text2.delete('1.0', END)
    #umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
    #Text1.insert(INSERT, "%.2f ºC"%temp)
    #Text2.insert(INSERT, "%.2f ur"%umid)
    #print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}n").format(temp, umid);

    dcFan = slider1.get()
    dcLed = slider2.get()
    print("PWM FAN = %d"%dcFan)
    print("PWM LED = %d"%dcLed)
    pwmFan.ChangeDutyCycle(dcFan)

    return



Titulo = Label(root, text="T3 - Domótica (Disp. Móveis)",bg="green",fg="white", font = "Helvetica 20 bold")
Titulo.grid(row=0, columnspan=6)


#Ligar Relé - Lâmpada
Titulo2 = Label(root, text="Ligar Lâmpada",bg = "green", fg="white", font = "Helvetica 16 bold")
Titulo2.grid(row=1, column=0, columnspan=2)

Ligarbt = Button(text="ON", command=LAMP_ON, height=2, width=8,font = "Helvetica 16 bold")
Ligarbt.grid(row=2, column=0, padx=10, pady=2)

Desligarbt = Button(text="OFF", command=LAMP_OFF, height=2, width=8,font = "Helvetica 16 bold")
Desligarbt.grid(row=2, column=1, padx=10, pady=2)

#Controle do FAN - PWM
Titulo3 = Label(root, text="PWM Fan",bg = "green", fg="white", font = "Helvetica 16 bold")
Titulo3.grid(row=1, column=4, columnspan=2)

slider1 = Scale(root, from_=0, to=100, orient=HORIZONTAL,length=120,font = "Helvetica 14 bold")
slider1.grid(row=2,column=4, columnspan=2)

#Dimmerização dos Leds - PWM
Titulo4 = Label(root, text="Dimmer Leds",bg = "green", fg="white", font = "Helvetica 16 bold")
Titulo4.grid(row=3, column=4, columnspan=2)

slider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL,length=120,font = "Helvetica 14 bold")
slider2.grid(row=4,column=4, columnspan=2)

#Temperatura - DHT11
Titulo5 = Label(root, text="Temperatura",bg = "green", fg="white", font = "Helvetica 16 bold")
Titulo5.grid(row=3, column=0)

Text1 = Text(root,height=1, width=8,font = "Helvetica 16 bold")
Text1.grid(row=3, column=1)

#Umidade - DHT11
Titulo6 = Label(root, text="Umidade",bg = "green", fg="white", font = "Helvetica 16 bold")
Titulo6.grid(row=4, column=0)

Text2 = Text(root,height=1, width=8,font = "Helvetica 16 bold")
Text2.grid(row=4, column=1)

#Atualizar
Atualizarbt = Button(text="Atualizar", command=ATUALIZA,height=2, width=8, font = "Helvetica 16 bold")
Atualizarbt.grid(row=10, column=1, columnspan=3, padx=10, pady=2)

root.mainloop()



