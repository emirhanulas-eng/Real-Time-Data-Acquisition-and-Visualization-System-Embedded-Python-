//Pin assignment
int analog = 27;


void setup() {

  Serial.begin(9600);       //initialize serial communication accordingly
  pinMode(analog, INPUT);

}

void loop() {

  int reading = analogRead(analog);
  Serial.println(reading);
  delay(100);               

}
