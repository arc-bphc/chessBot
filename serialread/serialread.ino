int data;
void setup() {
Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    data=Serial.read();
    Serial.print("\t");
    Serial.print(data-48);
  }
}
