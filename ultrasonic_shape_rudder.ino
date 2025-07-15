#include <NewPing.h>

// === Configuration ===
#define NUM_SENSORS 6
const int trigPins[NUM_SENSORS] = {12, 14, 26, 33, 22, 19};
const int echoPins[NUM_SENSORS] = {13, 27, 25, 32, 21, 18};
NewPing sonar[NUM_SENSORS] = {
  NewPing(trigPins[0], echoPins[0], 200),
  NewPing(trigPins[1], echoPins[1], 200),
  NewPing(trigPins[2], echoPins[2], 200),
  NewPing(trigPins[3], echoPins[3], 200),
  NewPing(trigPins[4], echoPins[4], 200),
  NewPing(trigPins[5], echoPins[5], 200)
};

const int sensorAngles[NUM_SENSORS] = {0, 30, 60, 90, 120, 150};

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < NUM_SENSORS; i++) {
    pinMode(trigPins[i], OUTPUT);
    pinMode(echoPins[i], INPUT);
  }
  delay(1000);
  Serial.println("Sensor Angle, Distance (cm)");
}

void loop() {
  for (int i = 0; i < NUM_SENSORS; i++) {
    delay(60); // To avoid crosstalk
    unsigned int dist = sonar[i].ping_cm();
    if (dist == 0) dist = 200; // Max distance fallback
    Serial.print(sensorAngles[i]);
    Serial.print(",");
    Serial.println(dist);
  }
  Serial.println("---"); // Separator for Python visualizer
  delay(200);
}
