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

int phase1_1 = 0;
int phase2_1 = 0;
int phase3_1 = 0;
int phase4_1 = 0;
int phase5_1 = 0;
int phase6_1 = 0;
int phase7_1 = 0;
int phase8_1 = 0;
int phase9_1 = 0;
int phase10_1 = 0;

int phase1_2 = 0;
int phase2_2 = 0;
int phase3_2 = 0;
int phase4_2 = 0;
int phase5_2 = 0;
int phase6_2 = 0;
int phase7_2 = 0;
int phase8_2 = 0;
int phase9_2 = 0;
int phase10_2 = 0;

int HourOn1_1 = 8;
int MinuteOn1_1 = 00;
int HourOff1_1 = 20;
int MinuteOff1_1 = 00;

int HourOn1_2 = 8;
int MinuteOn1_2 = 00;
int HourOff1_2 = 20;
int MinuteOff1_2 = 00;

int HourOn1_3 = 8;
int MinuteOn1_3 = 00;
int HourOff1_3 = 20;
int MinuteOff1_3 = 00;

int HourOn2_1 = 8;
int MinuteOn2_1 = 00;
int HourOff2_1 = 20;
int MinuteOff2_1 = 00;

int HourOn2_2 = 8;
int MinuteOn2_2 = 00;
int HourOff2_2 = 20;
int MinuteOff2_2 = 00;

int HourOn2_3 = 8;
int MinuteOn2_3 = 00;
int HourOff2_3 = 20;
int MinuteOff2_3 = 00;

int HourOn3_1 = 8;
int MinuteOn3_1 = 00;
int HourOff3_1 = 20;
int MinuteOff3_1 = 00;

int HourOn3_2 = 8;
int MinuteOn3_2 = 00;
int HourOff3_2 = 20;
int MinuteOff3_2 = 00;

int HourOn3_3 = 8;
int MinuteOn3_3 = 00;
int HourOff3_3 = 20;
int MinuteOff3_3 = 00;

int HourOn4_1 = 8;
int MinuteOn4_1 = 00;
int HourOff4_1 = 20;
int MinuteOff4_1 = 00;

int HourOn4_2 = 8;
int MinuteOn4_2 = 00;
int HourOff4_2 = 20;
int MinuteOff4_2 = 00;

int HourOn4_3 = 8;
int MinuteOn4_3 = 00;
int HourOff4_3 = 20;
int MinuteOff4_3 = 00;

int HourOn5_1 = 8;
int MinuteOn5_1 = 00;
int HourOff5_1 = 20;
int MinuteOff5_1 = 00;

int HourOn5_2 = 8;
int MinuteOn5_2 = 00;
int HourOff5_2 = 20;
int MinuteOff5_2 = 00;

int HourOn5_3 = 8;
int MinuteOn5_3 = 00;
int HourOff5_3 = 20;
int MinuteOff5_3 = 00;

int HourOn6_1 = 8;
int MinuteOn6_1 = 00;
int HourOff6_1 = 20;
int MinuteOff6_1 = 00;

int HourOn6_2 = 8;
int MinuteOn6_2 = 00;
int HourOff6_2 = 20;
int MinuteOff6_2 = 00;

int HourOn6_3 = 8;
int MinuteOn6_3 = 00;
int HourOff6_3 = 20;
int MinuteOff6_3 = 00;

int HourOn7_1 = 8;
int MinuteOn7_1 = 00;
int HourOff7_1 = 20;
int MinuteOff7_1 = 00;

int HourOn7_2 = 8;
int MinuteOn7_2 = 00;
int HourOff7_2 = 20;
int MinuteOff7_2 = 00;

int HourOn7_3 = 8;
int MinuteOn7_3 = 00;
int HourOff7_3 = 20;
int MinuteOff7_3 = 00;

int HourOn8_1 = 8;
int MinuteOn8_1 = 00;
int HourOff8_1 = 20;
int MinuteOff8_1 = 00;

int HourOn8_2 = 8;
int MinuteOn8_2 = 00;
int HourOff8_2 = 20;
int MinuteOff8_2 = 00;

int HourOn8_3 = 8;
int MinuteOn8_3 = 00;
int HourOff8_3 = 20;
int MinuteOff8_3 = 00;

int HourOn9_1 = 8;
int MinuteOn9_1 = 00;
int HourOff9_1 = 20;
int MinuteOff9_1 = 00;

int HourOn9_2 = 8;
int MinuteOn9_2 = 00;
int HourOff9_2 = 20;
int MinuteOff9_2 = 00;

int HourOn9_3 = 8;
int MinuteOn9_3 = 00;
int HourOff9_3 = 20;
int MinuteOff9_3 = 00;

int HourOn10_1 = 8;
int MinuteOn10_1 = 00;
int HourOff10_1 = 20;
int MinuteOff10_1 = 00;

int HourOn10_2 = 8;
int MinuteOn10_2 = 00;
int HourOff10_2 = 20;
int MinuteOff10_2 = 00;

int HourOn10_3 = 8;
int MinuteOn10_3 = 00;
int HourOff10_3 = 20;
int MinuteOff10_3 = 00;

int HourFrom1_2 = 00;
int HourFrom2_2 = 00;
int HourFrom3_2 = 00;
int HourFrom4_2 = 00;
int HourFrom5_2 = 00;
int HourFrom6_2 = 00;
int HourFrom7_2 = 00;
int HourFrom8_2 = 00;
int HourFrom9_2 = 00;
int HourFrom10_2 = 00;

int HourFrom1_3 = 00;
int HourFrom2_3 = 00;
int HourFrom3_3 = 00;
int HourFrom4_3 = 00;
int HourFrom5_3 = 00;
int HourFrom6_3 = 00;
int HourFrom7_3 = 00;
int HourFrom8_3 = 00;
int HourFrom9_3 = 00;
int HourFrom10_3 = 00;

int MinuteFrom1_2 = 00;
int MinuteFrom2_2 = 00;
int MinuteFrom3_2 = 00;
int MinuteFrom4_2 = 00;
int MinuteFrom5_2 = 00;
int MinuteFrom6_2 = 00;
int MinuteFrom7_2 = 00;
int MinuteFrom8_2 = 00;
int MinuteFrom9_2 = 00;
int MinuteFrom10_2 = 00;

int MinuteFrom1_3 = 00;
int MinuteFrom2_3 = 00;
int MinuteFrom3_3 = 00;
int MinuteFrom4_3 = 00;
int MinuteFrom5_3 = 00;
int MinuteFrom6_3 = 00;
int MinuteFrom7_3 = 00;
int MinuteFrom8_3 = 00;
int MinuteFrom9_3 = 00;
int MinuteFrom10_3 = 00;

int date1_2 = 10;
int date2_2 = 10;
int date3_2 = 10;
int date4_2 = 10;
int date5_2 = 10;
int date6_2 = 10;
int date7_2 = 10;
int date8_2 = 10;
int date9_2 = 10;
int date10_2 = 10;

int date1_3 = 10;
int date2_3 = 10;
int date3_3 = 10;
int date4_3 = 10;
int date5_3 = 10;
int date6_3 = 10;
int date7_3 = 10;
int date8_3 = 10;
int date9_3 = 10;
int date10_3 = 10;

int month1_2 = 12;
int month2_2 = 12;
int month3_2 = 12;
int month4_2 = 12;
int month5_2 = 12;
int month6_2 = 12;
int month7_2 = 12;
int month8_2 = 12;
int month9_2 = 12;
int month10_2 = 12;

int month1_3 = 12;
int month2_3 = 12;
int month3_3 = 12;
int month4_3 = 12;
int month5_3 = 12;
int month6_3 = 12;
int month7_3 = 12;
int month8_3 = 12;
int month9_3 = 12;
int month10_3 = 12;

int year1_2 = 2018;
int year2_2 = 2018;
int year3_2 = 2018;
int year4_2 = 2018;
int year5_2 = 2018;
int year6_2 = 2018;
int year7_2 = 2018;
int year8_2 = 2018;
int year9_2 = 2018;
int year10_2 = 2018;

int year1_3 = 2018;
int year2_3 = 2018;
int year3_3 = 2018;
int year4_3 = 2018;
int year5_3 = 2018;
int year6_3 = 2018;
int year7_3 = 2018;
int year8_3 = 2018;
int year9_3 = 2018;
int year10_3 = 2018;

