#define BOUNCE 0
#define OFF 2
void setup() {
  pinMode(BOUNCE, OUTPUT);
  pinMode(OFF, OUTPUT);
  digitalWrite(BOUNCE, HIGH);
  //Wait 3 seconds
  delay(3000);
  //power on pi
  digitalWrite(BOUNCE, LOW);
  delay(200);
  digitalWrite(BOUNCE, HIGH);
  delay(1000);
  //keeps relay on
  digitalWrite(OFF, LOW);
}

void loop() {
  // nothing is needed here

}
