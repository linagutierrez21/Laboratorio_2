int PIEZO = 11;
int LED = 10;   // PWM

// Botones
int BUTTON_C = 2;
int BUTTON_D = 3;
int BUTTON_E = 4;
int BUTTON_F = 5;
int BUTTON_G = 6;
int BUTTON_A = 7;
int BUTTON_B = 8;
int BUTTON_C2 = 9;

// Sensor de luz
int LDR = A0;

void setup()
{
  for(int i = 2; i <= 9; i++)
  {
    pinMode(i, INPUT_PULLUP);
  }

  pinMode(LED, OUTPUT);
}

void loop()
{
  int luz = analogRead(LDR); // ADC

  // MODULACIÓN
  int brillo = map(luz, 0, 1023, 0, 255);
  int variacion = map(luz, 0, 1023, -50, 50);

  int presionado = 0;  // detecta si hay tecla

  // TECLAS
  if(digitalRead(BUTTON_C) == LOW){
    tone(PIEZO, 262 + variacion);
    presionado = 1;
  }
  else if(digitalRead(BUTTON_D) == LOW){
    tone(PIEZO, 294 + variacion);
    presionado = 1;
  }
  else if(digitalRead(BUTTON_E) == LOW){
    tone(PIEZO, 330 + variacion);
    presionado = 1;
  }
  else if(digitalRead(BUTTON_F) == LOW){
    tone(PIEZO, 349 + variacion);
    presionado = 1;
  }
  else if(digitalRead(BUTTON_G) == LOW){
    tone(PIEZO, 392 + variacion);
    presionado = 1;
  }
  else if(digitalRead(BUTTON_A) == LOW){
    tone(PIEZO, 440 + variacion);
    presionado = 1;
  }
  else if(digitalRead(BUTTON_B) == LOW){
    tone(PIEZO, 494 + variacion);
    presionado = 1;
  }
  else if(digitalRead(BUTTON_C2) == LOW){
    tone(PIEZO, 523 + variacion);
    presionado = 1;
  }
  else{
    noTone(PIEZO);
  }

  // LED solo cuando hay tecla
  if(presionado == 1){
    analogWrite(LED, brillo);
  }else{
    analogWrite(LED, 0);
  }
}