int light1_1 = 0;
int light2_1 = 0;
int light3_1 = 0;
int light4_1 = 0;
int light5_1 = 0;
int light6_1 = 0;
int light7_1 = 0;
int light8_1 = 0;
int light9_1 = 0;
int light10_1 = 0;

int light1_2 = 0;
int light2_2 = 0;
int light3_2 = 0;
int light4_2 = 0;
int light5_2 = 0;
int light6_2 = 0;
int light7_2 = 0;
int light8_2 = 0;
int light9_2 = 0;
int light10_2 = 0;

int light1_3 = 0;
int light2_3 = 0;
int light3_3 = 0;
int light4_3 = 0;
int light5_3 = 0;
int light6_3 = 0;
int light7_3 = 0;
int light8_3 = 0;
int light9_3 = 0;
int light10_3 = 0;

int dark1_1 = 0;
int dark2_1 = 0;
int dark3_1 = 0;
int dark4_1 = 0;
int dark5_1 = 0;
int dark6_1 = 0;
int dark7_1 = 0;
int dark8_1 = 0;
int dark9_1 = 0;
int dark10_1 = 0;

int dark1_2 = 0;
int dark2_2 = 0;
int dark3_2 = 0;
int dark4_2 = 0;
int dark5_2 = 0;
int dark6_2 = 0;
int dark7_2 = 0;
int dark8_2 = 0;
int dark9_2 = 0;
int dark10_2 = 0;

int dark1_3 = 0;
int dark2_3 = 0;
int dark3_3 = 0;
int dark4_3 = 0;
int dark5_3 = 0;
int dark6_3 = 0;
int dark7_3 = 0;
int dark8_3 = 0;
int dark9_3 = 0;
int dark10_3 = 0;

// Digital In-Out
int DIn1 = 2;  // PIR1
int DOut1 = 3; // LED1

int DIn2 = 4;  // PIR2
int DOut2 = 5; // LED2

int DIn3 = 6;  // PIR3
int DOut3 = 7; // LED3

int DIn4 = 8;  // PIR4
int DOut4 = 9; // LED4

int DIn5 = 10;  // PIR5
int DOut5 = 11; // LED5

int DIn6 = 12;  // PIR6
int DOut6 = 13; // LED6

int DIn7 = 22;  // PIR7
int DOut7 = 23; // LED7

int DIn8 = 24;  // PIR8
int DOut8 = 25; // LED8

int DIn9 = 26;  // PIR9
int DOut9 = 27; // LED9

int DIn10 = 28;  // PIR10
int DOut10 = 29; // LED10

// Global variables
int LightFlag1 = 0;
int LightFlag2 = 0;
int LightFlag3 = 0;
int LightFlag4 = 0;
int LightFlag5 = 0;
int LightFlag6 = 0;
int LightFlag7 = 0;
int LightFlag8 = 0;
int LightFlag9 = 0;
int LightFlag10 = 0;

