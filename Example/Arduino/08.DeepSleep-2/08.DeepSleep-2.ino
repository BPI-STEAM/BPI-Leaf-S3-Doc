void setup() { 
  // put your setup code here, to run once: 
  pinMode(D9,OUTPUT);
  digitalWrite(D9,HIGH);
  delay(1000);
  digitalWrite(D9,LOW); 
  esp_deep_sleep_enable_ext0_wakeup(GPIO_NUM_25,LOW);
  esp_deep_sleep_start(); 
}  
void loop() { 
      // put your main code here, to run repeatedly: 
} 
