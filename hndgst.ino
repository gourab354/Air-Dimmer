#include <WiFi.h>

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASS";

WiFiServer server(80);

const int ledPin = 27;
int brightness = 0;
int targetBrightness = 0;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.println(WiFi.localIP());

  server.begin();

  // PWM setup (new ESP32 core compatible)
  ledcAttach(ledPin, 5000, 8);
}

void loop() {

  WiFiClient client = server.available();

  if (client) {
    String data = "";

    while (client.connected()) {
      while (client.available()) {
        char c = client.read();
        data += c;
      }
      break;
    }

    targetBrightness = constrain(data.toInt(), 0, 255);
    client.stop();
  }

  // Smooth transition (important)
  if (brightness < targetBrightness) brightness++;
  if (brightness > targetBrightness) brightness--;

  ledcWrite(ledPin, brightness);

  delay(5);  // smoothness control
}