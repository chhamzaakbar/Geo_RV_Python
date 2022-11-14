from Tkinter import *       # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time
import pigpio
# Configure the Pi to use the BOARD  pin names, rather than the pin positions
ESC_30A=12  #Connect the ESC in this GPIO pin 
ESC_40A=16
ESC_30A_2=21
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC_30A, 800)
pi.set_servo_pulsewidth(ESC_40A, 800)
pi.set_servo_pulsewidth(ESC_30A_2, 800)
GPIO.setwarnings(False)
# Start Pulse Width Modulation (PWM) on the red, green and blue channels to 
# control the brightness of the LEDs.
# Follow this link for more info on PWM: http://en.wikipedia.org/wiki/Pulse-width_modulation

# group together all of the GUI code into a class called App
class App:

    # this function gets called when the app is created
    def __init__(self, master):
        # A frame holds the various GUI controls
        frame = Frame(master)
        frame.pack()

        # Create the labels and position them in a grid layout
        Label(frame, text='Thruster 1').grid(row=0, column=0)
        Label(frame, text='Thruster 2').grid(row=1, column=0)
        Label(frame, text='Thruster 3').grid(row=2, column=0)
        T1 = Scale(frame, from_=0, to=500,
              orient=HORIZONTAL,length = 700, command=self.updateTr1)
        T1.grid(row=0, column=1)
        T2 = Scale(frame, from_=0, to=500,
              orient=HORIZONTAL,length = 700, command=self.updateTr2)
        T2.grid(row=1, column=1)
        T3 = Scale(frame, from_=0, to=500,
              orient=HORIZONTAL,length = 700, command=self.updateTr3)
        T3.grid(row=2, column=1)

    # These methods called whenever a slider moves
    def updateTr1(self, duty):
        # change the led brightness to match the slider
        pi.set_servo_pulsewidth(ESC_30A,float(duty)+800)
        #print ("hamza")

    def updateTr2(self, duty):
        pi.set_servo_pulsewidth(ESC_40A,float(duty)+800)
        #Tr2.ChangeDutyCycle(float(duty+800))

    def updateTr3(self, duty):
        pi.set_servo_pulsewidth(ESC_30A_2,float(duty)+1500)

root = Tk()
root.wm_title('Thruster')
app = App(root)
root.geometry("900x200+150+360")
try:
    root.mainloop()
    #print ("hamza")
finally:
    GPIO.cleanup()
    GPIO.setwarnings(False)

