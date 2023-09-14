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
 * 28 Dec 2018 (major development)
 */

#include <Wire.h>
#include "DS1307.h"
#include <Time.h>
#include <TimeLib.h>

DS1307 clock; //define a object of DS1307 class

String dateIn;
String lightIn1;

// declaration in array of 10 boxes
int PIR1[2] = {0, 0};
int PIR2[2] = {0, 0};
int mPIR1[2] = {0, 0};
int mPIR2[2] = {0, 0};

int LED1[2] = {0, 0};
int LED2[2] = {0, 0};
int LED3[2] = {0, 0};
int LED4[2] = {0, 0};

int Break1[2] = {0, 0};
int Break2[2] = {0, 0};
int mBreak1[2] = {0, 0};
int mBreak2[2] = {0, 0};

int HourOn1[2] = {8, 8}; // phase 1
int MinuteOn1[2] = {0, 0};
int HourOn2[2] = {8, 8}; // phase 2
int MinuteOn2[2] = {0, 0};
int HourOn3[2] = {8, 8}; // phase 3
int MinuteOn3[2] = {0, 0};
int HourOn4[2] = {8, 8}; // phase 1
int MinuteOn4[2] = {0, 0};
int HourOn5[2] = {8, 8}; // phase 2
int MinuteOn5[2] = {0, 0};
int HourOn6[2] = {8, 8}; // phase 1
int MinuteOn6[2] = {0, 0};
int HourOn7[2] = {8, 8}; // phase 2
int MinuteOn7[2] = {0, 0};
int HourOn8[2] = {8, 8}; // phase 3
int MinuteOn8[2] = {0, 0};
int HourOn9[2] = {8, 8}; // phase 1
int MinuteOn9[2] = {0, 0};
int HourOn10[2] = {8, 8}; // phase 2
int MinuteOn10[2] = {0, 0};
int HourOn11[2] = {8, 8}; // phase 1
int MinuteOn11[2] = {0, 0};
int HourOn12[2] = {8, 8}; // phase 2
int MinuteOn12[2] = {0, 0};
int HourOn13[2] = {8, 8}; // phase 3
int MinuteOn13[2] = {0, 0};
int HourOn14[2] = {8, 8}; // phase 1
int MinuteOn14[2] = {0, 0};
int HourOn15[2] = {8, 8}; // phase 2
int MinuteOn15[2] = {0, 0};
int HourOn16[2] = {8, 8}; // phase 1
int MinuteOn16[2] = {0, 0};
int HourOn17[2] = {8, 8}; // phase 2
int MinuteOn17[2] = {0, 0};
int HourOn18[2] = {8, 8}; // phase 3
int MinuteOn18[2] = {0, 0};
int HourOn19[2] = {8, 8}; // phase 1
int MinuteOn19[2] = {0, 0};
int HourOn20[2] = {8, 8}; // phase 2
int MinuteOn20[2] = {0, 0};

int light1[2] = {0, 0};  // phase 1
int light2[2] = {0, 0};  // phase 2
int light3[2] = {0, 0};  // phase 3
int light4[2] = {0, 0};  // phase 1
int light5[2] = {0, 0};  // phase 2
int light6[2] = {0, 0};  // phase 1
int light7[2] = {0, 0};  // phase 2
int light8[2] = {0, 0};  // phase 3
int light9[2] = {0, 0};  // phase 1
int light10[2] = {0, 0}; // phase 2
int light11[2] = {0, 0}; // phase 1
int light12[2] = {0, 0}; // phase 2
int light13[2] = {0, 0}; // phase 3
int light14[2] = {0, 0}; // phase 1
int light15[2] = {0, 0}; // phase 2
int light16[2] = {0, 0}; // phase 1
int light17[2] = {0, 0}; // phase 2
int light18[2] = {0, 0}; // phase 3
int light19[2] = {0, 0}; // phase 1
int light20[2] = {0, 0}; // phase 2

int dark1[2] = {0, 0};  // phase 1
int dark2[2] = {0, 0};  // phase 2
int dark3[2] = {0, 0};  // phase 3
int dark4[2] = {0, 0};  // phase 1
int dark5[2] = {0, 0};  // phase 2
int dark6[2] = {0, 0};  // phase 1
int dark7[2] = {0, 0};  // phase 2
int dark8[2] = {0, 0};  // phase 3
int dark9[2] = {0, 0};  // phase 1
int dark10[2] = {0, 0}; // phase 2
int dark11[2] = {0, 0}; // phase 1
int dark12[2] = {0, 0}; // phase 2
int dark13[2] = {0, 0}; // phase 3
int dark14[2] = {0, 0}; // phase 1
int dark15[2] = {0, 0}; // phase 2
int dark16[2] = {0, 0}; // phase 1
int dark17[2] = {0, 0}; // phase 2
int dark18[2] = {0, 0}; // phase 3
int dark19[2] = {0, 0}; // phase 1
int dark20[2] = {0, 0}; // phase 2

float RatioOn1[2] = {12, 12};
float RatioOn2[2] = {12, 12};
float RatioOn3[2] = {12, 12};
float RatioOn4[2] = {12, 12};
float RatioOn5[2] = {12, 12};
float RatioOn6[2] = {12, 12};
float RatioOn7[2] = {12, 12};
float RatioOn8[2] = {12, 12};
float RatioOn9[2] = {12, 12};
float RatioOn10[2] = {12, 12};
float RatioOn11[2] = {12, 12};
float RatioOn12[2] = {12, 12};
float RatioOn13[2] = {12, 12};
float RatioOn14[2] = {12, 12};
float RatioOn15[2] = {12, 12};
float RatioOn16[2] = {12, 12};
float RatioOn17[2] = {12, 12};
float RatioOn18[2] = {12, 12};
float RatioOn19[2] = {12, 12};
float RatioOn20[2] = {12, 12};

float RatioOff1[2] = {12, 12};
float RatioOff2[2] = {12, 12};
float RatioOff3[2] = {12, 12};
float RatioOff4[2] = {12, 12};
float RatioOff5[2] = {12, 12};
float RatioOff6[2] = {12, 12};
float RatioOff7[2] = {12, 12};
float RatioOff8[2] = {12, 12};
float RatioOff9[2] = {12, 12};
float RatioOff10[2] = {12, 12};
float RatioOff11[2] = {12, 12};
float RatioOff12[2] = {12, 12};
float RatioOff13[2] = {12, 12};
float RatioOff14[2] = {12, 12};
float RatioOff15[2] = {12, 12};
float RatioOff16[2] = {12, 12};
float RatioOff17[2] = {12, 12};
float RatioOff18[2] = {12, 12};
float RatioOff19[2] = {12, 12};
float RatioOff20[2] = {12, 12};

// Digital In-Out
// PIRs
int DIn1[2] = {2, 8};
int DIn2[2] = {3, 9};
// LEDs
int DOut1[2] = {4,10};
int DOut2[2] = {5,11};
int DOut3[2] = {6,12};
int DOut4[2] = {7,13};

// Analog In
// line breakers
const int AIn1[2] = {2, 4};
const int AIn2[2] = {3, 5};

// Global variables
int phase1 = 0;
int phase2 = 0;
int phase3 = 0;
int phase4 = 0;
int phase5 = 0;
int phase6 = 0;
int phase7 = 0;
int phase8 = 0;
int phase9 = 0;
int phase10 = 0;
int phase11 = 0;
int phase12 = 0;
int phase13 = 0;
int phase14 = 0;
int phase15 = 0;
int phase16 = 0;
int phase17 = 0;
int phase18 = 0;
int phase19 = 0;

int StartHour = 0;
int StartMinute = 0;
int StartYear = 2018;
int StartMonth = 01;
int StartDate = 01;

