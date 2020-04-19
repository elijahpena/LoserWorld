const int readyLED = D0;
const int brewingLED = D1;

void teaStatus(const char *event, const char *data);

int brewing(String isBrewing);
int isDone(String done);

void setup(){
  Serial.begin(9600);
  pinMode(readyLED, OUTPUT);
  pinMode(brewingLED, OUTPUT);
  Particle.subscribe("temperature", teaStatus, MY_DEVICES);
  Particle.function("brewing", brewing);
  Particle.function("isDone", isDone);
}

void loop() {

}

void teaStatus(const char *event, const char *data) {
  String myData = String(data);
  Serial.println(myData);
  Serial.println(atoi(myData.substring(15,17)));
  if (atoi(myData.substring(15,17)) >= 85) {
    digitalWrite(readyLED, HIGH);
    digitalWrite(brewingLED, LOW);
  }
}

int brewing(String isBrewing) {
  if (isBrewing.substring(0,4) == "true") {
    digitalWrite(brewingLED, HIGH);
    digitalWrite(readyLED, LOW);
  }
}

int isDone(String done) {
  if (done.substring(0,4) == "true") {
    digitalWrite(readyLED, HIGH);
    digitalWrite(brewingLED, LOW);
  }
}
