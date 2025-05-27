#include <WiFi.h>
#include <PubSubClient.h>

// Network credentials
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

// MQTT server
const char* mqtt_server = "YOUR_MQTT_BROKER_IP";

// Pin controlling the light via MOSFET
const int lightPin = 5;

// MQTT and WiFi clients
WiFiClient espClient;
PubSubClient client(espClient);

// Pulse data
int pulseSequence[10];
int pulseCount = 0;

void setup_wifi() {
  delay(10);
  Serial.println();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
}

void callback(char* topic, byte* payload, unsigned int length) {
  String input = "";
  for (unsigned int i = 0; i < length; i++) input += (char)payload[i];

  int idx = 0, num = 0;
  bool reading = false;
  for (char c : input) {
    if (isdigit(c)) {
      num = num * 10 + (c - '0');
      reading = true;
    } else if (reading) {
      pulseSequence[idx++] = num;
      num = 0;
      reading = false;
    }
    if (idx >= 10) break;
  }
  pulseCount = idx;
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32LightAgent")) {
      client.subscribe("eliornet/light");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(lightPin, OUTPUT);
  digitalWrite(lightPin, LOW);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

  for (int i = 0; i < pulseCount; i++) {
    digitalWrite(lightPin, i % 2 == 0 ? HIGH : LOW);
    delay(pulseSequence[i]);
  }
  digitalWrite(lightPin, LOW);
  pulseCount = 0;
}
