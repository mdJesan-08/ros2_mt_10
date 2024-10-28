
void forward(int p1, int p2) {
  analogWrite(p1, 150);
  analogWrite(p2, 0);
}
void backward(int p1, int p2) {
  analogWrite(p1, 0);
  analogWrite(p2, 150);
}
void stop(int p1, int p2) {
  analogWrite(p1, 0);
  analogWrite(p2, 0);
}

void pinSetup() {
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
}