void whole_forward(){
  forward(fr_1, fr_2);
  forward(fl_1, fl_2);
  forward(br_1, br_2);
  forward(bl_1, bl_2);
}

void whole_backward(){
  backward(fr_1, fr_2);
  backward(fl_1, fl_2);
  backward(br_1, br_2);
  backward(bl_1, bl_2);
}

void whole_stop(){
  stop(fr_1, fr_2);
  stop(fl_1, fl_2);
  stop(br_1, br_2);
  stop(bl_1, bl_2);

}
void whole_right_rotation(){
  forward(fl_1, fl_2);
  forward(bl_1, bl_2);
  backward(fr_1, fr_2);
  backward(br_1, br_2);
}

void whole_left_rotation(){
  forward(fr_1, fr_2);
  forward(br_1, br_2);
  backward(fl_1, fl_2);
  backward(bl_1, bl_2);

}

