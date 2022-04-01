void setup()
{
Serial.begin(115200); //Set serial communication baud rate
}
void loop()
{
static unsigned long i = 0; //Define variable i
Serial.println(i++); //i output i after incrementing by 1 
delay(1000); //Delay 1 second