float T_Cycle = 24;
float T_Cycle1 = 24;
float T_Cycle2 = 24;
float T_Cycle3 = 24;
float T_Cycle4 = 24;
float T_Cycle5 = 24;
float T_Cycle6 = 24;
float T_Cycle7 = 24;
float T_Cycle8 = 24;
float T_Cycle9 = 24;
float T_Cycle10 = 24;
float T_Cycle11 = 24;
float T_Cycle12 = 24;
float T_Cycle13 = 24;
float T_Cycle14 = 24;
float T_Cycle15 = 24;
float T_Cycle16 = 24;
float T_Cycle17 = 24;
float T_Cycle18 = 24;
float T_Cycle19 = 24;
float T_Cycle20 = 24;

int LightFlag[2] = {0, 0};
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
int LightSet11 = 0;
int LightSet12 = 0;
int LightSet13 = 0;
int LightSet14 = 0;
int LightSet15 = 0;
int LightSet16 = 0;
int LightSet17 = 0;
int LightSet18 = 0;
int LightSet19 = 0;
int LightSet20 = 0;
int LightSet21 = 0;
int LightSet22 = 0;
int LightSet23 = 0;
int LightSet24 = 0;
int LightSet25 = 0;
int LightSet26 = 0;
int LightSet27 = 0;
int LightSet28 = 0;
int LightSet29 = 0;
int LightSet30 = 0;
int LightSet31 = 0;
int LightSet32 = 0;
int LightSet33 = 0;
int LightSet34 = 0;
int LightSet35 = 0;
int LightSet36 = 0;
int LightSet37 = 0;

int InitialFlag = 0;

int reset1 = 0;
int reset2 = 0;
int addref1 = 0;
int addref2 = 0;

float timeStart = 0.;
float timeEnd = 0.;
float hourstart = 0.;
float minstart = 0.;
float secstart = 0.;
int Day = 0;
int Days1 = 0;
int Days2 = 0;
int Days3 = 0;
int Days4 = 0;
int Days5 = 0;
int Days6 = 0;
int Days7 = 0;
int Days8 = 0;
int Days9 = 0;
int Days10 = 0;
int Days11 = 0;
int Days12 = 0;
int Days13 = 0;
int Days14 = 0;
int Days15 = 0;
int Days16 = 0;
int Days17 = 0;
int Days18 = 0;
int Days19 = 0;
int Days20 = 0;

int LightIntensity1[2] = {1, 1};
int LightIntensity2[2] = {1, 1};
int LightIntensity3[2] = {1, 1};
int LightIntensity4[2] = {1, 1};
int LightIntensity5[2] = {1, 1};

int LightIntensity6[2] = {1, 1};
int LightIntensity7[2] = {1, 1};
int LightIntensity8[2] = {1, 1};
int LightIntensity9[2] = {1, 1};
int LightIntensity10[2] = {1, 1};

int LightIntensity11[2] = {1, 1};
int LightIntensity12[2] = {1, 1};
int LightIntensity13[2] = {1, 1};
int LightIntensity14[2] = {1, 1};
int LightIntensity15[2] = {1, 1};

int LightIntensity16[2] = {1, 1};
int LightIntensity17[2] = {1, 1};
int LightIntensity18[2] = {1, 1};
int LightIntensity19[2] = {1, 1};
int LightIntensity20[2] = {1, 1};

