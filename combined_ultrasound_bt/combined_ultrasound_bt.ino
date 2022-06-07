#include <SoftwareSerial.h>

const byte trigPin = 10;
const byte echoPin = 6;

const byte rxPin = 8;
const byte txPin = 9;

const byte led = 12;
char incVal = 0;

long duration;
int distance;
int prevDist = 0;
int change;

SoftwareSerial Bluetooth(rxPin,txPin);


void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);

  pinMode(led,OUTPUT);
  digitalWrite(led,HIGH);
  //38400
  Serial.begin(9600);
  Bluetooth.begin(9600);
  Serial.println("Serial Ready!");
  Bluetooth.println("Bluetooth Ready!");
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);

  duration = pulseIn(echoPin,HIGH);
  distance = duration * (0.034/2);

  change =abs(distance - prevDist);
  
  Bluetooth.println(distance);
  Serial.println(distance);

  // Delay could be a source of error
  delay(3400);
    
  
}
