// This is the prototype

#include "mbed.h"
#include "DHT.h"

// Buttons for temperature
DigitalIn mybutton1(A4);
DigitalIn mybutton2(A5);
DigitalIn mybutton3(D2);
DigitalIn mybutton4(D7);

// Buttons for humidity
DigitalIn mybutton5(A2);
DigitalIn mybutton6(A3);
DigitalIn mybutton7(D3);
DigitalIn mybutton8(D6);

// Temperature relay
DigitalOut myled(D10);

// Humidity relay
DigitalOut myled1(D4);

// Debug led
DigitalOut test(LED1);

// Temperature and humidity sensor
DHT sensor(A3, RHT01);

int main() {

  mybutton1.mode(PullNone);
  mybutton2.mode(PullNone);
  mybutton3.mode(PullNone);
  mybutton4.mode(PullNone);
  
  mybutton5.mode(PullNone);
  mybutton6.mode(PullNone);
  mybutton7.mode(PullNone);
  mybutton8.mode(PullNone);
  
  int min_temp = 20;
  int max_temp = 30;
  
  int min_hum = 30;
  int max_hum = 50;

  while(1) {
      
    sensor.readData();
    int t = sensor.ReadTemperature(CELCIUS);
    int h = sensor.ReadHumidity();
    
    printf("Temperature is: %i \n\r", t);
    if (t < min_temp) {
        printf("Temperature is too low! \n");
        myled = !myled;
        }
    if (t > max_temp) {
        printf("Temperature is too high! \n");
        myled = !myled;
        }
    printf("Range of optimal temperature is between %i and %i \n\r", min_temp, max_temp);
    
    printf("Humidity is: %i \n\r", h);
    if (h < min_hum) {
        printf("Humidity is too low! \n");
        myled = !myled;
        }
    if (h > max_hum) {
        printf("Humidity is too high! \n");
        myled = !myled;
        }
    printf("Range of optimal humidity is between %i and %i \n\n\r", min_hum, max_hum);
       
    // Changing temperature range.
    if (mybutton1 == 0){
            min_temp += 1;
        }
    if (mybutton2 == 0){
            min_temp -= 1;
        }
    if (mybutton3 == 0){
            max_temp += 1;
        }
    if (mybutton4 == 0){
            max_temp -= 1;
        }
        
    // Changing humidity range.
    if (mybutton5 == 0){
            min_hum += 1;
        }
    if (mybutton6 == 0){
            min_hum -= 1;
        }
    if (mybutton7 == 0){
            max_hum += 1;
        }
    if (mybutton8 == 0){
            max_hum -= 1;
        }
    wait(1);
    }
}