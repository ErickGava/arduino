
void setup() {
  pinMode(10, OUTPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}


void loop() {
  if(Serial.available()) {
    char comando = Serial.read();
    if(comando =='1'){
      digitalWrite(12, HIGH);
    }
    else if(comando == '2'){
      digitalWrite(10, HIGH);
    }
    else if(comando == '3'){
      digitalWrite(10, HIGH);
      digitalWrite(12, HIGH);
    }
    else if(comando == '4'){
      digitalWrite(12, LOW);
    }
    else if(comando == '5'){
      digitalWrite(10, LOW);
    }
    else if(comando == '0'){
      digitalWrite(10, LOW);
      digitalWrite(12, LOW);
    }
   }
}
