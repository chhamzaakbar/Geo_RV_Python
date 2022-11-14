//CODE BY SARANSH_MAHIMA//
#include<Servo.h>
Servo m1; //motor #1
int velocity=0; //motor velocity
int pot=0; //potentiometer pin----> A0
void setup()
{
  pinMode(pot,INPUT);
  Serial.begin(9600);
  m1.attach(10); //connect the signal pin of esc to any pwm enabled pin on the arduino. In this case its pin 6
  delay(1); // no use of this line -_-
  m1.write(40);// this arms the HW esc
  delay(3000);// this delay is a must.
}
void loop()
{
  //rest is self explanatory
 velocity=analogRead(pot);
 velocity=map(velocity,0,1023,60,180);//mapping values from 0-1023 to 60-180;
 Serial.println(velocity);//if you wanna see the speed on the serial monitor
 m1.write(velocity);//boom
}