float intTime = 0.;
float intTimeex = 0.; //For re-reference when the external clock turns 00:00:00
float intHour = 0.;
float intMinute = 0.;
float intSecond = 0.;
float anchor = 24.*3600. ;

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
  for (int i = 0; i < 2; i++)
  {
    pinMode(DIn1[i], INPUT);   // PIR1
    pinMode(DIn2[i], INPUT);   // PIR2
    pinMode(DOut1[i], OUTPUT); // LED1
    pinMode(DOut2[i], OUTPUT); // LED2
    pinMode(DOut3[i], OUTPUT); // LED3
    pinMode(DOut4[i], OUTPUT); // LED4
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
  if (Serial.available() == 12 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    StartHour = getInt(lightIn1.substring(0, 2));
    StartMinute = getInt(lightIn1.substring(2, 4));
    StartYear = getInt(lightIn1.substring(4, 8));
    StartMonth = getInt(lightIn1.substring(8, 10));
    StartDate = getInt(lightIn1.substring(10, 12));

    LightSet1 = 1;
  }

  if (Serial.available() == 12 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    dark1[0] = getInt(lightIn1.substring(0, 1));
    light1[0] = getInt(lightIn1.substring(1, 2));
    dark1[1] = getInt(lightIn1.substring(2, 3));
    light1[1] = getInt(lightIn1.substring(3, 4));

    dark2[0] = getInt(lightIn1.substring(4, 5));
    light2[0] = getInt(lightIn1.substring(5, 6));
    dark2[1] = getInt(lightIn1.substring(6, 7));
    light2[1] = getInt(lightIn1.substring(7, 8));

    dark3[0] = getInt(lightIn1.substring(8, 9));
    light3[0] = getInt(lightIn1.substring(9, 10));
    dark3[1] = getInt(lightIn1.substring(10, 11));
    light3[1] = getInt(lightIn1.substring(11, 12));

    LightSet2 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn1[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn1[0] = getInt(lightIn1.substring(2, 4));
    HourOn1[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn1[1] = getInt(lightIn1.substring(6, 8));

    RatioOn1[0] = getInt(lightIn1.substring(8, 10));
    RatioOff1[0] = getInt(lightIn1.substring(10, 12));
    RatioOn1[1] = getInt(lightIn1.substring(12, 14));
    RatioOff1[1] = getInt(lightIn1.substring(14, 16));

    LightSet3 = 1;

  }
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn2[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn2[0] = getInt(lightIn1.substring(2, 4));
    HourOn2[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn2[1] = getInt(lightIn1.substring(6, 8));

    LightIntensity1[0] = getInt(lightIn1.substring(8, 9));
    LightIntensity1[1] = getInt(lightIn1.substring(9, 10));

    LightIntensity2[0] = getInt(lightIn1.substring(10, 11));
    LightIntensity2[1] = getInt(lightIn1.substring(11, 12));

    LightIntensity3[0] = getInt(lightIn1.substring(12, 13));
    LightIntensity3[1] = getInt(lightIn1.substring(13, 14));

    LightIntensity4[0] = getInt(lightIn1.substring(14, 15));
    LightIntensity4[1] = getInt(lightIn1.substring(15, 16));

    LightIntensity5[0] = getInt(lightIn1.substring(16, 17));
    LightIntensity5[1] = getInt(lightIn1.substring(17, 18));

    LightIntensity6[0] = getInt(lightIn1.substring(18, 19));
    LightIntensity6[1] = getInt(lightIn1.substring(19, 20));

    LightIntensity7[0] = getInt(lightIn1.substring(20, 21));
    LightIntensity7[1] = getInt(lightIn1.substring(21, 22));

    LightIntensity8[0] = getInt(lightIn1.substring(22, 23));
    LightIntensity8[1] = getInt(lightIn1.substring(23, 24));

    LightIntensity9[0] = getInt(lightIn1.substring(24, 25));
    LightIntensity9[1] = getInt(lightIn1.substring(25, 26));

    LightIntensity10[0] = getInt(lightIn1.substring(26, 27));
    LightIntensity10[1] = getInt(lightIn1.substring(27, 28));

    LightIntensity11[0] = getInt(lightIn1.substring(28, 29));
    LightIntensity11[1] = getInt(lightIn1.substring(29, 30));

    LightIntensity12[0] = getInt(lightIn1.substring(30, 31));
    LightIntensity12[1] = getInt(lightIn1.substring(31, 32));

    LightIntensity13[0] = getInt(lightIn1.substring(32, 33));
    LightIntensity13[1] = getInt(lightIn1.substring(33, 34));

    LightIntensity14[0] = getInt(lightIn1.substring(34, 35));
    LightIntensity14[1] = getInt(lightIn1.substring(35, 36));

    LightIntensity15[0] = getInt(lightIn1.substring(36, 37));
    LightIntensity15[1] = getInt(lightIn1.substring(37, 38));

    LightIntensity16[0] = getInt(lightIn1.substring(38, 39));
    LightIntensity16[1] = getInt(lightIn1.substring(39, 40));

    LightSet4 = 1;
  }
  if (Serial.available() == 24 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn2[0] = getInt(lightIn1.substring(0, 2));
    RatioOff2[0] = getInt(lightIn1.substring(2, 4));
    RatioOn2[1] = getInt(lightIn1.substring(4, 6));
    RatioOff2[1] = getInt(lightIn1.substring(6, 8));

    HourOn3[0] = getInt(lightIn1.substring(8, 10));
    MinuteOn3[0] = getInt(lightIn1.substring(10, 12));
    HourOn3[1] = getInt(lightIn1.substring(12, 14));
    MinuteOn3[1] = getInt(lightIn1.substring(14, 16));

    LightIntensity17[0] = getInt(lightIn1.substring(16, 17));
    LightIntensity17[1] = getInt(lightIn1.substring(17, 18));

    LightIntensity18[0] = getInt(lightIn1.substring(18, 19));
    LightIntensity18[1] = getInt(lightIn1.substring(19, 20));

    LightIntensity19[0] = getInt(lightIn1.substring(20, 21));
    LightIntensity19[1] = getInt(lightIn1.substring(21, 22));

    LightIntensity20[0] = getInt(lightIn1.substring(22, 23));
    LightIntensity20[1] = getInt(lightIn1.substring(23, 24));

    LightSet5 = 1;
  }
  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn3[0] = getInt(lightIn1.substring(0, 2));
    RatioOff3[0] = getInt(lightIn1.substring(2, 4));
    RatioOn3[1] = getInt(lightIn1.substring(4, 6));
    RatioOff3[1] = getInt(lightIn1.substring(6, 8));

    LightSet6 = 1;
  }

  if (Serial.available() == 12 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark4[0] = getInt(lightIn1.substring(0, 1));
    light4[0] = getInt(lightIn1.substring(1, 2));
    dark4[1] = getInt(lightIn1.substring(2, 3));
    light4[1] = getInt(lightIn1.substring(3, 4));

    dark5[0] = getInt(lightIn1.substring(4, 5));
    light5[0] = getInt(lightIn1.substring(5, 6));
    dark5[1] = getInt(lightIn1.substring(6, 7));
    light5[1] = getInt(lightIn1.substring(7, 8));

    dark6[0] = getInt(lightIn1.substring(8, 9));
    light6[0] = getInt(lightIn1.substring(9, 10));
    dark6[1] = getInt(lightIn1.substring(10, 11));
    light6[1] = getInt(lightIn1.substring(11, 12));

    LightSet7 = 1;
  }
  if (Serial.available() == 12 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark7[0] = getInt(lightIn1.substring(0, 1));
    light7[0] = getInt(lightIn1.substring(1, 2));
    dark7[1] = getInt(lightIn1.substring(2, 3));
    light7[1] = getInt(lightIn1.substring(3, 4));

    dark8[0] = getInt(lightIn1.substring(4, 5));
    light8[0] = getInt(lightIn1.substring(5, 6));
    dark8[1] = getInt(lightIn1.substring(6, 7));
    light8[1] = getInt(lightIn1.substring(7, 8));

    dark9[0] = getInt(lightIn1.substring(8, 9));
    light9[0] = getInt(lightIn1.substring(9, 10));
    dark9[1] = getInt(lightIn1.substring(10, 11));
    light9[1] = getInt(lightIn1.substring(11, 12));

    LightSet8 = 1;
  }

  if (Serial.available() == 12 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark10[0] = getInt(lightIn1.substring(0, 1));
    light10[0] = getInt(lightIn1.substring(1, 2));
    dark10[1] = getInt(lightIn1.substring(2, 3));
    light10[1] = getInt(lightIn1.substring(3, 4));

    dark11[0] = getInt(lightIn1.substring(4, 5));
    light11[0] = getInt(lightIn1.substring(5, 6));
    dark11[1] = getInt(lightIn1.substring(6, 7));
    light11[1] = getInt(lightIn1.substring(7, 8));

    dark12[0] = getInt(lightIn1.substring(8, 9));
    light12[0] = getInt(lightIn1.substring(9, 10));
    dark12[1] = getInt(lightIn1.substring(10, 11));
    light12[1] = getInt(lightIn1.substring(11, 12));

    LightSet9 = 1;
  }

  if (Serial.available() == 12 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark13[0] = getInt(lightIn1.substring(0, 1));
    light13[0] = getInt(lightIn1.substring(1, 2));
    dark13[1] = getInt(lightIn1.substring(2, 3));
    light13[1] = getInt(lightIn1.substring(3, 4));

    dark14[0] = getInt(lightIn1.substring(4, 5));
    light14[0] = getInt(lightIn1.substring(5, 6));
    dark14[1] = getInt(lightIn1.substring(6, 7));
    light14[1] = getInt(lightIn1.substring(7, 8));

    dark15[0] = getInt(lightIn1.substring(8, 9));
    light15[0] = getInt(lightIn1.substring(9, 10));
    dark15[1] = getInt(lightIn1.substring(10, 11));
    light15[1] = getInt(lightIn1.substring(11, 12));

    LightSet10 = 1;
  }

  if (Serial.available() == 12 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark16[0] = getInt(lightIn1.substring(0, 1));
    light16[0] = getInt(lightIn1.substring(1, 2));
    dark16[1] = getInt(lightIn1.substring(2, 3));
    light16[1] = getInt(lightIn1.substring(3, 4));

    dark17[0] = getInt(lightIn1.substring(4, 5));
    light17[0] = getInt(lightIn1.substring(5, 6));
    dark17[1] = getInt(lightIn1.substring(6, 7));
    light17[1] = getInt(lightIn1.substring(7, 8));

    dark18[0] = getInt(lightIn1.substring(8, 9));
    light18[0] = getInt(lightIn1.substring(9, 10));
    dark18[1] = getInt(lightIn1.substring(10, 11));
    light18[1] = getInt(lightIn1.substring(11, 12));

    LightSet11 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark19[0] = getInt(lightIn1.substring(0, 1));
    light19[0] = getInt(lightIn1.substring(1, 2));
    dark19[1] = getInt(lightIn1.substring(2, 3));
    light19[1] = getInt(lightIn1.substring(3, 4));


    dark20[0] = getInt(lightIn1.substring(4, 5));
    light20[0] = getInt(lightIn1.substring(5, 6));
    dark20[1] = getInt(lightIn1.substring(6, 7));
    light20[1] = getInt(lightIn1.substring(7, 8));

    LightSet12 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn4[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn4[0] = getInt(lightIn1.substring(2, 4));
    HourOn4[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn4[1] = getInt(lightIn1.substring(6, 8));

    RatioOn4[0] = getInt(lightIn1.substring(8, 10));
    RatioOff4[0] = getInt(lightIn1.substring(10, 12));
    RatioOn4[1] = getInt(lightIn1.substring(12, 14));
    RatioOff4[1] = getInt(lightIn1.substring(14, 16));

    LightSet13 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn5[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn5[0] = getInt(lightIn1.substring(2, 4));
    HourOn5[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn5[1] = getInt(lightIn1.substring(6, 8));

    LightSet14 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn5[0] = getInt(lightIn1.substring(0, 2));
    RatioOff5[0] = getInt(lightIn1.substring(2, 4));
    RatioOn5[1] = getInt(lightIn1.substring(4, 6));
    RatioOff5[1] = getInt(lightIn1.substring(6, 8));

    HourOn6[0] = getInt(lightIn1.substring(8, 10));
    MinuteOn6[0] = getInt(lightIn1.substring(10, 12));
    HourOn6[1] = getInt(lightIn1.substring(12, 14));
    MinuteOn6[1] = getInt(lightIn1.substring(14, 16));

    LightSet15 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn6[0] = getInt(lightIn1.substring(0, 2));
    RatioOff6[0] = getInt(lightIn1.substring(2, 4));
    RatioOn6[1] = getInt(lightIn1.substring(4, 6));
    RatioOff6[1] = getInt(lightIn1.substring(6, 8));

    LightSet16 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn7[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn7[0] = getInt(lightIn1.substring(2, 4));
    HourOn7[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn7[1] = getInt(lightIn1.substring(6, 8));

    RatioOn7[0] = getInt(lightIn1.substring(8, 10));
    RatioOff7[0] = getInt(lightIn1.substring(10, 12));
    RatioOn7[1] = getInt(lightIn1.substring(12, 14));
    RatioOff7[1] = getInt(lightIn1.substring(14, 16));

    LightSet17 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn8[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn8[0] = getInt(lightIn1.substring(2, 4));
    HourOn8[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn8[1] = getInt(lightIn1.substring(6, 8));
    LightSet18 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn8[0] = getInt(lightIn1.substring(0, 2));
    RatioOff8[0] = getInt(lightIn1.substring(2, 4));
    RatioOn8[1] = getInt(lightIn1.substring(4, 6));
    RatioOff8[1] = getInt(lightIn1.substring(6, 8));

    HourOn9[0] = getInt(lightIn1.substring(8, 10));
    MinuteOn9[0] = getInt(lightIn1.substring(10, 12));
    HourOn9[1] = getInt(lightIn1.substring(12, 14));
    MinuteOn9[1] = getInt(lightIn1.substring(14, 16));

    LightSet19 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn9[0] = getInt(lightIn1.substring(0, 2));
    RatioOff9[0] = getInt(lightIn1.substring(2, 4));
    RatioOn9[1] = getInt(lightIn1.substring(4, 6));
    RatioOff9[1] = getInt(lightIn1.substring(6, 8));

    LightSet20 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn10[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn10[0] = getInt(lightIn1.substring(2, 4));
    HourOn10[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn10[1] = getInt(lightIn1.substring(6, 8));

    RatioOn10[0] = getInt(lightIn1.substring(8, 10));
    RatioOff10[0] = getInt(lightIn1.substring(10, 12));
    RatioOn10[1] = getInt(lightIn1.substring(12, 14));
    RatioOff10[1] = getInt(lightIn1.substring(14, 16));

    LightSet21 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn11[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn11[0] = getInt(lightIn1.substring(2, 4));
    HourOn11[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn11[1] = getInt(lightIn1.substring(6, 8));

    LightSet22 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn11[0] = getInt(lightIn1.substring(0, 2));
    RatioOff11[0] = getInt(lightIn1.substring(2, 4));
    RatioOn11[1] = getInt(lightIn1.substring(4, 6));
    RatioOff11[1] = getInt(lightIn1.substring(6, 8));

    HourOn12[0] = getInt(lightIn1.substring(8, 10));
    MinuteOn12[0] = getInt(lightIn1.substring(10, 12));
    HourOn12[1] = getInt(lightIn1.substring(12, 14));
    MinuteOn12[1] = getInt(lightIn1.substring(14, 16));

    LightSet23 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn12[0] = getInt(lightIn1.substring(0, 2));
    RatioOff12[0] = getInt(lightIn1.substring(2, 4));
    RatioOn12[1] = getInt(lightIn1.substring(4, 6));
    RatioOff12[1] = getInt(lightIn1.substring(6, 8));

    LightSet24 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn13[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn13[0] = getInt(lightIn1.substring(2, 4));
    HourOn13[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn13[1] = getInt(lightIn1.substring(6, 8));

    RatioOn13[0] = getInt(lightIn1.substring(8, 10));
    RatioOff13[0] = getInt(lightIn1.substring(10, 12));
    RatioOn13[1] = getInt(lightIn1.substring(12, 14));
    RatioOff13[1] = getInt(lightIn1.substring(14, 16));

    LightSet25 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn14[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn14[0] = getInt(lightIn1.substring(2, 4));
    HourOn14[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn14[1] = getInt(lightIn1.substring(6, 8));

    LightSet26 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn14[0] = getInt(lightIn1.substring(0, 2));
    RatioOff14[0] = getInt(lightIn1.substring(2, 4));
    RatioOn14[1] = getInt(lightIn1.substring(4, 6));
    RatioOff14[1] = getInt(lightIn1.substring(6, 8));

    HourOn15[0] = getInt(lightIn1.substring(8, 10));
    MinuteOn15[0] = getInt(lightIn1.substring(10, 12));
    HourOn15[1] = getInt(lightIn1.substring(12, 14));
    MinuteOn15[1] = getInt(lightIn1.substring(14, 16));

    LightSet27 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn15[0] = getInt(lightIn1.substring(0, 2));
    RatioOff15[0] = getInt(lightIn1.substring(2, 4));
    RatioOn15[1] = getInt(lightIn1.substring(4, 6));
    RatioOff15[1] = getInt(lightIn1.substring(6, 8));

    LightSet28 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn16[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn16[0] = getInt(lightIn1.substring(2, 4));
    HourOn16[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn16[1] = getInt(lightIn1.substring(6, 8));

    RatioOn16[0] = getInt(lightIn1.substring(8, 10));
    RatioOff16[0] = getInt(lightIn1.substring(10, 12));
    RatioOn16[1] = getInt(lightIn1.substring(12, 14));
    RatioOff16[1] = getInt(lightIn1.substring(14, 16));

    LightSet29 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn17[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn17[0] = getInt(lightIn1.substring(2, 4));
    HourOn17[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn17[1] = getInt(lightIn1.substring(6, 8));

    LightSet30 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn17[0] = getInt(lightIn1.substring(0, 2));
    RatioOff17[0] = getInt(lightIn1.substring(2, 4));
    RatioOn17[1] = getInt(lightIn1.substring(4, 6));
    RatioOff17[1] = getInt(lightIn1.substring(6, 8));

    HourOn18[0] = getInt(lightIn1.substring(8, 10));
    MinuteOn18[0] = getInt(lightIn1.substring(10, 12));
    HourOn18[1] = getInt(lightIn1.substring(12, 14));
    MinuteOn18[1] = getInt(lightIn1.substring(14, 16));

    LightSet31 = 1;
  }
  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 1 && LightSet32 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn18[0] = getInt(lightIn1.substring(0, 2));
    RatioOff18[0] = getInt(lightIn1.substring(2, 4));
    RatioOn18[1] = getInt(lightIn1.substring(4, 6));
    RatioOff18[1] = getInt(lightIn1.substring(6, 8));

    LightSet32 = 1;
  }

  if (Serial.available() == 16 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 1 && LightSet32 == 1 && LightSet33 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn19[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn19[0] = getInt(lightIn1.substring(2, 4));
    HourOn19[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn19[1] = getInt(lightIn1.substring(6, 8));

    RatioOn19[0] = getInt(lightIn1.substring(8, 10));
    RatioOff19[0] = getInt(lightIn1.substring(10, 12));
    RatioOn19[1] = getInt(lightIn1.substring(12, 14));
    RatioOff19[1] = getInt(lightIn1.substring(14, 16));

    LightSet33 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 1 && LightSet32 == 1 && LightSet33 == 1 && LightSet34 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn20[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn20[0] = getInt(lightIn1.substring(2, 4));
    HourOn20[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn20[1] = getInt(lightIn1.substring(6, 8));

    LightSet34 = 1;
  }

  if (Serial.available() == 8 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 1 && LightSet32 == 1 && LightSet33 == 1 && LightSet34 == 1 && LightSet35 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn20[0] = getInt(lightIn1.substring(0, 2));
    RatioOff20[0] = getInt(lightIn1.substring(2, 4));
    RatioOn20[1] = getInt(lightIn1.substring(4, 6));
    RatioOff20[1] = getInt(lightIn1.substring(6, 8));
    
    LightSet35 = 1;
  }

  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 1 && LightSet32 == 1 && LightSet33 == 1 && LightSet34 == 1 && LightSet35 == 1 && LightSet36 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    Days1 = getInt(lightIn1.substring(0, 2));
    Days2 = getInt(lightIn1.substring(2, 4));
    Days3 = getInt(lightIn1.substring(4, 6));
    Days4 = getInt(lightIn1.substring(6, 8));
    Days5 = getInt(lightIn1.substring(8, 10));
    Days6 = getInt(lightIn1.substring(10, 12));
    Days7 = getInt(lightIn1.substring(12, 14));
    Days8 = getInt(lightIn1.substring(14, 16));
    Days9 = getInt(lightIn1.substring(16, 18));
    Days10 = getInt(lightIn1.substring(18, 20));

    Days11 = getInt(lightIn1.substring(20, 22));
    Days12 = getInt(lightIn1.substring(22, 24));
    Days13 = getInt(lightIn1.substring(24, 26));
    Days14 = getInt(lightIn1.substring(26, 28));
    Days15 = getInt(lightIn1.substring(28, 30));
    Days16 = getInt(lightIn1.substring(30, 32));
    Days17 = getInt(lightIn1.substring(32, 34));
    Days18 = getInt(lightIn1.substring(34, 36));
    Days19 = getInt(lightIn1.substring(36, 38));
    Days20 = getInt(lightIn1.substring(38, 40));

    LightSet36 = 1;
  }
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 && LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 1 && LightSet32 == 1 && LightSet33 == 1 && LightSet34 == 1 && LightSet35 == 1 && LightSet36 == 1 && LightSet37 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    T_Cycle1 = getInt(lightIn1.substring(0, 2));
    T_Cycle2 = getInt(lightIn1.substring(2, 4));
    T_Cycle3 = getInt(lightIn1.substring(4, 6));
    T_Cycle4 = getInt(lightIn1.substring(6, 8));
    T_Cycle5 = getInt(lightIn1.substring(8, 10));
    T_Cycle6 = getInt(lightIn1.substring(10, 12));
    T_Cycle7 = getInt(lightIn1.substring(12, 14));
    T_Cycle8 = getInt(lightIn1.substring(14, 16));
    T_Cycle9 = getInt(lightIn1.substring(16, 18));
    T_Cycle10 = getInt(lightIn1.substring(18, 20));

    T_Cycle11 = getInt(lightIn1.substring(20, 22));
    T_Cycle12 = getInt(lightIn1.substring(22, 24));
    T_Cycle13 = getInt(lightIn1.substring(24, 26));
    T_Cycle14 = getInt(lightIn1.substring(26, 28));
    T_Cycle15 = getInt(lightIn1.substring(28, 30));
    T_Cycle16 = getInt(lightIn1.substring(30, 32));
    T_Cycle17 = getInt(lightIn1.substring(32, 34));
    T_Cycle18 = getInt(lightIn1.substring(34, 36));
    T_Cycle19 = getInt(lightIn1.substring(36, 38));
    T_Cycle20 = getInt(lightIn1.substring(38, 40));

    LightSet37 = 1;
  }

  // Begin to print the headers and set light flag
  if (InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 &&
      LightSet6 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 &&
      LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 &&
      LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 &&
      LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 == 1 && LightSet27 == 1 &&
      LightSet28 == 1 && LightSet29 == 1 && LightSet30 == 1 && LightSet31 == 1 && LightSet32 == 1 &&
      LightSet33 == 1 && LightSet34 == 1 && LightSet35 == 1 && LightSet36 == 1 && LightSet37 == 1)
  {
    Serial.println("HH:MM:SS MO/DY/YEAR DAY Internal LED01 PIR11 PIR12 BRK11 BRK12 LED02 PIR21 PIR22 BRK21 BRK22");
    InitialFlag = 1;
    T_Cycle = T_Cycle1;
  }

  if (InitialFlag == 1)
  {
    clock.getTime();
    while ((clock.second == 0) == false)
    {
      delay(1);
      clock.getTime();
    }

    // Calculate Internal Time based on External Time
    // Set the reference for Only for the first Day because we want to synchronize the first time point of internal and external clock
    if (reset1 == 0)
    {
      hourstart = clock.hour;
      minstart = clock.minute;
      secstart = clock.second;
      Day = Day + 1;
      reset1 = 1;
    }
    // For the first day, we need to add the reference day into the elapse time to get the internal time
    if (reset1 == 1 && reset2 == 0)
    {
      setTime(clock.hour, clock.minute, clock.second, clock.dayOfMonth, clock.month, (clock.year + 2000));

      // Additional step to make sure that the elapsed time calculation is correct when external clock resets from 23:59 to 00:00
      if (addref1 == 0 && clock.hour == 0 && clock.minute == 0 && clock.second == 0)
      {
        hourstart = 0;
        minstart = 0;
        secstart = 0;
        addref1 = 1;
      }
      // Before external clock resets
      if (addref1 == 0)
      {
        timeStart = (hourstart * 60. * 60.) + (minstart * 60.) + secstart; // second of the day
        timeEnd = hour() * 60. * 60. + minute() * 60. + second();          // second of the day
        intTime = timeStart + ((timeEnd - timeStart) * (24. / T_Cycle));

        //Internal Time
        intSecond = second(intTime);
        intMinute = minute(intTime);
        intHour = hour(intTime);
      }
      // After external clock resets
      if (addref1 == 1)
      {
        timeStart = (hourstart * 60. * 60.) + (minstart * 60.) + secstart; // second of the day
        timeEnd = hour() * 60. * 60. + minute() * 60. + second();          // second of the day
        intTimeex = timeStart + intTime + 60. * (24. / T_Cycle) + ((timeEnd - timeStart) * (24. / T_Cycle));

        //Internal Time
        intSecond = second(intTimeex);
        intMinute = minute(intTimeex);
        intHour = hour(intTimeex);
      }
    }

    // From the second day, we dont need to add the reference into internal time anymore
    if (reset1 == 1 && reset2 == 1)
    {
      setTime(clock.hour, clock.minute, clock.second, clock.dayOfMonth, clock.month, (clock.year + 2000));

      // Additional step to make sure that the elapsed time calculation is correct when external clock resets from 23:59 to 00:00
      if (addref2 == 0 && clock.hour == 0 && clock.minute == 0 && clock.second == 0)
      {
        hourstart = 0;
        minstart = 0;
        secstart = 0;
        addref2 = 1;
      }
      // Before external clock resets
      if (addref2 == 0)
      {
        timeStart = ((float)hourstart * 60. * 60.) + ((float)minstart * 60.) + (float)secstart; // second of the day
        timeEnd = ((float)hour() * 60. * 60.) + ((float)minute() * 60.) + (float)second();      // second of the day
        intTime = (timeEnd - timeStart) * (24. / T_Cycle);
        intSecond = second(intTime);
        intMinute = minute(intTime);
        intHour = hour(intTime);
      }
      // After external clock resets
      if (addref2 == 1)
      {
        timeStart = ((float)hourstart * 60. * 60.) + ((float)minstart * 60.) + (float)secstart; // second of the day
        timeEnd = ((float)hour() * 60. * 60.) + ((float)minute() * 60.) + (float)second();      // second of the day
        intTimeex = intTime + 60. * (24. / T_Cycle) + (timeEnd - timeStart) * (24. / T_Cycle);

        intSecond = second(intTimeex);
        intMinute = minute(intTimeex);
        intHour = hour(intTimeex);
      }
    }

    //To avoid the 00:00:00 can't be reached
    if (reset1 == 1 && (anchor - (intHour * 60 * 60 + intMinute * 60 + intSecond) < 30))
    {
      intHour = 0.;
      intMinute = 0.;
      intSecond = 0.;
    }
    //Reset the reference to clock time from the second Day at 23:59:00, after 1 min of PIR sampling, it becomes the next day

    if (reset1 == 1 && intHour == 0. && intMinute == 0. && intSecond == 0.)
    {
      hourstart = clock.hour;
      minstart = clock.minute;
      secstart = clock.second;
      Day = Day + 1;
      reset2 = 1;
      addref2 = 0;
    }

    // End phase 1 when

    if (Day > Days1)
    {
      phase1 = 1;
      T_Cycle = T_Cycle2;
    }

    // End phase 2 when

    if (Day > Days1 + Days2)
    {
      phase2 = 1;
      T_Cycle = T_Cycle3;
    }

    // End phase 3 when
    if (Day > Days1 + Days2 + Days3)
    {
      phase3 = 1;
      T_Cycle = T_Cycle4;
    }

    // End phase 4 when
    if (Day > Days1 + Days2 + Days3 + Days4)
    {
      phase4 = 1;
      T_Cycle = T_Cycle5;
    }
    // End phase 5 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5)
    {
      phase5 = 1;
      T_Cycle = T_Cycle6;
    }

    // End phase 6 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6)
    {
      phase6 = 1;
      T_Cycle = T_Cycle7;
    }

    // End phase 7 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7)
    {
      phase7 = 1;
      T_Cycle = T_Cycle8;
    }
    // End phase 8 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8)
    {
      phase8 = 1;
      T_Cycle = T_Cycle9;
    }

    // End phase 9 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9)
    {
      phase9 = 1;
      T_Cycle = T_Cycle10;
    }

    // End phase 10 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10)
    {
      phase10 = 1;
      T_Cycle = T_Cycle11;
    }

    // End phase 11 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11)
    {
      phase11 = 1;
      T_Cycle = T_Cycle12;
    }

    // End phase 12 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12)
    {
      phase12 = 1;
      T_Cycle = T_Cycle13;
    }

    // End phase 13 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12 + Days13)
    {
      phase13 = 1;
      T_Cycle = T_Cycle14;
    }

    // End phase 14 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12 + Days13 + Days14)
    {
      phase14 = 1;
      T_Cycle = T_Cycle15;
    }

    // End phase 15 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12 + Days13 + Days14 + Days15)
    {
      phase15 = 1;
      T_Cycle = T_Cycle16;
    }

    // End phase 16 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12 + Days13 + Days14 + Days15 + Days16)
    {
      phase16 = 1;
      T_Cycle = T_Cycle17;
    }

    // End phase 17 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12 + Days13 + Days14 + Days15 + Days16 + Days17)
    {
      phase17 = 1;
      T_Cycle = T_Cycle18;
    }

    // End phase 18 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12 + Days13 + Days14 + Days15 + Days16 + Days17 + Days18)
    {
      phase18 = 1;
      T_Cycle = T_Cycle19;
    }

    // End phase 19 when
    if (Day > Days1 + Days2 + Days3 + Days4 + Days5 + Days6 + Days7 + Days8 + Days9 + Days10 + Days11 + Days12 + Days13 + Days14 + Days15 + Days16 + Days17 + Days18 + Days19)
    {
      phase19 = 1;
      T_Cycle = T_Cycle20;
    }

    //////////For Phase1
    if (phase1 == 0)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn1[i] * 60 + MinuteOn1[i] && (intHour * 60 + intMinute) - (HourOn1[i] * 60 + MinuteOn1[i]) <= 24 * (RatioOn1[i] / (RatioOn1[i] + RatioOff1[i])) * 60)
        {
          if (light1[i] == 0 && dark1[i] == 0)
          {
            if (LightIntensity1[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity1[i];
          }
          if (light1[i] == 0 && dark1[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light1[i] == 1 && dark1[i] == 0)
          {
            if (LightIntensity1[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity1[i];
          }
        }
        else
        {
          if (light1[i] == 0 && dark1[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light1[i] == 0 && dark1[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light1[i] == 1 && dark1[i] == 0)
          {
            if (LightIntensity1[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity1[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity1[i];
          }
        }
      }
    }

    //Phase 2

    if (phase1 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn2[i] * 60 + MinuteOn2[i] && (intHour * 60 + intMinute) - (HourOn2[i] * 60 + MinuteOn2[i]) <= 24 * (RatioOn2[i] / (RatioOn2[i] + RatioOff2[i])) * 60)
        {
          if (light2[i] == 0 && dark2[i] == 0)
          {
            if (LightIntensity2[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity2[i];
          }
          if (light2[i] == 0 && dark2[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light2[i] == 1 && dark2[i] == 0)
          {
            if (LightIntensity2[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity2[i];
          }
        }
        else
        {
          if (light2[i] == 0 && dark2[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light2[i] == 0 && dark2[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light2[i] == 1 && dark2[i] == 0)
          {
            if (LightIntensity2[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity2[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity2[i];
          }
        }
      }
    }

    //Phase 3

    if (phase2 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn3[i] * 60 + MinuteOn3[i] && (intHour * 60 + intMinute) - (HourOn3[i] * 60 + MinuteOn3[i]) <= 24 * (RatioOn3[i] / (RatioOn3[i] + RatioOff3[i])) * 60)
        {
          if (light3[i] == 0 && dark3[i] == 0)
          {
            if (LightIntensity3[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity3[i];
          }
          if (light3[i] == 0 && dark3[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light3[i] == 1 && dark3[i] == 0)
          {
            if (LightIntensity3[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity3[i];
          }
        }
        else
        {
          if (light3[i] == 0 && dark3[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light3[i] == 0 && dark3[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light3[i] == 1 && dark3[i] == 0)
          {
            if (LightIntensity3[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity3[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity3[i];
          }
        }
      }
    }

    //Phase 4

    if (phase3 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn4[i] * 60 + MinuteOn4[i] && (intHour * 60 + intMinute) - (HourOn4[i] * 60 + MinuteOn4[i]) <= 24 * (RatioOn4[i] / (RatioOn4[i] + RatioOff4[i])) * 60)
        {
          if (light4[i] == 0 && dark4[i] == 0)
          {
            if (LightIntensity4[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity4[i];
          }
          if (light4[i] == 0 && dark4[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light4[i] == 1 && dark4[i] == 0)
          {
            if (LightIntensity4[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity4[i];
          }
        }
        else
        {
          if (light4[i] == 0 && dark4[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light4[i] == 0 && dark4[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light4[i] == 1 && dark4[i] == 0)
          {
            if (LightIntensity4[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity4[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity4[i];
          }
        }
      }
    }

    //Phase 5

    if (phase4 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn5[i] * 60 + MinuteOn5[i] && (intHour * 60 + intMinute) - (HourOn5[i] * 60 + MinuteOn5[i]) <= 24 * (RatioOn5[i] / (RatioOn5[i] + RatioOff5[i])) * 60)
        {
          if (light5[i] == 0 && dark5[i] == 0)
          {
            if (LightIntensity5[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity5[i];
          }
          if (light5[i] == 0 && dark5[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light5[i] == 1 && dark5[i] == 0)
          {
            if (LightIntensity5[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity5[i];
          }
        }
        else
        {
          if (light5[i] == 0 && dark5[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light5[i] == 0 && dark5[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light5[i] == 1 && dark5[i] == 0)
          {
            if (LightIntensity5[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity5[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity5[i];
          }
        }
      }
    }

    //Phase 6

    if (phase5 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn6[i] * 60 + MinuteOn6[i] && (intHour * 60 + intMinute) - (HourOn6[i] * 60 + MinuteOn6[i]) <= 24 * (RatioOn6[i] / (RatioOn6[i] + RatioOff6[i])) * 60)
        {
          if (light6[i] == 0 && dark6[i] == 0)
          {
            if (LightIntensity6[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity6[i];
          }
          if (light6[i] == 0 && dark6[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light6[i] == 1 && dark6[i] == 0)
          {
            if (LightIntensity6[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity6[i];
          }
        }
        else
        {
          if (light6[i] == 0 && dark6[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light6[i] == 0 && dark6[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light6[i] == 1 && dark6[i] == 0)
          {
            if (LightIntensity6[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity6[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity6[i];
          }
        }
      }
    }

    //Phase 7

    if (phase6 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn7[i] * 60 + MinuteOn7[i] && (intHour * 60 + intMinute) - (HourOn7[i] * 60 + MinuteOn7[i]) <= 24 * (RatioOn7[i] / (RatioOn7[i] + RatioOff7[i])) * 60)
        {
          if (light7[i] == 0 && dark7[i] == 0)
          {
            if (LightIntensity7[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity7[i];
          }
          if (light7[i] == 0 && dark7[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light7[i] == 1 && dark7[i] == 0)
          {
            if (LightIntensity7[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity7[i];
          }
        }
        else
        {
          if (light7[i] == 0 && dark7[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light7[i] == 0 && dark7[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light7[i] == 1 && dark7[i] == 0)
          {
            if (LightIntensity7[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity7[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity7[i];
          }
        }
      }
    }

    //Phase 8

    if (phase7 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn8[i] * 60 + MinuteOn8[i] && (intHour * 60 + intMinute) - (HourOn8[i] * 60 + MinuteOn8[i]) <= 24 * (RatioOn8[i] / (RatioOn8[i] + RatioOff8[i])) * 60)
        {
          if (light8[i] == 0 && dark8[i] == 0)
          {
            if (LightIntensity8[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity8[i];
          }
          if (light8[i] == 0 && dark8[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light8[i] == 1 && dark8[i] == 0)
          {
            if (LightIntensity8[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity8[i];
          }
        }
        else
        {
          if (light8[i] == 0 && dark8[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light8[i] == 0 && dark8[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light8[i] == 1 && dark8[i] == 0)
          {
            if (LightIntensity8[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity8[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity8[i];
          }
        }
      }
    }

    //Phase 9

    if (phase8 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn9[i] * 60 + MinuteOn9[i] && (intHour * 60 + intMinute) - (HourOn9[i] * 60 + MinuteOn9[i]) <= 24 * (RatioOn9[i] / (RatioOn9[i] + RatioOff9[i])) * 60)
        {
          if (light9[i] == 0 && dark9[i] == 0)
          {
            if (LightIntensity9[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity9[i];
          }
          if (light9[i] == 0 && dark9[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light9[i] == 1 && dark9[i] == 0)
          {
            if (LightIntensity9[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity9[i];
          }
        }
        else
        {
          if (light9[i] == 0 && dark9[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light9[i] == 0 && dark9[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light9[i] == 1 && dark9[i] == 0)
          {
            if (LightIntensity9[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity9[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity9[i];
          }
        }
      }
    }

    //Phase 10

    if (phase9 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn10[i] * 60 + MinuteOn10[i] && (intHour * 60 + intMinute) - (HourOn10[i] * 60 + MinuteOn10[i]) <= 24 * (RatioOn10[i] / (RatioOn10[i] + RatioOff10[i])) * 60)
        {
          if (light10[i] == 0 && dark10[i] == 0)
          {
            if (LightIntensity10[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity10[i];
          }
          if (light10[i] == 0 && dark10[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light10[i] == 1 && dark10[i] == 0)
          {
            if (LightIntensity10[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity10[i];
          }
        }
        else
        {
          if (light10[i] == 0 && dark10[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light10[i] == 0 && dark10[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light10[i] == 1 && dark10[i] == 0)
          {
            if (LightIntensity10[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity10[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity10[i];
          }
        }
      }
    }

    //Phase 11

    if (phase10 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn11[i] * 60 + MinuteOn11[i] && (intHour * 60 + intMinute) - (HourOn11[i] * 60 + MinuteOn11[i]) <= 24 * (RatioOn11[i] / (RatioOn11[i] + RatioOff11[i])) * 60)
        {
          if (light11[i] == 0 && dark11[i] == 0)
          {
            if (LightIntensity11[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity11[i];
          }
          if (light11[i] == 0 && dark11[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light11[i] == 1 && dark11[i] == 0)
          {
            if (LightIntensity11[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity11[i];
          }
        }
        else
        {
          if (light11[i] == 0 && dark11[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light11[i] == 0 && dark11[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light11[i] == 1 && dark11[i] == 0)
          {
            if (LightIntensity11[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity11[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity11[i];
          }
        }
      }
    }

    //Phase 12

    if (phase11 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn12[i] * 60 + MinuteOn12[i] && (intHour * 60 + intMinute) - (HourOn12[i] * 60 + MinuteOn12[i]) <= 24 * (RatioOn12[i] / (RatioOn12[i] + RatioOff12[i])) * 60)
        {
          if (light12[i] == 0 && dark12[i] == 0)
          {
            if (LightIntensity12[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity12[i];
          }
          if (light12[i] == 0 && dark12[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light12[i] == 1 && dark12[i] == 0)
          {
            if (LightIntensity12[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity12[i];
          }
        }
        else
        {
          if (light12[i] == 0 && dark12[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light12[i] == 0 && dark12[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light12[i] == 1 && dark12[i] == 0)
          {
            if (LightIntensity12[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity12[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity12[i];
          }
        }
      }
    }

    //Phase 13

    if (phase12 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn13[i] * 60 + MinuteOn13[i] && (intHour * 60 + intMinute) - (HourOn13[i] * 60 + MinuteOn13[i]) <= 24 * (RatioOn13[i] / (RatioOn13[i] + RatioOff13[i])) * 60)
        {
          if (light13[i] == 0 && dark13[i] == 0)
          {
            if (LightIntensity13[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity13[i];
          }
          if (light13[i] == 0 && dark13[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light13[i] == 1 && dark13[i] == 0)
          {
            if (LightIntensity13[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity13[i];
          }
        }
        else
        {
          if (light13[i] == 0 && dark13[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light13[i] == 0 && dark13[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light13[i] == 1 && dark13[i] == 0)
          {
            if (LightIntensity13[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity13[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity13[i];
          }
        }
      }
    }

    //Phase 14

    if (phase13 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn14[i] * 60 + MinuteOn14[i] && (intHour * 60 + intMinute) - (HourOn14[i] * 60 + MinuteOn14[i]) <= 24 * (RatioOn14[i] / (RatioOn14[i] + RatioOff14[i])) * 60)
        {
          if (light14[i] == 0 && dark14[i] == 0)
          {
            if (LightIntensity14[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity14[i];
          }
          if (light14[i] == 0 && dark14[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light14[i] == 1 && dark14[i] == 0)
          {
            if (LightIntensity14[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity14[i];
          }
        }
        else
        {
          if (light14[i] == 0 && dark14[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light14[i] == 0 && dark14[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light14[i] == 1 && dark14[i] == 0)
          {
            if (LightIntensity14[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity14[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity14[i];
          }
        }
      }
    }

    //Phase 15

    if (phase14 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn15[i] * 60 + MinuteOn15[i] && (intHour * 60 + intMinute) - (HourOn15[i] * 60 + MinuteOn15[i]) <= 24 * (RatioOn15[i] / (RatioOn15[i] + RatioOff15[i])) * 60)
        {
          if (light15[i] == 0 && dark15[i] == 0)
          {
            if (LightIntensity15[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity15[i];
          }
          if (light15[i] == 0 && dark15[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light15[i] == 1 && dark15[i] == 0)
          {
            if (LightIntensity15[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity15[i];
          }
        }
        else
        {
          if (light15[i] == 0 && dark15[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light15[i] == 0 && dark15[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light15[i] == 1 && dark15[i] == 0)
          {
            if (LightIntensity15[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity15[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity15[i];
          }
        }
      }
    }

    //Phase 16

    if (phase15 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn16[i] * 60 + MinuteOn16[i] && (intHour * 60 + intMinute) - (HourOn16[i] * 60 + MinuteOn16[i]) <= 24 * (RatioOn16[i] / (RatioOn16[i] + RatioOff16[i])) * 60)
        {
          if (light16[i] == 0 && dark16[i] == 0)
          {
            if (LightIntensity16[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity16[i];
          }
          if (light16[i] == 0 && dark16[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light16[i] == 1 && dark16[i] == 0)
          {
            if (LightIntensity16[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity16[i];
          }
        }
        else
        {
          if (light16[i] == 0 && dark16[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light16[i] == 0 && dark16[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light16[i] == 1 && dark16[i] == 0)
          {
            if (LightIntensity16[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity16[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity16[i];
          }
        }
      }
    }

    //Phase 17

    if (phase16 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn17[i] * 60 + MinuteOn17[i] && (intHour * 60 + intMinute) - (HourOn17[i] * 60 + MinuteOn17[i]) <= 24 * (RatioOn17[i] / (RatioOn17[i] + RatioOff17[i])) * 60)
        {
          if (light17[i] == 0 && dark17[i] == 0)
          {
            if (LightIntensity17[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity17[i];
          }
          if (light17[i] == 0 && dark17[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light17[i] == 1 && dark17[i] == 0)
          {
            if (LightIntensity17[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity17[i];
          }
        }
        else
        {
          if (light17[i] == 0 && dark17[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light17[i] == 0 && dark17[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light17[i] == 1 && dark17[i] == 0)
          {
            if (LightIntensity17[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity17[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity17[i];
          }
        }
      }
    }

    //Phase 18

    if (phase17 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn18[i] * 60 + MinuteOn18[i] && (intHour * 60 + intMinute) - (HourOn18[i] * 60 + MinuteOn18[i]) <= 24 * (RatioOn18[i] / (RatioOn18[i] + RatioOff18[i])) * 60)
        {
          if (light18[i] == 0 && dark18[i] == 0)
          {
            if (LightIntensity18[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity18[i];
          }
          if (light18[i] == 0 && dark18[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light18[i] == 1 && dark18[i] == 0)
          {
            if (LightIntensity18[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity18[i];
          }
        }
        else
        {
          if (light18[i] == 0 && dark18[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light18[i] == 0 && dark18[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light18[i] == 1 && dark18[i] == 0)
          {
            if (LightIntensity18[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity18[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity18[i];
          }
        }
      }
    }

    //Phase 19

    if (phase18 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn19[i] * 60 + MinuteOn19[i] && (intHour * 60 + intMinute) - (HourOn19[i] * 60 + MinuteOn19[i]) <= 24 * (RatioOn19[i] / (RatioOn19[i] + RatioOff19[i])) * 60)
        {
          if (light19[i] == 0 && dark19[i] == 0)
          {
            if (LightIntensity19[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity19[i];
          }
          if (light19[i] == 0 && dark19[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light19[i] == 1 && dark19[i] == 0)
          {
            if (LightIntensity19[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity19[i];
          }
        }
        else
        {
          if (light19[i] == 0 && dark19[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light19[i] == 0 && dark19[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light19[i] == 1 && dark19[i] == 0)
          {
            if (LightIntensity19[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity19[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity19[i];
          }
        }
      }
    }

    //Phase 20

    if (phase19 == 1)
    {
      for (int i = 0; i < 2; i++)
      {
        if (intHour * 60 + intMinute >= HourOn20[i] * 60 + MinuteOn20[i] && (intHour * 60 + intMinute) - (HourOn20[i] * 60 + MinuteOn20[i]) <= 24 * (RatioOn20[i] / (RatioOn20[i] + RatioOff20[i])) * 60)
        {
          if (light20[i] == 0 && dark20[i] == 0)
          {
            if (LightIntensity20[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity20[i];
          }
          if (light20[i] == 0 && dark20[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);

            LightFlag[i] = 0;
          }
          if (light20[i] == 1 && dark20[i] == 0)
          {
            if (LightIntensity20[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }

            LightFlag[i] = LightIntensity20[i];
          }
        }
        else
        {
          if (light20[i] == 0 && dark20[i] == 0)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light20[i] == 0 && dark20[i] == 1)
          {
            digitalWrite(DOut1[i], LOW);
            digitalWrite(DOut2[i], LOW);
            digitalWrite(DOut3[i], LOW);
            digitalWrite(DOut4[i], LOW);
            LightFlag[i] = 0;
          }
          if (light20[i] == 1 && dark20[i] == 0)
          {
            if (LightIntensity20[i] == 1)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], LOW);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 2)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], LOW);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 3)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], LOW);
            }

            if (LightIntensity20[i] == 4)
            {
              digitalWrite(DOut1[i], HIGH);
              digitalWrite(DOut2[i], HIGH);
              digitalWrite(DOut3[i], HIGH);
              digitalWrite(DOut4[i], HIGH);
            }
            LightFlag[i] = LightIntensity20[i];
          }
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
  for (int i = 0; i < 2; i++)
  {
    mPIR1[i] = 0;
    mPIR2[i] = 0;
    mBreak1[i] = 0;
    mBreak2[i] = 0;
  }

  // per-second sampling
  for (int i = 0; i < 2; i++)
  {
    PIR1[i] = digitalRead(DIn1[i]);
    PIR2[i] = digitalRead(DIn2[i]);
    Break1[i] = (1024 - analogRead(AIn1[i]));
    Break2[i] = (1024 - analogRead(AIn2[i]));
  }

  // sensor value sampling for 1-min
  for (int i = 0; i < 900; i++)
  {
    for (int j = 0; j < 2; j++)
    {
      PIR1[j] = PIR1[j] + digitalRead(DIn1[j]);
      PIR2[j] = PIR2[j] + digitalRead(DIn2[j]);
      Break1[j] = Break1[j] + (1024 - analogRead(AIn1[j]));
      Break2[j] = Break2[j] + (1024 - analogRead(AIn2[j]));
    }

    delay(60); // sampling 900 times per minute
  }

  // 1-min summation
  for (int i = 0; i < 2; i++)
  {
    mPIR1[i] = PIR1[i];
    mPIR2[i] = PIR2[i];
    mBreak1[i] = Break1[i];
    mBreak2[i] = Break2[i];
  }

  // Outputs

  printTime();
  Serial.print(" ");

  for (int i = 0; i < 2; i++)
  {
    Serial.print("0000");
    Serial.print(LightFlag[i]);
    Serial.print(" ");
    if (mPIR1[i] < 10000 && mPIR1[i] > 999)
    {
      Serial.print("0");
    }
    if (mPIR1[i] < 1000 && mPIR1[i] > 99)
    {
      Serial.print("00");
    }
    if (mPIR1[i] < 100 && mPIR1[i] > 9)
    {
      Serial.print("000");
    }
    if (mPIR1[i] < 10)
    {
      Serial.print("0000");
    }
    Serial.print(mPIR1[i]);
    Serial.print(" ");

    if (mPIR2[i] < 10000 && mPIR2[i] > 999)
    {
      Serial.print("0");
    }
    if (mPIR2[i] < 1000 && mPIR2[i] > 99)
    {
      Serial.print("00");
    }
    if (mPIR2[i] < 100 && mPIR2[i] > 9)
    {
      Serial.print("000");
    }
    if (mPIR2[i] < 10)
    {
      Serial.print("0000");
    }
    Serial.print(mPIR2[i]);
    
    Serial.print(" ");

    if (mBreak1[i] < 10000 && mBreak1[i] > 999)
    {
      Serial.print("0");
    }
    if (mBreak1[i] < 1000 && mBreak1[i] > 99)
    {
      Serial.print("00");
    }
    if (mBreak1[i] < 100 && mBreak1[i] > 9)
    {
      Serial.print("000");
    }
    if (mBreak1[i] < 100 && mBreak1[i] > 9)
    {
      Serial.print("0000");
    }
    Serial.print(mBreak1[i]);

    Serial.print(" ");

    if (mBreak2[i] < 10000 && mBreak2[i] > 999)
    {
      Serial.print("0");
    }
    if (mBreak2[i] < 1000 && mBreak2[i] > 99)
    {
      Serial.print("00");
    }
    if (mBreak2[i] < 100 && mBreak2[i] > 9)
    {
      Serial.print("000");
    }
    if (mBreak2[i] < 100 && mBreak2[i] > 9)
    {
      Serial.print("0000");
    }
    Serial.print(mBreak2[i]);

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
  Serial.print(" ");

  if (Day < 10)
  {
    Serial.print("00");
  }
  if (Day < 1000 && Day > 99)
  {
    Serial.print("0");
  }
  Serial.print(Day);
  Serial.print(" ");

  if (intHour < 10)
  {
    Serial.print("0");
  }
  Serial.print(intHour, 0);
  Serial.print(":");
  if (intMinute < 10)
  {
    Serial.print("0");
  }
  Serial.print(intMinute, 0);
  Serial.print(":");
  if (intSecond < 10)
  {
    Serial.print("0");
  }
  Serial.print(intSecond, 0);
}
