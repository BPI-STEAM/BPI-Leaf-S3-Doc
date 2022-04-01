 void setup() 
{ 
  Serial.begin(115200); 
      delay(1000); // give me time to bring up serial monitor 
      Serial.println("Leaf-S3 Touch Test");    
}  
void loop(){ 
  Serial.println(touchRead(T14));  // get value using T1->T14  
  delay(100); 
} 
