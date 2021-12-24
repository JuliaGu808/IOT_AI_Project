void initButton() {
  pinMode(BUTTON_PIN, INPUT);
  previousButtonState = digitalRead(BUTTON_PIN);
}

void checkBtnState() {
  currentMillis = millis();
  if (currentMillis - PREV_BTN_MILLIS >= BTN_INTERVAL) {
    buttonState = digitalRead(BUTTON_PIN);
    if (buttonState != previousButtonState) {
      PREV_BTN_MILLIS = currentMillis;
      previousButtonState = buttonState;
      if (buttonState == HIGH) {
        openDoor();
      }
      else{
        closeDoor();
      }
    }
  }
}
