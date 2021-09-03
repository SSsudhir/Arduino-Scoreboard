#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);


byte fullPixel[] = {
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111,
  B11111
};

byte emptyPixel[] = {
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000,
  B00000
};


void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("   Scoreboard   ");
  
  lcd.createChar(0, fullPixel);
  lcd.createChar(1, emptyPixel);
}

void loop() {
  if (Serial.available()) {
    delay(100);  //wait some time for the data to fully be read
    lcd.clear();
    while (Serial.available() > 0) {
      char c = Serial.read();
      if (c == '\\')
      {
        lcd.setCursor(0, 1);
      }
      else if (c == '~')
      {
        for(int i = 0; i < 16; i++)
        {
          lcd.setCursor(i,0);lcd.write(byte(0));
          lcd.setCursor(i,1);lcd.write(byte(0));
          delay(50);
        }
        for(int j = 0; j < 16; j++)
        {
          lcd.setCursor(j,0);lcd.write(byte(1));
          lcd.setCursor(j,1);lcd.write(byte(1));
          delay(50);
        }
        lcd.clear();
      }
      else
      {
        lcd.write(c);
      }
    }
  }
}
