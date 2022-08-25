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

String dateIn;
String initLEDs;
String lightIn1;
String lightIn2;
String lightIn3;
String lightIn4;
String lightIn5;
String lightIn6;
String lightIn7;
String lightIn8;
String lightIn9;
String lightIn10;
String lightIn11;
String lightIn12;

// declaration in array of 5 boxes
int PIR[5] = {0, 0, 0, 0, 0};
int mPIR[5] = {0, 0, 0, 0, 0};
int ANALOG[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int mANALOG[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // analog Values


// Default initial LED state (off) and applies for each box individually
int initLED[5] = {0, 0, 0, 0, 0};  // 0 off and 1 on

// Default light-on and off times for LD cycle
int phase1[5] = {0, 0, 0, 0, 0};
int HourOn1[5] = {7, 7, 7, 7, 7}; // phase 1
int MinuteOn1[5] = {0, 0, 0, 0, 0};
int HourOff1[5] = {19, 19, 19, 19, 19};
int MinuteOff1[5] = {0, 0, 0, 0, 0};
int light1[5] = {0, 0, 0, 0, 0}; // phase 1
int dark1[5] = {0, 0, 0, 0, 0};  // phase 1

int phase2[5] = {0, 0, 0, 0, 0};
int HourOn2[5] = {7, 7, 7, 7, 7}; // phase 2
int MinuteOn2[5] = {0, 0, 0, 0, 0};
int HourOff2[5] = {19, 19, 19, 19, 19};
int MinuteOff2[5] = {0, 0, 0, 0, 0};
int HourFrom2[5] = {0, 0, 0, 0, 0};            // phase 2
int MinuteFrom2[5] = {0, 0, 0, 0, 0};          // phase 2
int date2[5] = {10, 10, 10, 10, 10};           // phase 2
int month2[5] = {12, 12, 12, 12, 12};          // phase 2
int year2[5] = {2018, 2018, 2018, 2018, 2018}; // phase 2
int light2[5] = {0, 0, 0, 0, 0};               // phase 2
int dark2[5] = {0, 0, 0, 0, 0};                // phase 2

int phase3[5] = {0, 0, 0, 0, 0};
int HourOn3[5] = {7, 7, 7, 7, 7}; // phase 3
int MinuteOn3[5] = {0, 0, 0, 0, 0};
int HourOff3[5] = {19, 19, 19, 19, 19};
int MinuteOff3[5] = {0, 0, 0, 0, 0};
int HourFrom3[5] = {0, 0, 0, 0, 0};            // phase 3
int MinuteFrom3[5] = {0, 0, 0, 0, 0};          // phase 3
int date3[5] = {10, 10, 10, 10, 10};           // phase 3
int month3[5] = {12, 12, 12, 12, 12};          // phase 3
int year3[5] = {2018, 2018, 2018, 2018, 2018}; // phase 3
int light3[5] = {0, 0, 0, 0, 0};               // phase 3
int dark3[5] = {0, 0, 0, 0, 0};                // phase 3

int phase4[5] = {0, 0, 0, 0, 0};
int HourOn4[5] = {7, 7, 7, 7, 7}; // phase 4
int MinuteOn4[5] = {0, 0, 0, 0, 0};
int HourOff4[5] = {19, 19, 19, 19, 19};
int MinuteOff4[5] = {0, 0, 0, 0, 0};
int HourFrom4[5] = {0, 0, 0, 0, 0};            // phase 4
int MinuteFrom4[5] = {0, 0, 0, 0, 0};          // phase 4
int date4[5] = {10, 10, 10, 10, 10};           // phase 4
int month4[5] = {12, 12, 12, 12, 12};          // phase 4
int year4[5] = {2018, 2018, 2018, 2018, 2018}; // phase 4
int light4[5] = {0, 0, 0, 0, 0};               // phase 4
int dark4[5] = {0, 0, 0, 0, 0};                // phase 4

int phase5[5] = {0, 0, 0, 0, 0};
int HourOn5[5] = {7, 7, 7, 7, 7}; // phase 5
int MinuteOn5[5] = {0, 0, 0, 0, 0};
int HourOff5[5] = {19, 19, 19, 19, 19};
int MinuteOff5[5] = {0, 0, 0, 0, 0};
int HourFrom5[5] = {0, 0, 0, 0, 0};            // phase 5
int MinuteFrom5[5] = {0, 0, 0, 0, 0};          // phase 5
int date5[5] = {10, 10, 10, 10, 10};           // phase 5
int month5[5] = {12, 12, 12, 12, 12};          // phase 5
int year5[5] = {2018, 2018, 2018, 2018, 2018}; // phase 5
int light5[5] = {0, 0, 0, 0, 0};               // phase 5
int dark5[5] = {0, 0, 0, 0, 0};                // phase 5

int phase6[5] = {0, 0, 0, 0, 0};
int HourOn6[5] = {7, 7, 7, 7, 7}; // phase 6
int MinuteOn6[5] = {0, 0, 0, 0, 0};
int HourOff6[5] = {19, 19, 19, 19, 19};
int MinuteOff6[5] = {0, 0, 0, 0, 0};
int HourFrom6[5] = {0, 0, 0, 0, 0};            // phase 6
int MinuteFrom6[5] = {0, 0, 0, 0, 0};          // phase 6
int date6[5] = {10, 10, 10, 10, 10};           // phase 6
int month6[5] = {12, 12, 12, 12, 12};          // phase 6
int year6[5] = {2018, 2018, 2018, 2018, 2018}; // phase 6
int light6[5] = {0, 0, 0, 0, 0};               // phase 6
int dark6[5] = {0, 0, 0, 0, 0};                // phase 6

int phase7[5] = {0, 0, 0, 0, 0};
int HourOn7[5] = {7, 7, 7, 7, 7}; // phase 7
int MinuteOn7[5] = {0, 0, 0, 0, 0};
int HourOff7[5] = {19, 19, 19, 19, 19};
int MinuteOff7[5] = {0, 0, 0, 0, 0};
int HourFrom7[5] = {0, 0, 0, 0, 0};            // phase 7
int MinuteFrom7[5] = {0, 0, 0, 0, 0};          // phase 7
int date7[5] = {10, 10, 10, 10, 10};           // phase 7
int month7[5] = {12, 12, 12, 12, 12};          // phase 7
int year7[5] = {2018, 2018, 2018, 2018, 2018}; // phase 7
int light7[5] = {0, 0, 0, 0, 0};               // phase 7
int dark7[5] = {0, 0, 0, 0, 0};                // phase 7

int phase8[5] = {0, 0, 0, 0, 0};
int HourOn8[5] = {7, 7, 7, 7, 7}; // phase 8
int MinuteOn8[5] = {0, 0, 0, 0, 0};
int HourOff8[5] = {19, 19, 19, 19, 19};
int MinuteOff8[5] = {0, 0, 0, 0, 0};
int HourFrom8[5] = {0, 0, 0, 0, 0};            // phase 8
int MinuteFrom8[5] = {0, 0, 0, 0, 0};          // phase 8
int date8[5] = {10, 10, 10, 10, 10};           // phase 8
int month8[5] = {12, 12, 12, 12, 12};          // phase 8
int year8[5] = {2018, 2018, 2018, 2018, 2018}; // phase 8
int light8[5] = {0, 0, 0, 0, 0};               // phase 8
int dark8[5] = {0, 0, 0, 0, 0};                // phase 8

int phase9[5] = {0, 0, 0, 0, 0};
int HourOn9[5] = {7, 7, 7, 7, 7}; // phase 9
int MinuteOn9[5] = {0, 0, 0, 0, 0};
int HourOff9[5] = {19, 19, 19, 19, 19};
int MinuteOff9[5] = {0, 0, 0, 0, 0};
int HourFrom9[5] = {0, 0, 0, 0, 0};            // phase 9
int MinuteFrom9[5] = {0, 0, 0, 0, 0};          // phase 9
int date9[5] = {10, 10, 10, 10, 10};           // phase 9
int month9[5] = {12, 12, 12, 12, 12};          // phase 9
int year9[5] = {2018, 2018, 2018, 2018, 2018}; // phase 9
int light9[5] = {0, 0, 0, 0, 0};               // phase 9
int dark9[5] = {0, 0, 0, 0, 0};                // phase 9

int phase10[5] = {0, 0, 0, 0, 0};
int HourOn10[5] = {7, 7, 7, 7, 7}; // phase 10
int MinuteOn10[5] = {0, 0, 0, 0, 0};
int HourOff10[5] = {19, 19, 19, 19, 19};
int MinuteOff10[5] = {0, 0, 0, 0, 0};
int HourFrom10[5] = {0, 0, 0, 0, 0};            // phase 10
int MinuteFrom10[5] = {0, 0, 0, 0, 0};          // phase 10
int date10[5] = {10, 10, 10, 10, 10};           // phase 10
int month10[5] = {12, 12, 12, 12, 12};          // phase 10
int year10[5] = {2018, 2018, 2018, 2018, 2018}; // phase 10
int light10[5] = {0, 0, 0, 0, 0};               // phase 10
int dark10[5] = {0, 0, 0, 0, 0};                // phase 10

int phase11[5] = {0, 0, 0, 0, 0};
int HourOn11[5] = {7, 7, 7, 7, 7}; // phase 11
int MinuteOn11[5] = {0, 0, 0, 0, 0};
int HourOff11[5] = {19, 19, 19, 19, 19};
int MinuteOff11[5] = {0, 0, 0, 0, 0};
int HourFrom11[5] = {0, 0, 0, 0, 0};            // phase 11
int MinuteFrom11[5] = {0, 0, 0, 0, 0};          // phase 11
int date11[5] = {10, 10, 10, 10, 10};           // phase 11
int month11[5] = {12, 12, 12, 12, 12};          // phase 11
int year11[5] = {2018, 2018, 2018, 2018, 2018}; // phase 11
int light11[5] = {0, 0, 0, 0, 0};               // phase 11
int dark11[5] = {0, 0, 0, 0, 0};                // phase 11

int phase12[5] = {0, 0, 0, 0, 0};
int HourOn12[5] = {7, 7, 7, 7, 7}; // phase 12
int MinuteOn12[5] = {0, 0, 0, 0, 0};
int HourOff12[5] = {19, 19, 19, 19, 19};
int MinuteOff12[5] = {0, 0, 0, 0, 0};
int HourFrom12[5] = {0, 0, 0, 0, 0};            // phase 12
int MinuteFrom12[5] = {0, 0, 0, 0, 0};          // phase 12
int date12[5] = {10, 10, 10, 10, 10};           // phase 12
int month12[5] = {12, 12, 12, 12, 12};          // phase 12
int year12[5] = {2018, 2018, 2018, 2018, 2018}; // phase 12
int light12[5] = {0, 0, 0, 0, 0};               // phase 12
int dark12[5] = {0, 0, 0, 0, 0};                // phase 12


// Digital In-Out
int DIn[5] = {2, 4, 6, 8, 10};  // PIR evens number digital use pinMode
int DOut[5] = {3, 5, 7, 9, 11}; // LED odds number digital use pinMode

// Analog In
int AIn[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; // line breaker
int Acate[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int ASensi[10] = {990, 990, 990, 990, 990, 990, 990, 990, 990, 990};

// Light flags
int LightFlag[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int TimeSet = 0;
int LightSet[47] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // add/subtract(4) for phase checkpoints
int InitialFlag = 0;

// Interval (note the use of long)
unsigned long previousMillis = 0UL;
unsigned long interval1 = 1000UL;
unsigned long interval90 = 90UL;
unsigned long invalue = 0UL;
unsigned long maxValue = 16000000UL;
int previoussecs;

// Define a function to convert string to integer
int getInt(String text)
{
  char temp[6];
  text.toCharArray(temp, 5);
  int x = atoi(temp);
  return x;
}

void millis_delay(unsigned long interval)
{
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis > interval)
  {
    /* The Arduino executes this code once every second
     *  (interval = 1000 (ms) = 1 second).
     */
    // Don't forget to update the previousMillis value
    previousMillis = currentMillis;
  }
}

void count_delay2()
{
  if (invalue++ >= maxValue)
  {
    /* The Arduino executes this code approx. once every second
     *  (assuming clock speed = 16MHz)
     */

    // Don't forget to reset the counter
    invalue = 0UL;
  }
}

void rtc_delay()
{
  DateTime now = rtc.now();
  unsigned long currents = now.second();

  if (currents - previoussecs > 0)
  {

    previousMillis = currents;
  }
}

//////////////////////////////////////////////////////////////////////////////////////// Set up run
void setup()
{
  Serial.begin(9600);
  Wire.begin();
  // start the connexion to the RTC

  // rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
  for (int i = 0; i < 5; i++)
  {
    pinMode(DIn[i], INPUT);   // PIR
    pinMode(DOut[i], OUTPUT); // LED
  }

  if (!rtc.begin())
  {
    Serial.println("Couldn't find RTC");
    Serial.flush();
    while (1)
    {
      millis_delay(interval1); // recommended delay before start-up (1-sec)
    }
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
void loop()
{

  DateTime now = rtc.now(); // reads the time every second
  // Serial.println("Now");
  // String str = String(now.year(), DEC) + '/' + String(now.month(), DEC) + '/' + String(now.day(), DEC) + " " + String(now.hour(), DEC) + ':' + String(now.minute(), DEC) + ':' + String(now.second(), DEC);
  // Serial.println(str);

  // SETTING VALUES
  if (Serial.available() == 19 && TimeSet == 0)
  {
    dateIn = Serial.readString();
    // Wire.write(0x0E); // select register
    // Wire.write(0b00011100); // write register bitmap, bit 7 is /EOSC
    // rtc.adjust(DateTime(2017, 7, 16, 16, 35, 20));
    // clock.stopClock();
    int year = getInt(dateIn.substring(0, 4));
    int month = getInt(dateIn.substring(5, 7));
    int day = getInt(dateIn.substring(8, 10));
    int hour = getInt(dateIn.substring(11, 13));
    int minutes = getInt(dateIn.substring(14, 16));
    int seconds = getInt(dateIn.substring(17, 19));
    rtc.adjust(DateTime(year, month, day, hour, minutes, seconds));

    Serial.println(dateIn);

    TimeSet = 1;
  }

// Read initLEDs
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1)
  {
    initLEDs = Serial.readString();
    
    initLED[0] = getInt(initLEDs.substring(0, 1));
    initLED[1] = getInt(initLEDs.substring(1, 2));
    initLED[2] = getInt(initLEDs.substring(3, 4));
    initLED[3] = getInt(initLEDs.substring(5, 6));
    initLED[4] = getInt(initLEDs.substring(7, 8));
  }

  ////////////////////// Light Schedule (Get the input from Python interface)

  // Phase1
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 0)
  {
    lightIn1 = Serial.readString(); // Serial.readString() its command for getting number from Python interface
    
    //    Serial.print("-");Serial.print("Phase 1");
    // Box1
    HourOn1[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn1[0] = getInt(lightIn1.substring(2, 4));
    HourOff1[0] = getInt(lightIn1.substring(4, 6));
    MinuteOff1[0] = getInt(lightIn1.substring(6, 8));

    // Box2
    HourOn1[1] = getInt(lightIn1.substring(8, 10));
    MinuteOn1[1] = getInt(lightIn1.substring(10, 12));
    HourOff1[1] = getInt(lightIn1.substring(12, 14));
    MinuteOff1[1] = getInt(lightIn1.substring(14, 16));

    // Box3
    HourOn1[2] = getInt(lightIn1.substring(16, 18));
    MinuteOn1[2] = getInt(lightIn1.substring(18, 20));
    HourOff1[2] = getInt(lightIn1.substring(20, 22));
    MinuteOff1[2] = getInt(lightIn1.substring(22, 24));

    // Box4
    HourOn1[3] = getInt(lightIn1.substring(24, 26));
    MinuteOn1[3] = getInt(lightIn1.substring(26, 28));
    HourOff1[3] = getInt(lightIn1.substring(28, 30));
    MinuteOff1[3] = getInt(lightIn1.substring(30, 32));

    // Box5
    HourOn1[4] = getInt(lightIn1.substring(32, 34));
    MinuteOn1[4] = getInt(lightIn1.substring(34, 36));
    HourOff1[4] = getInt(lightIn1.substring(36, 38));
    MinuteOff1[4] = getInt(lightIn1.substring(38, 40));

    Serial.println(lightIn1);
    LightSet[1] = 1;
    //    Serial.print("-");Serial.print("1");
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 0)
  {
    lightIn1 = Serial.readString();

    dark1[0] = getInt(lightIn1.substring(0, 1));
    light1[0] = getInt(lightIn1.substring(1, 2));
    dark1[1] = getInt(lightIn1.substring(2, 3));
    light1[1] = getInt(lightIn1.substring(3, 4));
    dark1[2] = getInt(lightIn1.substring(4, 5));
    light1[2] = getInt(lightIn1.substring(5, 6));
    dark1[3] = getInt(lightIn1.substring(6, 7));
    light1[3] = getInt(lightIn1.substring(7, 8));
    dark1[4] = getInt(lightIn1.substring(8, 9));
    light1[4] = getInt(lightIn1.substring(9, 10));

    Serial.println(lightIn1);
    LightSet[2] = 1;
    //    Serial.print("-");Serial.print("2");
  }

  // Phase2
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[2] == 1 && LightSet[3] == 0)
  {
    lightIn2 = Serial.readString();
    // Box1
    HourOn2[0] = getInt(lightIn2.substring(0, 2));
    MinuteOn2[0] = getInt(lightIn2.substring(2, 4));
    HourOff2[0] = getInt(lightIn2.substring(4, 6));
    MinuteOff2[0] = getInt(lightIn2.substring(6, 8));

    // Box2
    HourOn2[1] = getInt(lightIn2.substring(8, 10));
    MinuteOn2[1] = getInt(lightIn2.substring(10, 12));
    HourOff2[1] = getInt(lightIn2.substring(12, 14));
    MinuteOff2[1] = getInt(lightIn2.substring(14, 16));

    // Box3
    HourOn2[2] = getInt(lightIn2.substring(16, 18));
    MinuteOn2[2] = getInt(lightIn2.substring(18, 20));
    HourOff2[2] = getInt(lightIn2.substring(20, 22));
    MinuteOff2[2] = getInt(lightIn2.substring(22, 24));

    // Box4
    HourOn2[3] = getInt(lightIn2.substring(24, 26));
    MinuteOn2[3] = getInt(lightIn2.substring(26, 28));
    HourOff2[3] = getInt(lightIn2.substring(28, 30));
    MinuteOff2[3] = getInt(lightIn2.substring(30, 32));

    // Box5
    HourOn2[4] = getInt(lightIn2.substring(32, 34));
    MinuteOn2[4] = getInt(lightIn2.substring(34, 36));
    HourOff2[4] = getInt(lightIn2.substring(36, 38));
    MinuteOff2[4] = getInt(lightIn2.substring(38, 40));

    Serial.println(lightIn2);
    LightSet[3] = 1;
    //    Serial.print("-");Serial.print("3");
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[3] == 1 && LightSet[4] == 0)
  {
    lightIn2 = Serial.readString();

    dark2[0] = getInt(lightIn2.substring(0, 1));
    light2[0] = getInt(lightIn2.substring(1, 2));
    dark2[1] = getInt(lightIn2.substring(2, 3));
    light2[1] = getInt(lightIn2.substring(3, 4));
    dark2[2] = getInt(lightIn2.substring(4, 5));
    light2[2] = getInt(lightIn2.substring(5, 6));
    dark2[3] = getInt(lightIn2.substring(6, 7));
    light2[3] = getInt(lightIn2.substring(7, 8));
    dark2[4] = getInt(lightIn2.substring(8, 9));
    light2[4] = getInt(lightIn2.substring(9, 10));

    Serial.println(lightIn2);
    LightSet[4] = 1;
    //    Serial.print("-");Serial.print("4");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[4] == 1 && LightSet[5] == 0 && LightSet[6] == 0)
  {
    lightIn2 = Serial.readString();

    date2[0] = getInt(lightIn2.substring(0, 2));
    month2[0] = getInt(lightIn2.substring(2, 4));
    year2[0] = getInt(lightIn2.substring(4, 8));
    date2[1] = getInt(lightIn2.substring(8, 10));
    month2[1] = getInt(lightIn2.substring(10, 12));
    year2[1] = getInt(lightIn2.substring(12, 16));
    date2[2] = getInt(lightIn2.substring(16, 18));
    month2[2] = getInt(lightIn2.substring(18, 20));
    year2[2] = getInt(lightIn2.substring(20, 24));
    date2[3] = getInt(lightIn2.substring(24, 26));
    month2[3] = getInt(lightIn2.substring(26, 28));
    year2[3] = getInt(lightIn2.substring(28, 32));
    date2[4] = getInt(lightIn2.substring(32, 34));
    month2[4] = getInt(lightIn2.substring(34, 36));
    year2[4] = getInt(lightIn2.substring(36, 40));
    HourFrom2[0] = getInt(lightIn2.substring(40, 42));
    MinuteFrom2[0] = getInt(lightIn2.substring(42, 44));
    HourFrom2[1] = getInt(lightIn2.substring(44, 46));
    MinuteFrom2[1] = getInt(lightIn2.substring(46, 48));
    HourFrom2[2] = getInt(lightIn2.substring(48, 50));
    MinuteFrom2[2] = getInt(lightIn2.substring(50, 52));
    HourFrom2[3] = getInt(lightIn2.substring(52, 54));
    MinuteFrom2[3] = getInt(lightIn2.substring(54, 56));
    HourFrom2[4] = getInt(lightIn2.substring(56, 58));
    MinuteFrom2[4] = getInt(lightIn2.substring(58, 60));

    Serial.println(lightIn2);
    LightSet[5] = 1;
    LightSet[6] = 1;
    //    Serial.print("-");Serial.print("5");
    //    Serial.print("-");Serial.print("6");
  }

  // Phase3
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[5] == 1 && LightSet[6] == 1 && LightSet[7] == 0)
  {
    lightIn3 = Serial.readString();
    // Box1
    HourOn3[0] = getInt(lightIn3.substring(0, 2));
    MinuteOn3[0] = getInt(lightIn3.substring(2, 4));
    HourOff3[0] = getInt(lightIn3.substring(4, 6));
    MinuteOff3[0] = getInt(lightIn3.substring(6, 8));

    // Box2
    HourOn3[1] = getInt(lightIn3.substring(8, 10));
    MinuteOn3[1] = getInt(lightIn3.substring(10, 12));
    HourOff3[1] = getInt(lightIn3.substring(12, 14));
    MinuteOff3[1] = getInt(lightIn3.substring(14, 16));

    // Box3
    HourOn3[2] = getInt(lightIn3.substring(16, 18));
    MinuteOn3[2] = getInt(lightIn3.substring(18, 20));
    HourOff3[2] = getInt(lightIn3.substring(20, 22));
    MinuteOff3[2] = getInt(lightIn3.substring(22, 24));

    // Box4
    HourOn3[3] = getInt(lightIn3.substring(24, 26));
    MinuteOn3[3] = getInt(lightIn3.substring(26, 28));
    HourOff3[3] = getInt(lightIn3.substring(28, 30));
    MinuteOff3[3] = getInt(lightIn3.substring(30, 32));

    // Box5
    HourOn3[4] = getInt(lightIn3.substring(32, 34));
    MinuteOn3[4] = getInt(lightIn3.substring(34, 36));
    HourOff3[4] = getInt(lightIn3.substring(36, 38));
    MinuteOff3[4] = getInt(lightIn3.substring(38, 40));

    Serial.println(lightIn3);
    //    Serial.print("-"); Serial.print("Phase 3");
    LightSet[7] = 1;
    //    Serial.print("-");Serial.print("7");
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[7] == 1 && LightSet[8] == 0)
  {
    lightIn3 = Serial.readString();

    dark3[0] = getInt(lightIn3.substring(0, 1));
    light3[0] = getInt(lightIn3.substring(1, 2));
    dark3[1] = getInt(lightIn3.substring(2, 3));
    light3[1] = getInt(lightIn3.substring(3, 4));
    dark3[2] = getInt(lightIn3.substring(4, 5));
    light3[2] = getInt(lightIn3.substring(5, 6));
    dark3[3] = getInt(lightIn3.substring(6, 7));
    light3[3] = getInt(lightIn3.substring(7, 8));
    dark3[4] = getInt(lightIn3.substring(8, 9));
    light3[4] = getInt(lightIn3.substring(9, 10));

    Serial.println(lightIn3);
    LightSet[8] = 1;
    //    Serial.print("-");Serial.print("8");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[8] == 1 && LightSet[9] == 0 && LightSet[10] == 0)
  {
    lightIn3 = Serial.readString();

    date3[0] = getInt(lightIn3.substring(0, 2));
    month3[0] = getInt(lightIn3.substring(2, 4));
    year3[0] = getInt(lightIn3.substring(4, 8));
    date3[1] = getInt(lightIn3.substring(8, 10));
    month3[1] = getInt(lightIn3.substring(10, 12));
    year3[1] = getInt(lightIn3.substring(12, 16));
    date3[2] = getInt(lightIn3.substring(16, 18));
    month3[2] = getInt(lightIn3.substring(18, 20));
    year3[2] = getInt(lightIn3.substring(20, 24));
    date3[3] = getInt(lightIn3.substring(24, 26));
    month3[3] = getInt(lightIn3.substring(26, 28));
    year3[3] = getInt(lightIn3.substring(28, 32));
    date3[4] = getInt(lightIn3.substring(32, 34));
    month3[4] = getInt(lightIn3.substring(34, 36));
    year3[4] = getInt(lightIn3.substring(36, 40));
    HourFrom3[0] = getInt(lightIn3.substring(40, 42));
    MinuteFrom3[0] = getInt(lightIn3.substring(42, 44));
    HourFrom3[1] = getInt(lightIn3.substring(44, 46));
    MinuteFrom3[1] = getInt(lightIn3.substring(46, 48));
    HourFrom3[2] = getInt(lightIn3.substring(48, 50));
    MinuteFrom3[2] = getInt(lightIn3.substring(50, 52));
    HourFrom3[3] = getInt(lightIn3.substring(52, 54));
    MinuteFrom3[3] = getInt(lightIn3.substring(54, 56));
    HourFrom3[4] = getInt(lightIn3.substring(56, 58));
    MinuteFrom3[4] = getInt(lightIn3.substring(58, 60));

    Serial.println(lightIn3);
    LightSet[9] = 1;
    LightSet[10] = 1;
    //    Serial.print("-");Serial.print("9");
    //    Serial.print("-");Serial.print("10");
  }

  // Phase4
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[9] == 1 && LightSet[10] == 1 && LightSet[11] == 0)
  {
    lightIn4 = Serial.readString();
    // Box1
    HourOn4[0] = getInt(lightIn4.substring(0, 2));
    MinuteOn4[0] = getInt(lightIn4.substring(2, 4));
    HourOff4[0] = getInt(lightIn4.substring(4, 6));
    MinuteOff4[0] = getInt(lightIn4.substring(6, 8));

    // Box2
    HourOn4[1] = getInt(lightIn4.substring(8, 10));
    MinuteOn4[1] = getInt(lightIn4.substring(10, 12));
    HourOff4[1] = getInt(lightIn4.substring(12, 14));
    MinuteOff4[1] = getInt(lightIn4.substring(14, 16));

    // Box3
    HourOn4[2] = getInt(lightIn4.substring(16, 18));
    MinuteOn4[2] = getInt(lightIn4.substring(18, 20));
    HourOff4[2] = getInt(lightIn4.substring(20, 22));
    MinuteOff4[2] = getInt(lightIn4.substring(22, 24));

    // Box4
    HourOn4[3] = getInt(lightIn4.substring(24, 26));
    MinuteOn4[3] = getInt(lightIn4.substring(26, 28));
    HourOff4[3] = getInt(lightIn4.substring(28, 30));
    MinuteOff4[3] = getInt(lightIn4.substring(30, 32));

    // Box5
    HourOn4[4] = getInt(lightIn4.substring(32, 34));
    MinuteOn4[4] = getInt(lightIn4.substring(34, 36));
    HourOff4[4] = getInt(lightIn4.substring(36, 38));
    MinuteOff4[4] = getInt(lightIn4.substring(38, 40));

    Serial.println(lightIn4);
    //    Serial.print("-"); Serial.print("Phase 4");
    LightSet[11] = 1;
    //    Serial.print("-");Serial.print("11");
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[11] == 1 && LightSet[12] == 0)
  {
    lightIn4 = Serial.readString();

    dark4[0] = getInt(lightIn4.substring(0, 1));
    light4[0] = getInt(lightIn4.substring(1, 2));
    dark4[1] = getInt(lightIn4.substring(2, 3));
    light4[1] = getInt(lightIn4.substring(3, 4));
    dark4[2] = getInt(lightIn4.substring(4, 5));
    light4[2] = getInt(lightIn4.substring(5, 6));
    dark4[3] = getInt(lightIn4.substring(6, 7));
    light4[3] = getInt(lightIn4.substring(7, 8));
    dark4[4] = getInt(lightIn4.substring(8, 9));
    light4[4] = getInt(lightIn4.substring(9, 10));

    Serial.println(lightIn4);
    LightSet[12] = 1;
    //    Serial.print("-");Serial.print("12");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[12] == 1 && LightSet[13] == 0 && LightSet[14] == 0)
  {
    lightIn4 = Serial.readString();

    date4[0] = getInt(lightIn4.substring(0, 2));
    month4[0] = getInt(lightIn4.substring(2, 4));
    year4[0] = getInt(lightIn4.substring(4, 8));
    date4[1] = getInt(lightIn4.substring(8, 10));
    month4[1] = getInt(lightIn4.substring(10, 12));
    year4[1] = getInt(lightIn4.substring(12, 16));
    date4[2] = getInt(lightIn4.substring(16, 18));
    month4[2] = getInt(lightIn4.substring(18, 20));
    year4[2] = getInt(lightIn4.substring(20, 24));
    date4[3] = getInt(lightIn4.substring(24, 26));
    month4[3] = getInt(lightIn4.substring(26, 28));
    year4[3] = getInt(lightIn4.substring(28, 32));
    date4[4] = getInt(lightIn4.substring(32, 34));
    month4[4] = getInt(lightIn4.substring(34, 36));
    year4[4] = getInt(lightIn4.substring(36, 40));
    HourFrom4[0] = getInt(lightIn4.substring(40, 42));
    MinuteFrom4[0] = getInt(lightIn4.substring(42, 44));
    HourFrom4[1] = getInt(lightIn4.substring(44, 46));
    MinuteFrom4[1] = getInt(lightIn4.substring(46, 48));
    HourFrom4[2] = getInt(lightIn4.substring(48, 50));
    MinuteFrom4[2] = getInt(lightIn4.substring(50, 52));
    HourFrom4[3] = getInt(lightIn4.substring(52, 54));
    MinuteFrom4[3] = getInt(lightIn4.substring(54, 56));
    HourFrom4[4] = getInt(lightIn4.substring(56, 58));
    MinuteFrom4[4] = getInt(lightIn4.substring(58, 60));

    Serial.println(lightIn4);
    LightSet[13] = 1;
    LightSet[14] = 1;
    //    Serial.print("-");Serial.print("13");
    //    Serial.print("-");Serial.print("14");
  }

  // Phase5
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[13] == 1 && LightSet[14] == 1 && LightSet[15] == 0)
  {
    lightIn5 = Serial.readString();
    // Box1
    HourOn5[0] = getInt(lightIn5.substring(0, 2));
    MinuteOn5[0] = getInt(lightIn5.substring(2, 4));
    HourOff5[0] = getInt(lightIn5.substring(4, 6));
    MinuteOff5[0] = getInt(lightIn5.substring(6, 8));

    // Box2
    HourOn5[1] = getInt(lightIn5.substring(8, 10));
    MinuteOn5[1] = getInt(lightIn5.substring(10, 12));
    HourOff5[1] = getInt(lightIn5.substring(12, 14));
    MinuteOff5[1] = getInt(lightIn5.substring(14, 16));

    // Box3
    HourOn5[2] = getInt(lightIn5.substring(16, 18));
    MinuteOn5[2] = getInt(lightIn5.substring(18, 20));
    HourOff5[2] = getInt(lightIn5.substring(20, 22));
    MinuteOff5[2] = getInt(lightIn5.substring(22, 24));

    // Box4
    HourOn5[3] = getInt(lightIn5.substring(24, 26));
    MinuteOn5[3] = getInt(lightIn5.substring(26, 28));
    HourOff5[3] = getInt(lightIn5.substring(28, 30));
    MinuteOff5[3] = getInt(lightIn5.substring(30, 32));

    // Box5
    HourOn5[4] = getInt(lightIn5.substring(32, 34));
    MinuteOn5[4] = getInt(lightIn5.substring(34, 36));
    HourOff5[4] = getInt(lightIn5.substring(36, 38));
    MinuteOff5[4] = getInt(lightIn5.substring(38, 40));

    Serial.println(lightIn5);
    //    Serial.print("-"); Serial.print("Phase 5");
    LightSet[15] = 1;

    //    Serial.print("-");Serial.print("15");
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[15] == 1 && LightSet[16] == 0)
  {

    lightIn5 = Serial.readString();

    dark5[0] = getInt(lightIn5.substring(0, 1));
    light5[0] = getInt(lightIn5.substring(1, 2));
    dark5[1] = getInt(lightIn5.substring(2, 3));
    light5[1] = getInt(lightIn5.substring(3, 4));
    dark5[2] = getInt(lightIn5.substring(4, 5));
    light5[2] = getInt(lightIn5.substring(5, 6));
    dark5[3] = getInt(lightIn5.substring(6, 7));
    light5[3] = getInt(lightIn5.substring(7, 8));
    dark5[4] = getInt(lightIn5.substring(8, 9));
    light5[4] = getInt(lightIn5.substring(9, 10));
    Serial.println(lightIn5);
    LightSet[16] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && LightSet[16] == 1 && LightSet[17] == 0 && LightSet[18] == 0)
  {
    lightIn5 = Serial.readString();

    date5[0] = getInt(lightIn5.substring(0, 2));
    month5[0] = getInt(lightIn5.substring(2, 4));
    year5[0] = getInt(lightIn5.substring(4, 8));
    date5[1] = getInt(lightIn5.substring(8, 10));
    month5[1] = getInt(lightIn5.substring(10, 12));
    year5[1] = getInt(lightIn5.substring(12, 16));
    date5[2] = getInt(lightIn5.substring(16, 18));
    month5[2] = getInt(lightIn5.substring(18, 20));
    year5[2] = getInt(lightIn5.substring(20, 24));
    date5[3] = getInt(lightIn5.substring(24, 26));
    month5[3] = getInt(lightIn5.substring(26, 28));
    year5[3] = getInt(lightIn5.substring(28, 32));
    date5[4] = getInt(lightIn5.substring(32, 34));
    month5[4] = getInt(lightIn5.substring(34, 36));
    year5[4] = getInt(lightIn5.substring(36, 40));
    HourFrom5[0] = getInt(lightIn5.substring(40, 42));
    MinuteFrom5[0] = getInt(lightIn5.substring(42, 44));
    HourFrom5[1] = getInt(lightIn5.substring(44, 46));
    MinuteFrom5[1] = getInt(lightIn5.substring(46, 48));
    HourFrom5[2] = getInt(lightIn5.substring(48, 50));
    MinuteFrom5[2] = getInt(lightIn5.substring(50, 52));
    HourFrom5[3] = getInt(lightIn5.substring(52, 54));
    MinuteFrom5[3] = getInt(lightIn5.substring(54, 56));
    HourFrom5[4] = getInt(lightIn5.substring(56, 58));
    MinuteFrom5[4] = getInt(lightIn5.substring(58, 60));

    Serial.println(lightIn5);
    LightSet[17] = 1;
    LightSet[18] = 1;

    //    Serial.println(InitialFlag);
    //    Serial.println(TimeSet);
    //    Serial.println(LightSet[14]);
    //    Serial.println(LightSet[15]);
    //    Serial.println(LightSet[16]);
    //    Serial.println(LightSet[17]);
    //    Serial.println(LightSet[18]);
    // This test showed unnormal result if we define LightSet[18], would be affecting LightSet to be 1, need to add more element LightSet[19] for made it normal
  }

  // Phase6
  if (Serial.available() == 40 && InitialFlag == 0 && LightSet[17] == 1 && LightSet[18] == 1 && LightSet[19] == 0)
  {
    lightIn6 = Serial.readString();
    // Box1
    HourOn6[0] = getInt(lightIn6.substring(0, 2));
    MinuteOn6[0] = getInt(lightIn6.substring(2, 4));
    HourOff6[0] = getInt(lightIn6.substring(4, 6));
    MinuteOff6[0] = getInt(lightIn6.substring(6, 8));

    // Box2
    HourOn6[1] = getInt(lightIn6.substring(8, 10));
    MinuteOn6[1] = getInt(lightIn6.substring(10, 12));
    HourOff6[1] = getInt(lightIn6.substring(12, 14));
    MinuteOff6[1] = getInt(lightIn6.substring(14, 16));

    // Box3
    HourOn6[2] = getInt(lightIn6.substring(16, 18));
    MinuteOn6[2] = getInt(lightIn6.substring(18, 20));
    HourOff6[2] = getInt(lightIn6.substring(20, 22));
    MinuteOff6[2] = getInt(lightIn6.substring(22, 24));

    // Box4
    HourOn6[3] = getInt(lightIn6.substring(24, 26));
    MinuteOn6[3] = getInt(lightIn6.substring(26, 28));
    HourOff6[3] = getInt(lightIn6.substring(28, 30));
    MinuteOff6[3] = getInt(lightIn6.substring(30, 32));

    // Box5
    HourOn6[4] = getInt(lightIn6.substring(32, 34));
    MinuteOn6[4] = getInt(lightIn6.substring(34, 36));
    HourOff6[4] = getInt(lightIn6.substring(36, 38));
    MinuteOff6[4] = getInt(lightIn6.substring(38, 40));

    Serial.println(lightIn6);
    //    Serial.print("-"); Serial.print("Phase 6");
    LightSet[19] = 1;

    //    Serial.print("-");Serial.print("15");
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[19] == 1 && LightSet[20] == 0)
  {

    lightIn6 = Serial.readString();

    dark6[0] = getInt(lightIn6.substring(0, 1));
    light6[0] = getInt(lightIn6.substring(1, 2));
    dark6[1] = getInt(lightIn6.substring(2, 3));
    light6[1] = getInt(lightIn6.substring(3, 4));
    dark6[2] = getInt(lightIn6.substring(4, 5));
    light6[2] = getInt(lightIn6.substring(5, 6));
    dark6[3] = getInt(lightIn6.substring(6, 7));
    light6[3] = getInt(lightIn6.substring(7, 8));
    dark6[4] = getInt(lightIn6.substring(8, 9));
    light6[4] = getInt(lightIn6.substring(9, 10));
    Serial.println(lightIn6);
    LightSet[20] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[20] == 1 && LightSet[21] == 0 && LightSet[22] == 0)
  {
    lightIn6 = Serial.readString();

    date6[0] = getInt(lightIn6.substring(0, 2));
    month6[0] = getInt(lightIn6.substring(2, 4));
    year6[0] = getInt(lightIn6.substring(4, 8));
    date6[1] = getInt(lightIn6.substring(8, 10));
    month6[1] = getInt(lightIn6.substring(10, 12));
    year6[1] = getInt(lightIn6.substring(12, 16));
    date6[2] = getInt(lightIn6.substring(16, 18));
    month6[2] = getInt(lightIn6.substring(18, 20));
    year6[2] = getInt(lightIn6.substring(20, 24));
    date6[3] = getInt(lightIn6.substring(24, 26));
    month6[3] = getInt(lightIn6.substring(26, 28));
    year6[3] = getInt(lightIn6.substring(28, 32));
    date6[4] = getInt(lightIn6.substring(32, 34));
    month6[4] = getInt(lightIn6.substring(34, 36));
    year6[4] = getInt(lightIn6.substring(36, 40));
    HourFrom6[0] = getInt(lightIn6.substring(40, 42));
    MinuteFrom6[0] = getInt(lightIn6.substring(42, 44));
    HourFrom6[1] = getInt(lightIn6.substring(44, 46));
    MinuteFrom6[1] = getInt(lightIn6.substring(46, 48));
    HourFrom6[2] = getInt(lightIn6.substring(48, 50));
    MinuteFrom6[2] = getInt(lightIn6.substring(50, 52));
    HourFrom6[3] = getInt(lightIn6.substring(52, 54));
    MinuteFrom6[3] = getInt(lightIn6.substring(54, 56));
    HourFrom6[4] = getInt(lightIn6.substring(56, 58));
    MinuteFrom6[4] = getInt(lightIn6.substring(58, 60));

    Serial.println(lightIn6);
    LightSet[21] = 1;
    LightSet[22] = 1;
  }

  // Phase7
  if (Serial.available() == 40 && InitialFlag == 0 && LightSet[21] == 1 && LightSet[22] == 1 && LightSet[23] == 0)
  {
    lightIn7 = Serial.readString();
    // Box1
    HourOn7[0] = getInt(lightIn7.substring(0, 2));
    MinuteOn7[0] = getInt(lightIn7.substring(2, 4));
    HourOff7[0] = getInt(lightIn7.substring(4, 6));
    MinuteOff7[0] = getInt(lightIn7.substring(6, 8));

    // Box2
    HourOn7[1] = getInt(lightIn7.substring(8, 10));
    MinuteOn7[1] = getInt(lightIn7.substring(10, 12));
    HourOff7[1] = getInt(lightIn7.substring(12, 14));
    MinuteOff7[1] = getInt(lightIn7.substring(14, 16));

    // Box3
    HourOn7[2] = getInt(lightIn7.substring(16, 18));
    MinuteOn7[2] = getInt(lightIn7.substring(18, 20));
    HourOff7[2] = getInt(lightIn7.substring(20, 22));
    MinuteOff7[2] = getInt(lightIn7.substring(22, 24));

    // Box4
    HourOn7[3] = getInt(lightIn7.substring(24, 26));
    MinuteOn7[3] = getInt(lightIn7.substring(26, 28));
    HourOff7[3] = getInt(lightIn7.substring(28, 30));
    MinuteOff7[3] = getInt(lightIn7.substring(30, 32));

    // Box5
    HourOn7[4] = getInt(lightIn7.substring(32, 34));
    MinuteOn7[4] = getInt(lightIn7.substring(34, 36));
    HourOff7[4] = getInt(lightIn7.substring(36, 38));
    MinuteOff7[4] = getInt(lightIn7.substring(38, 40));

    Serial.println(lightIn7);
    LightSet[23] = 1;
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[23] == 1 && LightSet[24] == 0)
  {

    lightIn7 = Serial.readString();

    dark7[0] = getInt(lightIn7.substring(0, 1));
    light7[0] = getInt(lightIn7.substring(1, 2));
    dark7[1] = getInt(lightIn7.substring(2, 3));
    light7[1] = getInt(lightIn7.substring(3, 4));
    dark7[2] = getInt(lightIn7.substring(4, 5));
    light7[2] = getInt(lightIn7.substring(5, 6));
    dark7[3] = getInt(lightIn7.substring(6, 7));
    light7[3] = getInt(lightIn7.substring(7, 8));
    dark7[4] = getInt(lightIn7.substring(8, 9));
    light7[4] = getInt(lightIn7.substring(9, 10));
    Serial.println(lightIn7);
    LightSet[24] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[24] == 1 && LightSet[25] == 0 && LightSet[26] == 0)
  {
    lightIn7 = Serial.readString();

    date7[0] = getInt(lightIn7.substring(0, 2));
    month7[0] = getInt(lightIn7.substring(2, 4));
    year7[0] = getInt(lightIn7.substring(4, 8));
    date7[1] = getInt(lightIn7.substring(8, 10));
    month7[1] = getInt(lightIn7.substring(10, 12));
    year7[1] = getInt(lightIn7.substring(12, 16));
    date7[2] = getInt(lightIn7.substring(16, 18));
    month7[2] = getInt(lightIn7.substring(18, 20));
    year7[2] = getInt(lightIn7.substring(20, 24));
    date7[3] = getInt(lightIn7.substring(24, 26));
    month7[3] = getInt(lightIn7.substring(26, 28));
    year7[3] = getInt(lightIn7.substring(28, 32));
    date7[4] = getInt(lightIn7.substring(32, 34));
    month7[4] = getInt(lightIn7.substring(34, 36));
    year7[4] = getInt(lightIn7.substring(36, 40));
    HourFrom7[0] = getInt(lightIn7.substring(40, 42));
    MinuteFrom7[0] = getInt(lightIn7.substring(42, 44));
    HourFrom7[1] = getInt(lightIn7.substring(44, 46));
    MinuteFrom7[1] = getInt(lightIn7.substring(46, 48));
    HourFrom7[2] = getInt(lightIn7.substring(48, 50));
    MinuteFrom7[2] = getInt(lightIn7.substring(50, 52));
    HourFrom7[3] = getInt(lightIn7.substring(52, 54));
    MinuteFrom7[3] = getInt(lightIn7.substring(54, 56));
    HourFrom7[4] = getInt(lightIn7.substring(56, 58));
    MinuteFrom7[4] = getInt(lightIn7.substring(58, 60));

    Serial.println(lightIn7);
    LightSet[25] = 1;
    LightSet[26] = 1;
  }

  // Phase8
  if (Serial.available() == 40 && InitialFlag == 0 && LightSet[25] == 1 && LightSet[26] == 1 && LightSet[27] == 0)
  {
    lightIn8 = Serial.readString();
    // Box1
    HourOn8[0] = getInt(lightIn8.substring(0, 2));
    MinuteOn8[0] = getInt(lightIn8.substring(2, 4));
    HourOff8[0] = getInt(lightIn8.substring(4, 6));
    MinuteOff8[0] = getInt(lightIn8.substring(6, 8));

    // Box2
    HourOn8[1] = getInt(lightIn8.substring(8, 10));
    MinuteOn8[1] = getInt(lightIn8.substring(10, 12));
    HourOff8[1] = getInt(lightIn8.substring(12, 14));
    MinuteOff8[1] = getInt(lightIn8.substring(14, 16));

    // Box3
    HourOn8[2] = getInt(lightIn8.substring(16, 18));
    MinuteOn8[2] = getInt(lightIn8.substring(18, 20));
    HourOff8[2] = getInt(lightIn8.substring(20, 22));
    MinuteOff8[2] = getInt(lightIn8.substring(22, 24));

    // Box4
    HourOn8[3] = getInt(lightIn8.substring(24, 26));
    MinuteOn8[3] = getInt(lightIn8.substring(26, 28));
    HourOff8[3] = getInt(lightIn8.substring(28, 30));
    MinuteOff8[3] = getInt(lightIn8.substring(30, 32));

    // Box5
    HourOn8[4] = getInt(lightIn8.substring(32, 34));
    MinuteOn8[4] = getInt(lightIn8.substring(34, 36));
    HourOff8[4] = getInt(lightIn8.substring(36, 38));
    MinuteOff8[4] = getInt(lightIn8.substring(38, 40));

    Serial.println(lightIn8);
    LightSet[27] = 1;
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[27] == 1 && LightSet[28] == 0)
  {

    lightIn8 = Serial.readString();

    dark8[0] = getInt(lightIn8.substring(0, 1));
    light8[0] = getInt(lightIn8.substring(1, 2));
    dark8[1] = getInt(lightIn8.substring(2, 3));
    light8[1] = getInt(lightIn8.substring(3, 4));
    dark8[2] = getInt(lightIn8.substring(4, 5));
    light8[2] = getInt(lightIn8.substring(5, 6));
    dark8[3] = getInt(lightIn8.substring(6, 8));
    light8[3] = getInt(lightIn8.substring(8, 8));
    dark8[4] = getInt(lightIn8.substring(8, 9));
    light8[4] = getInt(lightIn8.substring(9, 10));
    Serial.println(lightIn8);
    LightSet[28] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[28] == 1 && LightSet[29] == 0 && LightSet[30] == 0)
  {
    lightIn8 = Serial.readString();

    date8[0] = getInt(lightIn8.substring(0, 2));
    month8[0] = getInt(lightIn8.substring(2, 4));
    year8[0] = getInt(lightIn8.substring(4, 8));
    date8[1] = getInt(lightIn8.substring(8, 10));
    month8[1] = getInt(lightIn8.substring(10, 12));
    year8[1] = getInt(lightIn8.substring(12, 16));
    date8[2] = getInt(lightIn8.substring(16, 18));
    month8[2] = getInt(lightIn8.substring(18, 20));
    year8[2] = getInt(lightIn8.substring(20, 24));
    date8[3] = getInt(lightIn8.substring(24, 26));
    month8[3] = getInt(lightIn8.substring(26, 28));
    year8[3] = getInt(lightIn8.substring(28, 32));
    date8[4] = getInt(lightIn8.substring(32, 34));
    month8[4] = getInt(lightIn8.substring(34, 36));
    year8[4] = getInt(lightIn8.substring(36, 40));
    HourFrom8[0] = getInt(lightIn8.substring(40, 42));
    MinuteFrom8[0] = getInt(lightIn8.substring(42, 44));
    HourFrom8[1] = getInt(lightIn8.substring(44, 46));
    MinuteFrom8[1] = getInt(lightIn8.substring(46, 48));
    HourFrom8[2] = getInt(lightIn8.substring(48, 50));
    MinuteFrom8[2] = getInt(lightIn8.substring(50, 52));
    HourFrom8[3] = getInt(lightIn8.substring(52, 54));
    MinuteFrom8[3] = getInt(lightIn8.substring(54, 56));
    HourFrom8[4] = getInt(lightIn8.substring(56, 58));
    MinuteFrom8[4] = getInt(lightIn8.substring(58, 60));

    Serial.println(lightIn8);
    LightSet[29] = 1;
    LightSet[30] = 1;
  }

  // Phase9
  if (Serial.available() == 40 && InitialFlag == 0 && LightSet[29] == 1 && LightSet[30] == 1 && LightSet[31] == 0)
  {
    lightIn9 = Serial.readString();
    // Box1
    HourOn9[0] = getInt(lightIn9.substring(0, 2));
    MinuteOn9[0] = getInt(lightIn9.substring(2, 4));
    HourOff9[0] = getInt(lightIn9.substring(4, 6));
    MinuteOff9[0] = getInt(lightIn9.substring(6, 8));

    // Box2
    HourOn9[1] = getInt(lightIn9.substring(8, 10));
    MinuteOn9[1] = getInt(lightIn9.substring(10, 12));
    HourOff9[1] = getInt(lightIn9.substring(12, 14));
    MinuteOff9[1] = getInt(lightIn9.substring(14, 16));

    // Box3
    HourOn9[2] = getInt(lightIn9.substring(16, 18));
    MinuteOn9[2] = getInt(lightIn9.substring(18, 20));
    HourOff9[2] = getInt(lightIn9.substring(20, 22));
    MinuteOff9[2] = getInt(lightIn9.substring(22, 24));

    // Box4
    HourOn9[3] = getInt(lightIn9.substring(24, 26));
    MinuteOn9[3] = getInt(lightIn9.substring(26, 28));
    HourOff9[3] = getInt(lightIn9.substring(28, 30));
    MinuteOff9[3] = getInt(lightIn9.substring(30, 32));

    // Box5
    HourOn9[4] = getInt(lightIn9.substring(32, 34));
    MinuteOn9[4] = getInt(lightIn9.substring(34, 36));
    HourOff9[4] = getInt(lightIn9.substring(36, 38));
    MinuteOff9[4] = getInt(lightIn9.substring(38, 40));

    Serial.println(lightIn9);
    LightSet[31] = 1;
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[31] == 1 && LightSet[32] == 0)
  {

    lightIn9 = Serial.readString();

    dark9[0] = getInt(lightIn9.substring(0, 1));
    light9[0] = getInt(lightIn9.substring(1, 2));
    dark9[1] = getInt(lightIn9.substring(2, 3));
    light9[1] = getInt(lightIn9.substring(3, 4));
    dark9[2] = getInt(lightIn9.substring(4, 5));
    light9[2] = getInt(lightIn9.substring(5, 6));
    dark9[3] = getInt(lightIn9.substring(6, 8));
    light9[3] = getInt(lightIn9.substring(8, 8));
    dark9[4] = getInt(lightIn9.substring(8, 9));
    light9[4] = getInt(lightIn9.substring(9, 10));
    Serial.println(lightIn9);
    LightSet[32] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[32] == 1 && LightSet[33] == 0 && LightSet[34] == 0)
  {
    lightIn9 = Serial.readString();

    date9[0] = getInt(lightIn9.substring(0, 2));
    month9[0] = getInt(lightIn9.substring(2, 4));
    year9[0] = getInt(lightIn9.substring(4, 8));
    date9[1] = getInt(lightIn9.substring(8, 10));
    month9[1] = getInt(lightIn9.substring(10, 12));
    year9[1] = getInt(lightIn9.substring(12, 16));
    date9[2] = getInt(lightIn9.substring(16, 18));
    month9[2] = getInt(lightIn9.substring(18, 20));
    year9[2] = getInt(lightIn9.substring(20, 24));
    date9[3] = getInt(lightIn9.substring(24, 26));
    month9[3] = getInt(lightIn9.substring(26, 28));
    year9[3] = getInt(lightIn9.substring(28, 32));
    date9[4] = getInt(lightIn9.substring(32, 34));
    month9[4] = getInt(lightIn9.substring(34, 36));
    year9[4] = getInt(lightIn9.substring(36, 40));
    HourFrom9[0] = getInt(lightIn9.substring(40, 42));
    MinuteFrom9[0] = getInt(lightIn9.substring(42, 44));
    HourFrom9[1] = getInt(lightIn9.substring(44, 46));
    MinuteFrom9[1] = getInt(lightIn9.substring(46, 48));
    HourFrom9[2] = getInt(lightIn9.substring(48, 50));
    MinuteFrom9[2] = getInt(lightIn9.substring(50, 52));
    HourFrom9[3] = getInt(lightIn9.substring(52, 54));
    MinuteFrom9[3] = getInt(lightIn9.substring(54, 56));
    HourFrom9[4] = getInt(lightIn9.substring(56, 58));
    MinuteFrom9[4] = getInt(lightIn9.substring(58, 60));

    Serial.println(lightIn9);
    LightSet[33] = 1;
    LightSet[34] = 1;
  }

  // Phase10
  if (Serial.available() == 40 && InitialFlag == 0 && LightSet[33] == 1 && LightSet[34] == 1 && LightSet[35] == 0)
  {
    lightIn10 = Serial.readString();
    // Box1
    HourOn10[0] = getInt(lightIn10.substring(0, 2));
    MinuteOn10[0] = getInt(lightIn10.substring(2, 4));
    HourOff10[0] = getInt(lightIn10.substring(4, 6));
    MinuteOff10[0] = getInt(lightIn10.substring(6, 8));

    // Box2
    HourOn10[1] = getInt(lightIn10.substring(8, 10));
    MinuteOn10[1] = getInt(lightIn10.substring(10, 12));
    HourOff10[1] = getInt(lightIn10.substring(12, 14));
    MinuteOff10[1] = getInt(lightIn10.substring(14, 16));

    // Box3
    HourOn10[2] = getInt(lightIn10.substring(16, 18));
    MinuteOn10[2] = getInt(lightIn10.substring(18, 20));
    HourOff10[2] = getInt(lightIn10.substring(20, 22));
    MinuteOff10[2] = getInt(lightIn10.substring(22, 24));

    // Box4
    HourOn10[3] = getInt(lightIn10.substring(24, 26));
    MinuteOn10[3] = getInt(lightIn10.substring(26, 28));
    HourOff10[3] = getInt(lightIn10.substring(28, 30));
    MinuteOff10[3] = getInt(lightIn10.substring(30, 32));

    // Box5
    HourOn10[4] = getInt(lightIn10.substring(32, 34));
    MinuteOn10[4] = getInt(lightIn10.substring(34, 36));
    HourOff10[4] = getInt(lightIn10.substring(36, 38));
    MinuteOff10[4] = getInt(lightIn10.substring(38, 40));

    Serial.println(lightIn10);
    LightSet[35] = 1;
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[35] == 1 && LightSet[36] == 0)
  {

    lightIn10 = Serial.readString();

    dark10[0] = getInt(lightIn10.substring(0, 1));
    light10[0] = getInt(lightIn10.substring(1, 2));
    dark10[1] = getInt(lightIn10.substring(2, 3));
    light10[1] = getInt(lightIn10.substring(3, 4));
    dark10[2] = getInt(lightIn10.substring(4, 5));
    light10[2] = getInt(lightIn10.substring(5, 6));
    dark10[3] = getInt(lightIn10.substring(6, 8));
    light10[3] = getInt(lightIn10.substring(8, 8));
    dark10[4] = getInt(lightIn10.substring(8, 9));
    light10[4] = getInt(lightIn10.substring(9, 10));
    Serial.println(lightIn10);
    LightSet[36] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[36] == 1 && LightSet[37] == 0 && LightSet[38] == 0)
  {
    lightIn10 = Serial.readString();

    date10[0] = getInt(lightIn10.substring(0, 2));
    month10[0] = getInt(lightIn10.substring(2, 4));
    year10[0] = getInt(lightIn10.substring(4, 8));
    date10[1] = getInt(lightIn10.substring(8, 10));
    month10[1] = getInt(lightIn10.substring(10, 12));
    year10[1] = getInt(lightIn10.substring(12, 16));
    date10[2] = getInt(lightIn10.substring(16, 18));
    month10[2] = getInt(lightIn10.substring(18, 20));
    year10[2] = getInt(lightIn10.substring(20, 24));
    date10[3] = getInt(lightIn10.substring(24, 26));
    month10[3] = getInt(lightIn10.substring(26, 28));
    year10[3] = getInt(lightIn10.substring(28, 32));
    date10[4] = getInt(lightIn10.substring(32, 34));
    month10[4] = getInt(lightIn10.substring(34, 36));
    year10[4] = getInt(lightIn10.substring(36, 40));
    HourFrom10[0] = getInt(lightIn10.substring(40, 42));
    MinuteFrom10[0] = getInt(lightIn10.substring(42, 44));
    HourFrom10[1] = getInt(lightIn10.substring(44, 46));
    MinuteFrom10[1] = getInt(lightIn10.substring(46, 48));
    HourFrom10[2] = getInt(lightIn10.substring(48, 50));
    MinuteFrom10[2] = getInt(lightIn10.substring(50, 52));
    HourFrom10[3] = getInt(lightIn10.substring(52, 54));
    MinuteFrom10[3] = getInt(lightIn10.substring(54, 56));
    HourFrom10[4] = getInt(lightIn10.substring(56, 58));
    MinuteFrom10[4] = getInt(lightIn10.substring(58, 60));

    Serial.println(lightIn10);
    LightSet[37] = 1;
    LightSet[38] = 1;
  }

  // Phase11
  if (Serial.available() == 40 && InitialFlag == 0 && LightSet[37] == 1 && LightSet[38] == 1 && LightSet[39] == 0)
  {
    lightIn11 = Serial.readString();
    // Box1
    HourOn11[0] = getInt(lightIn11.substring(0, 2));
    MinuteOn11[0] = getInt(lightIn11.substring(2, 4));
    HourOff11[0] = getInt(lightIn11.substring(4, 6));
    MinuteOff11[0] = getInt(lightIn11.substring(6, 8));

    // Box2
    HourOn11[1] = getInt(lightIn11.substring(8, 10));
    MinuteOn11[1] = getInt(lightIn11.substring(10, 12));
    HourOff11[1] = getInt(lightIn11.substring(12, 14));
    MinuteOff11[1] = getInt(lightIn11.substring(14, 16));

    // Box3
    HourOn11[2] = getInt(lightIn11.substring(16, 18));
    MinuteOn11[2] = getInt(lightIn11.substring(18, 20));
    HourOff11[2] = getInt(lightIn11.substring(20, 22));
    MinuteOff11[2] = getInt(lightIn11.substring(22, 24));

    // Box4
    HourOn11[3] = getInt(lightIn11.substring(24, 26));
    MinuteOn11[3] = getInt(lightIn11.substring(26, 28));
    HourOff11[3] = getInt(lightIn11.substring(28, 30));
    MinuteOff11[3] = getInt(lightIn11.substring(30, 32));

    // Box5
    HourOn11[4] = getInt(lightIn11.substring(32, 34));
    MinuteOn11[4] = getInt(lightIn11.substring(34, 36));
    HourOff11[4] = getInt(lightIn11.substring(36, 38));
    MinuteOff11[4] = getInt(lightIn11.substring(38, 40));

    Serial.println(lightIn11);
    LightSet[39] = 1;
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[39] == 1 && LightSet[40] == 0)
  {

    lightIn11 = Serial.readString();

    dark11[0] = getInt(lightIn11.substring(0, 1));
    light11[0] = getInt(lightIn11.substring(1, 2));
    dark11[1] = getInt(lightIn11.substring(2, 3));
    light11[1] = getInt(lightIn11.substring(3, 4));
    dark11[2] = getInt(lightIn11.substring(4, 5));
    light11[2] = getInt(lightIn11.substring(5, 6));
    dark11[3] = getInt(lightIn11.substring(6, 8));
    light11[3] = getInt(lightIn11.substring(8, 8));
    dark11[4] = getInt(lightIn11.substring(8, 9));
    light11[4] = getInt(lightIn11.substring(9, 10));
    Serial.println(lightIn11);
    LightSet[40] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[40] == 1 && LightSet[41] == 0 && LightSet[42] == 0)
  {
    lightIn11 = Serial.readString();

    date11[0] = getInt(lightIn11.substring(0, 2));
    month11[0] = getInt(lightIn11.substring(2, 4));
    year11[0] = getInt(lightIn11.substring(4, 8));
    date11[1] = getInt(lightIn11.substring(8, 10));
    month11[1] = getInt(lightIn11.substring(10, 12));
    year11[1] = getInt(lightIn11.substring(12, 16));
    date11[2] = getInt(lightIn11.substring(16, 18));
    month11[2] = getInt(lightIn11.substring(18, 20));
    year11[2] = getInt(lightIn11.substring(20, 24));
    date11[3] = getInt(lightIn11.substring(24, 26));
    month11[3] = getInt(lightIn11.substring(26, 28));
    year11[3] = getInt(lightIn11.substring(28, 32));
    date11[4] = getInt(lightIn11.substring(32, 34));
    month11[4] = getInt(lightIn11.substring(34, 36));
    year11[4] = getInt(lightIn11.substring(36, 40));
    HourFrom11[0] = getInt(lightIn11.substring(40, 42));
    MinuteFrom11[0] = getInt(lightIn11.substring(42, 44));
    HourFrom11[1] = getInt(lightIn11.substring(44, 46));
    MinuteFrom11[1] = getInt(lightIn11.substring(46, 48));
    HourFrom11[2] = getInt(lightIn11.substring(48, 50));
    MinuteFrom11[2] = getInt(lightIn11.substring(50, 52));
    HourFrom11[3] = getInt(lightIn11.substring(52, 54));
    MinuteFrom11[3] = getInt(lightIn11.substring(54, 56));
    HourFrom11[4] = getInt(lightIn11.substring(56, 58));
    MinuteFrom11[4] = getInt(lightIn11.substring(58, 60));

    Serial.println(lightIn11);
    LightSet[41] = 1;
    LightSet[42] = 1;
  }

  // Phase12
  if (Serial.available() == 40 && InitialFlag == 0 && LightSet[41] == 1 && LightSet[42] == 1 && LightSet[43] == 0)
  {
    lightIn12 = Serial.readString();
    // Box1
    HourOn12[0] = getInt(lightIn12.substring(0, 2));
    MinuteOn12[0] = getInt(lightIn12.substring(2, 4));
    HourOff12[0] = getInt(lightIn12.substring(4, 6));
    MinuteOff12[0] = getInt(lightIn12.substring(6, 8));

    // Box2
    HourOn12[1] = getInt(lightIn12.substring(8, 10));
    MinuteOn12[1] = getInt(lightIn12.substring(10, 12));
    HourOff12[1] = getInt(lightIn12.substring(12, 14));
    MinuteOff12[1] = getInt(lightIn12.substring(14, 16));

    // Box3
    HourOn12[2] = getInt(lightIn12.substring(16, 18));
    MinuteOn12[2] = getInt(lightIn12.substring(18, 20));
    HourOff12[2] = getInt(lightIn12.substring(20, 22));
    MinuteOff12[2] = getInt(lightIn12.substring(22, 24));

    // Box4
    HourOn12[3] = getInt(lightIn12.substring(24, 26));
    MinuteOn12[3] = getInt(lightIn12.substring(26, 28));
    HourOff12[3] = getInt(lightIn12.substring(28, 30));
    MinuteOff12[3] = getInt(lightIn12.substring(30, 32));

    // Box5
    HourOn12[4] = getInt(lightIn12.substring(32, 34));
    MinuteOn12[4] = getInt(lightIn12.substring(34, 36));
    HourOff12[4] = getInt(lightIn12.substring(36, 38));
    MinuteOff12[4] = getInt(lightIn12.substring(38, 40));

    Serial.println(lightIn12);
    LightSet[43] = 1;
  }

  if (Serial.available() == 10 && InitialFlag == 0 && TimeSet == 1 && LightSet[43] == 1 && LightSet[44] == 0)
  {

    lightIn12 = Serial.readString();

    dark12[0] = getInt(lightIn12.substring(0, 1));
    light12[0] = getInt(lightIn12.substring(1, 2));
    dark12[1] = getInt(lightIn12.substring(2, 3));
    light12[1] = getInt(lightIn12.substring(3, 4));
    dark12[2] = getInt(lightIn12.substring(4, 5));
    light12[2] = getInt(lightIn12.substring(5, 6));
    dark12[3] = getInt(lightIn12.substring(6, 8));
    light12[3] = getInt(lightIn12.substring(8, 8));
    dark12[4] = getInt(lightIn12.substring(8, 9));
    light12[4] = getInt(lightIn12.substring(9, 10));
    Serial.println(lightIn12);
    LightSet[44] = 1;
    //    Serial.print("-");Serial.print("16");
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[44] == 1 && LightSet[45] == 0 && LightSet[46] == 0)
  {
    lightIn12 = Serial.readString();

    date12[0] = getInt(lightIn12.substring(0, 2));
    month12[0] = getInt(lightIn12.substring(2, 4));
    year12[0] = getInt(lightIn12.substring(4, 8));
    date12[1] = getInt(lightIn12.substring(8, 10));
    month12[1] = getInt(lightIn12.substring(10, 12));
    year12[1] = getInt(lightIn12.substring(12, 16));
    date12[2] = getInt(lightIn12.substring(16, 18));
    month12[2] = getInt(lightIn12.substring(18, 20));
    year12[2] = getInt(lightIn12.substring(20, 24));
    date12[3] = getInt(lightIn12.substring(24, 26));
    month12[3] = getInt(lightIn12.substring(26, 28));
    year12[3] = getInt(lightIn12.substring(28, 32));
    date12[4] = getInt(lightIn12.substring(32, 34));
    month12[4] = getInt(lightIn12.substring(34, 36));
    year12[4] = getInt(lightIn12.substring(36, 40));
    HourFrom12[0] = getInt(lightIn12.substring(40, 42));
    MinuteFrom12[0] = getInt(lightIn12.substring(42, 44));
    HourFrom12[1] = getInt(lightIn12.substring(44, 46));
    MinuteFrom12[1] = getInt(lightIn12.substring(46, 48));
    HourFrom12[2] = getInt(lightIn12.substring(48, 50));
    MinuteFrom12[2] = getInt(lightIn12.substring(50, 52));
    HourFrom12[3] = getInt(lightIn12.substring(52, 54));
    MinuteFrom12[3] = getInt(lightIn12.substring(54, 56));
    HourFrom12[4] = getInt(lightIn12.substring(56, 58));
    MinuteFrom12[4] = getInt(lightIn12.substring(58, 60));

    Serial.println(lightIn12);
    LightSet[45] = 1;
    LightSet[46] = 1;
  }

  // Begin to print the headers and set light flag
  if (InitialFlag == 0 && TimeSet == 1 && LightSet[46] == 1)
  {
    //    Serial.println("HH:MM:SS MO/DY/YEAR LED01 PIR01 ANG011 ANG012 LED02 PIR02 ANG021 ANG022 LED03 PIR03 ANG031 ANG032 LED04 PIR04 ANG041 ANG042 LED05 PIR05 ANG051 ANG052");
    Serial.println("HH:MM:SS MO/DY/YEAR LED01 PIR01 LED02 PIR02 LED03 PIR03 LED04 PIR04 LED05 PIR05");
    InitialFlag = 1;
  }
  // Only start recording when the now.second()=0, otherwise stay in the (delay 1 sec) loop

  // now = rtc.now();
  if (InitialFlag == 1)
  {
    while ((now.second() == 0) == false) // now.second() == 0
    {

      now = rtc.now();
    }

    //     End phase 1 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 0 && now.day() == date2[i] && now.month() == month2[i] && now.year() == year2[i] && now.hour() * 60 + now.minute() >= HourFrom2[i] * 60 + MinuteFrom2[i])
      {
        phase1[i] = 1;
      }
    }

    // End phase 2 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && now.day() == date3[i] && now.month() == month3[i] && now.year() == year3[i] && now.hour() * 60 + now.minute() >= HourFrom3[i] * 60 + MinuteFrom3[i])
      {
        phase2[i] = 1;
      }
    }
    // End phase 3 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] == 1 && now.day() == date4[i] && now.month() == month4[i] && now.year() == year4[i] && now.hour() * 60 + now.minute() >= HourFrom4[i] * 60 + MinuteFrom4[i])
      {
        phase3[i] = 1;
      }
    }
    // End phase 4 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] && phase3[i] == 1 && now.day() == date5[i] && now.month() == month5[i] && now.year() == year5[i] && now.hour() * 60 + now.minute() >= HourFrom5[i] * 60 + MinuteFrom5[i])
      {
        phase4[i] = 1;
      }
    }
    // End phase 5 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] && phase3[i] == 1 && phase4[i] == 1 && now.day() == date6[i] && now.month() == month6[i] && now.year() == year6[i] && now.hour() * 60 + now.minute() >= HourFrom6[i] * 60 + MinuteFrom6[i])
      {
        phase5[i] = 1;
      }
    }
    // End phase 6 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase3[i] && phase4[i] == 1 && phase5[i] == 1 && now.day() == date7[i] && now.month() == month7[i] && now.year() == year7[i] && now.hour() * 60 + now.minute() >= HourFrom7[i] * 60 + MinuteFrom7[i])
      {
        phase6[i] = 1;
      }
    }
    // End phase 7 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase4[i] && phase5[i] == 1 && phase6[i] == 1 && now.day() == date8[i] && now.month() == month8[i] && now.year() == year8[i] && now.hour() * 60 + now.minute() >= HourFrom8[i] * 60 + MinuteFrom8[i])
      {
        phase7[i] = 1;
      }
    }
    // End phase 8 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase5[i] && phase6[i] == 1 && phase7[i] == 1 && now.day() == date9[i] && now.month() == month9[i] && now.year() == year9[i] && now.hour() * 60 + now.minute() >= HourFrom9[i] * 60 + MinuteFrom9[i])
      {
        phase8[i] = 1;
      }
    }
    // End phase 9 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase6[i] && phase7[i] == 1 && phase8[i] == 1 && now.day() == date10[i] && now.month() == month10[i] && now.year() == year10[i] && now.hour() * 60 + now.minute() >= HourFrom10[i] * 60 + MinuteFrom10[i])
      {
        phase9[i] = 1;
      }
    }
    // End phase 10 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase7[i] && phase8[i] == 1 && phase9[i] == 1 && now.day() == date11[i] && now.month() == month11[i] && now.year() == year11[i] && now.hour() * 60 + now.minute() >= HourFrom11[i] * 60 + MinuteFrom11[i])
      {
        phase10[i] = 1;
      }
    }
    // End phase 11 when
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase8[i] && phase9[i] == 1 && phase10[i] == 1 && now.day() == date12[i] && now.month() == month12[i] && now.year() == year12[i] && now.hour() * 60 + now.minute() >= HourFrom12[i] * 60 + MinuteFrom12[i])
      {
        phase11[i] = 1;
      }
    }

    //-----------------------
    // LED CONTROL
    //-----------------------
    // Phase 1 Logic Schedule
    for (int i = 0; i < 5; i++) // loop for 5 boxes
    {
      if (phase1[i] == 0)                                                      //&& (int)dd2 <= date2 && (int)mo2 == month2 && (int)yy2 <= year2
      {                                                                        // Serial.print("Phase1 HourOn1: "); Serial.print(HourOn1[0]); Serial.print(" "); Serial.print(MinuteOn1[0]); Serial.print("-Phase1HourOff");Serial.print(HourOff1[0]);Serial.print(" ");Serial.print(MinuteOff1[0]);
        if (HourOn1[i] * 60 + MinuteOn1[i] < HourOff1[i] * 60 + MinuteOff1[i]) // 0-24 condition Turn On
        {
          if (HourOn1[i] * 60 + MinuteOn1[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff1[i] * 60 + MinuteOff1[i]) // after ON and before OFF
          {
            if (light1[i] == 0 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light1[i] == 0 && dark1[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light1[i] == 1 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (HourOff1[i] * 60 + MinuteOff1[i] <= now.hour() * 60 + now.minute() && light1[i] == 0 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (now.hour() * 60 + now.minute() < HourOn1[i] * 60 + MinuteOn1[i] && light1[i] == 0 && dark1[i] == 0 && initLED[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (now.hour() * 60 + now.minute() < HourOn1[i] * 60 + MinuteOn1[i] && light1[i] == 0 && dark1[i] == 0 && initLED[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 1;
            }
            if (light1[i] == 0 && dark1[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light1[i] == 1 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn1[i] * 60 + MinuteOn1[i] > HourOff1[i] * 60 + MinuteOff1[i]) // 19-07 condition Turn On
        {
          if (HourOn1[i] * 60 + MinuteOn1[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff1[i] * 60 + MinuteOff1[i]) // after ON or before OFF (DL cycle)
          {
            if (HourOn1[i] * 60 + MinuteOn1[i] <= now.hour() * 60 + now.minute() && light1[i] == 0 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (now.hour() * 60 + now.minute() < HourOff1[i] * 60 + MinuteOff1[i] && light1[i] == 0 && dark1[i] == 0 && initLED[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 0;
            }
            if (now.hour() * 60 + now.minute() < HourOff1[i] * 60 + MinuteOff1[i] && light1[i] == 0 && dark1[i] == 0 && initLED[i] == 1)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }

            if (light1[i] == 0 && dark1[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light1[i] == 1 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light1[i] == 0 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light1[i] == 0 && dark1[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light1[i] == 1 && dark1[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    }

    // Phase 2 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] == 0)
      {
        if (HourOn2[i] * 60 + MinuteOn2[i] < HourOff2[i] * 60 + MinuteOff2[i]) // am to pm condition Turn On
        {
          if (HourOn2[i] * 60 + MinuteOn2[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff2[i] * 60 + MinuteOff2[i])
          {
            if (light2[i] == 0 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light2[i] == 0 && dark2[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light2[i] == 1 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light2[i] == 0 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light2[i] == 0 && dark2[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light2[i] == 1 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn2[i] * 60 + MinuteOn2[i] > HourOff2[i] * 60 + MinuteOff2[i]) // pm to am condition Turn On
        {
          if (HourOn2[i] * 60 + MinuteOn2[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff2[i] * 60 + MinuteOff2[i])
          {
            if (light2[i] == 0 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light2[i] == 0 && dark2[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light2[i] == 1 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light2[i] == 0 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light2[i] == 0 && dark2[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light2[i] == 1 && dark2[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    }

    // Phase 3 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] == 1 && phase3[i] == 0)
      {
        if (HourOn3[i] * 60 + MinuteOn3[i] < HourOff3[i] * 60 + MinuteOff3[i]) // am to pm condition Turn On
        {
          if (HourOn3[i] * 60 + MinuteOn3[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff3[i] * 60 + MinuteOff3[i])
          {
            if (light3[i] == 0 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light3[i] == 0 && dark3[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light3[i] == 1 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light3[i] == 0 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light3[i] == 0 && dark3[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light3[i] == 1 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn3[i] * 60 + MinuteOn3[i] > HourOff3[i] * 60 + MinuteOff3[i]) // 19-07 condition Turn On
        {
          if (HourOn3[i] * 60 + MinuteOn3[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff3[i] * 60 + MinuteOff3[i])
          {
            if (light3[i] == 0 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light3[i] == 0 && dark3[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light3[i] == 1 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light3[i] == 0 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light3[i] == 0 && dark3[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light3[i] == 1 && dark3[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 3

    // Phase 4 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] == 1 && phase3[i] == 1)
      {
        if (HourOn4[i] * 60 + MinuteOn4[i] < HourOff4[i] * 60 + MinuteOff4[i]) // am to pm condition Turn On
        {
          if (HourOn4[i] * 60 + MinuteOn4[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff4[i] * 60 + MinuteOff4[i])
          {
            if (light4[i] == 0 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light4[i] == 0 && dark4[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light4[i] == 1 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light4[i] == 0 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light4[i] == 0 && dark4[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light4[i] == 1 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn4[i] * 60 + MinuteOn4[i] > HourOff4[i] * 60 + MinuteOff4[i]) // pm to am condition Turn On
        {
          if (HourOn4[i] * 60 + MinuteOn4[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff4[i] * 60 + MinuteOff4[i])
          {
            if (light4[i] == 0 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light4[i] == 0 && dark4[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light4[i] == 1 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light4[i] == 0 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light4[i] == 0 && dark4[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light4[i] == 1 && dark4[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 4

    // Phase 5 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] == 1 && phase3[i] == 1 && phase4[i] == 1)
      {
        if (HourOn5[i] * 60 + MinuteOn5[i] < HourOff5[i] * 60 + MinuteOff5[i]) // am to pm condition Turn On
        {
          if (HourOn5[i] * 60 + MinuteOn5[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff5[i] * 60 + MinuteOff5[i])
          {
            if (light5[i] == 0 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light5[i] == 0 && dark5[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light5[i] == 1 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light5[i] == 0 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light5[i] == 0 && dark5[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light5[i] == 1 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn5[i] * 60 + MinuteOn5[i] > HourOff5[i] * 60 + MinuteOff5[i]) // pm to am condition Turn On
        {
          if (HourOn5[i] * 60 + MinuteOn5[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff5[i] * 60 + MinuteOff5[i])
          {
            if (light5[i] == 0 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light5[i] == 0 && dark5[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light5[i] == 1 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light5[i] == 0 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light5[i] == 0 && dark5[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light5[i] == 1 && dark5[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 5

    // Phase 6 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase1[i] == 1 && phase2[i] == 1 && phase3[i] == 1 && phase4[i] == 1 && phase5[i] == 1)
      {
        if (HourOn6[i] * 60 + MinuteOn6[i] < HourOff6[i] * 60 + MinuteOff6[i]) // am to pm condition Turn On
        {
          if (HourOn6[i] * 60 + MinuteOn6[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff6[i] * 60 + MinuteOff6[i])
          {
            if (light6[i] == 0 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light6[i] == 0 && dark6[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light6[i] == 1 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light6[i] == 0 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light6[i] == 0 && dark6[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light6[i] == 1 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn6[i] * 60 + MinuteOn6[i] > HourOff6[i] * 60 + MinuteOff6[i]) // pm to am condition Turn On
        {
          if (HourOn6[i] * 60 + MinuteOn6[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff6[i] * 60 + MinuteOff6[i])
          {
            if (light6[i] == 0 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light6[i] == 0 && dark6[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light6[i] == 1 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light6[i] == 0 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light6[i] == 0 && dark6[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light6[i] == 1 && dark6[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 6

    // Phase 7 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase5[i] == 1 && phase6[i] == 1)
      {
        if (HourOn7[i] * 60 + MinuteOn7[i] < HourOff7[i] * 60 + MinuteOff7[i]) // am to pm condition Turn On
        {
          if (HourOn7[i] * 60 + MinuteOn7[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff7[i] * 60 + MinuteOff7[i])
          {
            if (light7[i] == 0 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light7[i] == 0 && dark7[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light7[i] == 1 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light7[i] == 0 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light7[i] == 0 && dark7[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light7[i] == 1 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn7[i] * 60 + MinuteOn7[i] > HourOff7[i] * 60 + MinuteOff7[i]) // pm to am condition Turn On
        {
          if (HourOn7[i] * 60 + MinuteOn7[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff7[i] * 60 + MinuteOff7[i])
          {
            if (light7[i] == 0 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light7[i] == 0 && dark7[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light7[i] == 1 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light7[i] == 0 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light7[i] == 0 && dark7[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light7[i] == 1 && dark7[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 7

    // Phase 8 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase6[i] == 1 && phase7[i] == 1)
      {
        if (HourOn8[i] * 60 + MinuteOn8[i] < HourOff8[i] * 60 + MinuteOff8[i]) // am to pm condition Turn On
        {
          if (HourOn8[i] * 60 + MinuteOn8[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff8[i] * 60 + MinuteOff8[i])
          {
            if (light8[i] == 0 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light8[i] == 0 && dark8[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light8[i] == 1 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light8[i] == 0 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light8[i] == 0 && dark8[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light8[i] == 1 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn8[i] * 60 + MinuteOn8[i] > HourOff8[i] * 60 + MinuteOff8[i]) // pm to am condition Turn On
        {
          if (HourOn8[i] * 60 + MinuteOn8[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff8[i] * 60 + MinuteOff8[i])
          {
            if (light8[i] == 0 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light8[i] == 0 && dark8[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light8[i] == 1 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light8[i] == 0 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light8[i] == 0 && dark8[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light8[i] == 1 && dark8[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 8

    // Phase 9 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase7[i] == 1 && phase8[i] == 1)
      {
        if (HourOn9[i] * 60 + MinuteOn9[i] < HourOff9[i] * 60 + MinuteOff9[i]) // am to pm condition Turn On
        {
          if (HourOn9[i] * 60 + MinuteOn9[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff9[i] * 60 + MinuteOff9[i])
          {
            if (light9[i] == 0 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light9[i] == 0 && dark9[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light9[i] == 1 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light9[i] == 0 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light9[i] == 0 && dark9[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light9[i] == 1 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn9[i] * 60 + MinuteOn9[i] > HourOff9[i] * 60 + MinuteOff9[i]) // pm to am condition Turn On
        {
          if (HourOn9[i] * 60 + MinuteOn9[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff9[i] * 60 + MinuteOff9[i])
          {
            if (light9[i] == 0 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light9[i] == 0 && dark9[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light9[i] == 1 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light9[i] == 0 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light9[i] == 0 && dark9[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light9[i] == 1 && dark9[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 9

    // Phase 10 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase8[i] == 1 && phase9[i] == 1)
      {
        if (HourOn10[i] * 60 + MinuteOn10[i] < HourOff10[i] * 60 + MinuteOff10[i]) // am to pm condition Turn On
        {
          if (HourOn10[i] * 60 + MinuteOn10[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff10[i] * 60 + MinuteOff10[i])
          {
            if (light10[i] == 0 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light10[i] == 0 && dark10[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light10[i] == 1 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light10[i] == 0 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light10[i] == 0 && dark10[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light10[i] == 1 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn10[i] * 60 + MinuteOn10[i] > HourOff10[i] * 60 + MinuteOff10[i]) // pm to am condition Turn On
        {
          if (HourOn10[i] * 60 + MinuteOn10[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff10[i] * 60 + MinuteOff10[i])
          {
            if (light10[i] == 0 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light10[i] == 0 && dark10[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light10[i] == 1 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light10[i] == 0 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light10[i] == 0 && dark10[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light10[i] == 1 && dark10[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 10

    // Phase 11 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase9[i] == 1 && phase10[i] == 1)
      {
        if (HourOn11[i] * 60 + MinuteOn11[i] < HourOff11[i] * 60 + MinuteOff11[i]) // am to pm condition Turn On
        {
          if (HourOn11[i] * 60 + MinuteOn11[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff11[i] * 60 + MinuteOff11[i])
          {
            if (light11[i] == 0 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light11[i] == 0 && dark11[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light11[i] == 1 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light11[i] == 0 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light11[i] == 0 && dark11[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light11[i] == 1 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn11[i] * 60 + MinuteOn11[i] > HourOff11[i] * 60 + MinuteOff11[i]) // pm to am condition Turn On
        {
          if (HourOn11[i] * 60 + MinuteOn11[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff11[i] * 60 + MinuteOff11[i])
          {
            if (light11[i] == 0 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light11[i] == 0 && dark11[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light11[i] == 1 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light11[i] == 0 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light11[i] == 0 && dark11[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light11[i] == 1 && dark11[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 11

    // Phase 12 Logic Schedule
    for (int i = 0; i < 5; i++)
    {
      if (phase10[i] == 1 && phase11[i] == 1)
      {
        if (HourOn12[i] * 60 + MinuteOn12[i] < HourOff12[i] * 60 + MinuteOff12[i]) // am to pm condition Turn On
        {
          if (HourOn12[i] * 60 + MinuteOn12[i] <= now.hour() * 60 + now.minute() && now.hour() * 60 + now.minute() < HourOff12[i] * 60 + MinuteOff12[i])
          {
            if (light12[i] == 0 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light12[i] == 0 && dark12[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light12[i] == 1 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light12[i] == 0 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light12[i] == 0 && dark12[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light12[i] == 1 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
        else if (HourOn12[i] * 60 + MinuteOn12[i] > HourOff12[i] * 60 + MinuteOff12[i]) // pm to am condition Turn On
        {
          if (HourOn12[i] * 60 + MinuteOn12[i] <= now.hour() * 60 + now.minute() || now.hour() * 60 + now.minute() < HourOff12[i] * 60 + MinuteOff12[i])
          {
            if (light12[i] == 0 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
            if (light12[i] == 0 && dark12[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light12[i] == 1 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          }
          else
          {
            if (light12[i] == 0 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light12[i] == 0 && dark12[i] == 1)
            {
              digitalWrite(DOut[i], LOW);
              LightFlag[i] = 0;
            }
            if (light12[i] == 1 && dark12[i] == 0)
            {
              digitalWrite(DOut[i], HIGH);
              LightFlag[i] = 1;
            }
          } // else
        }
      }
    } // end of for loop phase 12

    // If the after all of the settings (Time, Light, Initial header printing, Check schedule) begin to print time stamps and measurements

    // hh2 +=1;
    //    printMeasurementExpan();
    printMeasurement();
    //    timeExpansion();
    Serial.println(" ");

    rtc_delay();

    // if (Serial.read() == 0)
    // {
    //   for (int i = 0; i < 5; i++)
    //   {
    //     digitalWrite(DOut[i], LOW);
    //     LightFlag[i] = 0;
    //   }
    // }
  }
}

// Define a function to print measurement
void printMeasurement()
{
  // mean values over 1-min
  for (int i = 0; i < 5; i++)
  {
    mPIR[i] = 0;
  }
  //  for (int i = 0; i < 10; i++){
  //     mANALOG[i]=0;
  //     Acate[i]=0;
  //  }

  // per-second sampling
  for (int i = 0; i < 5; i++)
  {
    PIR[i] = digitalRead(DIn[i]);
  }

  // sensor value sampling for 1-min
  for (int i = 0; i < 299; ++i)
  {
    for (int j = 0; j < 5; j++)
    {
      PIR[j] = PIR[j] + digitalRead(DIn[j]);
    }

    //      for (int j = 0; j < 10; j++){
    //        ANALOG[j] = analogRead(AIn[j]);
    //         if(ANALOG[j] <= ASensi[j]){
    //            Acate[j] += 1;
    //          } else{
    //              Acate[j] += 0;
    //            }
    //      }

    // millis_delay(90);
    delay(200); // sampling 299 times per minute
  }

  // 1-min summation
  for (int i = 0; i < 5; i++)
  {
    mPIR[i] = PIR[i];
  }
  //  for (int i = 0; i < 10; i++){
  //     mANALOG[i] = Acate[i];
  //  }

  // Outputs

  printTime();
  Serial.print(" ");

  for (int i = 0; i < 5; i++)
  {
    Serial.print("0000");
    Serial.print(LightFlag[i]);
    Serial.print(" ");
    if (mPIR[i] < 10000 && mPIR[i] > 999)
    {
      Serial.print("0");
    }
    if (mPIR[i] < 1000 && mPIR[i] > 99)
    {
      Serial.print("00");
    }
    if (mPIR[i] < 100 && mPIR[i] > 9)
    {
      Serial.print("000");
    }
    if (mPIR[i] < 10)
    {
      Serial.print("0000");
    }
    Serial.print(mPIR[i]);
    Serial.print(" ");

    //      int iOdds, iEven;
    ////      //      analogSignal even
    //        iEven = i*2;
    //        if(mANALOG[iEven]<10000 && mANALOG[iEven]>999)
    //        {
    //          Serial.print("00");
    //        }
    //        if(mANALOG[iEven]<1000 && mANALOG[iEven]>99)
    //        {
    //          Serial.print("000");
    //        }
    //        if(mANALOG[iEven]<100 && mANALOG[iEven]>9)
    //        {
    //          Serial.print("0000");
    //        }
    //        if(mANALOG[iEven]<10)
    //        {
    //          Serial.print("00000");
    //        }
    //        Serial.print(mANALOG[iEven]);
    //        Serial.print(" ");
    //////      analogSignal odd
    //      iOdds = 2*i+1;
    //
    //      if(mANALOG[iOdds]<10000 && mANALOG[iOdds]>999)
    //        {
    //          Serial.print("00");
    //        }
    //        if(mANALOG[iOdds]<1000 && mANALOG[iOdds]>99)
    //        {
    //          Serial.print("000");
    //        }
    //        if(mANALOG[iOdds]<100 && mANALOG[iOdds]>9)
    //        {
    //          Serial.print("0000");
    //        }
    //        if(mANALOG[iOdds]<10)
    //        {
    //          Serial.print("00000");
    //        }
    //        Serial.print(mANALOG[iOdds]);
    //        Serial.print(" ");
  }
}

// Define a function to print time
void printTime()
{
  DateTime now = rtc.now();
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
