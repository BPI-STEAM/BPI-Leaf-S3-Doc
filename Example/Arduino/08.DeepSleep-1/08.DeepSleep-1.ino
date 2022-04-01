void setup() { 
  // put your setup code here, to run once: 
  pinMode(D9,OUTPUT);
  digitalWrite(D9,HIGH);
  delay(1000);
  digitalWrite(D9,LOW); 
  ESP.deepSleep(5000000); 
}  
void loop() { 
      // put your main code here, to run repeatedly: 
} 
