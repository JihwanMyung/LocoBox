#include <Adafruit_I2CDevice.h>
#include <Adafruit_BusIO_Register.h>
#include <Adafruit_SPIDevice.h>
#include <Adafruit_I2CRegister.h>

/*
 * 1-LED, 1-PIR box driver (1 arduino driving 10 box)
 *
 * Jihwan Myung
 * 28 Mar 2022 DS3231 correction
 * 14 Oct 2018 PIR range increased [0, 1000]
 * 30 Sep 2018
 * 29 Sep 2018 (initial)
 *
 * Vuong Truong
 * 9 Oct 2018 make the GUI
 * 5 Oct 2018 complete the code
 * 3 Oct 2018 (major revision)
 *
 */

#include <RTClib.h>
#include <Wire.h>
// #include <DS3231.h>

//#include <DS1307.h>
RTC_DS3231 rtc; // define a object of RTClib class, DS3231
// using https://learn.adafruit.com/adafruit-ds3231-precision-rtc-breakout/arduino-usage

uint32_t T_cycle_time;
uint32_t unix_time;
int init_time_flag;

// Define a function to convert string to integer
int getInt(String text)
{
  char temp[6];
  text.toCharArray(temp, 5);
  int x = atoi(temp);
  return x;
}

//////////////////////////////////////////////////////////////////////////////////////// Set up run
void setup()
{
  Serial.begin(9600);
  Wire.begin();
  // start the connexion to the RTC

  if (!rtc.begin())
  {
    Serial.println("Couldn't find RTC");
    Serial.flush();
  }

  if (rtc.lostPower())
  {
    Serial.println("RTC lost power, let's set the time!");
    // When time needs to be set on a new device, or after a power loss, the
    // following line sets the RTC to the date & time this sketch was compiled
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    // This line sets the RTC with an explicit date & time, for example to set
    // January 21, 2014 at 3am you would call:
    // rtc.adjust(DateTime(2014, 1, 21, 3, 0, 0));
  }
}

//////////////////////////////////////////////////////////////////////////////////////// Main loop
float T_cycle_ratio = 2;

void loop()
{
  DateTime timenow = rtc.now();

  while (timenow.second() != 0) // now.second() == 0
  { 
    timenow = rtc.now();
  }

  if (init_time_flag == 1){
  T_cycle_time = T_cycle_time + round(60 * 48/24);
  }

  if (init_time_flag == 0){
    unix_time = timenow.unixtime();
    T_cycle_time = unix_time;
    init_time_flag = 1;
  }



  delay(1000);
  printTime(T_cycle_time);
  Serial.println(" ");
  printTime(timenow);
  Serial.println(" ");
  Serial.println(" ");
}


// Define a function to print time
void printTime(DateTime now)
{
  //DateTime now = rtc.now();
  if (now.hour() < 10)
  {
    Serial.print("0");
  }
  Serial.print(now.hour(), DEC);
  Serial.print(":");
  if (now.minute() < 10)
  {
    Serial.print("0");
  }
  Serial.print(now.minute(), DEC);
  Serial.print(":");
  if (now.second() < 10)
  {
    Serial.print("0");
  }
  Serial.print(now.second(), DEC);
  Serial.print(" ");
  if (now.month() < 10)
  {
    Serial.print("0");
  }
  Serial.print(now.month(), DEC);
  Serial.print("/");
  if (now.day() < 10)
  {
    Serial.print("0");
  }
  Serial.print(now.day(), DEC);
  Serial.print("/");
  Serial.print(now.year(), DEC);
}
