//front right
#define fr_1 3
#define fr_2 2

//front left
#define fl_1 4
#define fl_2 5

//back right
#define br_1 7
#define br_2 6
//back  left
#define bl_1 8
#define bl_2 9



void setup() {
  Serial.begin(115200);
  pinSetup();
}

// void loop() {
//   if (Serial.available() > 0) {
//     myCmd = Serial.read();
//     myCmd -= 1;
//     if (myCmd == 1) {
//         forward();
//     }
//     else if (myCmd == 0) {
//        stop();
//     }
//     else{
//       backward();
//     }
//   }
// }
void loop() {
  forward(fr_1, fr_2);
  forward(fl_1, fl_2);
  forward(br_1, br_2);
  forward(bl_1, bl_2);

  delay(2000);
  
  stop(fr_1, fr_2);
  stop(fl_1, fl_2);
  stop(br_1, br_2);
  stop(bl_1, bl_2);

  delay(2000);

  backward(fr_1, fr_2);
  backward(fl_1, fl_2);
  backward(br_1, br_2);
  backward(bl_1, bl_2);

  delay(2000);

  stop(fr_1, fr_2);
  stop(fl_1, fl_2);
  stop(br_1, br_2);
  stop(bl_1, bl_2);

  delay(2000);
}
