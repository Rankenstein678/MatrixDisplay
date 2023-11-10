#include <Adafruit_NeoPixel.h>
#define PIN_NEO_PIXEL  7   // Arduino pin that connects to NeoPixel
#define NUM_PIXELS     144  // The number of LEDs (pixels) on NeoPixel
Adafruit_NeoPixel NeoPixel(NUM_PIXELS, PIN_NEO_PIXEL, NEO_GRB + NEO_KHZ800);

void setup() {
  NeoPixel.begin();
  NeoPixel.clear();
  NeoPixel.setBrightness(50); // a value from 0 to 255
  NeoPixel.show();
  Serial.begin(138000 );
  Serial.setTimeout(1);
}


int state = 0;
int pos, r, g, b;
void loop() {
  if (Serial.available() > 0) {
    int data =  Serial.read();
    if (data == 255) {
      NeoPixel.show();
      state=-1;
    } else if (state == 0) {
      pos = data;
    } else if (state == 1) {
      r = data;
    } else if (state == 2) {
      g = data;
    } else {
      b = data;
      NeoPixel.setPixelColor(pos, NeoPixel.Color(r, g, b));
      state = -1;
      digitalWrite(LED_BUILTIN,HIGH);
    }
    state++;
  }
}