int TimeSet = 0;
int LightSet1 = 0;
int LightSet2 = 0;
int LightSet3 = 0;
int LightSet4 = 0;
int LightSet5 = 0;
int LightSet6 = 0;
int LightSet7 = 0;
int LightSet8 = 0;
int LightSet9 = 0;
int LightSet10 = 0;
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
  pinMode(DIn1, INPUT);    // PIR1
  pinMode(DOut1, OUTPUT);  // LED1
  pinMode(DIn2, INPUT);    // PIR2
  pinMode(DOut2, OUTPUT);  // LED2
  pinMode(DIn3, INPUT);    // PIR3
  pinMode(DOut3, OUTPUT);  // LED3
  pinMode(DIn4, INPUT);    // PIR4
  pinMode(DOut4, OUTPUT);  // LED4
  pinMode(DIn5, INPUT);    // PIR5
  pinMode(DOut5, OUTPUT);  // LED5
  pinMode(DIn6, INPUT);    // PIR6
  pinMode(DOut6, OUTPUT);  // LED6
  pinMode(DIn7, INPUT);    // PIR7
  pinMode(DOut7, OUTPUT);  // LED7
  pinMode(DIn8, INPUT);    // PIR8
  pinMode(DOut8, OUTPUT);  // LED8
  pinMode(DIn9, INPUT);    // PIR9
  pinMode(DOut9, OUTPUT);  // LED9
  pinMode(DIn10, INPUT);   // PIR10
  pinMode(DOut10, OUTPUT); // LED10

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
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    //Box1
    HourOn1_1 = getInt(lightIn1.substring(0, 2));
    MinuteOn1_1 = getInt(lightIn1.substring(2, 4));
    HourOff1_1 = getInt(lightIn1.substring(4, 6));
    MinuteOff1_1 = getInt(lightIn1.substring(6, 8));

    //Box2
    HourOn2_1 = getInt(lightIn1.substring(8, 10));
    MinuteOn2_1 = getInt(lightIn1.substring(10, 12));
    HourOff2_1 = getInt(lightIn1.substring(12, 14));
    MinuteOff2_1 = getInt(lightIn1.substring(14, 16));

    //Box3
    HourOn3_1 = getInt(lightIn1.substring(16, 18));
    MinuteOn3_1 = getInt(lightIn1.substring(18, 20));
    HourOff3_1 = getInt(lightIn1.substring(20, 22));
    MinuteOff3_1 = getInt(lightIn1.substring(22, 24));

    //Box4
    HourOn4_1 = getInt(lightIn1.substring(24, 26));
    MinuteOn4_1 = getInt(lightIn1.substring(26, 28));
    HourOff4_1 = getInt(lightIn1.substring(28, 30));
    MinuteOff4_1 = getInt(lightIn1.substring(30, 32));

    //Box5
    HourOn5_1 = getInt(lightIn1.substring(32, 34));
    MinuteOn5_1 = getInt(lightIn1.substring(34, 36));
    HourOff5_1 = getInt(lightIn1.substring(36, 38));
    MinuteOff5_1 = getInt(lightIn1.substring(38, 40));

    LightSet1 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 0)
  {
    lightIn1 = Serial.readString();
    //Box6
    HourOn6_1 = getInt(lightIn1.substring(0, 2));
    MinuteOn6_1 = getInt(lightIn1.substring(2, 4));
    HourOff6_1 = getInt(lightIn1.substring(4, 6));
    MinuteOff6_1 = getInt(lightIn1.substring(6, 8));

    //Box7
    HourOn7_1 = getInt(lightIn1.substring(8, 10));
    MinuteOn7_1 = getInt(lightIn1.substring(10, 12));
    HourOff7_1 = getInt(lightIn1.substring(12, 14));
    MinuteOff7_1 = getInt(lightIn1.substring(14, 16));

    //Box8
    HourOn8_1 = getInt(lightIn1.substring(16, 18));
    MinuteOn8_1 = getInt(lightIn1.substring(18, 20));
    HourOff8_1 = getInt(lightIn1.substring(20, 22));
    MinuteOff8_1 = getInt(lightIn1.substring(22, 24));

    //Box9
    HourOn9_1 = getInt(lightIn1.substring(24, 26));
    MinuteOn9_1 = getInt(lightIn1.substring(26, 28));
    HourOff9_1 = getInt(lightIn1.substring(28, 30));
    MinuteOff9_1 = getInt(lightIn1.substring(30, 32));

    //Box10
    HourOn10_1 = getInt(lightIn1.substring(32, 34));
    MinuteOn10_1 = getInt(lightIn1.substring(34, 36));
    HourOff10_1 = getInt(lightIn1.substring(36, 38));
    MinuteOff10_1 = getInt(lightIn1.substring(38, 40));

    dark1_1 = getInt(lightIn1.substring(40, 41));
    light1_1 = getInt(lightIn1.substring(41, 42));
    dark2_1 = getInt(lightIn1.substring(42, 43));
    light2_1 = getInt(lightIn1.substring(43, 44));
    dark3_1 = getInt(lightIn1.substring(44, 45));
    light3_1 = getInt(lightIn1.substring(45, 46));
    dark4_1 = getInt(lightIn1.substring(46, 47));
    light4_1 = getInt(lightIn1.substring(47, 48));
    dark5_1 = getInt(lightIn1.substring(48, 49));
    light5_1 = getInt(lightIn1.substring(49, 50));
    dark6_1 = getInt(lightIn1.substring(50, 51));
    light6_1 = getInt(lightIn1.substring(51, 52));
    dark7_1 = getInt(lightIn1.substring(52, 53));
    light7_1 = getInt(lightIn1.substring(53, 54));
    dark8_1 = getInt(lightIn1.substring(54, 55));
    light8_1 = getInt(lightIn1.substring(55, 56));
    dark9_1 = getInt(lightIn1.substring(56, 57));
    light9_1 = getInt(lightIn1.substring(57, 58));
    dark10_1 = getInt(lightIn1.substring(58, 59));
    light10_1 = getInt(lightIn1.substring(59, 60));

    Serial.println(lightIn1);
    LightSet2 = 1;
  }

  // Phase2
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 0)
  {
    lightIn2 = Serial.readString();
    //Box1
    HourOn1_2 = getInt(lightIn2.substring(0, 2));
    MinuteOn1_2 = getInt(lightIn2.substring(2, 4));
    HourOff1_2 = getInt(lightIn2.substring(4, 6));
    MinuteOff1_2 = getInt(lightIn2.substring(6, 8));

    //Box2
    HourOn2_2 = getInt(lightIn2.substring(8, 10));
    MinuteOn2_2 = getInt(lightIn2.substring(10, 12));
    HourOff2_2 = getInt(lightIn2.substring(12, 14));
    MinuteOff2_2 = getInt(lightIn2.substring(14, 16));

    //Box3
    HourOn3_2 = getInt(lightIn2.substring(16, 18));
    MinuteOn3_2 = getInt(lightIn2.substring(18, 20));
    HourOff3_2 = getInt(lightIn2.substring(20, 22));
    MinuteOff3_2 = getInt(lightIn2.substring(22, 24));

    //Box4
    HourOn4_2 = getInt(lightIn2.substring(24, 26));
    MinuteOn4_2 = getInt(lightIn2.substring(26, 28));
    HourOff4_2 = getInt(lightIn2.substring(28, 30));
    MinuteOff4_2 = getInt(lightIn2.substring(30, 32));

    //Box5
    HourOn5_2 = getInt(lightIn2.substring(32, 34));
    MinuteOn5_2 = getInt(lightIn2.substring(34, 36));
    HourOff5_2 = getInt(lightIn2.substring(36, 38));
    MinuteOff5_2 = getInt(lightIn2.substring(38, 40));

    Serial.println(lightIn2);
    LightSet3 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 0)
  {
    lightIn2 = Serial.readString();

    //Box6
    HourOn6_2 = getInt(lightIn2.substring(0, 2));
    MinuteOn6_2 = getInt(lightIn2.substring(2, 4));
    HourOff6_2 = getInt(lightIn2.substring(4, 6));
    MinuteOff6_2 = getInt(lightIn2.substring(6, 8));

    //Box7
    HourOn7_2 = getInt(lightIn2.substring(8, 10));
    MinuteOn7_2 = getInt(lightIn2.substring(10, 12));
    HourOff7_2 = getInt(lightIn2.substring(12, 14));
    MinuteOff7_2 = getInt(lightIn2.substring(14, 16));

    //Box8
    HourOn8_2 = getInt(lightIn2.substring(16, 18));
    MinuteOn8_2 = getInt(lightIn2.substring(18, 20));
    HourOff8_2 = getInt(lightIn2.substring(20, 22));
    MinuteOff8_2 = getInt(lightIn2.substring(22, 24));

    //Box9
    HourOn9_2 = getInt(lightIn2.substring(24, 26));
    MinuteOn9_2 = getInt(lightIn2.substring(26, 28));
    HourOff9_2 = getInt(lightIn2.substring(28, 30));
    MinuteOff9_2 = getInt(lightIn2.substring(30, 32));

    //Box10
    HourOn10_2 = getInt(lightIn2.substring(32, 34));
    MinuteOn10_2 = getInt(lightIn2.substring(34, 36));
    HourOff10_2 = getInt(lightIn2.substring(36, 38));
    MinuteOff10_2 = getInt(lightIn2.substring(38, 40));

    dark1_2 = getInt(lightIn2.substring(40, 41));
    light1_2 = getInt(lightIn2.substring(41, 42));
    dark2_2 = getInt(lightIn2.substring(42, 43));
    light2_2 = getInt(lightIn2.substring(43, 44));
    dark3_2 = getInt(lightIn2.substring(44, 45));
    light3_2 = getInt(lightIn2.substring(45, 46));
    dark4_2 = getInt(lightIn2.substring(46, 47));
    light4_2 = getInt(lightIn2.substring(47, 48));
    dark5_2 = getInt(lightIn2.substring(48, 49));
    light5_2 = getInt(lightIn2.substring(49, 50));
    dark6_2 = getInt(lightIn2.substring(50, 51));
    light6_2 = getInt(lightIn2.substring(51, 52));
    dark7_2 = getInt(lightIn2.substring(52, 53));
    light7_2 = getInt(lightIn2.substring(53, 54));
    dark8_2 = getInt(lightIn2.substring(54, 55));
    light8_2 = getInt(lightIn2.substring(55, 56));
    dark9_2 = getInt(lightIn2.substring(56, 57));
    light9_2 = getInt(lightIn2.substring(57, 58));
    dark10_2 = getInt(lightIn2.substring(58, 59));
    light10_2 = getInt(lightIn2.substring(59, 60));

    Serial.println(lightIn2);
    LightSet4 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 0)
  {
    lightIn2 = Serial.readString();

    date1_2 = getInt(lightIn2.substring(0, 2));
    month1_2 = getInt(lightIn2.substring(2, 4));
    year1_2 = getInt(lightIn2.substring(4, 8));
    date2_2 = getInt(lightIn2.substring(8, 10));
    month2_2 = getInt(lightIn2.substring(10, 12));
    year2_2 = getInt(lightIn2.substring(12, 16));
    date3_2 = getInt(lightIn2.substring(16, 18));
    month3_2 = getInt(lightIn2.substring(18, 20));
    year3_2 = getInt(lightIn2.substring(20, 24));
    date4_2 = getInt(lightIn2.substring(24, 26));
    month4_2 = getInt(lightIn2.substring(26, 28));
    year4_2 = getInt(lightIn2.substring(28, 32));
    date5_2 = getInt(lightIn2.substring(32, 34));
    month5_2 = getInt(lightIn2.substring(34, 36));
    year5_2 = getInt(lightIn2.substring(36, 40));
    HourFrom1_2 = getInt(lightIn2.substring(40, 42));
    MinuteFrom1_2 = getInt(lightIn2.substring(42, 44));
    HourFrom2_2 = getInt(lightIn2.substring(44, 46));
    MinuteFrom2_2 = getInt(lightIn2.substring(46, 48));
    HourFrom3_2 = getInt(lightIn2.substring(48, 50));
    MinuteFrom3_2 = getInt(lightIn2.substring(50, 52));
    HourFrom4_2 = getInt(lightIn2.substring(52, 54));
    MinuteFrom4_2 = getInt(lightIn2.substring(54, 56));
    HourFrom5_2 = getInt(lightIn2.substring(56, 58));
    MinuteFrom5_2 = getInt(lightIn2.substring(58, 60));

    Serial.println(lightIn2);
    LightSet5 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 0)
  {
    lightIn2 = Serial.readString();

    date6_2 = getInt(lightIn2.substring(0, 2));
    month6_2 = getInt(lightIn2.substring(2, 4));
    year6_2 = getInt(lightIn2.substring(4, 8));
    date7_2 = getInt(lightIn2.substring(8, 10));
    month7_2 = getInt(lightIn2.substring(10, 12));
    year7_2 = getInt(lightIn2.substring(12, 16));
    date8_2 = getInt(lightIn2.substring(16, 18));
    month8_2 = getInt(lightIn2.substring(18, 20));
    year8_2 = getInt(lightIn2.substring(20, 24));
    date9_2 = getInt(lightIn2.substring(24, 26));
    month9_2 = getInt(lightIn2.substring(26, 28));
    year9_2 = getInt(lightIn2.substring(28, 32));
    date10_2 = getInt(lightIn2.substring(32, 34));
    month10_2 = getInt(lightIn2.substring(34, 36));
    year10_2 = getInt(lightIn2.substring(36, 40));
    HourFrom6_2 = getInt(lightIn2.substring(40, 42));
    MinuteFrom6_2 = getInt(lightIn2.substring(42, 44));
    HourFrom7_2 = getInt(lightIn2.substring(44, 46));
    MinuteFrom7_2 = getInt(lightIn2.substring(46, 48));
    HourFrom8_2 = getInt(lightIn2.substring(48, 50));
    MinuteFrom8_2 = getInt(lightIn2.substring(50, 52));
    HourFrom9_2 = getInt(lightIn2.substring(52, 54));
    MinuteFrom9_2 = getInt(lightIn2.substring(54, 56));
    HourFrom10_2 = getInt(lightIn2.substring(56, 58));
    MinuteFrom10_2 = getInt(lightIn2.substring(58, 60));

    Serial.println(lightIn2);
    LightSet6 = 1;
  }

  // Phase3
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 0)
  {
    lightIn3 = Serial.readString();
    //Box1
    HourOn1_3 = getInt(lightIn3.substring(0, 2));
    MinuteOn1_3 = getInt(lightIn3.substring(2, 4));
    HourOff1_3 = getInt(lightIn3.substring(4, 6));
    MinuteOff1_3 = getInt(lightIn3.substring(6, 8));

    //Box2
    HourOn2_3 = getInt(lightIn3.substring(8, 10));
    MinuteOn2_3 = getInt(lightIn3.substring(10, 12));
    HourOff2_3 = getInt(lightIn3.substring(12, 14));
    MinuteOff2_3 = getInt(lightIn3.substring(14, 16));

    //Box3
    HourOn3_3 = getInt(lightIn3.substring(16, 18));
    MinuteOn3_3 = getInt(lightIn3.substring(18, 20));
    HourOff3_3 = getInt(lightIn3.substring(20, 22));
    MinuteOff3_3 = getInt(lightIn3.substring(22, 24));

    //Box4
    HourOn4_3 = getInt(lightIn3.substring(24, 26));
    MinuteOn4_3 = getInt(lightIn3.substring(26, 28));
    HourOff4_3 = getInt(lightIn3.substring(28, 30));
    MinuteOff4_3 = getInt(lightIn3.substring(30, 32));

    //Box5
    HourOn5_3 = getInt(lightIn3.substring(32, 34));
    MinuteOn5_3 = getInt(lightIn3.substring(34, 36));
    HourOff5_3 = getInt(lightIn3.substring(36, 38));
    MinuteOff5_3 = getInt(lightIn3.substring(38, 40));

    Serial.println(lightIn3);
    LightSet7 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 0)
  {
    lightIn3 = Serial.readString();

    //Box6
    HourOn6_3 = getInt(lightIn3.substring(0, 2));
    MinuteOn6_3 = getInt(lightIn3.substring(2, 4));
    HourOff6_3 = getInt(lightIn3.substring(4, 6));
    MinuteOff6_3 = getInt(lightIn3.substring(6, 8));

    //Box7
    HourOn7_3 = getInt(lightIn3.substring(8, 10));
    MinuteOn7_3 = getInt(lightIn3.substring(10, 12));
    HourOff7_3 = getInt(lightIn3.substring(12, 14));
    MinuteOff7_3 = getInt(lightIn3.substring(14, 16));

    //Box8
    HourOn8_3 = getInt(lightIn3.substring(16, 18));
    MinuteOn8_3 = getInt(lightIn3.substring(18, 20));
    HourOff8_3 = getInt(lightIn3.substring(20, 22));
    MinuteOff8_3 = getInt(lightIn3.substring(22, 24));

    //Box9
    HourOn9_3 = getInt(lightIn3.substring(24, 26));
    MinuteOn9_3 = getInt(lightIn3.substring(26, 28));
    HourOff9_3 = getInt(lightIn3.substring(28, 30));
    MinuteOff9_3 = getInt(lightIn3.substring(30, 32));

    //Box10
    HourOn10_3 = getInt(lightIn3.substring(32, 34));
    MinuteOn10_3 = getInt(lightIn3.substring(34, 36));
    HourOff10_3 = getInt(lightIn3.substring(36, 38));
    MinuteOff10_3 = getInt(lightIn3.substring(38, 40));

    dark1_3 = getInt(lightIn3.substring(40, 41));
    light1_3 = getInt(lightIn3.substring(41, 42));
    dark2_3 = getInt(lightIn3.substring(42, 43));
    light2_3 = getInt(lightIn3.substring(43, 44));
    dark3_3 = getInt(lightIn3.substring(44, 45));
    light3_3 = getInt(lightIn3.substring(45, 46));
    dark4_3 = getInt(lightIn3.substring(46, 47));
    light4_3 = getInt(lightIn3.substring(47, 48));
    dark5_3 = getInt(lightIn3.substring(48, 49));
    light5_3 = getInt(lightIn3.substring(49, 50));
    dark6_3 = getInt(lightIn3.substring(50, 51));
    light6_3 = getInt(lightIn3.substring(51, 52));
    dark7_3 = getInt(lightIn3.substring(52, 53));
    light7_3 = getInt(lightIn3.substring(53, 54));
    dark8_3 = getInt(lightIn3.substring(54, 55));
    light8_3 = getInt(lightIn3.substring(55, 56));
    dark9_3 = getInt(lightIn3.substring(56, 57));
    light9_3 = getInt(lightIn3.substring(57, 58));
    dark10_3 = getInt(lightIn3.substring(58, 59));
    light10_3 = getInt(lightIn3.substring(59, 60));

    Serial.println(lightIn3);
    LightSet8 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 0)
  {
    lightIn3 = Serial.readString();

    date1_3 = getInt(lightIn3.substring(0, 2));
    month1_3 = getInt(lightIn3.substring(2, 4));
    year1_3 = getInt(lightIn3.substring(4, 8));
    date2_3 = getInt(lightIn3.substring(8, 10));
    month2_3 = getInt(lightIn3.substring(10, 12));
    year2_3 = getInt(lightIn3.substring(12, 16));
    date3_3 = getInt(lightIn3.substring(16, 18));
    month3_3 = getInt(lightIn3.substring(18, 20));
    year3_3 = getInt(lightIn3.substring(20, 24));
    date4_3 = getInt(lightIn3.substring(24, 26));
    month4_3 = getInt(lightIn3.substring(26, 28));
    year4_3 = getInt(lightIn3.substring(28, 32));
    date5_3 = getInt(lightIn3.substring(32, 34));
    month5_3 = getInt(lightIn3.substring(34, 36));
    year5_3 = getInt(lightIn3.substring(36, 40));
    HourFrom1_3 = getInt(lightIn3.substring(40, 42));
    MinuteFrom1_3 = getInt(lightIn3.substring(42, 44));
    HourFrom2_3 = getInt(lightIn3.substring(44, 46));
    MinuteFrom2_3 = getInt(lightIn3.substring(46, 48));
    HourFrom3_3 = getInt(lightIn3.substring(48, 50));
    MinuteFrom3_3 = getInt(lightIn3.substring(50, 52));
    HourFrom4_3 = getInt(lightIn3.substring(52, 54));
    MinuteFrom4_3 = getInt(lightIn3.substring(54, 56));
    HourFrom5_3 = getInt(lightIn3.substring(56, 58));
    MinuteFrom5_3 = getInt(lightIn3.substring(58, 60));

    Serial.println(lightIn3);
    LightSet9 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 0)
  {
    lightIn3 = Serial.readString();

    date6_3 = getInt(lightIn3.substring(0, 2));
    month6_3 = getInt(lightIn3.substring(2, 4));
    year6_3 = getInt(lightIn3.substring(4, 8));
    date7_3 = getInt(lightIn3.substring(8, 10));
    month7_3 = getInt(lightIn3.substring(10, 12));
    year7_3 = getInt(lightIn3.substring(12, 16));
    date8_3 = getInt(lightIn3.substring(16, 18));
    month8_3 = getInt(lightIn3.substring(18, 20));
    year8_3 = getInt(lightIn3.substring(20, 24));
    date9_3 = getInt(lightIn3.substring(24, 26));
    month9_3 = getInt(lightIn3.substring(26, 28));
    year9_3 = getInt(lightIn3.substring(28, 32));
    date10_3 = getInt(lightIn3.substring(32, 34));
    month10_3 = getInt(lightIn3.substring(34, 36));
    year10_3 = getInt(lightIn3.substring(36, 40));
    HourFrom6_3 = getInt(lightIn3.substring(40, 42));
    MinuteFrom6_3 = getInt(lightIn3.substring(42, 44));
    HourFrom7_3 = getInt(lightIn3.substring(44, 46));
    MinuteFrom7_3 = getInt(lightIn3.substring(46, 48));
    HourFrom8_3 = getInt(lightIn3.substring(48, 50));
    MinuteFrom8_3 = getInt(lightIn3.substring(50, 52));
    HourFrom9_3 = getInt(lightIn3.substring(52, 54));
    MinuteFrom9_3 = getInt(lightIn3.substring(54, 56));
    HourFrom10_3 = getInt(lightIn3.substring(56, 58));
    MinuteFrom10_3 = getInt(lightIn3.substring(58, 60));

    Serial.println(lightIn3);
    LightSet10 = 1;
  }

  // Begin to print the headers and set light flag
  if (InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1)
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

    if (phase1_1 == 0 && clock.dayOfMonth == date1_2 && clock.month == month1_2 && clock.year + 2000 == year1_2 && clock.hour * 60 + clock.minute >= HourFrom1_2 * 60 + MinuteFrom1_2)
    {
      phase1_1 = 1;
    }

    if (phase2_1 == 0 && clock.dayOfMonth == date2_2 && clock.month == month2_2 && clock.year + 2000 == year2_2 && clock.hour * 60 + clock.minute >= HourFrom2_2 * 60 + MinuteFrom2_2)
    {
      phase2_1 = 1;
    }

    if (phase3_1 == 0 && clock.dayOfMonth == date3_2 && clock.month == month3_2 && clock.year + 2000 == year3_2 && clock.hour * 60 + clock.minute >= HourFrom3_2 * 60 + MinuteFrom3_2)
    {
      phase3_1 = 1;
    }

    if (phase4_1 == 0 && clock.dayOfMonth == date4_2 && clock.month == month4_2 && clock.year + 2000 == year4_2 && clock.hour * 60 + clock.minute >= HourFrom4_2 * 60 + MinuteFrom4_2)
    {
      phase4_1 = 1;
    }

    if (phase5_1 == 0 && clock.dayOfMonth == date5_2 && clock.month == month5_2 && clock.year + 2000 == year5_2 && clock.hour * 60 + clock.minute >= HourFrom5_2 * 60 + MinuteFrom5_2)
    {
      phase5_1 = 1;
    }

    if (phase6_1 == 0 && clock.dayOfMonth == date6_2 && clock.month == month6_2 && clock.year + 2000 == year6_2 && clock.hour * 60 + clock.minute >= HourFrom6_2 * 60 + MinuteFrom6_2)
    {
      phase6_1 = 1;
    }

    if (phase7_1 == 0 && clock.dayOfMonth == date7_2 && clock.month == month7_2 && clock.year + 2000 == year7_2 && clock.hour * 60 + clock.minute >= HourFrom7_2 * 60 + MinuteFrom7_2)
    {
      phase7_1 = 1;
    }

    if (phase8_1 == 0 && clock.dayOfMonth == date8_2 && clock.month == month8_2 && clock.year + 2000 == year8_2 && clock.hour * 60 + clock.minute >= HourFrom8_2 * 60 + MinuteFrom8_2)
    {
      phase8_1 = 1;
    }

    if (phase9_1 == 0 && clock.dayOfMonth == date9_2 && clock.month == month9_2 && clock.year + 2000 == year9_2 && clock.hour * 60 + clock.minute >= HourFrom9_2 * 60 + MinuteFrom1_2)
    {
      phase9_1 = 1;
    }

    if (phase10_1 == 0 && clock.dayOfMonth == date10_2 && clock.month == month10_2 && clock.year + 2000 == year10_2 && clock.hour * 60 + clock.minute >= HourFrom10_2 * 60 + MinuteFrom10_2)
    {
      phase10_1 = 1;
    }

    // End phase 2 when

    if (phase1_2 == 0 && clock.dayOfMonth == date1_3 && clock.month == month1_3 && clock.year + 2000 == year1_3 && clock.hour * 60 + clock.minute >= HourFrom1_3 * 60 + MinuteFrom1_3)
    {
      phase1_2 = 1;
    }
    if (phase2_2 == 0 && clock.dayOfMonth == date2_3 && clock.month == month2_3 && clock.year + 2000 == year2_3 && clock.hour * 60 + clock.minute >= HourFrom2_3 * 60 + MinuteFrom2_3)
    {
      phase2_2 = 1;
    }
    if (phase3_2 == 0 && clock.dayOfMonth == date3_3 && clock.month == month3_3 && clock.year + 2000 == year3_3 && clock.hour * 60 + clock.minute >= HourFrom3_3 * 60 + MinuteFrom3_3)
    {
      phase3_2 = 1;
    }
    if (phase4_2 == 0 && clock.dayOfMonth == date4_3 && clock.month == month4_3 && clock.year + 2000 == year4_3 && clock.hour * 60 + clock.minute >= HourFrom4_3 * 60 + MinuteFrom4_3)
    {
      phase4_2 = 1;
    }
    if (phase5_2 == 0 && clock.dayOfMonth == date5_3 && clock.month == month5_3 && clock.year + 2000 == year5_3 && clock.hour * 60 + clock.minute >= HourFrom5_3 * 60 + MinuteFrom5_3)
    {
      phase5_2 = 1;
    }
    if (phase6_2 == 0 && clock.dayOfMonth == date6_3 && clock.month == month6_3 && clock.year + 2000 == year6_3 && clock.hour * 60 + clock.minute >= HourFrom6_3 * 60 + MinuteFrom6_3)
    {
      phase6_2 = 1;
    }
    if (phase7_2 == 0 && clock.dayOfMonth == date7_3 && clock.month == month7_3 && clock.year + 2000 == year7_3 && clock.hour * 60 + clock.minute >= HourFrom7_3 * 60 + MinuteFrom7_3)
    {
      phase7_2 = 1;
    }
    if (phase8_2 == 0 && clock.dayOfMonth == date8_3 && clock.month == month8_3 && clock.year + 2000 == year8_3 && clock.hour * 60 + clock.minute >= HourFrom8_3 * 60 + MinuteFrom8_3)
    {
      phase8_2 = 1;
    }
    if (phase9_2 == 0 && clock.dayOfMonth == date9_3 && clock.month == month9_3 && clock.year + 2000 == year9_3 && clock.hour * 60 + clock.minute >= HourFrom9_3 * 60 + MinuteFrom9_3)
    {
      phase9_2 = 1;
    }
    if (phase10_2 == 0 && clock.dayOfMonth == date10_3 && clock.month == month10_3 && clock.year + 2000 == year10_3 && clock.hour * 60 + clock.minute >= HourFrom10_3 * 60 + MinuteFrom10_3)
    {
      phase10_2 = 1;
    }

    //////////For Phase1
    //Box1
    if (phase1_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn1_1 * 60 + MinuteOn1_1 && clock.hour * 60 + clock.minute < HourOff1_1 * 60 + MinuteOff1_1)
      {
        if (light1_1 == 0 && dark1_1 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
        if (light1_1 == 0 && dark1_1 == 1)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_1 == 1 && dark1_1 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
      }
      else
      {
        if (light1_1 == 0 && dark1_1 == 0)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_1 == 0 && dark1_1 == 1)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_1 == 1 && dark1_1 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
      }
    }

    //Box2
    if (phase2_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn2_1 * 60 + MinuteOn2_1 && clock.hour * 60 + clock.minute < HourOff2_1 * 60 + MinuteOff2_1)
      {
        if (light2_1 == 0 && dark2_1 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
        if (light2_1 == 0 && dark2_1 == 1)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_1 == 1 && dark2_1 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
      }
      else
      {
        if (light2_1 == 0 && dark2_1 == 0)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_1 == 0 && dark2_1 == 1)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_1 == 1 && dark2_1 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
      }
    }

    //Box3
    if (phase3_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn3_1 * 60 + MinuteOn3_1 && clock.hour * 60 + clock.minute < HourOff3_1 * 60 + MinuteOff3_1)
      {
        if (light3_1 == 0 && dark3_1 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
        if (light3_1 == 0 && dark3_1 == 1)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_1 == 1 && dark3_1 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
      }
      else
      {
        if (light3_1 == 0 && dark3_1 == 0)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_1 == 0 && dark3_1 == 1)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_1 == 1 && dark3_1 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
      }
    }
    //Box4
    if (phase4_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn4_1 * 60 + MinuteOn4_1 && clock.hour * 60 + clock.minute < HourOff4_1 * 60 + MinuteOff4_1)
      {
        if (light4_1 == 0 && dark4_1 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
        if (light4_1 == 0 && dark4_1 == 1)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_1 == 1 && dark4_1 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
      }
      else
      {
        if (light4_1 == 0 && dark4_1 == 0)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_1 == 0 && dark4_1 == 1)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_1 == 1 && dark4_1 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
      }
    }
    //Box5
    if (phase5_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn5_1 * 60 + MinuteOn5_1 && clock.hour * 60 + clock.minute < HourOff5_1 * 60 + MinuteOff5_1)
      {
        if (light5_1 == 0 && dark5_1 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
        if (light5_1 == 0 && dark5_1 == 1)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_1 == 1 && dark5_1 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
      }
      else
      {
        if (light5_1 == 0 && dark5_1 == 0)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_1 == 0 && dark5_1 == 1)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_1 == 1 && dark5_1 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
      }
    }
    //Box6
    if (phase6_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn6_1 * 60 + MinuteOn6_1 && clock.hour * 60 + clock.minute < HourOff6_1 * 60 + MinuteOff6_1)
      {
        if (light6_1 == 0 && dark6_1 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
        if (light6_1 == 0 && dark6_1 == 1)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_1 == 1 && dark6_1 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
      }
      else
      {
        if (light6_1 == 0 && dark6_1 == 0)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_1 == 0 && dark6_1 == 1)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_1 == 1 && dark6_1 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
      }
    }
    //Box7
    if (phase7_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn7_1 * 60 + MinuteOn7_1 && clock.hour * 60 + clock.minute < HourOff7_1 * 60 + MinuteOff7_1)
      {
        if (light7_1 == 0 && dark7_1 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
        if (light7_1 == 0 && dark7_1 == 1)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_1 == 1 && dark7_1 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
      }
      else
      {
        if (light7_1 == 0 && dark7_1 == 0)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_1 == 0 && dark7_1 == 1)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_1 == 1 && dark7_1 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
      }
    }
    //Box8
    if (phase8_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn8_1 * 60 + MinuteOn8_1 && clock.hour * 60 + clock.minute < HourOff8_1 * 60 + MinuteOff8_1)
      {
        if (light8_1 == 0 && dark8_1 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
        if (light8_1 == 0 && dark8_1 == 1)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_1 == 1 && dark8_1 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
      }
      else
      {
        if (light8_1 == 0 && dark8_1 == 0)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_1 == 0 && dark8_1 == 1)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_1 == 1 && dark8_1 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
      }
    }
    //Box9
    if (phase9_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn9_1 * 60 + MinuteOn9_1 && clock.hour * 60 + clock.minute < HourOff9_1 * 60 + MinuteOff9_1)
      {
        if (light9_1 == 0 && dark9_1 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
        if (light9_1 == 0 && dark9_1 == 1)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_1 == 1 && dark9_1 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
      }
      else
      {
        if (light9_1 == 0 && dark9_1 == 0)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_1 == 0 && dark9_1 == 1)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_1 == 1 && dark9_1 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
      }
    }
    //Box10
    if (phase10_1 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn10_1 * 60 + MinuteOn10_1 && clock.hour * 60 + clock.minute < HourOff10_1 * 60 + MinuteOff10_1)
      {
        if (light10_1 == 0 && dark10_1 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
        if (light10_1 == 0 && dark10_1 == 1)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_1 == 1 && dark10_1 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
      }
      else
      {
        if (light10_1 == 0 && dark10_1 == 0)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_1 == 0 && dark10_1 == 1)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_1 == 1 && dark10_1 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
      }
    }

    ///////For phase 2
    //Box1
    if (phase1_1 == 1 && phase1_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn1_2 * 60 + MinuteOn1_2 && clock.hour * 60 + clock.minute < HourOff1_2 * 60 + MinuteOff1_2)

      {
        if (light1_2 == 0 && dark1_2 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
        if (light1_2 == 0 && dark1_2 == 1)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_2 == 1 && dark1_2 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
      }
      else
      {
        if (light1_2 == 0 && dark1_2 == 0)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_2 == 0 && dark1_2 == 1)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_2 == 1 && dark1_2 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
      }
    }
    //Box2
    if (phase2_1 == 1 && phase2_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn2_2 * 60 + MinuteOn2_2 && clock.hour * 60 + clock.minute < HourOff2_2 * 60 + MinuteOff2_2)
      {
        if (light2_2 == 0 && dark2_2 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
        if (light2_2 == 0 && dark2_2 == 1)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_2 == 1 && dark2_2 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
      }
      else
      {
        if (light2_2 == 0 && dark2_2 == 0)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_2 == 0 && dark2_2 == 1)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_2 == 1 && dark2_2 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
      }
    }
    //Box3
    if (phase3_1 == 1 && phase3_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn3_2 * 60 + MinuteOn3_2 && clock.hour * 60 + clock.minute < HourOff3_2 * 60 + MinuteOff3_2)
      {
        if (light3_2 == 0 && dark3_2 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
        if (light3_2 == 0 && dark3_2 == 1)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_2 == 1 && dark3_2 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
      }
      else
      {
        if (light3_2 == 0 && dark3_2 == 0)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_2 == 0 && dark3_2 == 1)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_2 == 1 && dark3_2 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
      }
    }
    //Box4
    if (phase4_1 == 1 && phase4_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn4_2 * 60 + MinuteOn4_2 && clock.hour * 60 + clock.minute < HourOff4_2 * 60 + MinuteOff4_2)
      {
        if (light4_2 == 0 && dark4_2 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
        if (light4_2 == 0 && dark4_2 == 1)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_2 == 1 && dark4_2 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
      }
      else
      {
        if (light4_2 == 0 && dark4_2 == 0)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_2 == 0 && dark4_2 == 1)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_2 == 1 && dark4_2 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
      }
    }
    //Box5
    if (phase5_1 == 1 && phase5_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn5_2 * 60 + MinuteOn5_2 && clock.hour * 60 + clock.minute < HourOff5_2 * 60 + MinuteOff5_2)
      {
        if (light5_2 == 0 && dark5_2 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
        if (light5_2 == 0 && dark5_2 == 1)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_2 == 1 && dark5_2 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
      }
      else
      {
        if (light5_2 == 0 && dark5_2 == 0)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_2 == 0 && dark5_2 == 1)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_2 == 1 && dark5_2 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
      }
    }
    //Box6
    if (phase6_1 == 1 && phase6_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn6_2 * 60 + MinuteOn6_2 && clock.hour * 60 + clock.minute < HourOff6_2 * 60 + MinuteOff6_2)
      {
        if (light6_2 == 0 && dark6_2 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
        if (light6_2 == 0 && dark6_2 == 1)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_2 == 1 && dark6_2 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
      }
      else
      {
        if (light6_2 == 0 && dark6_2 == 0)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_2 == 0 && dark6_2 == 1)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_2 == 1 && dark6_2 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
      }
    }
    //Box7
    if (phase7_1 == 1 && phase7_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn7_2 * 60 + MinuteOn7_2 && clock.hour * 60 + clock.minute < HourOff7_2 * 60 + MinuteOff7_2)
      {
        if (light7_2 == 0 && dark7_2 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
        if (light7_2 == 0 && dark7_2 == 1)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_2 == 1 && dark7_2 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
      }
      else
      {
        if (light7_2 == 0 && dark7_2 == 0)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_2 == 0 && dark7_2 == 1)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_2 == 1 && dark7_2 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
      }
    }
    //Box8
    if (phase8_1 == 1 && phase8_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn8_2 * 60 + MinuteOn8_2 && clock.hour * 60 + clock.minute < HourOff8_2 * 60 + MinuteOff8_2)
      {
        if (light8_2 == 0 && dark8_2 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
        if (light8_2 == 0 && dark8_2 == 1)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_2 == 1 && dark8_2 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
      }
      else
      {
        if (light8_2 == 0 && dark8_2 == 0)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_2 == 0 && dark8_2 == 1)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_2 == 1 && dark8_2 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
      }
    }
    //Box9
    if (phase9_1 == 1 && phase9_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn9_2 * 60 + MinuteOn9_2 && clock.hour * 60 + clock.minute < HourOff9_2 * 60 + MinuteOff9_2)
      {
        if (light9_2 == 0 && dark9_2 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
        if (light9_2 == 0 && dark9_2 == 1)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_2 == 1 && dark9_2 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
      }
      else
      {
        if (light9_2 == 0 && dark9_2 == 0)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_2 == 0 && dark9_2 == 1)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_2 == 1 && dark9_2 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
      }
    }
    //Box10
    if (phase10_1 == 1 && phase10_2 == 0)
    {
      if (clock.hour * 60 + clock.minute >= HourOn10_2 * 60 + MinuteOn10_2 && clock.hour * 60 + clock.minute < HourOff10_2 * 60 + MinuteOff10_2)
      {
        if (light10_2 == 0 && dark10_2 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
        if (light10_2 == 0 && dark10_2 == 1)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_2 == 1 && dark10_2 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
      }
      else
      {
        if (light10_2 == 0 && dark10_2 == 0)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_2 == 0 && dark10_2 == 1)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_2 == 1 && dark10_2 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
      }
    }

    ///////For phase 3
    //Box1
    if (phase1_1 == 1 && phase1_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn1_3 * 60 + MinuteOn1_3 && clock.hour * 60 + clock.minute < HourOff1_3 * 60 + MinuteOff1_3)
      {
        if (light1_3 == 0 && dark1_3 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
        if (light1_3 == 0 && dark1_3 == 1)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_3 == 1 && dark1_3 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
      }
      else
      {
        if (light1_3 == 0 && dark1_3 == 0)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_3 == 0 && dark1_3 == 1)
        {
          digitalWrite(DOut1, LOW);
          LightFlag1 = 0;
        }
        if (light1_3 == 1 && dark1_3 == 0)
        {
          digitalWrite(DOut1, HIGH);
          LightFlag1 = 1;
        }
      }
    }
    //Box2
    if (phase2_1 == 1 && phase2_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn2_3 * 60 + MinuteOn2_3 && clock.hour * 60 + clock.minute < HourOff2_3 * 60 + MinuteOff2_3)
      {
        if (light2_3 == 0 && dark2_3 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
        if (light2_3 == 0 && dark2_3 == 1)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_3 == 1 && dark2_3 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
      }
      else
      {
        if (light2_3 == 0 && dark2_3 == 0)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_3 == 0 && dark2_3 == 1)
        {
          digitalWrite(DOut2, LOW);
          LightFlag2 = 0;
        }
        if (light2_3 == 1 && dark2_3 == 0)
        {
          digitalWrite(DOut2, HIGH);
          LightFlag2 = 1;
        }
      }
    }
    //Box3
    if (phase3_1 == 1 && phase3_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn3_3 * 60 + MinuteOn3_3 && clock.hour * 60 + clock.minute < HourOff3_3 * 60 + MinuteOff3_3)
      {
        if (light3_3 == 0 && dark3_3 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
        if (light3_3 == 0 && dark3_3 == 1)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_3 == 1 && dark3_3 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
      }
      else
      {
        if (light3_3 == 0 && dark3_3 == 0)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_3 == 0 && dark3_3 == 1)
        {
          digitalWrite(DOut3, LOW);
          LightFlag3 = 0;
        }
        if (light3_3 == 1 && dark3_3 == 0)
        {
          digitalWrite(DOut3, HIGH);
          LightFlag3 = 1;
        }
      }
    }
    //Box4
    if (phase4_1 == 1 && phase4_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn4_3 * 60 + MinuteOn4_3 && clock.hour * 60 + clock.minute < HourOff4_3 * 60 + MinuteOff4_3)
      {
        if (light4_3 == 0 && dark4_3 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
        if (light4_3 == 0 && dark4_3 == 1)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_3 == 1 && dark4_3 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
      }
      else
      {
        if (light4_3 == 0 && dark4_3 == 0)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_3 == 0 && dark4_3 == 1)
        {
          digitalWrite(DOut4, LOW);
          LightFlag4 = 0;
        }
        if (light4_3 == 1 && dark4_3 == 0)
        {
          digitalWrite(DOut4, HIGH);
          LightFlag4 = 1;
        }
      }
    }
    //Box5
    if (phase5_1 == 1 && phase5_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn5_3 * 60 + MinuteOn5_3 && clock.hour * 60 + clock.minute < HourOff5_3 * 60 + MinuteOff5_3)
      {
        if (light5_3 == 0 && dark5_3 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
        if (light5_3 == 0 && dark5_3 == 1)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_3 == 1 && dark5_3 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
      }
      else
      {
        if (light5_3 == 0 && dark5_3 == 0)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_3 == 0 && dark5_3 == 1)
        {
          digitalWrite(DOut5, LOW);
          LightFlag5 = 0;
        }
        if (light5_3 == 1 && dark5_3 == 0)
        {
          digitalWrite(DOut5, HIGH);
          LightFlag5 = 1;
        }
      }
    }
    //Box6
    if (phase6_1 == 1 && phase6_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn6_3 * 60 + MinuteOn6_3 && clock.hour * 60 + clock.minute < HourOff6_3 * 60 + MinuteOff6_3)
      {
        if (light6_3 == 0 && dark6_3 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
        if (light6_3 == 0 && dark6_3 == 1)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_3 == 1 && dark6_3 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
      }
      else
      {
        if (light6_3 == 0 && dark6_3 == 0)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_3 == 0 && dark6_3 == 1)
        {
          digitalWrite(DOut6, LOW);
          LightFlag6 = 0;
        }
        if (light6_3 == 1 && dark6_3 == 0)
        {
          digitalWrite(DOut6, HIGH);
          LightFlag6 = 1;
        }
      }
    }
    //Box7
    if (phase7_1 == 1 && phase7_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn7_3 * 60 + MinuteOn7_3 && clock.hour * 60 + clock.minute < HourOff7_3 * 60 + MinuteOff7_3)
      {
        if (light7_3 == 0 && dark7_3 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
        if (light7_3 == 0 && dark7_3 == 1)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_3 == 1 && dark7_3 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
      }
      else
      {
        if (light7_3 == 0 && dark7_3 == 0)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_3 == 0 && dark7_3 == 1)
        {
          digitalWrite(DOut7, LOW);
          LightFlag7 = 0;
        }
        if (light7_3 == 1 && dark7_3 == 0)
        {
          digitalWrite(DOut7, HIGH);
          LightFlag7 = 1;
        }
      }
    }
    //Box8
    if (phase8_1 == 1 && phase8_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn8_3 * 60 + MinuteOn8_3 && clock.hour * 60 + clock.minute < HourOff8_3 * 60 + MinuteOff8_3)
      {
        if (light8_3 == 0 && dark8_3 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
        if (light8_3 == 0 && dark8_3 == 1)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_3 == 1 && dark8_3 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
      }
      else
      {
        if (light8_3 == 0 && dark8_3 == 0)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_3 == 0 && dark8_3 == 1)
        {
          digitalWrite(DOut8, LOW);
          LightFlag8 = 0;
        }
        if (light8_3 == 1 && dark8_3 == 0)
        {
          digitalWrite(DOut8, HIGH);
          LightFlag8 = 1;
        }
      }
    }
    //Box9
    if (phase9_1 == 1 && phase9_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn9_3 * 60 + MinuteOn9_3 && clock.hour * 60 + clock.minute < HourOff9_3 * 60 + MinuteOff9_3)
      {
        if (light9_3 == 0 && dark9_3 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
        if (light9_3 == 0 && dark9_3 == 1)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_3 == 1 && dark9_3 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
      }
      else
      {
        if (light9_3 == 0 && dark9_3 == 0)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_3 == 0 && dark9_3 == 1)
        {
          digitalWrite(DOut9, LOW);
          LightFlag9 = 0;
        }
        if (light9_3 == 1 && dark9_3 == 0)
        {
          digitalWrite(DOut9, HIGH);
          LightFlag9 = 1;
        }
      }
    }
    //Box10
    if (phase10_1 == 1 && phase10_2 == 1)
    {
      if (clock.hour * 60 + clock.minute >= HourOn10_3 * 60 + MinuteOn10_3 && clock.hour * 60 + clock.minute < HourOff10_3 * 60 + MinuteOff10_3)
      {
        if (light10_3 == 0 && dark10_3 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
        if (light10_3 == 0 && dark10_3 == 1)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_3 == 1 && dark10_3 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
      }
      else
      {
        if (light10_3 == 0 && dark10_3 == 0)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_3 == 0 && dark10_3 == 1)
        {
          digitalWrite(DOut10, LOW);
          LightFlag10 = 0;
        }
        if (light10_3 == 1 && dark10_3 == 0)
        {
          digitalWrite(DOut10, HIGH);
          LightFlag10 = 1;
        }
      }
    }

    // If the after all of the settings (Time, Light, Initial header printing, Check schedule) begin to print time stamps and measurements

    printMeasurement();
    Serial.println(" ");
  }
}
// Define a function to print measurement
void printMeasurement()
{
  // mean values over 1-min
  int mPIR1 = 0;
  int mPIR2 = 0;
  int mPIR3 = 0;
  int mPIR4 = 0;
  int mPIR5 = 0;
  int mPIR6 = 0;
  int mPIR7 = 0;
  int mPIR8 = 0;
  int mPIR9 = 0;
  int mPIR10 = 0;

  // per-second sampling
  int PIR1 = digitalRead(DIn1);
  int PIR2 = digitalRead(DIn2);
  int PIR3 = digitalRead(DIn3);
  int PIR4 = digitalRead(DIn4);
  int PIR5 = digitalRead(DIn5);
  int PIR6 = digitalRead(DIn6);
  int PIR7 = digitalRead(DIn7);
  int PIR8 = digitalRead(DIn8);
  int PIR9 = digitalRead(DIn9);
  int PIR10 = digitalRead(DIn10);

  // sensor value sampling for 1-min
  for (int i = 0; i < 9999; i++)
  {
    PIR1 = PIR1 + digitalRead(DIn1);
    PIR2 = PIR2 + digitalRead(DIn2);
    PIR3 = PIR3 + digitalRead(DIn3);
    PIR4 = PIR4 + digitalRead(DIn4);
    PIR5 = PIR5 + digitalRead(DIn5);
    PIR6 = PIR6 + digitalRead(DIn6);
    PIR7 = PIR7 + digitalRead(DIn7);
    PIR8 = PIR8 + digitalRead(DIn8);
    PIR9 = PIR9 + digitalRead(DIn9);
    PIR10 = PIR10 + digitalRead(DIn10);

    delay(5); // sampling 10000 times per minute
  }

  // 1-min summation
  mPIR1 = PIR1;
  mPIR2 = PIR2;
  mPIR3 = PIR3;
  mPIR4 = PIR4;
  mPIR5 = PIR5;
  mPIR6 = PIR6;
  mPIR7 = PIR7;
  mPIR8 = PIR8;
  mPIR9 = PIR9;
  mPIR10 = PIR10;

  // Outputs

  printTime();
  Serial.print(" ");

  //Box1
  Serial.print("0000");
  Serial.print(LightFlag1);
  Serial.print(" ");
  if(mPIR1<10000 && mPIR1>999)
  {
    Serial.print("0");
  }
  if(mPIR1<1000 && mPIR1>99)
  {
    Serial.print("00");
  }
  if(mPIR1<100 && mPIR1>9)
  {
    Serial.print("000");
  }
  if(mPIR1<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR1);
  Serial.print(" ");
  //Box2
  Serial.print("0000");
  Serial.print(LightFlag2);
  Serial.print(" ");
  if(mPIR2<10000 && mPIR2>999)
  {
    Serial.print("0");
  }
  if(mPIR2<1000 && mPIR2>99)
  {
    Serial.print("00");
  }
  if(mPIR2<100 && mPIR2>9)
  {
    Serial.print("000");
  }
  if(mPIR2<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR2);
  Serial.print(" ");
  //Box3
  Serial.print("0000");
  Serial.print(LightFlag3);
  Serial.print(" ");
  if(mPIR3<10000 && mPIR3>999)
  {
    Serial.print("0");
  }
  if(mPIR3<1000 && mPIR3>99)
  {
    Serial.print("00");
  }
  if(mPIR3<100 && mPIR3>9)
  {
    Serial.print("000");
  }
  if(mPIR3<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR3);
  Serial.print(" ");
  //Box4
  Serial.print("0000");
  Serial.print(LightFlag4);
  Serial.print(" ");
  if(mPIR4<10000 && mPIR4>999)
  {
    Serial.print("0");
  }
  if(mPIR4<1000 && mPIR4>99)
  {
    Serial.print("00");
  }
  if(mPIR4<100 && mPIR4>9)
  {
    Serial.print("000");
  }
  if(mPIR4<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR4);
  Serial.print(" ");
  //Box5
  Serial.print("0000");
  Serial.print(LightFlag5);
  Serial.print(" ");
  if(mPIR5<10000 && mPIR5>999)
  {
    Serial.print("0");
  }
  if(mPIR5<1000 && mPIR5>99)
  {
    Serial.print("00");
  }
  if(mPIR5<100 && mPIR5>9)
  {
    Serial.print("000");
  }
  if(mPIR5<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR5);
  Serial.print(" ");
  //Box6
  Serial.print("0000");
  Serial.print(LightFlag6);
  Serial.print(" ");
  if(mPIR6<10000 && mPIR6>999)
  {
    Serial.print("0");
  }
  if(mPIR6<1000 && mPIR6>99)
  {
    Serial.print("00");
  }
  if(mPIR6<100 && mPIR6>9)
  {
    Serial.print("000");
  }
  if(mPIR6<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR6);
  Serial.print(" ");
  //Box7
  Serial.print("0000");
  Serial.print(LightFlag7);
  Serial.print(" ");
  if(mPIR7<10000 && mPIR7>999)
  {
    Serial.print("0");
  }
  if(mPIR7<1000 && mPIR7>99)
  {
    Serial.print("00");
  }
  if(mPIR7<100 && mPIR7>9)
  {
    Serial.print("000");
  }
  if(mPIR7<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR7);
  Serial.print(" ");
  //Box8
  Serial.print("0000");
  Serial.print(LightFlag8);
  Serial.print(" ");
  if(mPIR8<10000 && mPIR8>999)
  {
    Serial.print("0");
  }
  if(mPIR8<1000 && mPIR8>99)
  {
    Serial.print("00");
  }
  if(mPIR8<100 && mPIR8>9)
  {
    Serial.print("000");
  }
  if(mPIR8<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR8);
  Serial.print(" ");
  //Box9
  Serial.print("0000");
  Serial.print(LightFlag9);
  Serial.print(" ");
  if(mPIR9<10000 && mPIR9>999)
  {
    Serial.print("0");
  }
  if(mPIR9<1000 && mPIR9>99)
  {
    Serial.print("00");
  }
  if(mPIR9<100 && mPIR9>9)
  {
    Serial.print("000");
  }
  if(mPIR9<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR9);
  Serial.print(" ");
  //Box10
  Serial.print("0000");
  Serial.print(LightFlag10);
  Serial.print(" ");
  if(mPIR10<10000 && mPIR10>999)
  {
    Serial.print("0");
  }
  if(mPIR10<1000 && mPIR10>99)
  {
    Serial.print("00");
  }
  if(mPIR10<100 && mPIR10>9)
  {
    Serial.print("000");
  }
  if(mPIR10<10)
  {
    Serial.print("0000");
  }
  Serial.print(mPIR10);
  Serial.print(" ");
}

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
