#include <Servo.h>
Servo myservo;
int pos;

void setup() {
 
  myservo.attach(2); // servo on pin 2
  Serial.begin(115200); // begin serial at baud rate of 115200.
}

void loop()
{    
    while (!Serial.available()); // wait until serial is available:
    pos = Serial.readString().toInt(); // read serial value to int
    myservo.write(pos);     // move servo
    Serial.print("Servo in position: ");  
    Serial.println(pos);
}
