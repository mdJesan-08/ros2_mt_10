//setting up the pin is the most necessary thing
void pinSetup() {
  //forward pin setup
  pinMode(fr_1, OUTPUT);
  pinMode(fr_2, OUTPUT);
  pinMode(fl_1, OUTPUT);
  pinMode(fl_2, OUTPUT); 
  //backwad pin setup
  pinMode(br_1, OUTPUT);
  pinMode(br_2, OUTPUT);
  pinMode(bl_1, OUTPUT);
  pinMode(bl_2, OUTPUT);
  pinMode(13,OUTPUT);

}


//Single Single motor forward
void forward(int p1, int p2) {
  analogWrite(p1, 70);
  analogWrite(p2, 0);
}
void backward(int p1, int p2) {
  analogWrite(p1, 0);
  analogWrite(p2, 70);
}
void stop(int p1, int p2) {
  analogWrite(p1, 0);
  analogWrite(p2, 0);
}

