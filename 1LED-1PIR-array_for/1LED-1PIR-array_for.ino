/*
 * 1-LED, 1-PIR box driver (1 arduino driving 10 box)
 * 
 * Jihwan Myung 
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

#include <Wire.h>
#include "DS1307.h"

DS1307 clock; //define a object of DS1307 class

String dateIn;
String lightIn1;
String lightIn2;
String lightIn3;

// declaration in array of 10 boxes
int PIR[10]  = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int mPIR[10]  = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int phase1[10]  = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int phase2[10]  = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int HourOn1[10]    = { 8, 8, 8, 8, 8, 8, 8, 8, 8, 8};  // phase 1
int MinuteOn1[10]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOff1[10]   = {20,20,20,20,20,20,20,20,20,20};
int MinuteOff1[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn2[10]    = { 8, 8, 8, 8, 8, 8, 8, 8, 8, 8};  // phase 2
int MinuteOn2[10]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOff2[10]   = {20,20,20,20,20,20,20,20,20,20};
int MinuteOff2[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn3[10]    = { 8, 8, 8, 8, 8, 8, 8, 8, 8, 8};  // phase 3
int MinuteOn3[10]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOff3[10]   = {20,20,20,20,20,20,20,20,20,20};
int MinuteOff3[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int HourFrom2[10]   = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int HourFrom3[10]   = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 3
int MinuteFrom2[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int MinuteFrom3[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 3

int date2[10]  = {10,10,10,10,10,10,10,10,10,10};      // phase 2
int date3[10]  = {10,10,10,10,10,10,10,10,10,10};      // phase 3
int month2[10] = {12,12,12,12,12,12,12,12,12,12};      // phase 2
int month3[10] = {12,12,12,12,12,12,12,12,12,12};      // phase 3
int year2[10]  = {2018,2018,2018,2018,2018,2018,2018,2018,2018,2018}; // phase 2
int year3[10]  = {2018,2018,2018,2018,2018,2018,2018,2018,2018,2018}; // phase 3

int light1[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};      // phase 1
int light2[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};      // phase 2
int light3[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};      // phase 3
int dark1[10]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};      // phase 1
int dark2[10]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};      // phase 2
int dark3[10]  = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};      // phase 3

// Digital In-Out
int DIn[10]  = { 2, 4, 6, 8, 10, 12, 22, 24, 26, 28};  // PIR
int DOut[10] = { 3, 5, 7, 9, 11, 13, 23, 25, 27, 29};  // LED

// Light flags
int LightFlag[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int TimeSet = 0;
int LightSet[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int InitialFlag = 0;

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
  for (int i=0; i<10; i++){
     pinMode(DIn[i], INPUT);    // PIR
     pinMode(DOut[i], OUTPUT);  // LED
  }

  delay(1000); // recommended delay before start-up (1-sec)
}

//////////////////////////////////////////////////////////////////////////////////////// Main loop
void loop()
{

  //Time Synching (Get the input from computer time through Python interface)
  if (Serial.available() == 19 && TimeSet == 0)
  {
    dateIn = Serial.readString();
    clock.stopClock();
    clock.fillByYMD(getInt(dateIn.substring(0, 4)), getInt(dateIn.substring(5, 7)), getInt(dateIn.substring(8, 10)));
    clock.fillByHMS(getInt(dateIn.substring(11, 13)), getInt(dateIn.substring(14, 16)), getInt(dateIn.substring(17, 19)));
    clock.setTime();
    clock.startClock();

    Serial.println(dateIn);

    TimeSet = 1;
  }
  ////////////////////// Light Schedule (Get the input from Python interface)

  // Phase1
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    //Box1
    HourOn1[0]    = getInt(lightIn1.substring(0, 2));
    MinuteOn1[0]  = getInt(lightIn1.substring(2, 4));
    HourOff1[0]   = getInt(lightIn1.substring(4, 6));
    MinuteOff1[0] = getInt(lightIn1.substring(6, 8));

    //Box2
    HourOn1[1]    = getInt(lightIn1.substring(8, 10));
    MinuteOn1[1]  = getInt(lightIn1.substring(10, 12));
    HourOff1[1]   = getInt(lightIn1.substring(12, 14));
    MinuteOff1[1] = getInt(lightIn1.substring(14, 16));

    //Box3
    HourOn1[2]    = getInt(lightIn1.substring(16, 18));
    MinuteOn1[2]  = getInt(lightIn1.substring(18, 20));
    HourOff1[2]   = getInt(lightIn1.substring(20, 22));
    MinuteOff1[2] = getInt(lightIn1.substring(22, 24));

    //Box4
    HourOn1[3]    = getInt(lightIn1.substring(24, 26));
    MinuteOn1[3]  = getInt(lightIn1.substring(26, 28));
    HourOff1[3]   = getInt(lightIn1.substring(28, 30));
    MinuteOff1[3] = getInt(lightIn1.substring(30, 32));

    //Box5
    HourOn1[4]    = getInt(lightIn1.substring(32, 34));
    MinuteOn1[4]  = getInt(lightIn1.substring(34, 36));
    HourOff1[4]   = getInt(lightIn1.substring(36, 38));
    MinuteOff1[4] = getInt(lightIn1.substring(38, 40));

    LightSet[1] = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 0)
  {
    lightIn1 = Serial.readString();
    //Box6
    HourOn1[5]    = getInt(lightIn1.substring(0, 2));
    MinuteOn1[5]  = getInt(lightIn1.substring(2, 4));
    HourOff1[5]   = getInt(lightIn1.substring(4, 6));
    MinuteOff1[5] = getInt(lightIn1.substring(6, 8));

    //Box7
    HourOn1[6]    = getInt(lightIn1.substring(8, 10));
    MinuteOn1[6]  = getInt(lightIn1.substring(10, 12));
    HourOff1[6]   = getInt(lightIn1.substring(12, 14));
    MinuteOff1[6] = getInt(lightIn1.substring(14, 16));

    //Box8
    HourOn1[7]    = getInt(lightIn1.substring(16, 18));
    MinuteOn1[7]  = getInt(lightIn1.substring(18, 20));
    HourOff1[7]   = getInt(lightIn1.substring(20, 22));
    MinuteOff1[7] = getInt(lightIn1.substring(22, 24));

    //Box9
    HourOn1[8]    = getInt(lightIn1.substring(24, 26));
    MinuteOn1[8]  = getInt(lightIn1.substring(26, 28));
    HourOff1[8]   = getInt(lightIn1.substring(28, 30));
    MinuteOff1[8] = getInt(lightIn1.substring(30, 32));

    //Box10
    HourOn1[9]    = getInt(lightIn1.substring(32, 34));
    MinuteOn1[9]  = getInt(lightIn1.substring(34, 36));
    HourOff1[9]   = getInt(lightIn1.substring(36, 38));
    MinuteOff1[9] = getInt(lightIn1.substring(38, 40));

    dark1[0]  = getInt(lightIn1.substring(40, 41));
    light1[0] = getInt(lightIn1.substring(41, 42));
    dark1[1]  = getInt(lightIn1.substring(42, 43));
    light1[1] = getInt(lightIn1.substring(43, 44));
    dark1[2]  = getInt(lightIn1.substring(44, 45));
    light1[2] = getInt(lightIn1.substring(45, 46));
    dark1[3]  = getInt(lightIn1.substring(46, 47));
    light1[3] = getInt(lightIn1.substring(47, 48));
    dark1[4]  = getInt(lightIn1.substring(48, 49));
    light1[4] = getInt(lightIn1.substring(49, 50));
    dark1[5]  = getInt(lightIn1.substring(50, 51));
    light1[5] = getInt(lightIn1.substring(51, 52));
    dark1[6]  = getInt(lightIn1.substring(52, 53));
    light1[6] = getInt(lightIn1.substring(53, 54));
    dark1[7]  = getInt(lightIn1.substring(54, 55));
    light1[7] = getInt(lightIn1.substring(55, 56));
    dark1[8]  = getInt(lightIn1.substring(56, 57));
    light1[8] = getInt(lightIn1.substring(57, 58));
    dark1[9]  = getInt(lightIn1.substring(58, 59));
    light1[9] = getInt(lightIn1.substring(59, 60));

    Serial.println(lightIn1);
    LightSet[2] = 1;
  }

  // Phase2
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 0)
  {
    lightIn2 = Serial.readString();
    //Box1
    HourOn2[0]    = getInt(lightIn2.substring(0, 2));
    MinuteOn2[0]  = getInt(lightIn2.substring(2, 4));
    HourOff2[0]   = getInt(lightIn2.substring(4, 6));
    MinuteOff2[0] = getInt(lightIn2.substring(6, 8));

    //Box2
    HourOn2[1]    = getInt(lightIn2.substring(8, 10));
    MinuteOn2[1]  = getInt(lightIn2.substring(10, 12));
    HourOff2[1]   = getInt(lightIn2.substring(12, 14));
    MinuteOff2[1] = getInt(lightIn2.substring(14, 16));

    //Box3
    HourOn2[2]    = getInt(lightIn2.substring(16, 18));
    MinuteOn2[2]  = getInt(lightIn2.substring(18, 20));
    HourOff2[2]   = getInt(lightIn2.substring(20, 22));
    MinuteOff2[2] = getInt(lightIn2.substring(22, 24));

    //Box4
    HourOn2[3]    = getInt(lightIn2.substring(24, 26));
    MinuteOn2[3]  = getInt(lightIn2.substring(26, 28));
    HourOff2[3]   = getInt(lightIn2.substring(28, 30));
    MinuteOff2[3] = getInt(lightIn2.substring(30, 32));

    //Box5
    HourOn2[4]    = getInt(lightIn2.substring(32, 34));
    MinuteOn2[4]  = getInt(lightIn2.substring(34, 36));
    HourOff2[4]   = getInt(lightIn2.substring(36, 38));
    MinuteOff2[4] = getInt(lightIn2.substring(38, 40));

    Serial.println(lightIn2);
    LightSet[3] = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 0)
  {
    lightIn2 = Serial.readString();

    //Box6
    HourOn2[5]    = getInt(lightIn2.substring(0, 2));
    MinuteOn2[5]  = getInt(lightIn2.substring(2, 4));
    HourOff2[5]   = getInt(lightIn2.substring(4, 6));
    MinuteOff2[5] = getInt(lightIn2.substring(6, 8));

    //Box7
    HourOn2[6]    = getInt(lightIn2.substring(8, 10));
    MinuteOn2[6]  = getInt(lightIn2.substring(10, 12));
    HourOff2[6]   = getInt(lightIn2.substring(12, 14));
    MinuteOff2[6] = getInt(lightIn2.substring(14, 16));

    //Box8
    HourOn2[7]    = getInt(lightIn2.substring(16, 18));
    MinuteOn2[7]  = getInt(lightIn2.substring(18, 20));
    HourOff2[7]   = getInt(lightIn2.substring(20, 22));
    MinuteOff2[7] = getInt(lightIn2.substring(22, 24));

    //Box9
    HourOn2[8]    = getInt(lightIn2.substring(24, 26));
    MinuteOn2[8]  = getInt(lightIn2.substring(26, 28));
    HourOff2[8]   = getInt(lightIn2.substring(28, 30));
    MinuteOff2[8] = getInt(lightIn2.substring(30, 32));

    //Box10
    HourOn2[9]    = getInt(lightIn2.substring(32, 34));
    MinuteOn2[9]  = getInt(lightIn2.substring(34, 36));
    HourOff2[9]   = getInt(lightIn2.substring(36, 38));
    MinuteOff2[9] = getInt(lightIn2.substring(38, 40));

    dark2[0]  = getInt(lightIn2.substring(40, 41));
    light2[0] = getInt(lightIn2.substring(41, 42));
    dark2[1]  = getInt(lightIn2.substring(42, 43));
    light2[1] = getInt(lightIn2.substring(43, 44));
    dark2[2]  = getInt(lightIn2.substring(44, 45));
    light2[2] = getInt(lightIn2.substring(45, 46));
    dark2[3]  = getInt(lightIn2.substring(46, 47));
    light2[3] = getInt(lightIn2.substring(47, 48));
    dark2[4]  = getInt(lightIn2.substring(48, 49));
    light2[4] = getInt(lightIn2.substring(49, 50));
    dark2[5]  = getInt(lightIn2.substring(50, 51));
    light2[5] = getInt(lightIn2.substring(51, 52));
    dark2[6]  = getInt(lightIn2.substring(52, 53));
    light2[6] = getInt(lightIn2.substring(53, 54));
    dark2[7]  = getInt(lightIn2.substring(54, 55));
    light2[7] = getInt(lightIn2.substring(55, 56));
    dark2[8]  = getInt(lightIn2.substring(56, 57));
    light2[8] = getInt(lightIn2.substring(57, 58));
    dark2[9]  = getInt(lightIn2.substring(58, 59));
    light2[9] = getInt(lightIn2.substring(59, 60));

    Serial.println(lightIn2);
    LightSet[4] = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 1 && LightSet[5] == 0)
  {
    lightIn2 = Serial.readString();

    date2[0]  = getInt(lightIn2.substring(0, 2));
    month2[0] = getInt(lightIn2.substring(2, 4));
    year2[0]  = getInt(lightIn2.substring(4, 8));
    date2[1]  = getInt(lightIn2.substring(8, 10));
    month2[1] = getInt(lightIn2.substring(10, 12));
    year2[1]  = getInt(lightIn2.substring(12, 16));
    date2[2]  = getInt(lightIn2.substring(16, 18));
    month2[2] = getInt(lightIn2.substring(18, 20));
    year2[2]  = getInt(lightIn2.substring(20, 24));
    date2[3]  = getInt(lightIn2.substring(24, 26));
    month2[3] = getInt(lightIn2.substring(26, 28));
    year2[3]  = getInt(lightIn2.substring(28, 32));
    date2[4]  = getInt(lightIn2.substring(32, 34));
    month2[4] = getInt(lightIn2.substring(34, 36));
    year2[4]  = getInt(lightIn2.substring(36, 40));
    HourFrom2[0]   = getInt(lightIn2.substring(40, 42));
    MinuteFrom2[0] = getInt(lightIn2.substring(42, 44));
    HourFrom2[1]   = getInt(lightIn2.substring(44, 46));
    MinuteFrom2[1] = getInt(lightIn2.substring(46, 48));
    HourFrom2[2]   = getInt(lightIn2.substring(48, 50));
    MinuteFrom2[2] = getInt(lightIn2.substring(50, 52));
    HourFrom2[3]   = getInt(lightIn2.substring(52, 54));
    MinuteFrom2[3] = getInt(lightIn2.substring(54, 56));
    HourFrom2[4]   = getInt(lightIn2.substring(56, 58));
    MinuteFrom2[4] = getInt(lightIn2.substring(58, 60));

    Serial.println(lightIn2);
    LightSet[5] = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 1 && LightSet[5] == 1 && LightSet[6] == 0)
  {
    lightIn2 = Serial.readString();

    date2[5]  = getInt(lightIn2.substring(0, 2));
    month2[5] = getInt(lightIn2.substring(2, 4));
    year2[5]  = getInt(lightIn2.substring(4, 8));
    date2[6]  = getInt(lightIn2.substring(8, 10));
    month2[6] = getInt(lightIn2.substring(10, 12));
    year2[6]  = getInt(lightIn2.substring(12, 16));
    date2[7]  = getInt(lightIn2.substring(16, 18));
    month2[7] = getInt(lightIn2.substring(18, 20));
    year2[7]  = getInt(lightIn2.substring(20, 24));
    date2[8]  = getInt(lightIn2.substring(24, 26));
    month2[8] = getInt(lightIn2.substring(26, 28));
    year2[8]  = getInt(lightIn2.substring(28, 32));
    date2[9]  = getInt(lightIn2.substring(32, 34));
    month2[9] = getInt(lightIn2.substring(34, 36));
    year2[9]  = getInt(lightIn2.substring(36, 40));
    HourFrom2[5]   = getInt(lightIn2.substring(40, 42));
    MinuteFrom2[5] = getInt(lightIn2.substring(42, 44));
    HourFrom2[6]   = getInt(lightIn2.substring(44, 46));
    MinuteFrom2[6] = getInt(lightIn2.substring(46, 48));
    HourFrom2[7]   = getInt(lightIn2.substring(48, 50));
    MinuteFrom2[7] = getInt(lightIn2.substring(50, 52));
    HourFrom2[8]   = getInt(lightIn2.substring(52, 54));
    MinuteFrom2[8] = getInt(lightIn2.substring(54, 56));
    HourFrom2[9]   = getInt(lightIn2.substring(56, 58));
    MinuteFrom2[9] = getInt(lightIn2.substring(58, 60));

    Serial.println(lightIn2);
    LightSet[6] = 1;
  }

  // Phase3
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 1 && LightSet[5] == 1 && LightSet[6] == 1 && LightSet[7] == 0)
  {
    lightIn3 = Serial.readString();
    //Box1
    HourOn3[0]    = getInt(lightIn3.substring(0, 2));
    MinuteOn3[0]  = getInt(lightIn3.substring(2, 4));
    HourOff3[0]   = getInt(lightIn3.substring(4, 6));
    MinuteOff3[0] = getInt(lightIn3.substring(6, 8));

    //Box2
    HourOn3[1]    = getInt(lightIn3.substring(8, 10));
    MinuteOn3[1]  = getInt(lightIn3.substring(10, 12));
    HourOff3[1]   = getInt(lightIn3.substring(12, 14));
    MinuteOff3[1] = getInt(lightIn3.substring(14, 16));

    //Box3
    HourOn3[2]    = getInt(lightIn3.substring(16, 18));
    MinuteOn3[2]  = getInt(lightIn3.substring(18, 20));
    HourOff3[2]   = getInt(lightIn3.substring(20, 22));
    MinuteOff3[2] = getInt(lightIn3.substring(22, 24));

    //Box4
    HourOn3[3]    = getInt(lightIn3.substring(24, 26));
    MinuteOn3[3]  = getInt(lightIn3.substring(26, 28));
    HourOff3[3]   = getInt(lightIn3.substring(28, 30));
    MinuteOff3[3] = getInt(lightIn3.substring(30, 32));

    //Box5
    HourOn3[4]    = getInt(lightIn3.substring(32, 34));
    MinuteOn3[4]  = getInt(lightIn3.substring(34, 36));
    HourOff3[4]   = getInt(lightIn3.substring(36, 38));
    MinuteOff3[4] = getInt(lightIn3.substring(38, 40));

    Serial.println(lightIn3);
    LightSet[7] = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 1 && LightSet[5] == 1 && LightSet[6] == 1 && LightSet[7] == 1 && LightSet[8] == 0)
  {
    lightIn3 = Serial.readString();

    //Box6
    HourOn3[5]    = getInt(lightIn3.substring(0, 2));
    MinuteOn3[5]  = getInt(lightIn3.substring(2, 4));
    HourOff3[5]   = getInt(lightIn3.substring(4, 6));
    MinuteOff3[5] = getInt(lightIn3.substring(6, 8));

    //Box7
    HourOn3[6]    = getInt(lightIn3.substring(8, 10));
    MinuteOn3[6]  = getInt(lightIn3.substring(10, 12));
    HourOff3[6]   = getInt(lightIn3.substring(12, 14));
    MinuteOff3[6] = getInt(lightIn3.substring(14, 16));

    //Box8
    HourOn3[7]    = getInt(lightIn3.substring(16, 18));
    MinuteOn3[7]  = getInt(lightIn3.substring(18, 20));
    HourOff3[7]   = getInt(lightIn3.substring(20, 22));
    MinuteOff3[7] = getInt(lightIn3.substring(22, 24));

    //Box9
    HourOn3[8]    = getInt(lightIn3.substring(24, 26));
    MinuteOn3[8]  = getInt(lightIn3.substring(26, 28));
    HourOff3[8]   = getInt(lightIn3.substring(28, 30));
    MinuteOff3[8] = getInt(lightIn3.substring(30, 32));

    //Box10
    HourOn3[9]    = getInt(lightIn3.substring(32, 34));
    MinuteOn3[9]  = getInt(lightIn3.substring(34, 36));
    HourOff3[9]   = getInt(lightIn3.substring(36, 38));
    MinuteOff3[9] = getInt(lightIn3.substring(38, 40));

    dark3[0]  = getInt(lightIn3.substring(40, 41));
    light3[0] = getInt(lightIn3.substring(41, 42));
    dark3[1]  = getInt(lightIn3.substring(42, 43));
    light3[1] = getInt(lightIn3.substring(43, 44));
    dark3[2]  = getInt(lightIn3.substring(44, 45));
    light3[2] = getInt(lightIn3.substring(45, 46));
    dark3[3]  = getInt(lightIn3.substring(46, 47));
    light3[3] = getInt(lightIn3.substring(47, 48));
    dark3[4]  = getInt(lightIn3.substring(48, 49));
    light3[4] = getInt(lightIn3.substring(49, 50));
    dark3[5]  = getInt(lightIn3.substring(50, 51));
    light3[5] = getInt(lightIn3.substring(51, 52));
    dark3[6]  = getInt(lightIn3.substring(52, 53));
    light3[6] = getInt(lightIn3.substring(53, 54));
    dark3[7]  = getInt(lightIn3.substring(54, 55));
    light3[7] = getInt(lightIn3.substring(55, 56));
    dark3[8]  = getInt(lightIn3.substring(56, 57));
    light3[8] = getInt(lightIn3.substring(57, 58));
    dark3[9]  = getInt(lightIn3.substring(58, 59));
    light3[9] = getInt(lightIn3.substring(59, 60));

    Serial.println(lightIn3);
    LightSet[8] = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 1 && LightSet[5] == 1 && LightSet[6] == 1 && LightSet[7] == 1 && LightSet[8] == 1 && LightSet[9] == 0)
  {
    lightIn3 = Serial.readString();

    date3[0]  = getInt(lightIn3.substring(0, 2));
    month3[0] = getInt(lightIn3.substring(2, 4));
    year3[0]  = getInt(lightIn3.substring(4, 8));
    date3[1]  = getInt(lightIn3.substring(8, 10));
    month3[1] = getInt(lightIn3.substring(10, 12));
    year3[1]  = getInt(lightIn3.substring(12, 16));
    date3[2]  = getInt(lightIn3.substring(16, 18));
    month3[2] = getInt(lightIn3.substring(18, 20));
    year3[2]  = getInt(lightIn3.substring(20, 24));
    date3[3]  = getInt(lightIn3.substring(24, 26));
    month3[3] = getInt(lightIn3.substring(26, 28));
    year3[3]  = getInt(lightIn3.substring(28, 32));
    date3[4]  = getInt(lightIn3.substring(32, 34));
    month3[4] = getInt(lightIn3.substring(34, 36));
    year3[4]  = getInt(lightIn3.substring(36, 40));
    HourFrom3[0]   = getInt(lightIn3.substring(40, 42));
    MinuteFrom3[0] = getInt(lightIn3.substring(42, 44));
    HourFrom3[1]   = getInt(lightIn3.substring(44, 46));
    MinuteFrom3[1] = getInt(lightIn3.substring(46, 48));
    HourFrom3[2]   = getInt(lightIn3.substring(48, 50));
    MinuteFrom3[2] = getInt(lightIn3.substring(50, 52));
    HourFrom3[3]   = getInt(lightIn3.substring(52, 54));
    MinuteFrom3[3] = getInt(lightIn3.substring(54, 56));
    HourFrom3[4]   = getInt(lightIn3.substring(56, 58));
    MinuteFrom3[4] = getInt(lightIn3.substring(58, 60));

    Serial.println(lightIn3);
    LightSet[9] = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 1 && LightSet[5] == 1 && LightSet[6] == 1 && LightSet[7] == 1 && LightSet[8] == 1 && LightSet[9] == 1 && LightSet[0] == 0)
  {
    lightIn3 = Serial.readString();

    date3[5]  = getInt(lightIn3.substring(0, 2));
    month3[5] = getInt(lightIn3.substring(2, 4));
    year3[5]  = getInt(lightIn3.substring(4, 8));
    date3[6]  = getInt(lightIn3.substring(8, 10));
    month3[6] = getInt(lightIn3.substring(10, 12));
    year3[6]  = getInt(lightIn3.substring(12, 16));
    date3[7]  = getInt(lightIn3.substring(16, 18));
    month3[7] = getInt(lightIn3.substring(18, 20));
    year3[7]  = getInt(lightIn3.substring(20, 24));
    date3[8]  = getInt(lightIn3.substring(24, 26));
    month3[8] = getInt(lightIn3.substring(26, 28));
    year3[8]  = getInt(lightIn3.substring(28, 32));
    date3[9]  = getInt(lightIn3.substring(32, 34));
    month3[9] = getInt(lightIn3.substring(34, 36));
    year3[9]  = getInt(lightIn3.substring(36, 40));
    HourFrom3[5]   = getInt(lightIn3.substring(40, 42));
    MinuteFrom3[5] = getInt(lightIn3.substring(42, 44));
    HourFrom3[6]   = getInt(lightIn3.substring(44, 46));
    MinuteFrom3[6] = getInt(lightIn3.substring(46, 48));
    HourFrom3[7]   = getInt(lightIn3.substring(48, 50));
    MinuteFrom3[7] = getInt(lightIn3.substring(50, 52));
    HourFrom3[8]   = getInt(lightIn3.substring(52, 54));
    MinuteFrom3[8] = getInt(lightIn3.substring(54, 56));
    HourFrom3[9]   = getInt(lightIn3.substring(56, 58));
    MinuteFrom3[9] = getInt(lightIn3.substring(58, 60));

    Serial.println(lightIn3);
    LightSet[0] = 1;
  }

  // Begin to print the headers and set light flag
  if (InitialFlag == 0 && TimeSet == 1 && LightSet[0] == 1 && LightSet[1] == 1 && LightSet[2] == 1 && LightSet[3] == 1 && LightSet[4] == 1 && LightSet[5] == 1 && LightSet[6] == 1 && LightSet[7] == 1 && LightSet[8] == 1 && LightSet[9] == 1)
  {
    Serial.println("HH:MM:SS MO/DY/YEAR LED01 PIR01 LED02 PIR02 LED03 PIR03 LED04 PIR04 LED05 PIR05 LED06 PIR06 LED07 PIR07 LED08 PIR08 LED09 PIR09 LED10 PIR10");
    InitialFlag = 1;
  }
  // Only start recording when the Clock.second=0, otherwise stay in the (delay 1 sec) loop
  clock.getTime();
  if (InitialFlag == 1)
  {
    while ((clock.second == 0) == false)
    {
      delay(1);
      clock.getTime();
    }

    // End phase 1 when
    for (int i=0; i<10; i++){
      if (phase1[i] == 0 && clock.dayOfMonth == date2[i] && clock.month == month2[i] && clock.year + 2000 == year2[i] && clock.hour * 60 + clock.minute >= HourFrom2[i] * 60 + MinuteFrom2[i]){
         phase1[i] = 1;
      }
    }

    // End phase 2 when
    for (int i=0; i<10; i++){
      if (phase2[i] == 0 && clock.dayOfMonth == date3[i] && clock.month == month3[i] && clock.year + 2000 == year3[i] && clock.hour * 60 + clock.minute >= HourFrom3[i] * 60 + MinuteFrom3[i]){
         phase2[i] = 1;
      }
    }
    
    //////////For Phase1
    for (int i=0; i<10; i++){
      if (phase1[i] == 0)
      {
        if (clock.hour * 60 + clock.minute >= HourOn1[i] * 60 + MinuteOn1[i] && clock.hour * 60 + clock.minute < HourOff1[i] * 60 + MinuteOff1[i])
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
         } // if time condition is met
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
          } //else
      } // if phase1
    } // end of for loop

    ///////For phase 2
    for (int i=0; i<10; i++){
      if (phase1[i] == 1 && phase2[i] == 0)
      {
        if (clock.hour * 60 + clock.minute >= HourOn2[i] * 60 + MinuteOn2[i] && clock.hour * 60 + clock.minute < HourOff2[i] * 60 + MinuteOff2[i])
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
         } // if time condition is met
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
          } //else
      } // if phase2
    } // end of for loop

    ///////For phase 3
    for (int i=0; i<10; i++){
      if (phase1[i] == 1 && phase2[i] == 1)
      {
        if (clock.hour * 60 + clock.minute >= HourOn3[i] * 60 + MinuteOn3[i] && clock.hour * 60 + clock.minute < HourOff3[i] * 60 + MinuteOff3[i])
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
         } // if time condition is met
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
          } //else
      } // if phase3
    } // end of for loop

    // If the after all of the settings (Time, Light, Initial header printing, Check schedule) begin to print time stamps and measurements

    printMeasurement();
    Serial.println(" ");
  }
}

// Define a function to print measurement
void printMeasurement()
{
  // mean values over 1-min  
  for (int i = 0; i < 10; i++){
     mPIR[i] = 0;
  }

  // per-second sampling
  for (int i = 0; i < 10; i++){
     PIR[i] = digitalRead(DIn[i]);
  }

  // sensor value sampling for 1-min
  for (int i = 0; i < 999; i++)
  {
      for (int j = 0; j < 10; j++){
         PIR[j] = PIR[j] + digitalRead(DIn[j]);
      }
      
    delay(60); // sampling 1000 times per minute
  }

  // 1-min summation
  for (int i = 0; i < 10; i++){
     mPIR[i] = PIR[i];
  }

  // Outputs

  printTime();
  Serial.print(" ");

  for (int i = 0; i < 10; i++){
      Serial.print("0000");
      Serial.print(LightFlag[i]);
      Serial.print(" ");
      if(mPIR[i]<10000 && mPIR[i]>999)
      {
        Serial.print("0");
      }
      if(mPIR[i]<1000 && mPIR[i]>99)
      {
        Serial.print("00");
      }
      if(mPIR[i]<100 && mPIR[i]>9)
      {
        Serial.print("000");
      }
      if(mPIR[i]<10)
      {
        Serial.print("0000");
      }
      Serial.print(mPIR[i]);
      Serial.print(" ");
  }
} // void

// Define a function to print time
void printTime()
{
  if (clock.hour < 10)
  {
    Serial.print("0");
  }
  Serial.print(clock.hour, DEC);
  Serial.print(":");
  if (clock.minute < 10)
  {
    Serial.print("0");
  }
  Serial.print(clock.minute, DEC);
  Serial.print(":");
  if (clock.second < 10)
  {
    Serial.print("0");
  }
  Serial.print(clock.second, DEC);
  Serial.print(" ");
  if (clock.month < 10)
  {
    Serial.print("0");
  }
  Serial.print(clock.month, DEC);
  Serial.print("/");
  if (clock.dayOfMonth < 10)
  {
    Serial.print("0");
  }
  Serial.print(clock.dayOfMonth, DEC);
  Serial.print("/");
  Serial.print(clock.year + 2000, DEC);
}
