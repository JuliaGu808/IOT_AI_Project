/* General settings */
unsigned long currentMillis;

/* Servo SETTINGS */
#define SERVO_PIN 12
#define INTERVAL 50

unsigned long PREV_SERVO_MILLIS = millis();
static Servo servo;

/* Button SETTINGS */
#define BUTTON_PIN 7
#define BTN_INTERVAL 50

unsigned long PREV_BTN_MILLIS = millis();
byte previousButtonState;
byte buttonState;
