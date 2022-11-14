import pygame
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
#----------------------------------------
from tcpcom import TCPClient
#import PID
import time

#IP_ADDRESS = "192.168.43.31"  #HONOR
IP_ADDRESS = "169.254.152.165"
IP_PORT = 22000
def onStateChanged(state, msg):
    global isConnected
    if state == "CONNECTING":
       print "Client:-- Waiting for connection..."
    elif state == "CONNECTED":
       print "Client:-- Connection estabished."
    elif state == "DISCONNECTED":
       print "Client:-- Connection lost."
       isConnected = False
    elif state == "MESSAGE":
       print "\nClient:-- Received data:", msg
# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printt(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    


client = TCPClient(IP_ADDRESS, IP_PORT, stateChanged = onStateChanged)
rc = client.connect()
t=time.time()
print t
if rc:
    isConnected = True
    while isConnected:
        pygame.init()

        # Set the width and height of the screen [width,height]
        size = [500, 700]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("My Game")

        #Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # Initialize the joysticks
        pygame.joystick.init()

        # Get ready to print
        textPrint = TextPrint()


        # -------- Main Program Loop -----------
        while done==False:
            # EVENT PROCESSING STEP
            #print("YOYOOOOO")
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop
                
                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")
                    #client.sendMessage("Joystick button pressed.")
                if event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.")
                    #client.sendMessage("Joystick button released.")
                    
         
            # DRAWING STEP
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            screen.fill(WHITE)
            textPrint.reset()

            # Get count of joysticks
            joystick_count = pygame.joystick.get_count()

            textPrint.printt(screen, "Number of joysticks: {}".format(joystick_count) )
            textPrint.indent()
            
            # For each joystick:
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
            
                textPrint.printt(screen, "Joystick {}".format(i) )
                textPrint.indent()
            
                # Get the name from the OS for the controller/joystick
                name = joystick.get_name()
                textPrint.printt(screen, "Joystick name: {}".format(name) )
                
                # Usually axis run in pairs, up/down for one, and left/right for
                # the other.
                axes = joystick.get_numaxes()
                textPrint.printt(screen, "Number of axes: {}".format(axes) )
                textPrint.indent()
                jyk=2
                for i in range( axes ):
                    axis = joystick.get_axis( i )
                    textPrint.printt(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
                    if (i==0) & (axis>0.8) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TL+100"
                        client.sendMessage("TL+100")
                        #break
                    elif (i==0) & (axis<-0.8) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TL-100"
                        client.sendMessage("TL-100")
                        #break
                    elif (i==1) & (axis>0.8) & ((time.time()-t)>0.3):
                        t=time.time()
                        print "TL-10"
                        client.sendMessage("TL-10")
                        break
                    elif (i==1) & (axis<-0.8) & ((time.time()-t)>0.3):
                        t=time.time()
                        print "TL+10"
                        client.sendMessage("TL+10")
                        #break
                    elif (i==2) & (axis>0.8) & ((time.time()-t)>0.2):
                        t=time.time()
                        print "VT+10"
                        client.sendMessage("VT+10")
                        #break
                    elif (i==2) & (axis<-0.8) & ((time.time()-t)>0.2):
                        t=time.time()
                        print "VT-10"
                        client.sendMessage("VT-10")
                        #break
                    elif (i==3) & (axis>0.8) & ((time.time()-t)>0.3):
                        t=time.time()
                        print "TR-10"
                        client.sendMessage("TR-10")
                        #break
                    elif (i==3) & (axis<-0.8) & ((time.time()-t)>0.3):
                        t=time.time()
                        print "TR+10"
                        client.sendMessage("TR+10")
                        #break
                    elif (i==4) & (axis>0.8) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TR+100"
                        client.sendMessage("TR+100")
                        break
                    elif (i==4) & (axis<-0.8) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TR-100"
                        client.sendMessage("TR-100")
                        #break
                textPrint.unindent()
                    
                buttons = joystick.get_numbuttons()
                textPrint.printt(screen, "Number of buttons: {}".format(buttons) )
                textPrint.indent()

                for i in range( buttons ):
                    button = joystick.get_button( i )
                    textPrint.printt(screen, "Button {:>2} value: {}".format(i,button) )
                    if (i==0) & (button==1) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "VT=1350"
                        client.sendMessage("VT=1350")
                        #break
                    elif (i==1) & (button==1) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TR=800"
                        client.sendMessage("TR=800")
                        #break
                    elif (i==3) & (button==1) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "VT=1650"
                        client.sendMessage("VT=1650")
                        #break
                    elif (i==2) & (button==1) & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TL=800"
                        client.sendMessage("TL=800")
                        #break
                textPrint.unindent()
                    
                # Hat switch. All or nothing for direction, not like joysticks.
                # Value comes back in an array.
                hats = joystick.get_numhats()
                textPrint.printt(screen, "Number of hats: {}".format(hats) )
                textPrint.indent()

                for i in range( hats ):
                    hat = joystick.get_hat( i )
                    textPrint.printt(screen, "Hat {} value: {}".format(i, str(hat)) )
                    #print str(hat)
                    if (str(hat)=="(0, 1)") & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TR,TL+10"
                        client.sendMessage("TR,TL+10")
                        #break
                    elif (str(hat)=="(-1, 0)") & ((time.time()-t)>1):
                        t=time.time()
                        print "TL=800 AND TR=SPEED+100"
                        client.sendMessage("TL=800 AND TR=SPEED+100")
                        #break
                    elif (str(hat)=="(0, -1)") & ((time.time()-t)>0.5):
                        t=time.time()
                        print "TR,TL+10"
                        client.sendMessage("TR,TL+10")
                        #break
                    elif (str(hat)=="(1, 0)") & ((time.time()-t)>1):
                        t=time.time()
                        print "TR=800 AND TL=SPEED+100"
                        client.sendMessage("TR=800 AND TL=SPEED+100")
                        #break
                textPrint.unindent()
                
                textPrint.unindent()

            
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 20 frames per second
            clock.tick(20)
            
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        client.sendMessage("Done")
        pygame.quit ()
        break
    print "Done"    
else:
    print "Client:-- Connection failed"
        
