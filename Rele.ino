// Definir los pines
const int ledPin = 12;
const int relayPin = 2;

void setup() {
  // Configurar los pines como salida
  pinMode(ledPin, OUTPUT);
  pinMode(relayPin, OUTPUT);
}

void loop() {
  // Encender el relé
  digitalWrite(relayPin, HIGH);
  // Encender el LED
  digitalWrite(ledPin, HIGH);
  // Esperar 2 segundos
  delay(2000);
  // Apagar el relé
  digitalWrite(relayPin, LOW);
  // Apagar el LED
  digitalWrite(ledPin, LOW);
  // Esperar 5 segundos
  delay(5000);
}
