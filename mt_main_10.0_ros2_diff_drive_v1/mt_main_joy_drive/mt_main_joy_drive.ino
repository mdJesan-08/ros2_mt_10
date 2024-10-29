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


int myCmd = 0;

long timer;

void setup() {
  Serial.begin(115200);
  //Check wether all the pins are defined or not in the setup function
  pinSetup();
  timer = millis() - 100;
}
// # we are mapping from 0 to  5
// -1----->+1=0 BACKWARD
//  0----->+1=1 LINEAR STOP
//  1----->+1=2 FORWARD



// -1----->+4=3 LEFT ROTATE
//  0----->+4=4  ANGULAR STOP
//  1----->+4=5  RIGHT ROTATE

void loop() {
  // analogWrite(13,0);
  myCmd = 0;
  // Serial.available() actually returns the number of bytes avaiable
  // Serial.println(Serial.available());

  //If there is something is there what to do actually
  if (Serial.available() > 0) {
    myCmd = Serial.read();
    if (myCmd == 2) {
      whole_forward();
      Serial.println("F");
      analogWrite(13,250);
    }

    else if (myCmd == 0) {
      analogWrite(13,0);
      Serial.println("B");
      whole_backward();
    }

    else if (myCmd == 3) {
      Serial.println("LR");
      whole_left_rotation();
    }

    else if (myCmd == 5) {
      Serial.println("RR");
      whole_right_rotation();
    }

    else {
      Serial.println("SE");
      analogWrite(13, 70);
      whole_stop();
    }

    //we  just start the timer
    timer = millis();
  }


  // safety case to make the rover stop if we lsoe serial communication
  else if (millis() - timer > 100) {
    whole_stop();
    analogWrite(13, 70);
  }
}


// void loop(){
//   whole_right_rotation();
//   delay(2000);
//   whole_stop();
//   delay(2000);
//   whole_left_rotation();
//   delay(2000);
//   whole_stop();
//   delay(2000);

// }
