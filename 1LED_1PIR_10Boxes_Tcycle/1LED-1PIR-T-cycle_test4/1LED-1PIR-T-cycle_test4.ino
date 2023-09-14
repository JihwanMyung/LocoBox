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
#include <Time.h>
#include <TimeLib.h>

DS1307 clock; //define a object of DS1307 class

String dateIn;
String lightIn1;

// declaration in array of 10 boxes
int PIR[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int mPIR[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int HourOn1[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn1[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn2[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn2[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn3[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 3
int MinuteOn3[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn4[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn4[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn5[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn5[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn6[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn6[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn7[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn7[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn8[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 3
int MinuteOn8[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn9[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn9[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn10[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn10[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn11[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn11[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn12[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn12[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn13[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 3
int MinuteOn13[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn14[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn14[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn15[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn15[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn16[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn16[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn17[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn17[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn18[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 3
int MinuteOn18[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn19[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 1
int MinuteOn19[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int HourOn20[10] = {8, 8, 8, 8, 8, 8, 8, 8, 8, 8}; // phase 2
int MinuteOn20[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

int light1[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light2[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int light3[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 3
int light4[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light5[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int light6[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light7[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int light8[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 3
int light9[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light10[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int light11[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light12[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int light13[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 3
int light14[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light15[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int light16[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light17[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2
int light18[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 3
int light19[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 1
int light20[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // phase 2

int dark1[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark2[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2
int dark3[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 3
int dark4[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark5[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2
int dark6[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark7[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2
int dark8[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 3
int dark9[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark10[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2
int dark11[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark12[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2
int dark13[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 3
int dark14[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark15[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2
int dark16[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark17[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2
int dark18[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 3
int dark19[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 1
int dark20[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};  // phase 2

float RatioOn1[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn2[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn3[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn4[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn5[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn6[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn7[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn8[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn9[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn10[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn11[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn12[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn13[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn14[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn15[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn16[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn17[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn18[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn19[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOn20[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};


float RatioOff1[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff2[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff3[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff4[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff5[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff6[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff7[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff8[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff9[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff10[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff11[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff12[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff13[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff14[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff15[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff16[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff17[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff18[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff19[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};
float RatioOff20[10] = {12, 12, 12, 12, 12, 12, 12, 12, 12, 12};

// Digital In-Out
int DIn[10] = {2, 4, 6, 8, 10, 12, 22, 24, 26, 28};  // PIR
int DOut[10] = {3, 5, 7, 9, 11, 13, 23, 25, 27, 29}; // LED

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

int LightFlag[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
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
  for (int i = 0; i < 10; i++)
  {
    pinMode(DIn[i], INPUT);   // PIR
    pinMode(DOut[i], OUTPUT); // LED
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
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
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
    dark1[5] = getInt(lightIn1.substring(10, 11));
    light1[5] = getInt(lightIn1.substring(11, 12));
    dark1[6] = getInt(lightIn1.substring(12, 13));
    light1[6] = getInt(lightIn1.substring(13, 14));
    dark1[7] = getInt(lightIn1.substring(14, 15));
    light1[7] = getInt(lightIn1.substring(15, 16));
    dark1[8] = getInt(lightIn1.substring(16, 17));
    light1[8] = getInt(lightIn1.substring(17, 18));
    dark1[9] = getInt(lightIn1.substring(18, 19));
    light1[9] = getInt(lightIn1.substring(19, 20));

    dark2[0] = getInt(lightIn1.substring(20, 21));
    light2[0] = getInt(lightIn1.substring(21, 22));
    dark2[1] = getInt(lightIn1.substring(22, 23));
    light2[1] = getInt(lightIn1.substring(23, 24));
    dark2[2] = getInt(lightIn1.substring(24, 25));
    light2[2] = getInt(lightIn1.substring(25, 26));
    dark2[3] = getInt(lightIn1.substring(26, 27));
    light2[3] = getInt(lightIn1.substring(27, 28));
    dark2[4] = getInt(lightIn1.substring(28, 29));
    light2[4] = getInt(lightIn1.substring(29, 30));
    dark2[5] = getInt(lightIn1.substring(30, 31));
    light2[5] = getInt(lightIn1.substring(31, 32));
    dark2[6] = getInt(lightIn1.substring(32, 33));
    light2[6] = getInt(lightIn1.substring(33, 34));
    dark2[7] = getInt(lightIn1.substring(34, 35));
    light2[7] = getInt(lightIn1.substring(35, 36));
    dark2[8] = getInt(lightIn1.substring(36, 37));
    light2[8] = getInt(lightIn1.substring(37, 38));
    dark2[9] = getInt(lightIn1.substring(38, 39));
    light2[9] = getInt(lightIn1.substring(39, 40));

    dark3[0] = getInt(lightIn1.substring(40, 41));
    light3[0] = getInt(lightIn1.substring(41, 42));
    dark3[1] = getInt(lightIn1.substring(42, 43));
    light3[1] = getInt(lightIn1.substring(43, 44));
    dark3[2] = getInt(lightIn1.substring(44, 45));
    light3[2] = getInt(lightIn1.substring(45, 46));
    dark3[3] = getInt(lightIn1.substring(46, 47));
    light3[3] = getInt(lightIn1.substring(47, 48));
    dark3[4] = getInt(lightIn1.substring(48, 49));
    light3[4] = getInt(lightIn1.substring(49, 50));
    dark3[5] = getInt(lightIn1.substring(50, 51));
    light3[5] = getInt(lightIn1.substring(51, 52));
    dark3[6] = getInt(lightIn1.substring(52, 53));
    light3[6] = getInt(lightIn1.substring(53, 54));
    dark3[7] = getInt(lightIn1.substring(54, 55));
    light3[7] = getInt(lightIn1.substring(55, 56));
    dark3[8] = getInt(lightIn1.substring(56, 57));
    light3[8] = getInt(lightIn1.substring(57, 58));
    dark3[9] = getInt(lightIn1.substring(58, 59));
    light3[9] = getInt(lightIn1.substring(59, 60));

    LightSet2 = 1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn1[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn1[0] = getInt(lightIn1.substring(2, 4));
    HourOn1[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn1[1] = getInt(lightIn1.substring(6, 8));
    HourOn1[2] = getInt(lightIn1.substring(8, 10));
    MinuteOn1[2] = getInt(lightIn1.substring(10, 12));
    HourOn1[3] = getInt(lightIn1.substring(12, 14));
    MinuteOn1[3] = getInt(lightIn1.substring(14, 16));
    HourOn1[4] = getInt(lightIn1.substring(16, 18));
    MinuteOn1[4] = getInt(lightIn1.substring(18, 20));
    HourOn1[5] = getInt(lightIn1.substring(20, 22));
    MinuteOn1[5] = getInt(lightIn1.substring(22, 24));
    HourOn1[6] = getInt(lightIn1.substring(24, 26));
    MinuteOn1[6] = getInt(lightIn1.substring(26, 28));
    HourOn1[7] = getInt(lightIn1.substring(28, 30));
    MinuteOn1[7] = getInt(lightIn1.substring(30, 32));
    HourOn1[8] = getInt(lightIn1.substring(32, 34));
    MinuteOn1[8] = getInt(lightIn1.substring(34, 36));
    HourOn1[9] = getInt(lightIn1.substring(36, 38));
    MinuteOn1[9] = getInt(lightIn1.substring(38, 40));

    RatioOn1[0] = getInt(lightIn1.substring(40, 42));
    RatioOff1[0] = getInt(lightIn1.substring(42, 44));
    RatioOn1[1] = getInt(lightIn1.substring(44, 46));
    RatioOff1[1] = getInt(lightIn1.substring(46, 48));
    RatioOn1[2] = getInt(lightIn1.substring(48, 50));
    RatioOff1[2] = getInt(lightIn1.substring(50, 52));
    RatioOn1[3] = getInt(lightIn1.substring(52, 54));
    RatioOff1[3] = getInt(lightIn1.substring(54, 56));
    RatioOn1[4] = getInt(lightIn1.substring(56, 58));
    RatioOff1[4] = getInt(lightIn1.substring(58, 60));

    LightSet3 = 1;
    //Serial.println(HourOn1[5]);
    //Serial.println(MinuteOn1[5]);
  }
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn1[5] = getInt(lightIn1.substring(0, 2));
    RatioOff1[5] = getInt(lightIn1.substring(2, 4));
    RatioOn1[6] = getInt(lightIn1.substring(4, 6));
    RatioOff1[6] = getInt(lightIn1.substring(6, 8));
    RatioOn1[7] = getInt(lightIn1.substring(8, 10));
    RatioOff1[7] = getInt(lightIn1.substring(10, 12));
    RatioOn1[8] = getInt(lightIn1.substring(12, 14));
    RatioOff1[8] = getInt(lightIn1.substring(14, 16));
    RatioOn1[9] = getInt(lightIn1.substring(16, 18));
    RatioOff1[9] = getInt(lightIn1.substring(18, 20));

    HourOn2[0] = getInt(lightIn1.substring(20, 22));
    MinuteOn2[0] = getInt(lightIn1.substring(22, 24));
    HourOn2[1] = getInt(lightIn1.substring(24, 26));
    MinuteOn2[1] = getInt(lightIn1.substring(26, 28));
    HourOn2[2] = getInt(lightIn1.substring(28, 30));
    MinuteOn2[2] = getInt(lightIn1.substring(30, 32));
    HourOn2[3] = getInt(lightIn1.substring(32, 34));
    MinuteOn2[3] = getInt(lightIn1.substring(34, 36));
    HourOn2[4] = getInt(lightIn1.substring(36, 38));
    MinuteOn2[4] = getInt(lightIn1.substring(38, 40));
    HourOn2[5] = getInt(lightIn1.substring(40, 42));
    MinuteOn2[5] = getInt(lightIn1.substring(42, 44));
    HourOn2[6] = getInt(lightIn1.substring(44, 46));
    MinuteOn2[6] = getInt(lightIn1.substring(46, 48));
    HourOn2[7] = getInt(lightIn1.substring(48, 50));
    MinuteOn2[7] = getInt(lightIn1.substring(50, 52));
    HourOn2[8] = getInt(lightIn1.substring(52, 54));
    MinuteOn2[8] = getInt(lightIn1.substring(54, 56));
    HourOn2[9] = getInt(lightIn1.substring(56, 58));
    MinuteOn2[9] = getInt(lightIn1.substring(58, 60));

    LightSet4 = 1;
    //Serial.println(RatioOn1[5]);
    //Serial.println(RatioOff1[5]);
  }
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    RatioOn2[0] = getInt(lightIn1.substring(0, 2));
    RatioOff2[0] = getInt(lightIn1.substring(2, 4));
    RatioOn2[1] = getInt(lightIn1.substring(4, 6));
    RatioOff2[1] = getInt(lightIn1.substring(6, 8));
    RatioOn2[2] = getInt(lightIn1.substring(8, 10));
    RatioOff2[2] = getInt(lightIn1.substring(10, 12));
    RatioOn2[3] = getInt(lightIn1.substring(12, 14));
    RatioOff2[3] = getInt(lightIn1.substring(14, 16));
    RatioOn2[4] = getInt(lightIn1.substring(16, 18));
    RatioOff2[4] = getInt(lightIn1.substring(18, 20));
    RatioOn2[5] = getInt(lightIn1.substring(20, 22));
    RatioOff2[5] = getInt(lightIn1.substring(22, 24));
    RatioOn2[6] = getInt(lightIn1.substring(24, 26));
    RatioOff2[6] = getInt(lightIn1.substring(26, 28));
    RatioOn2[7] = getInt(lightIn1.substring(28, 30));
    RatioOff2[7] = getInt(lightIn1.substring(30, 32));
    RatioOn2[8] = getInt(lightIn1.substring(32, 34));
    RatioOff2[8] = getInt(lightIn1.substring(34, 36));
    RatioOn2[9] = getInt(lightIn1.substring(36, 38));
    RatioOff2[9] = getInt(lightIn1.substring(38, 40));

    HourOn3[0] = getInt(lightIn1.substring(40, 42));
    MinuteOn3[0] = getInt(lightIn1.substring(42, 44));
    HourOn3[1] = getInt(lightIn1.substring(44, 46));
    MinuteOn3[1] = getInt(lightIn1.substring(46, 48));
    HourOn3[2] = getInt(lightIn1.substring(48, 50));
    MinuteOn3[2] = getInt(lightIn1.substring(50, 52));
    HourOn3[3] = getInt(lightIn1.substring(52, 54));
    MinuteOn3[3] = getInt(lightIn1.substring(54, 56));
    HourOn3[4] = getInt(lightIn1.substring(56, 58));
    MinuteOn3[4] = getInt(lightIn1.substring(58, 60));

    LightSet5 = 1;
  }
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn3[5] = getInt(lightIn1.substring(0, 2));
    MinuteOn3[5] = getInt(lightIn1.substring(2, 4));
    HourOn3[6] = getInt(lightIn1.substring(4, 6));
    MinuteOn3[6] = getInt(lightIn1.substring(6, 8));
    HourOn3[7] = getInt(lightIn1.substring(8, 10));
    MinuteOn3[7] = getInt(lightIn1.substring(10, 12));
    HourOn3[8] = getInt(lightIn1.substring(12, 14));
    MinuteOn3[8] = getInt(lightIn1.substring(14, 16));
    HourOn3[9] = getInt(lightIn1.substring(16, 18));
    MinuteOn3[9] = getInt(lightIn1.substring(18, 20));

    RatioOn3[0] = getInt(lightIn1.substring(20, 22));
    RatioOff3[0] = getInt(lightIn1.substring(22, 24));
    RatioOn3[1] = getInt(lightIn1.substring(24, 26));
    RatioOff3[1] = getInt(lightIn1.substring(26, 28));
    RatioOn3[2] = getInt(lightIn1.substring(28, 30));
    RatioOff3[2] = getInt(lightIn1.substring(30, 32));
    RatioOn3[3] = getInt(lightIn1.substring(32, 34));
    RatioOff3[3] = getInt(lightIn1.substring(34, 36));
    RatioOn3[4] = getInt(lightIn1.substring(36, 38));
    RatioOff3[4] = getInt(lightIn1.substring(38, 40));
    RatioOn3[5] = getInt(lightIn1.substring(40, 42));
    RatioOff3[5] = getInt(lightIn1.substring(42, 44));
    RatioOn3[6] = getInt(lightIn1.substring(44, 46));
    RatioOff3[6] = getInt(lightIn1.substring(46, 48));
    RatioOn3[7] = getInt(lightIn1.substring(48, 50));
    RatioOff3[7] = getInt(lightIn1.substring(50, 52));
    RatioOn3[8] = getInt(lightIn1.substring(52, 54));
    RatioOff3[8] = getInt(lightIn1.substring(54, 56));
    RatioOn3[9] = getInt(lightIn1.substring(56, 58));
    RatioOff3[9] = getInt(lightIn1.substring(58, 60));

    LightSet6 = 1;
  }


  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark4[0] = getInt(lightIn1.substring(0, 1));
    light4[0] = getInt(lightIn1.substring(1, 2));
    dark4[1] = getInt(lightIn1.substring(2, 3));
    light4[1] = getInt(lightIn1.substring(3, 4));
    dark4[2] = getInt(lightIn1.substring(4, 5));
    light4[2] = getInt(lightIn1.substring(5, 6));
    dark4[3] = getInt(lightIn1.substring(6, 7));
    light4[3] = getInt(lightIn1.substring(7, 8));
    dark4[4] = getInt(lightIn1.substring(8, 9));
    light4[4] = getInt(lightIn1.substring(9, 10));
    dark4[5] = getInt(lightIn1.substring(10, 11));
    light4[5] = getInt(lightIn1.substring(11, 12));
    dark4[6] = getInt(lightIn1.substring(12, 13));
    light4[6] = getInt(lightIn1.substring(13, 14));
    dark4[7] = getInt(lightIn1.substring(14, 15));
    light4[7] = getInt(lightIn1.substring(15, 16));
    dark4[8] = getInt(lightIn1.substring(16, 17));
    light4[8] = getInt(lightIn1.substring(17, 18));
    dark4[9] = getInt(lightIn1.substring(18, 19));
    light4[9] = getInt(lightIn1.substring(19, 20));

    dark5[0] = getInt(lightIn1.substring(20, 21));
    light5[0] = getInt(lightIn1.substring(21, 22));
    dark5[1] = getInt(lightIn1.substring(22, 23));
    light5[1] = getInt(lightIn1.substring(23, 24));
    dark5[2] = getInt(lightIn1.substring(24, 25));
    light5[2] = getInt(lightIn1.substring(25, 26));
    dark5[3] = getInt(lightIn1.substring(26, 27));
    light5[3] = getInt(lightIn1.substring(27, 28));
    dark5[4] = getInt(lightIn1.substring(28, 29));
    light5[4] = getInt(lightIn1.substring(29, 30));
    dark5[5] = getInt(lightIn1.substring(30, 31));
    light5[5] = getInt(lightIn1.substring(31, 32));
    dark5[6] = getInt(lightIn1.substring(32, 33));
    light5[6] = getInt(lightIn1.substring(33, 34));
    dark5[7] = getInt(lightIn1.substring(34, 35));
    light5[7] = getInt(lightIn1.substring(35, 36));
    dark5[8] = getInt(lightIn1.substring(36, 37));
    light5[8] = getInt(lightIn1.substring(37, 38));
    dark5[9] = getInt(lightIn1.substring(38, 39));
    light5[9] = getInt(lightIn1.substring(39, 40));

    dark6[0] = getInt(lightIn1.substring(40, 41));
    light6[0] = getInt(lightIn1.substring(41, 42));
    dark6[1] = getInt(lightIn1.substring(42, 43));
    light6[1] = getInt(lightIn1.substring(43, 44));
    dark6[2] = getInt(lightIn1.substring(44, 45));
    light6[2] = getInt(lightIn1.substring(45, 46));
    dark6[3] = getInt(lightIn1.substring(46, 47));
    light6[3] = getInt(lightIn1.substring(47, 48));
    dark6[4] = getInt(lightIn1.substring(48, 49));
    light6[4] = getInt(lightIn1.substring(49, 50));
    dark6[5] = getInt(lightIn1.substring(50, 51));
    light6[5] = getInt(lightIn1.substring(51, 52));
    dark6[6] = getInt(lightIn1.substring(52, 53));
    light6[6] = getInt(lightIn1.substring(53, 54));
    dark6[7] = getInt(lightIn1.substring(54, 55));
    light6[7] = getInt(lightIn1.substring(55, 56));
    dark6[8] = getInt(lightIn1.substring(56, 57));
    light6[8] = getInt(lightIn1.substring(57, 58));
    dark6[9] = getInt(lightIn1.substring(58, 59));
    light6[9] = getInt(lightIn1.substring(59, 60));

    LightSet7=1;
  }
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark7[0] = getInt(lightIn1.substring(0, 1));
    light7[0] = getInt(lightIn1.substring(1, 2));
    dark7[1] = getInt(lightIn1.substring(2, 3));
    light7[1] = getInt(lightIn1.substring(3, 4));
    dark7[2] = getInt(lightIn1.substring(4, 5));
    light7[2] = getInt(lightIn1.substring(5, 6));
    dark7[3] = getInt(lightIn1.substring(6, 7));
    light7[3] = getInt(lightIn1.substring(7, 8));
    dark7[4] = getInt(lightIn1.substring(8, 9));
    light7[4] = getInt(lightIn1.substring(9, 10));
    dark7[5] = getInt(lightIn1.substring(10, 11));
    light7[5] = getInt(lightIn1.substring(11, 12));
    dark7[6] = getInt(lightIn1.substring(12, 13));
    light7[6] = getInt(lightIn1.substring(13, 14));
    dark7[7] = getInt(lightIn1.substring(14, 15));
    light7[7] = getInt(lightIn1.substring(15, 16));
    dark7[8] = getInt(lightIn1.substring(16, 17));
    light7[8] = getInt(lightIn1.substring(17, 18));
    dark7[9] = getInt(lightIn1.substring(18, 19));
    light7[9] = getInt(lightIn1.substring(19, 20));

    dark8[0] = getInt(lightIn1.substring(20, 21));
    light8[0] = getInt(lightIn1.substring(21, 22));
    dark8[1] = getInt(lightIn1.substring(22, 23));
    light8[1] = getInt(lightIn1.substring(23, 24));
    dark8[2] = getInt(lightIn1.substring(24, 25));
    light8[2] = getInt(lightIn1.substring(25, 26));
    dark8[3] = getInt(lightIn1.substring(26, 27));
    light8[3] = getInt(lightIn1.substring(27, 28));
    dark8[4] = getInt(lightIn1.substring(28, 29));
    light8[4] = getInt(lightIn1.substring(29, 30));
    dark8[5] = getInt(lightIn1.substring(30, 31));
    light8[5] = getInt(lightIn1.substring(31, 32));
    dark8[6] = getInt(lightIn1.substring(32, 33));
    light8[6] = getInt(lightIn1.substring(33, 34));
    dark8[7] = getInt(lightIn1.substring(34, 35));
    light8[7] = getInt(lightIn1.substring(35, 36));
    dark8[8] = getInt(lightIn1.substring(36, 37));
    light8[8] = getInt(lightIn1.substring(37, 38));
    dark8[9] = getInt(lightIn1.substring(38, 39));
    light8[9] = getInt(lightIn1.substring(39, 40));

    dark9[0] = getInt(lightIn1.substring(40, 41));
    light9[0] = getInt(lightIn1.substring(41, 42));
    dark9[1] = getInt(lightIn1.substring(42, 43));
    light9[1] = getInt(lightIn1.substring(43, 44));
    dark9[2] = getInt(lightIn1.substring(44, 45));
    light9[2] = getInt(lightIn1.substring(45, 46));
    dark9[3] = getInt(lightIn1.substring(46, 47));
    light9[3] = getInt(lightIn1.substring(47, 48));
    dark9[4] = getInt(lightIn1.substring(48, 49));
    light9[4] = getInt(lightIn1.substring(49, 50));
    dark9[5] = getInt(lightIn1.substring(50, 51));
    light9[5] = getInt(lightIn1.substring(51, 52));
    dark9[6] = getInt(lightIn1.substring(52, 53));
    light9[6] = getInt(lightIn1.substring(53, 54));
    dark9[7] = getInt(lightIn1.substring(54, 55));
    light9[7] = getInt(lightIn1.substring(55, 56));
    dark9[8] = getInt(lightIn1.substring(56, 57));
    light9[8] = getInt(lightIn1.substring(57, 58));
    dark9[9] = getInt(lightIn1.substring(58, 59));
    light9[9] = getInt(lightIn1.substring(59, 60));

    LightSet8=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark10[0] = getInt(lightIn1.substring(0, 1));
    light10[0] = getInt(lightIn1.substring(1, 2));
    dark10[1] = getInt(lightIn1.substring(2, 3));
    light10[1] = getInt(lightIn1.substring(3, 4));
    dark10[2] = getInt(lightIn1.substring(4, 5));
    light10[2] = getInt(lightIn1.substring(5, 6));
    dark10[3] = getInt(lightIn1.substring(6, 7));
    light10[3] = getInt(lightIn1.substring(7, 8));
    dark10[4] = getInt(lightIn1.substring(8, 9));
    light10[4] = getInt(lightIn1.substring(9, 10));
    dark10[5] = getInt(lightIn1.substring(10, 11));
    light10[5] = getInt(lightIn1.substring(11, 12));
    dark10[6] = getInt(lightIn1.substring(12, 13));
    light10[6] = getInt(lightIn1.substring(13, 14));
    dark10[7] = getInt(lightIn1.substring(14, 15));
    light10[7] = getInt(lightIn1.substring(15, 16));
    dark10[8] = getInt(lightIn1.substring(16, 17));
    light10[8] = getInt(lightIn1.substring(17, 18));
    dark10[9] = getInt(lightIn1.substring(18, 19));
    light10[9] = getInt(lightIn1.substring(19, 20));

    dark11[0] = getInt(lightIn1.substring(20, 21));
    light11[0] = getInt(lightIn1.substring(21, 22));
    dark11[1] = getInt(lightIn1.substring(22, 23));
    light11[1] = getInt(lightIn1.substring(23, 24));
    dark11[2] = getInt(lightIn1.substring(24, 25));
    light11[2] = getInt(lightIn1.substring(25, 26));
    dark11[3] = getInt(lightIn1.substring(26, 27));
    light11[3] = getInt(lightIn1.substring(27, 28));
    dark11[4] = getInt(lightIn1.substring(28, 29));
    light11[4] = getInt(lightIn1.substring(29, 30));
    dark11[5] = getInt(lightIn1.substring(30, 31));
    light11[5] = getInt(lightIn1.substring(31, 32));
    dark11[6] = getInt(lightIn1.substring(32, 33));
    light11[6] = getInt(lightIn1.substring(33, 34));
    dark11[7] = getInt(lightIn1.substring(34, 35));
    light11[7] = getInt(lightIn1.substring(35, 36));
    dark11[8] = getInt(lightIn1.substring(36, 37));
    light11[8] = getInt(lightIn1.substring(37, 38));
    dark11[9] = getInt(lightIn1.substring(38, 39));
    light11[9] = getInt(lightIn1.substring(39, 40));

    dark12[0] = getInt(lightIn1.substring(40, 41));
    light12[0] = getInt(lightIn1.substring(41, 42));
    dark12[1] = getInt(lightIn1.substring(42, 43));
    light12[1] = getInt(lightIn1.substring(43, 44));
    dark12[2] = getInt(lightIn1.substring(44, 45));
    light12[2] = getInt(lightIn1.substring(45, 46));
    dark12[3] = getInt(lightIn1.substring(46, 47));
    light12[3] = getInt(lightIn1.substring(47, 48));
    dark12[4] = getInt(lightIn1.substring(48, 49));
    light12[4] = getInt(lightIn1.substring(49, 50));
    dark12[5] = getInt(lightIn1.substring(50, 51));
    light12[5] = getInt(lightIn1.substring(51, 52));
    dark12[6] = getInt(lightIn1.substring(52, 53));
    light12[6] = getInt(lightIn1.substring(53, 54));
    dark12[7] = getInt(lightIn1.substring(54, 55));
    light12[7] = getInt(lightIn1.substring(55, 56));
    dark12[8] = getInt(lightIn1.substring(56, 57));
    light12[8] = getInt(lightIn1.substring(57, 58));
    dark12[9] = getInt(lightIn1.substring(58, 59));
    light12[9] = getInt(lightIn1.substring(59, 60));

    LightSet9=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark13[0] = getInt(lightIn1.substring(0, 1));
    light13[0] = getInt(lightIn1.substring(1, 2));
    dark13[1] = getInt(lightIn1.substring(2, 3));
    light13[1] = getInt(lightIn1.substring(3, 4));
    dark13[2] = getInt(lightIn1.substring(4, 5));
    light13[2] = getInt(lightIn1.substring(5, 6));
    dark13[3] = getInt(lightIn1.substring(6, 7));
    light13[3] = getInt(lightIn1.substring(7, 8));
    dark13[4] = getInt(lightIn1.substring(8, 9));
    light13[4] = getInt(lightIn1.substring(9, 10));
    dark13[5] = getInt(lightIn1.substring(10, 11));
    light13[5] = getInt(lightIn1.substring(11, 12));
    dark13[6] = getInt(lightIn1.substring(12, 13));
    light13[6] = getInt(lightIn1.substring(13, 14));
    dark13[7] = getInt(lightIn1.substring(14, 15));
    light13[7] = getInt(lightIn1.substring(15, 16));
    dark13[8] = getInt(lightIn1.substring(16, 17));
    light13[8] = getInt(lightIn1.substring(17, 18));
    dark13[9] = getInt(lightIn1.substring(18, 19));
    light13[9] = getInt(lightIn1.substring(19, 20));

    dark14[0] = getInt(lightIn1.substring(20, 21));
    light14[0] = getInt(lightIn1.substring(21, 22));
    dark14[1] = getInt(lightIn1.substring(22, 23));
    light14[1] = getInt(lightIn1.substring(23, 24));
    dark14[2] = getInt(lightIn1.substring(24, 25));
    light14[2] = getInt(lightIn1.substring(25, 26));
    dark14[3] = getInt(lightIn1.substring(26, 27));
    light14[3] = getInt(lightIn1.substring(27, 28));
    dark14[4] = getInt(lightIn1.substring(28, 29));
    light14[4] = getInt(lightIn1.substring(29, 30));
    dark14[5] = getInt(lightIn1.substring(30, 31));
    light14[5] = getInt(lightIn1.substring(31, 32));
    dark14[6] = getInt(lightIn1.substring(32, 33));
    light14[6] = getInt(lightIn1.substring(33, 34));
    dark14[7] = getInt(lightIn1.substring(34, 35));
    light14[7] = getInt(lightIn1.substring(35, 36));
    dark14[8] = getInt(lightIn1.substring(36, 37));
    light14[8] = getInt(lightIn1.substring(37, 38));
    dark14[9] = getInt(lightIn1.substring(38, 39));
    light14[9] = getInt(lightIn1.substring(39, 40));

    dark15[0] = getInt(lightIn1.substring(40, 41));
    light15[0] = getInt(lightIn1.substring(41, 42));
    dark15[1] = getInt(lightIn1.substring(42, 43));
    light15[1] = getInt(lightIn1.substring(43, 44));
    dark15[2] = getInt(lightIn1.substring(44, 45));
    light15[2] = getInt(lightIn1.substring(45, 46));
    dark15[3] = getInt(lightIn1.substring(46, 47));
    light15[3] = getInt(lightIn1.substring(47, 48));
    dark15[4] = getInt(lightIn1.substring(48, 49));
    light15[4] = getInt(lightIn1.substring(49, 50));
    dark15[5] = getInt(lightIn1.substring(50, 51));
    light15[5] = getInt(lightIn1.substring(51, 52));
    dark15[6] = getInt(lightIn1.substring(52, 53));
    light15[6] = getInt(lightIn1.substring(53, 54));
    dark15[7] = getInt(lightIn1.substring(54, 55));
    light15[7] = getInt(lightIn1.substring(55, 56));
    dark15[8] = getInt(lightIn1.substring(56, 57));
    light15[8] = getInt(lightIn1.substring(57, 58));
    dark15[9] = getInt(lightIn1.substring(58, 59));
    light15[9] = getInt(lightIn1.substring(59, 60));

    LightSet10=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark16[0] = getInt(lightIn1.substring(0, 1));
    light16[0] = getInt(lightIn1.substring(1, 2));
    dark16[1] = getInt(lightIn1.substring(2, 3));
    light16[1] = getInt(lightIn1.substring(3, 4));
    dark16[2] = getInt(lightIn1.substring(4, 5));
    light16[2] = getInt(lightIn1.substring(5, 6));
    dark16[3] = getInt(lightIn1.substring(6, 7));
    light16[3] = getInt(lightIn1.substring(7, 8));
    dark16[4] = getInt(lightIn1.substring(8, 9));
    light16[4] = getInt(lightIn1.substring(9, 10));
    dark16[5] = getInt(lightIn1.substring(10, 11));
    light16[5] = getInt(lightIn1.substring(11, 12));
    dark16[6] = getInt(lightIn1.substring(12, 13));
    light16[6] = getInt(lightIn1.substring(13, 14));
    dark16[7] = getInt(lightIn1.substring(14, 15));
    light16[7] = getInt(lightIn1.substring(15, 16));
    dark16[8] = getInt(lightIn1.substring(16, 17));
    light16[8] = getInt(lightIn1.substring(17, 18));
    dark16[9] = getInt(lightIn1.substring(18, 19));
    light16[9] = getInt(lightIn1.substring(19, 20));

    dark17[0] = getInt(lightIn1.substring(20, 21));
    light17[0] = getInt(lightIn1.substring(21, 22));
    dark17[1] = getInt(lightIn1.substring(22, 23));
    light17[1] = getInt(lightIn1.substring(23, 24));
    dark17[2] = getInt(lightIn1.substring(24, 25));
    light17[2] = getInt(lightIn1.substring(25, 26));
    dark17[3] = getInt(lightIn1.substring(26, 27));
    light17[3] = getInt(lightIn1.substring(27, 28));
    dark17[4] = getInt(lightIn1.substring(28, 29));
    light17[4] = getInt(lightIn1.substring(29, 30));
    dark17[5] = getInt(lightIn1.substring(30, 31));
    light17[5] = getInt(lightIn1.substring(31, 32));
    dark17[6] = getInt(lightIn1.substring(32, 33));
    light17[6] = getInt(lightIn1.substring(33, 34));
    dark17[7] = getInt(lightIn1.substring(34, 35));
    light17[7] = getInt(lightIn1.substring(35, 36));
    dark17[8] = getInt(lightIn1.substring(36, 37));
    light17[8] = getInt(lightIn1.substring(37, 38));
    dark17[9] = getInt(lightIn1.substring(38, 39));
    light17[9] = getInt(lightIn1.substring(39, 40));

    dark18[0] = getInt(lightIn1.substring(40, 41));
    light18[0] = getInt(lightIn1.substring(41, 42));
    dark18[1] = getInt(lightIn1.substring(42, 43));
    light18[1] = getInt(lightIn1.substring(43, 44));
    dark18[2] = getInt(lightIn1.substring(44, 45));
    light18[2] = getInt(lightIn1.substring(45, 46));
    dark18[3] = getInt(lightIn1.substring(46, 47));
    light18[3] = getInt(lightIn1.substring(47, 48));
    dark18[4] = getInt(lightIn1.substring(48, 49));
    light18[4] = getInt(lightIn1.substring(49, 50));
    dark18[5] = getInt(lightIn1.substring(50, 51));
    light18[5] = getInt(lightIn1.substring(51, 52));
    dark18[6] = getInt(lightIn1.substring(52, 53));
    light18[6] = getInt(lightIn1.substring(53, 54));
    dark18[7] = getInt(lightIn1.substring(54, 55));
    light18[7] = getInt(lightIn1.substring(55, 56));
    dark18[8] = getInt(lightIn1.substring(56, 57));
    light18[8] = getInt(lightIn1.substring(57, 58));
    dark18[9] = getInt(lightIn1.substring(58, 59));
    light18[9] = getInt(lightIn1.substring(59, 60));

    LightSet11=1;
  }

  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    dark19[0] = getInt(lightIn1.substring(0, 1));
    light19[0] = getInt(lightIn1.substring(1, 2));
    dark19[1] = getInt(lightIn1.substring(2, 3));
    light19[1] = getInt(lightIn1.substring(3, 4));
    dark19[2] = getInt(lightIn1.substring(4, 5));
    light19[2] = getInt(lightIn1.substring(5, 6));
    dark19[3] = getInt(lightIn1.substring(6, 7));
    light19[3] = getInt(lightIn1.substring(7, 8));
    dark19[4] = getInt(lightIn1.substring(8, 9));
    light19[4] = getInt(lightIn1.substring(9, 10));
    dark19[5] = getInt(lightIn1.substring(10, 11));
    light19[5] = getInt(lightIn1.substring(11, 12));
    dark19[6] = getInt(lightIn1.substring(12, 13));
    light19[6] = getInt(lightIn1.substring(13, 14));
    dark19[7] = getInt(lightIn1.substring(14, 15));
    light19[7] = getInt(lightIn1.substring(15, 16));
    dark19[8] = getInt(lightIn1.substring(16, 17));
    light19[8] = getInt(lightIn1.substring(17, 18));
    dark19[9] = getInt(lightIn1.substring(18, 19));
    light19[9] = getInt(lightIn1.substring(19, 20));

    dark20[0] = getInt(lightIn1.substring(20, 21));
    light20[0] = getInt(lightIn1.substring(21, 22));
    dark20[1] = getInt(lightIn1.substring(22, 23));
    light20[1] = getInt(lightIn1.substring(23, 24));
    dark20[2] = getInt(lightIn1.substring(24, 25));
    light20[2] = getInt(lightIn1.substring(25, 26));
    dark20[3] = getInt(lightIn1.substring(26, 27));
    light20[3] = getInt(lightIn1.substring(27, 28));
    dark20[4] = getInt(lightIn1.substring(28, 29));
    light20[4] = getInt(lightIn1.substring(29, 30));
    dark20[5] = getInt(lightIn1.substring(30, 31));
    light20[5] = getInt(lightIn1.substring(31, 32));
    dark20[6] = getInt(lightIn1.substring(32, 33));
    light20[6] = getInt(lightIn1.substring(33, 34));
    dark20[7] = getInt(lightIn1.substring(34, 35));
    light20[7] = getInt(lightIn1.substring(35, 36));
    dark20[8] = getInt(lightIn1.substring(36, 37));
    light20[8] = getInt(lightIn1.substring(37, 38));
    dark20[9] = getInt(lightIn1.substring(38, 39));
    light20[9] = getInt(lightIn1.substring(39, 40));

    LightSet12=1;
  }
    
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);

    HourOn4[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn4[0] = getInt(lightIn1.substring(2, 4));
    HourOn4[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn4[1] = getInt(lightIn1.substring(6, 8));
    HourOn4[2] = getInt(lightIn1.substring(8, 10));
    MinuteOn4[2] = getInt(lightIn1.substring(10, 12));
    HourOn4[3] = getInt(lightIn1.substring(12, 14));
    MinuteOn4[3] = getInt(lightIn1.substring(14, 16));
    HourOn4[4] = getInt(lightIn1.substring(16, 18));
    MinuteOn4[4] = getInt(lightIn1.substring(18, 20));
    HourOn4[5] = getInt(lightIn1.substring(20, 22));
    MinuteOn4[5] = getInt(lightIn1.substring(22, 24));
    HourOn4[6] = getInt(lightIn1.substring(24, 26));
    MinuteOn4[6] = getInt(lightIn1.substring(26, 28));
    HourOn4[7] = getInt(lightIn1.substring(28, 30));
    MinuteOn4[7] = getInt(lightIn1.substring(30, 32));
    HourOn4[8] = getInt(lightIn1.substring(32, 34));
    MinuteOn4[8] = getInt(lightIn1.substring(34, 36));
    HourOn4[9] = getInt(lightIn1.substring(36, 38));
    MinuteOn4[9] = getInt(lightIn1.substring(38, 40));

    RatioOn4[0] = getInt(lightIn1.substring(40, 42));
    RatioOff4[0] = getInt(lightIn1.substring(42, 44));
    RatioOn4[1] = getInt(lightIn1.substring(44, 46));
    RatioOff4[1] = getInt(lightIn1.substring(46, 48));
    RatioOn4[2] = getInt(lightIn1.substring(48, 50));
    RatioOff4[2] = getInt(lightIn1.substring(50, 52));
    RatioOn4[3] = getInt(lightIn1.substring(52, 54));
    RatioOff4[3] = getInt(lightIn1.substring(54, 56));
    RatioOn4[4] = getInt(lightIn1.substring(56, 58));
    RatioOff4[4] = getInt(lightIn1.substring(58, 60));

    LightSet13=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn4[5] = getInt(lightIn1.substring(0, 2));
    RatioOff4[5] = getInt(lightIn1.substring(2, 4));
    RatioOn4[6] = getInt(lightIn1.substring(4, 6));
    RatioOff4[6] = getInt(lightIn1.substring(6, 8));
    RatioOn4[7] = getInt(lightIn1.substring(8, 10));
    RatioOff4[7] = getInt(lightIn1.substring(10, 12));
    RatioOn4[8] = getInt(lightIn1.substring(12, 14));
    RatioOff4[8] = getInt(lightIn1.substring(14, 16));
    RatioOn4[9] = getInt(lightIn1.substring(16, 18));
    RatioOff4[9] = getInt(lightIn1.substring(18, 20));

    HourOn5[0] = getInt(lightIn1.substring(20, 22));
    MinuteOn5[0] = getInt(lightIn1.substring(22, 24));
    HourOn5[1] = getInt(lightIn1.substring(24, 26));
    MinuteOn5[1] = getInt(lightIn1.substring(26, 28));
    HourOn5[2] = getInt(lightIn1.substring(28, 30));
    MinuteOn5[2] = getInt(lightIn1.substring(30, 32));
    HourOn5[3] = getInt(lightIn1.substring(32, 34));
    MinuteOn5[3] = getInt(lightIn1.substring(34, 36));
    HourOn5[4] = getInt(lightIn1.substring(36, 38));
    MinuteOn5[4] = getInt(lightIn1.substring(38, 40));

    HourOn5[5] = getInt(lightIn1.substring(40, 42));
    MinuteOn5[5] = getInt(lightIn1.substring(42, 44));
    HourOn5[6] = getInt(lightIn1.substring(44, 46));
    MinuteOn5[6] = getInt(lightIn1.substring(46, 48));
    HourOn5[7] = getInt(lightIn1.substring(48, 50));
    MinuteOn5[7] = getInt(lightIn1.substring(50, 52));
    HourOn5[8] = getInt(lightIn1.substring(52, 54));
    MinuteOn5[8] = getInt(lightIn1.substring(54, 56));
    HourOn5[9] = getInt(lightIn1.substring(56, 58));
    MinuteOn5[9] = getInt(lightIn1.substring(58, 60));

    LightSet14=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn5[0] = getInt(lightIn1.substring(0, 2));
    RatioOff5[0] = getInt(lightIn1.substring(2, 4));
    RatioOn5[1] = getInt(lightIn1.substring(4, 6));
    RatioOff5[1] = getInt(lightIn1.substring(6, 8));
    RatioOn5[2] = getInt(lightIn1.substring(8, 10));
    RatioOff5[2] = getInt(lightIn1.substring(10, 12));
    RatioOn5[3] = getInt(lightIn1.substring(12, 14));
    RatioOff5[3] = getInt(lightIn1.substring(14, 16));
    RatioOn5[4] = getInt(lightIn1.substring(16, 18));
    RatioOff5[4] = getInt(lightIn1.substring(18, 20));

    RatioOn5[5] = getInt(lightIn1.substring(20, 22));
    RatioOff5[5] = getInt(lightIn1.substring(22, 24));
    RatioOn5[6] = getInt(lightIn1.substring(24, 26));
    RatioOff5[6] = getInt(lightIn1.substring(26, 28));
    RatioOn5[7] = getInt(lightIn1.substring(28, 30));
    RatioOff5[7] = getInt(lightIn1.substring(30, 32));
    RatioOn5[8] = getInt(lightIn1.substring(32, 34));
    RatioOff5[8] = getInt(lightIn1.substring(34, 36));
    RatioOn5[9] = getInt(lightIn1.substring(36, 38));
    RatioOff5[9] = getInt(lightIn1.substring(38, 40));

    HourOn6[0] = getInt(lightIn1.substring(40, 42));
    MinuteOn6[0] = getInt(lightIn1.substring(42, 44));
    HourOn6[1] = getInt(lightIn1.substring(44, 46));
    MinuteOn6[1] = getInt(lightIn1.substring(46, 48));
    HourOn6[2] = getInt(lightIn1.substring(48, 50));
    MinuteOn6[2] = getInt(lightIn1.substring(50, 52));
    HourOn6[3] = getInt(lightIn1.substring(52, 54));
    MinuteOn6[3] = getInt(lightIn1.substring(54, 56));
    HourOn6[4] = getInt(lightIn1.substring(56, 58));
    MinuteOn6[4] = getInt(lightIn1.substring(58, 60));

    LightSet15=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn6[5] = getInt(lightIn1.substring(0, 2));
    MinuteOn6[5] = getInt(lightIn1.substring(2, 4));
    HourOn6[6] = getInt(lightIn1.substring(4, 6));
    MinuteOn6[6] = getInt(lightIn1.substring(6, 8));
    HourOn6[7] = getInt(lightIn1.substring(8, 10));
    MinuteOn6[7] = getInt(lightIn1.substring(10, 12));
    HourOn6[8] = getInt(lightIn1.substring(12, 14));
    MinuteOn6[8] = getInt(lightIn1.substring(14, 16));
    HourOn6[9] = getInt(lightIn1.substring(16, 18));
    MinuteOn6[9] = getInt(lightIn1.substring(18, 20));

    RatioOn6[0] = getInt(lightIn1.substring(20, 22));
    RatioOff6[0] = getInt(lightIn1.substring(22, 24));
    RatioOn6[1] = getInt(lightIn1.substring(24, 26));
    RatioOff6[1] = getInt(lightIn1.substring(26, 28));
    RatioOn6[2] = getInt(lightIn1.substring(28, 30));
    RatioOff6[2] = getInt(lightIn1.substring(30, 32));
    RatioOn6[3] = getInt(lightIn1.substring(32, 34));
    RatioOff6[3] = getInt(lightIn1.substring(34, 36));
    RatioOn6[4] = getInt(lightIn1.substring(36, 38));
    RatioOff6[4] = getInt(lightIn1.substring(38, 40));

    RatioOn6[5] = getInt(lightIn1.substring(40, 42));
    RatioOff6[5] = getInt(lightIn1.substring(42, 44));
    RatioOn6[6] = getInt(lightIn1.substring(44, 46));
    RatioOff6[6] = getInt(lightIn1.substring(46, 48));
    RatioOn6[7] = getInt(lightIn1.substring(48, 50));
    RatioOff6[7] = getInt(lightIn1.substring(50, 52));
    RatioOn6[8] = getInt(lightIn1.substring(52, 54));
    RatioOff6[8] = getInt(lightIn1.substring(54, 56));
    RatioOn6[9] = getInt(lightIn1.substring(56, 58));
    RatioOff6[9] = getInt(lightIn1.substring(58, 60));

    LightSet16=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 ==0 )
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn7[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn7[0] = getInt(lightIn1.substring(2, 4));
    HourOn7[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn7[1] = getInt(lightIn1.substring(6, 8));
    HourOn7[2] = getInt(lightIn1.substring(8, 10));
    MinuteOn7[2] = getInt(lightIn1.substring(10, 12));
    HourOn7[3] = getInt(lightIn1.substring(12, 14));
    MinuteOn7[3] = getInt(lightIn1.substring(14, 16));
    HourOn7[4] = getInt(lightIn1.substring(16, 18));
    MinuteOn7[4] = getInt(lightIn1.substring(18, 20));

    HourOn7[5] = getInt(lightIn1.substring(20, 22));
    MinuteOn7[5] = getInt(lightIn1.substring(22, 24));
    HourOn7[6] = getInt(lightIn1.substring(24, 26));
    MinuteOn7[6] = getInt(lightIn1.substring(26, 28));
    HourOn7[7] = getInt(lightIn1.substring(28, 30));
    MinuteOn7[7] = getInt(lightIn1.substring(30, 32));
    HourOn7[8] = getInt(lightIn1.substring(32, 34));
    MinuteOn7[8] = getInt(lightIn1.substring(34, 36));
    HourOn7[9] = getInt(lightIn1.substring(36, 38));
    MinuteOn7[9] = getInt(lightIn1.substring(38, 40));

    RatioOn7[0] = getInt(lightIn1.substring(40, 42));
    RatioOff7[0] = getInt(lightIn1.substring(42, 44));
    RatioOn7[1] = getInt(lightIn1.substring(44, 46));
    RatioOff7[1] = getInt(lightIn1.substring(46, 48));
    RatioOn7[2] = getInt(lightIn1.substring(48, 50));
    RatioOff7[2] = getInt(lightIn1.substring(50, 52));
    RatioOn7[3] = getInt(lightIn1.substring(52, 54));
    RatioOff7[3] = getInt(lightIn1.substring(54, 56));
    RatioOn7[4] = getInt(lightIn1.substring(56, 58));
    RatioOff7[4] = getInt(lightIn1.substring(58, 60));

    LightSet17=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 0 )
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn7[5] = getInt(lightIn1.substring(0, 2));
    RatioOff7[5] = getInt(lightIn1.substring(2, 4));
    RatioOn7[6] = getInt(lightIn1.substring(4, 6));
    RatioOff7[6] = getInt(lightIn1.substring(6, 8));
    RatioOn7[7] = getInt(lightIn1.substring(8, 10));
    RatioOff7[7] = getInt(lightIn1.substring(10, 12));
    RatioOn7[8] = getInt(lightIn1.substring(12, 14));
    RatioOff7[8] = getInt(lightIn1.substring(14, 16));
    RatioOn7[9] = getInt(lightIn1.substring(16, 18));
    RatioOff7[9] = getInt(lightIn1.substring(18, 20));

    HourOn8[0] = getInt(lightIn1.substring(20, 22));
    MinuteOn8[0] = getInt(lightIn1.substring(22, 24));
    HourOn8[1] = getInt(lightIn1.substring(24, 26));
    MinuteOn8[1] = getInt(lightIn1.substring(26, 28));
    HourOn8[2] = getInt(lightIn1.substring(28, 30));
    MinuteOn8[2] = getInt(lightIn1.substring(30, 32));
    HourOn8[3] = getInt(lightIn1.substring(32, 34));
    MinuteOn8[3] = getInt(lightIn1.substring(34, 36));
    HourOn8[4] = getInt(lightIn1.substring(36, 38));
    MinuteOn8[4] = getInt(lightIn1.substring(38, 40));

    HourOn8[5] = getInt(lightIn1.substring(40, 42));
    MinuteOn8[5] = getInt(lightIn1.substring(42, 44));
    HourOn8[6] = getInt(lightIn1.substring(44, 46));
    MinuteOn8[6] = getInt(lightIn1.substring(46, 48));
    HourOn8[7] = getInt(lightIn1.substring(48, 50));
    MinuteOn8[7] = getInt(lightIn1.substring(50, 52));
    HourOn8[8] = getInt(lightIn1.substring(52, 54));
    MinuteOn8[8] = getInt(lightIn1.substring(54, 56));
    HourOn8[9] = getInt(lightIn1.substring(56, 58));
    MinuteOn8[9] = getInt(lightIn1.substring(58, 60));

    LightSet18=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn8[0] = getInt(lightIn1.substring(0, 2));
    RatioOff8[0] = getInt(lightIn1.substring(2, 4));
    RatioOn8[1] = getInt(lightIn1.substring(4, 6));
    RatioOff8[1] = getInt(lightIn1.substring(6, 8));
    RatioOn8[2] = getInt(lightIn1.substring(8, 10));
    RatioOff8[2] = getInt(lightIn1.substring(10, 12));
    RatioOn8[3] = getInt(lightIn1.substring(12, 14));
    RatioOff8[3] = getInt(lightIn1.substring(14, 16));
    RatioOn8[4] = getInt(lightIn1.substring(16, 18));
    RatioOff8[4] = getInt(lightIn1.substring(18, 20));

    RatioOn8[5] = getInt(lightIn1.substring(20, 22));
    RatioOff8[5] = getInt(lightIn1.substring(22, 24));
    RatioOn8[6] = getInt(lightIn1.substring(24, 26));
    RatioOff8[6] = getInt(lightIn1.substring(26, 28));
    RatioOn8[7] = getInt(lightIn1.substring(28, 30));
    RatioOff8[7] = getInt(lightIn1.substring(30, 32));
    RatioOn8[8] = getInt(lightIn1.substring(32, 34));
    RatioOff8[8] = getInt(lightIn1.substring(34, 36));
    RatioOn8[9] = getInt(lightIn1.substring(36, 38));
    RatioOff8[9] = getInt(lightIn1.substring(38, 40));

    HourOn9[0] = getInt(lightIn1.substring(40, 42));
    MinuteOn9[0] = getInt(lightIn1.substring(42, 44));
    HourOn9[1] = getInt(lightIn1.substring(44, 46));
    MinuteOn9[1] = getInt(lightIn1.substring(46, 48));
    HourOn9[2] = getInt(lightIn1.substring(48, 50));
    MinuteOn9[2] = getInt(lightIn1.substring(50, 52));
    HourOn9[3] = getInt(lightIn1.substring(52, 54));
    MinuteOn9[3] = getInt(lightIn1.substring(54, 56));
    HourOn9[4] = getInt(lightIn1.substring(56, 58));
    MinuteOn9[4] = getInt(lightIn1.substring(58, 60));

    LightSet19=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn9[5] = getInt(lightIn1.substring(0, 2));
    MinuteOn9[5] = getInt(lightIn1.substring(2, 4));
    HourOn9[6] = getInt(lightIn1.substring(4, 6));
    MinuteOn9[6] = getInt(lightIn1.substring(6, 8));
    HourOn9[7] = getInt(lightIn1.substring(8, 10));
    MinuteOn9[7] = getInt(lightIn1.substring(10, 12));
    HourOn9[8] = getInt(lightIn1.substring(12, 14));
    MinuteOn9[8] = getInt(lightIn1.substring(14, 16));
    HourOn9[9] = getInt(lightIn1.substring(16, 18));
    MinuteOn9[9] = getInt(lightIn1.substring(18, 20));

    RatioOn9[0] = getInt(lightIn1.substring(20, 22));
    RatioOff9[0] = getInt(lightIn1.substring(22, 24));
    RatioOn9[1] = getInt(lightIn1.substring(24, 26));
    RatioOff9[1] = getInt(lightIn1.substring(26, 28));
    RatioOn9[2] = getInt(lightIn1.substring(28, 30));
    RatioOff9[2] = getInt(lightIn1.substring(30, 32));
    RatioOn9[3] = getInt(lightIn1.substring(32, 34));
    RatioOff9[3] = getInt(lightIn1.substring(34, 36));
    RatioOn9[4] = getInt(lightIn1.substring(36, 38));
    RatioOff9[4] = getInt(lightIn1.substring(38, 40));

    RatioOn9[5] = getInt(lightIn1.substring(40, 42));
    RatioOff9[5] = getInt(lightIn1.substring(42, 44));
    RatioOn9[6] = getInt(lightIn1.substring(44, 46));
    RatioOff9[6] = getInt(lightIn1.substring(46, 48));
    RatioOn9[7] = getInt(lightIn1.substring(48, 50));
    RatioOff9[7] = getInt(lightIn1.substring(50, 52));
    RatioOn9[8] = getInt(lightIn1.substring(52, 54));
    RatioOff9[8] = getInt(lightIn1.substring(54, 56));
    RatioOn9[9] = getInt(lightIn1.substring(56, 58));
    RatioOff9[9] = getInt(lightIn1.substring(58, 60));

    LightSet20=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn10[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn10[0] = getInt(lightIn1.substring(2, 4));
    HourOn10[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn10[1] = getInt(lightIn1.substring(6, 8));
    HourOn10[2] = getInt(lightIn1.substring(8, 10));
    MinuteOn10[2] = getInt(lightIn1.substring(10, 12));
    HourOn10[3] = getInt(lightIn1.substring(12, 14));
    MinuteOn10[3] = getInt(lightIn1.substring(14, 16));
    HourOn10[4] = getInt(lightIn1.substring(16, 18));
    MinuteOn10[4] = getInt(lightIn1.substring(18, 20));

    HourOn10[5] = getInt(lightIn1.substring(20, 22));
    MinuteOn10[5] = getInt(lightIn1.substring(22, 24));
    HourOn10[6] = getInt(lightIn1.substring(24, 26));
    MinuteOn10[6] = getInt(lightIn1.substring(26, 28));
    HourOn10[7] = getInt(lightIn1.substring(28, 30));
    MinuteOn10[7] = getInt(lightIn1.substring(30, 32));
    HourOn10[8] = getInt(lightIn1.substring(32, 34));
    MinuteOn10[8] = getInt(lightIn1.substring(34, 36));
    HourOn10[9] = getInt(lightIn1.substring(36, 38));
    MinuteOn10[9] = getInt(lightIn1.substring(38, 40));

    RatioOn10[0] = getInt(lightIn1.substring(40, 42));
    RatioOff10[0] = getInt(lightIn1.substring(42, 44));
    RatioOn10[1] = getInt(lightIn1.substring(44, 46));
    RatioOff10[1] = getInt(lightIn1.substring(46, 48));
    RatioOn10[2] = getInt(lightIn1.substring(48, 50));
    RatioOff10[2] = getInt(lightIn1.substring(50, 52));
    RatioOn10[3] = getInt(lightIn1.substring(52, 54));
    RatioOff10[3] = getInt(lightIn1.substring(54, 56));
    RatioOn10[4] = getInt(lightIn1.substring(56, 58));
    RatioOff10[4] = getInt(lightIn1.substring(58, 60));

    LightSet21=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn10[5] = getInt(lightIn1.substring(0, 2));
    RatioOff10[5] = getInt(lightIn1.substring(2, 4));
    RatioOn10[6] = getInt(lightIn1.substring(4, 6));
    RatioOff10[6] = getInt(lightIn1.substring(6, 8));
    RatioOn10[7] = getInt(lightIn1.substring(8, 10));
    RatioOff10[7] = getInt(lightIn1.substring(10, 12));
    RatioOn10[8] = getInt(lightIn1.substring(12, 14));
    RatioOff10[8] = getInt(lightIn1.substring(14, 16));
    RatioOn10[9] = getInt(lightIn1.substring(16, 18));
    RatioOff10[9] = getInt(lightIn1.substring(18, 20));

    HourOn11[0] = getInt(lightIn1.substring(20, 22));
    MinuteOn11[0] = getInt(lightIn1.substring(22, 24));
    HourOn11[1] = getInt(lightIn1.substring(24, 26));
    MinuteOn11[1] = getInt(lightIn1.substring(26, 28));
    HourOn11[2] = getInt(lightIn1.substring(28, 30));
    MinuteOn11[2] = getInt(lightIn1.substring(30, 32));
    HourOn11[3] = getInt(lightIn1.substring(32, 34));
    MinuteOn11[3] = getInt(lightIn1.substring(34, 36));
    HourOn11[4] = getInt(lightIn1.substring(36, 38));
    MinuteOn11[4] = getInt(lightIn1.substring(38, 40));

    HourOn11[5] = getInt(lightIn1.substring(40, 42));
    MinuteOn11[5] = getInt(lightIn1.substring(42, 44));
    HourOn11[6] = getInt(lightIn1.substring(44, 46));
    MinuteOn11[6] = getInt(lightIn1.substring(46, 48));
    HourOn11[7] = getInt(lightIn1.substring(48, 50));
    MinuteOn11[7] = getInt(lightIn1.substring(50, 52));
    HourOn11[8] = getInt(lightIn1.substring(52, 54));
    MinuteOn11[8] = getInt(lightIn1.substring(54, 56));
    HourOn11[9] = getInt(lightIn1.substring(56, 58));
    MinuteOn11[9] = getInt(lightIn1.substring(58, 60));
    
    LightSet22=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn11[0] = getInt(lightIn1.substring(0, 2));
    RatioOff11[0] = getInt(lightIn1.substring(2, 4));
    RatioOn11[1] = getInt(lightIn1.substring(4, 6));
    RatioOff11[1] = getInt(lightIn1.substring(6, 8));
    RatioOn11[2] = getInt(lightIn1.substring(8, 10));
    RatioOff11[2] = getInt(lightIn1.substring(10, 12));
    RatioOn11[3] = getInt(lightIn1.substring(12, 14));
    RatioOff11[3] = getInt(lightIn1.substring(14, 16));
    RatioOn11[4] = getInt(lightIn1.substring(16, 18));
    RatioOff11[4] = getInt(lightIn1.substring(18, 20));

    RatioOn11[5] = getInt(lightIn1.substring(20, 22));
    RatioOff11[5] = getInt(lightIn1.substring(22, 24));
    RatioOn11[6] = getInt(lightIn1.substring(24, 26));
    RatioOff11[6] = getInt(lightIn1.substring(26, 28));
    RatioOn11[7] = getInt(lightIn1.substring(28, 30));
    RatioOff11[7] = getInt(lightIn1.substring(30, 32));
    RatioOn11[8] = getInt(lightIn1.substring(32, 34));
    RatioOff11[8] = getInt(lightIn1.substring(34, 36));
    RatioOn11[9] = getInt(lightIn1.substring(36, 38));
    RatioOff11[9] = getInt(lightIn1.substring(38, 40));

    HourOn12[0] = getInt(lightIn1.substring(40, 42));
    MinuteOn12[0] = getInt(lightIn1.substring(42, 44));
    HourOn12[1] = getInt(lightIn1.substring(44, 46));
    MinuteOn12[1] = getInt(lightIn1.substring(46, 48));
    HourOn12[2] = getInt(lightIn1.substring(48, 50));
    MinuteOn12[2] = getInt(lightIn1.substring(50, 52));
    HourOn12[3] = getInt(lightIn1.substring(52, 54));
    MinuteOn12[3] = getInt(lightIn1.substring(54, 56));
    HourOn12[4] = getInt(lightIn1.substring(56, 58));
    MinuteOn12[4] = getInt(lightIn1.substring(58, 60));
    
    LightSet23=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn12[5] = getInt(lightIn1.substring(0, 2));
    MinuteOn12[5] = getInt(lightIn1.substring(2, 4));
    HourOn12[6] = getInt(lightIn1.substring(4, 6));
    MinuteOn12[6] = getInt(lightIn1.substring(6, 8));
    HourOn12[7] = getInt(lightIn1.substring(8, 10));
    MinuteOn12[7] = getInt(lightIn1.substring(10, 12));
    HourOn12[8] = getInt(lightIn1.substring(12, 14));
    MinuteOn12[8] = getInt(lightIn1.substring(14, 16));
    HourOn12[9] = getInt(lightIn1.substring(16, 18));
    MinuteOn12[9] = getInt(lightIn1.substring(18, 20));

    RatioOn12[0] = getInt(lightIn1.substring(20, 22));
    RatioOff12[0] = getInt(lightIn1.substring(22, 24));
    RatioOn12[1] = getInt(lightIn1.substring(24, 26));
    RatioOff12[1] = getInt(lightIn1.substring(26, 28));
    RatioOn12[2] = getInt(lightIn1.substring(28, 30));
    RatioOff12[2] = getInt(lightIn1.substring(30, 32));
    RatioOn12[3] = getInt(lightIn1.substring(32, 34));
    RatioOff12[3] = getInt(lightIn1.substring(34, 36));
    RatioOn12[4] = getInt(lightIn1.substring(36, 38));
    RatioOff12[4] = getInt(lightIn1.substring(38, 40));

    RatioOn12[5] = getInt(lightIn1.substring(40, 42));
    RatioOff12[5] = getInt(lightIn1.substring(42, 44));
    RatioOn12[6] = getInt(lightIn1.substring(44, 46));
    RatioOff12[6] = getInt(lightIn1.substring(46, 48));
    RatioOn12[7] = getInt(lightIn1.substring(48, 50));
    RatioOff12[7] = getInt(lightIn1.substring(50, 52));
    RatioOn12[8] = getInt(lightIn1.substring(52, 54));
    RatioOff12[8] = getInt(lightIn1.substring(54, 56));
    RatioOn12[9] = getInt(lightIn1.substring(56, 58));
    RatioOff12[9] = getInt(lightIn1.substring(58, 60));
    
    LightSet24=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn13[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn13[0] = getInt(lightIn1.substring(2, 4));
    HourOn13[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn13[1] = getInt(lightIn1.substring(6, 8));
    HourOn13[2] = getInt(lightIn1.substring(8, 10));
    MinuteOn13[2] = getInt(lightIn1.substring(10, 12));
    HourOn13[3] = getInt(lightIn1.substring(12, 14));
    MinuteOn13[3] = getInt(lightIn1.substring(14, 16));
    HourOn13[4] = getInt(lightIn1.substring(16, 18));
    MinuteOn13[4] = getInt(lightIn1.substring(18, 20));

    HourOn13[5] = getInt(lightIn1.substring(20, 22));
    MinuteOn13[5] = getInt(lightIn1.substring(22, 24));
    HourOn13[6] = getInt(lightIn1.substring(24, 26));
    MinuteOn13[6] = getInt(lightIn1.substring(26, 28));
    HourOn13[7] = getInt(lightIn1.substring(28, 30));
    MinuteOn13[7] = getInt(lightIn1.substring(30, 32));
    HourOn13[8] = getInt(lightIn1.substring(32, 34));
    MinuteOn13[8] = getInt(lightIn1.substring(34, 36));
    HourOn13[9] = getInt(lightIn1.substring(36, 38));
    MinuteOn13[9] = getInt(lightIn1.substring(38, 40));

    RatioOn13[0] = getInt(lightIn1.substring(40, 42));
    RatioOff13[0] = getInt(lightIn1.substring(42, 44));
    RatioOn13[1] = getInt(lightIn1.substring(44, 46));
    RatioOff13[1] = getInt(lightIn1.substring(46, 48));
    RatioOn13[2] = getInt(lightIn1.substring(48, 50));
    RatioOff13[2] = getInt(lightIn1.substring(50, 52));
    RatioOn13[3] = getInt(lightIn1.substring(52, 54));
    RatioOff13[3] = getInt(lightIn1.substring(54, 56));
    RatioOn13[4] = getInt(lightIn1.substring(56, 58));
    RatioOff13[4] = getInt(lightIn1.substring(58, 60));
    
    LightSet25=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn13[5] = getInt(lightIn1.substring(0, 2));
    RatioOff13[5] = getInt(lightIn1.substring(2, 4));
    RatioOn13[6] = getInt(lightIn1.substring(4, 6));
    RatioOff13[6] = getInt(lightIn1.substring(6, 8));
    RatioOn13[7] = getInt(lightIn1.substring(8, 10));
    RatioOff13[7] = getInt(lightIn1.substring(10, 12));
    RatioOn13[8] = getInt(lightIn1.substring(12, 14));
    RatioOff13[8] = getInt(lightIn1.substring(14, 16));
    RatioOn13[9] = getInt(lightIn1.substring(16, 18));
    RatioOff13[9] = getInt(lightIn1.substring(18, 20));
    
    HourOn14[0] = getInt(lightIn1.substring(20, 22));
    MinuteOn14[0] = getInt(lightIn1.substring(22, 24));
    HourOn14[1] = getInt(lightIn1.substring(24, 26));
    MinuteOn14[1] = getInt(lightIn1.substring(26, 28));
    HourOn14[2] = getInt(lightIn1.substring(28, 30));
    MinuteOn14[2] = getInt(lightIn1.substring(30, 32));
    HourOn14[3] = getInt(lightIn1.substring(32, 34));
    MinuteOn14[3] = getInt(lightIn1.substring(34, 36));
    HourOn14[4] = getInt(lightIn1.substring(36, 38));
    MinuteOn14[4] = getInt(lightIn1.substring(38, 40));

    HourOn14[5] = getInt(lightIn1.substring(40, 42));
    MinuteOn14[5] = getInt(lightIn1.substring(42, 44));
    HourOn14[6] = getInt(lightIn1.substring(44, 46));
    MinuteOn14[6] = getInt(lightIn1.substring(46, 48));
    HourOn14[7] = getInt(lightIn1.substring(48, 50));
    MinuteOn14[7] = getInt(lightIn1.substring(50, 52));
    HourOn14[8] = getInt(lightIn1.substring(52, 54));
    MinuteOn14[8] = getInt(lightIn1.substring(54, 56));
    HourOn14[9] = getInt(lightIn1.substring(56, 58));
    MinuteOn14[9] = getInt(lightIn1.substring(58, 60));
    
    LightSet26=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn14[0] = getInt(lightIn1.substring(0, 2));
    RatioOff14[0] = getInt(lightIn1.substring(2, 4));
    RatioOn14[1] = getInt(lightIn1.substring(4, 6));
    RatioOff14[1] = getInt(lightIn1.substring(6, 8));
    RatioOn14[2] = getInt(lightIn1.substring(8, 10));
    RatioOff14[2] = getInt(lightIn1.substring(10, 12));
    RatioOn14[3] = getInt(lightIn1.substring(12, 14));
    RatioOff14[3] = getInt(lightIn1.substring(14, 16));
    RatioOn14[4] = getInt(lightIn1.substring(16, 18));
    RatioOff14[4] = getInt(lightIn1.substring(18, 20));

    RatioOn14[5] = getInt(lightIn1.substring(20, 22));
    RatioOff14[5] = getInt(lightIn1.substring(22, 24));
    RatioOn14[6] = getInt(lightIn1.substring(24, 26));
    RatioOff14[6] = getInt(lightIn1.substring(26, 28));
    RatioOn14[7] = getInt(lightIn1.substring(28, 30));
    RatioOff14[7] = getInt(lightIn1.substring(30, 32));
    RatioOn14[8] = getInt(lightIn1.substring(32, 34));
    RatioOff14[8] = getInt(lightIn1.substring(34, 36));
    RatioOn14[9] = getInt(lightIn1.substring(36, 38));
    RatioOff14[9] = getInt(lightIn1.substring(38, 40));

    HourOn15[0] = getInt(lightIn1.substring(40, 42));
    MinuteOn15[0] = getInt(lightIn1.substring(42, 44));
    HourOn15[1] = getInt(lightIn1.substring(44, 46));
    MinuteOn15[1] = getInt(lightIn1.substring(46, 48));
    HourOn15[2] = getInt(lightIn1.substring(48, 50));
    MinuteOn15[2] = getInt(lightIn1.substring(50, 52));
    HourOn15[3] = getInt(lightIn1.substring(52, 54));
    MinuteOn15[3] = getInt(lightIn1.substring(54, 56));
    HourOn15[4] = getInt(lightIn1.substring(56, 58));
    MinuteOn15[4] = getInt(lightIn1.substring(58, 60));
    
    LightSet27=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn15[5] = getInt(lightIn1.substring(0, 2));
    MinuteOn15[5] = getInt(lightIn1.substring(2, 4));
    HourOn15[6] = getInt(lightIn1.substring(4, 6));
    MinuteOn15[6] = getInt(lightIn1.substring(6, 8));
    HourOn15[7] = getInt(lightIn1.substring(8, 10));
    MinuteOn15[7] = getInt(lightIn1.substring(10, 12));
    HourOn15[8] = getInt(lightIn1.substring(12, 14));
    MinuteOn15[8] = getInt(lightIn1.substring(14, 16));
    HourOn15[9] = getInt(lightIn1.substring(16, 18));
    MinuteOn15[9] = getInt(lightIn1.substring(18, 20));

    RatioOn15[0] = getInt(lightIn1.substring(20, 22));
    RatioOff15[0] = getInt(lightIn1.substring(22, 24));
    RatioOn15[1] = getInt(lightIn1.substring(24, 26));
    RatioOff15[1] = getInt(lightIn1.substring(26, 28));
    RatioOn15[2] = getInt(lightIn1.substring(28, 30));
    RatioOff15[2] = getInt(lightIn1.substring(30, 32));
    RatioOn15[3] = getInt(lightIn1.substring(32, 34));
    RatioOff15[3] = getInt(lightIn1.substring(34, 36));
    RatioOn15[4] = getInt(lightIn1.substring(36, 38));
    RatioOff15[4] = getInt(lightIn1.substring(38, 40));

    RatioOn15[5] = getInt(lightIn1.substring(40, 42));
    RatioOff15[5] = getInt(lightIn1.substring(42, 44));
    RatioOn15[6] = getInt(lightIn1.substring(44, 46));
    RatioOff15[6] = getInt(lightIn1.substring(46, 48));
    RatioOn15[7] = getInt(lightIn1.substring(48, 50));
    RatioOff15[7] = getInt(lightIn1.substring(50, 52));
    RatioOn15[8] = getInt(lightIn1.substring(52, 54));
    RatioOff15[8] = getInt(lightIn1.substring(54, 56));
    RatioOn15[9] = getInt(lightIn1.substring(56, 58));
    RatioOff15[9] = getInt(lightIn1.substring(58, 60));
    
    LightSet28=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn16[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn16[0] = getInt(lightIn1.substring(2, 4));
    HourOn16[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn16[1] = getInt(lightIn1.substring(6, 8));
    HourOn16[2] = getInt(lightIn1.substring(8, 10));
    MinuteOn16[2] = getInt(lightIn1.substring(10, 12));
    HourOn16[3] = getInt(lightIn1.substring(12, 14));
    MinuteOn16[3] = getInt(lightIn1.substring(14, 16));
    HourOn16[4] = getInt(lightIn1.substring(16, 18));
    MinuteOn16[4] = getInt(lightIn1.substring(18, 20));

    HourOn16[5] = getInt(lightIn1.substring(20, 22));
    MinuteOn16[5] = getInt(lightIn1.substring(22, 24));
    HourOn16[6] = getInt(lightIn1.substring(24, 26));
    MinuteOn16[6] = getInt(lightIn1.substring(26, 28));
    HourOn16[7] = getInt(lightIn1.substring(28, 30));
    MinuteOn16[7] = getInt(lightIn1.substring(30, 32));
    HourOn16[8] = getInt(lightIn1.substring(32, 34));
    MinuteOn16[8] = getInt(lightIn1.substring(34, 36));
    HourOn16[9] = getInt(lightIn1.substring(36, 38));
    MinuteOn16[9] = getInt(lightIn1.substring(38, 40));

    RatioOn16[0] = getInt(lightIn1.substring(40, 42));
    RatioOff16[0] = getInt(lightIn1.substring(42, 44));
    RatioOn16[1] = getInt(lightIn1.substring(44, 46));
    RatioOff16[1] = getInt(lightIn1.substring(46, 48));
    RatioOn16[2] = getInt(lightIn1.substring(48, 50));
    RatioOff16[2] = getInt(lightIn1.substring(50, 52));
    RatioOn16[3] = getInt(lightIn1.substring(52, 54));
    RatioOff16[3] = getInt(lightIn1.substring(54, 56));
    RatioOn16[4] = getInt(lightIn1.substring(56, 58));
    RatioOff16[4] = getInt(lightIn1.substring(58, 60));
    
    LightSet29=1;
  }
    
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn16[5] = getInt(lightIn1.substring(0, 2));
    RatioOff16[5] = getInt(lightIn1.substring(2, 4));
    RatioOn16[6] = getInt(lightIn1.substring(4, 6));
    RatioOff16[6] = getInt(lightIn1.substring(6, 8));
    RatioOn16[7] = getInt(lightIn1.substring(8, 10));
    RatioOff16[7] = getInt(lightIn1.substring(10, 12));
    RatioOn16[8] = getInt(lightIn1.substring(12, 14));
    RatioOff16[8] = getInt(lightIn1.substring(14, 16));
    RatioOn16[9] = getInt(lightIn1.substring(16, 18));
    RatioOff16[9] = getInt(lightIn1.substring(18, 20));

    HourOn17[0] = getInt(lightIn1.substring(20, 22));
    MinuteOn17[0] = getInt(lightIn1.substring(22, 24));
    HourOn17[1] = getInt(lightIn1.substring(24, 26));
    MinuteOn17[1] = getInt(lightIn1.substring(26, 28));
    HourOn17[2] = getInt(lightIn1.substring(28, 30));
    MinuteOn17[2] = getInt(lightIn1.substring(30, 32));
    HourOn17[3] = getInt(lightIn1.substring(32, 34));
    MinuteOn17[3] = getInt(lightIn1.substring(34, 36));
    HourOn17[4] = getInt(lightIn1.substring(36, 38));
    MinuteOn17[4] = getInt(lightIn1.substring(38, 40));

    HourOn17[5] = getInt(lightIn1.substring(40, 42));
    MinuteOn17[5] = getInt(lightIn1.substring(42, 44));
    HourOn17[6] = getInt(lightIn1.substring(44, 46));
    MinuteOn17[6] = getInt(lightIn1.substring(46, 48));
    HourOn17[7] = getInt(lightIn1.substring(48, 50));
    MinuteOn17[7] = getInt(lightIn1.substring(50, 52));
    HourOn17[8] = getInt(lightIn1.substring(52, 54));
    MinuteOn17[8] = getInt(lightIn1.substring(54, 56));
    HourOn17[9] = getInt(lightIn1.substring(56, 58));
    MinuteOn17[9] = getInt(lightIn1.substring(58, 60));
    
    LightSet30=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==1 && LightSet31 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn17[0] = getInt(lightIn1.substring(0, 2));
    RatioOff17[0] = getInt(lightIn1.substring(2, 4));
    RatioOn17[1] = getInt(lightIn1.substring(4, 6));
    RatioOff17[1] = getInt(lightIn1.substring(6, 8));
    RatioOn17[2] = getInt(lightIn1.substring(8, 10));
    RatioOff17[2] = getInt(lightIn1.substring(10, 12));
    RatioOn17[3] = getInt(lightIn1.substring(12, 14));
    RatioOff17[3] = getInt(lightIn1.substring(14, 16));
    RatioOn17[4] = getInt(lightIn1.substring(16, 18));
    RatioOff17[4] = getInt(lightIn1.substring(18, 20));

    RatioOn17[5] = getInt(lightIn1.substring(20, 22));
    RatioOff17[5] = getInt(lightIn1.substring(22, 24));
    RatioOn17[6] = getInt(lightIn1.substring(24, 26));
    RatioOff17[6] = getInt(lightIn1.substring(26, 28));
    RatioOn17[7] = getInt(lightIn1.substring(28, 30));
    RatioOff17[7] = getInt(lightIn1.substring(30, 32));
    RatioOn17[8] = getInt(lightIn1.substring(32, 34));
    RatioOff17[8] = getInt(lightIn1.substring(34, 36));
    RatioOn17[9] = getInt(lightIn1.substring(36, 38));
    RatioOff17[9] = getInt(lightIn1.substring(38, 40));

    HourOn18[0] = getInt(lightIn1.substring(40, 42));
    MinuteOn18[0] = getInt(lightIn1.substring(42, 44));
    HourOn18[1] = getInt(lightIn1.substring(44, 46));
    MinuteOn18[1] = getInt(lightIn1.substring(46, 48));
    HourOn18[2] = getInt(lightIn1.substring(48, 50));
    MinuteOn18[2] = getInt(lightIn1.substring(50, 52));
    HourOn18[3] = getInt(lightIn1.substring(52, 54));
    MinuteOn18[3] = getInt(lightIn1.substring(54, 56));
    HourOn18[4] = getInt(lightIn1.substring(56, 58));
    MinuteOn18[4] = getInt(lightIn1.substring(58, 60));
    
    LightSet31=1;
  }
  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==1 && LightSet31 ==1 && LightSet32 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn18[5] = getInt(lightIn1.substring(0, 2));
    MinuteOn18[5] = getInt(lightIn1.substring(2, 4));
    HourOn18[6] = getInt(lightIn1.substring(4, 6));
    MinuteOn18[6] = getInt(lightIn1.substring(6, 8));
    HourOn18[7] = getInt(lightIn1.substring(8, 10));
    MinuteOn18[7] = getInt(lightIn1.substring(10, 12));
    HourOn18[8] = getInt(lightIn1.substring(12, 14));
    MinuteOn18[8] = getInt(lightIn1.substring(14, 16));
    HourOn18[9] = getInt(lightIn1.substring(16, 18));
    MinuteOn18[9] = getInt(lightIn1.substring(18, 20));

    RatioOn18[0] = getInt(lightIn1.substring(20, 22));
    RatioOff18[0] = getInt(lightIn1.substring(22, 24));
    RatioOn18[1] = getInt(lightIn1.substring(24, 26));
    RatioOff18[1] = getInt(lightIn1.substring(26, 28));
    RatioOn18[2] = getInt(lightIn1.substring(28, 30));
    RatioOff18[2] = getInt(lightIn1.substring(30, 32));
    RatioOn18[3] = getInt(lightIn1.substring(32, 34));
    RatioOff18[3] = getInt(lightIn1.substring(34, 36));
    RatioOn18[4] = getInt(lightIn1.substring(36, 38));
    RatioOff18[4] = getInt(lightIn1.substring(38, 40));

    RatioOn18[5] = getInt(lightIn1.substring(40, 42));
    RatioOff18[5] = getInt(lightIn1.substring(42, 44));
    RatioOn18[6] = getInt(lightIn1.substring(44, 46));
    RatioOff18[6] = getInt(lightIn1.substring(46, 48));
    RatioOn18[7] = getInt(lightIn1.substring(48, 50));
    RatioOff18[7] = getInt(lightIn1.substring(50, 52));
    RatioOn18[8] = getInt(lightIn1.substring(52, 54));
    RatioOff18[8] = getInt(lightIn1.substring(54, 56));
    RatioOn18[9] = getInt(lightIn1.substring(56, 58));
    RatioOff18[9] = getInt(lightIn1.substring(58, 60));
    
    LightSet32=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==1 && LightSet31 ==1 && LightSet32 ==1 && LightSet33 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    HourOn19[0] = getInt(lightIn1.substring(0, 2));
    MinuteOn19[0] = getInt(lightIn1.substring(2, 4));
    HourOn19[1] = getInt(lightIn1.substring(4, 6));
    MinuteOn19[1] = getInt(lightIn1.substring(6, 8));
    HourOn19[2] = getInt(lightIn1.substring(8, 10));
    MinuteOn19[2] = getInt(lightIn1.substring(10, 12));
    HourOn19[3] = getInt(lightIn1.substring(12, 14));
    MinuteOn19[3] = getInt(lightIn1.substring(14, 16));
    HourOn19[4] = getInt(lightIn1.substring(16, 18));
    MinuteOn19[4] = getInt(lightIn1.substring(18, 20));

    HourOn19[5] = getInt(lightIn1.substring(20, 22));
    MinuteOn19[5] = getInt(lightIn1.substring(22, 24));
    HourOn19[6] = getInt(lightIn1.substring(24, 26));
    MinuteOn19[6] = getInt(lightIn1.substring(26, 28));
    HourOn19[7] = getInt(lightIn1.substring(28, 30));
    MinuteOn19[7] = getInt(lightIn1.substring(30, 32));
    HourOn19[8] = getInt(lightIn1.substring(32, 34));
    MinuteOn19[8] = getInt(lightIn1.substring(34, 36));
    HourOn19[9] = getInt(lightIn1.substring(36, 38));
    MinuteOn19[9] = getInt(lightIn1.substring(38, 40));

    RatioOn19[0] = getInt(lightIn1.substring(40, 42));
    RatioOff19[0] = getInt(lightIn1.substring(42, 44));
    RatioOn19[1] = getInt(lightIn1.substring(44, 46));
    RatioOff19[1] = getInt(lightIn1.substring(46, 48));
    RatioOn19[2] = getInt(lightIn1.substring(48, 50));
    RatioOff19[2] = getInt(lightIn1.substring(50, 52));
    RatioOn19[3] = getInt(lightIn1.substring(52, 54));
    RatioOff19[3] = getInt(lightIn1.substring(54, 56));
    RatioOn19[4] = getInt(lightIn1.substring(56, 58));
    RatioOff19[4] = getInt(lightIn1.substring(58, 60));
    
    LightSet33=1;
  }

  if (Serial.available() == 60 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==1 && LightSet31 ==1 && LightSet32 ==1 && LightSet33 ==1 && LightSet34 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn19[5] = getInt(lightIn1.substring(0, 2));
    RatioOff19[5] = getInt(lightIn1.substring(2, 4));
    RatioOn19[6] = getInt(lightIn1.substring(4, 6));
    RatioOff19[6] = getInt(lightIn1.substring(6, 8));
    RatioOn19[7] = getInt(lightIn1.substring(8, 10));
    RatioOff19[7] = getInt(lightIn1.substring(10, 12));
    RatioOn19[8] = getInt(lightIn1.substring(12, 14));
    RatioOff19[8] = getInt(lightIn1.substring(14, 16));
    RatioOn19[9] = getInt(lightIn1.substring(16, 18));
    RatioOff19[9] = getInt(lightIn1.substring(18, 20));

    HourOn20[0] = getInt(lightIn1.substring(20, 22));
    MinuteOn20[0] = getInt(lightIn1.substring(22, 24));
    HourOn20[1] = getInt(lightIn1.substring(24, 26));
    MinuteOn20[1] = getInt(lightIn1.substring(26, 28));
    HourOn20[2] = getInt(lightIn1.substring(28, 30));
    MinuteOn20[2] = getInt(lightIn1.substring(30, 32));
    HourOn20[3] = getInt(lightIn1.substring(32, 34));
    MinuteOn20[3] = getInt(lightIn1.substring(34, 36));
    HourOn20[4] = getInt(lightIn1.substring(36, 38));
    MinuteOn20[4] = getInt(lightIn1.substring(38, 40));

    HourOn20[5] = getInt(lightIn1.substring(40, 42));
    MinuteOn20[5] = getInt(lightIn1.substring(42, 44));
    HourOn20[6] = getInt(lightIn1.substring(44, 46));
    MinuteOn20[6] = getInt(lightIn1.substring(46, 48));
    HourOn20[7] = getInt(lightIn1.substring(48, 50));
    MinuteOn20[7] = getInt(lightIn1.substring(50, 52));
    HourOn20[8] = getInt(lightIn1.substring(52, 54));
    MinuteOn20[8] = getInt(lightIn1.substring(54, 56));
    HourOn20[9] = getInt(lightIn1.substring(56, 58));
    MinuteOn20[9] = getInt(lightIn1.substring(58, 60));
    
    LightSet34=1;
  }

  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==1 && LightSet31 ==1 && LightSet32 ==1 && LightSet33 ==1 && LightSet34 ==1 && LightSet35 ==0)
  {
    lightIn1 = Serial.readString();
    Serial.println(lightIn1);
    RatioOn20[0] = getInt(lightIn1.substring(0, 2));
    RatioOff20[0] = getInt(lightIn1.substring(2, 4));
    RatioOn20[1] = getInt(lightIn1.substring(4, 6));
    RatioOff20[1] = getInt(lightIn1.substring(6, 8));
    RatioOn20[2] = getInt(lightIn1.substring(8, 10));
    RatioOff20[2] = getInt(lightIn1.substring(10, 12));
    RatioOn20[3] = getInt(lightIn1.substring(12, 14));
    RatioOff20[3] = getInt(lightIn1.substring(14, 16));
    RatioOn20[4] = getInt(lightIn1.substring(16, 18));
    RatioOff20[4] = getInt(lightIn1.substring(18, 20));

    RatioOn20[5] = getInt(lightIn1.substring(20, 22));
    RatioOff20[5] = getInt(lightIn1.substring(22, 24));
    RatioOn20[6] = getInt(lightIn1.substring(24, 26));
    RatioOff20[6] = getInt(lightIn1.substring(26, 28));
    RatioOn20[7] = getInt(lightIn1.substring(28, 30));
    RatioOff20[7] = getInt(lightIn1.substring(30, 32));
    RatioOn20[8] = getInt(lightIn1.substring(32, 34));
    RatioOff20[8] = getInt(lightIn1.substring(34, 36));
    RatioOn20[9] = getInt(lightIn1.substring(36, 38));
    RatioOff20[9] = getInt(lightIn1.substring(38, 40));
    
    LightSet35=1;
  }

  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==1 && LightSet31 ==1 && LightSet32 ==1 && LightSet33 ==1 && LightSet34 ==1 && LightSet35 ==1 && LightSet36 ==0 )
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
    
    LightSet36=1;
  }
  if (Serial.available() == 40 && InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && LightSet6 == 1 && LightSet7 == 1 && LightSet8 == 1 && LightSet9 == 1 && LightSet10 == 1 && LightSet11 == 1 && LightSet12 == 1 && LightSet13 == 1 && LightSet14 == 1 && LightSet15 == 1 && LightSet16 == 1 && LightSet17 == 1 && LightSet18 == 1 && LightSet19 == 1 && LightSet20 == 1 && LightSet21 == 1 && LightSet22 == 1 && LightSet23 == 1 && LightSet24 == 1 && LightSet25 == 1 && LightSet26 ==1 && LightSet27 ==1 && LightSet28 ==1 && LightSet29 ==1 && LightSet30 ==1 && LightSet31 ==1 && LightSet32 ==1 && LightSet33 ==1 && LightSet34 ==1 && LightSet35 ==1 && LightSet36 ==1 && LightSet37 ==0 )
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
    
    LightSet37=1;
  }

  
  // Begin to print the headers and set light flag
  if (InitialFlag == 0 && TimeSet == 1 && LightSet1 == 1 && LightSet2 == 1 && LightSet3 == 1 && LightSet4 == 1 && LightSet5 == 1 && 
  LightSet6 == 1 && LightSet8 == 1 && LightSet9 == 1&& LightSet10 == 1&& LightSet11 == 1&& LightSet12 == 1&&
  LightSet13 == 1 && LightSet14 == 1&& LightSet15 == 1&& LightSet16 == 1&& LightSet17 == 1&&
  LightSet18 == 1 && LightSet19 == 1&& LightSet20 == 1&& LightSet21 == 1&& LightSet22 == 1&&
  LightSet23 == 1 && LightSet24 == 1&& LightSet25 == 1&& LightSet26 == 1&& LightSet27 == 1&&
  LightSet28 == 1 && LightSet29 == 1&& LightSet30 == 1&& LightSet31 == 1&& LightSet32 == 1&&
  LightSet33 == 1 && LightSet34 == 1&& LightSet35 == 1&& LightSet36 == 1&& LightSet37 ==1)
  {
    Serial.println("HH:MM:SS MO/DY/YEAR DAY Internal LED01 PIR01 LED02 PIR02 LED03 PIR03 LED04 PIR04 LED05 PIR05 LED06 PIR06 LED07 PIR07 LED08 PIR08 LED09 PIR09 LED10 PIR10");
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
    //Box1
    if (phase1 == 0)
    {
      for (int i = 0; i < 10; i++)
      {
        //Box1
        if (intHour * 60 + intMinute >= HourOn1[i] * 60 + MinuteOn1[i] && (intHour * 60 + intMinute) - (HourOn1[i] * 60 + MinuteOn1[i]) <= 24 * (RatioOn1[i] / (RatioOn1[i] + RatioOff1[i])) * 60)
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
        }
      }
    }

    //////////For Phase2
    if (phase1 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn2[i] * 60 + MinuteOn2[i] && (intHour * 60 + intMinute) - (HourOn2[i] * 60 + MinuteOn2[i]) <= 24 * (RatioOn2[i] / (RatioOn2[i] + RatioOff2[i])) * 60)
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
        }
      }
    }
    //////////For Phase3
    if (phase2 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn3[i] * 60 + MinuteOn3[i] && (intHour * 60 + intMinute) - (HourOn3[i] * 60 + MinuteOn3[i]) <= 24 * (RatioOn3[i] / (RatioOn3[i] + RatioOff3[i])) * 60)
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
        }
      }
    }
    //////////For Phase4
    if (phase3 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn4[i] * 60 + MinuteOn4[i] && (intHour * 60 + intMinute) - (HourOn4[i] * 60 + MinuteOn4[i]) <= 24 * (RatioOn4[i] / (RatioOn4[i] + RatioOff4[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }
    //////////For Phase5
    if (phase4 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn5[i] * 60 + MinuteOn5[i] && (intHour * 60 + intMinute) - (HourOn5[i] * 60 + MinuteOn5[i]) <= 24 * (RatioOn5[i] / (RatioOn5[i] + RatioOff5[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }
    //////////For Phase6
    if (phase5 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn6[i] * 60 + MinuteOn6[i] && (intHour * 60 + intMinute) - (HourOn6[i] * 60 + MinuteOn6[i]) <= 24 * (RatioOn6[i] / (RatioOn6[i] + RatioOff6[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }

    //////////For Phase7
    if (phase6 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn7[i] * 60 + MinuteOn7[i] && (intHour * 60 + intMinute) - (HourOn7[i] * 60 + MinuteOn7[i]) <= 24 * (RatioOn7[i] / (RatioOn7[i] + RatioOff7[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }
    //////////For Phase8
    if (phase7 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn8[i] * 60 + MinuteOn8[i] && (intHour * 60 + intMinute) - (HourOn8[i] * 60 + MinuteOn8[i]) <= 24 * (RatioOn8[i] / (RatioOn8[i] + RatioOff8[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }

    //////////For Phase9
    if (phase8 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn9[i] * 60 + MinuteOn9[i] && (intHour * 60 + intMinute) - (HourOn9[i] * 60 + MinuteOn9[i]) <= 24 * (RatioOn9[i] / (RatioOn9[i] + RatioOff9[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }

    //////////For Phase10
    if (phase9 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn10[i] * 60 + MinuteOn10[i] && (intHour * 60 + intMinute) - (HourOn10[i] * 60 + MinuteOn10[i]) <= 24 * (RatioOn10[i] / (RatioOn10[i] + RatioOff10[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }
    //////////For Phase11
    if (phase10 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn11[i] * 60 + MinuteOn11[i] && (intHour * 60 + intMinute) - (HourOn11[i] * 60 + MinuteOn11[i]) <= 24 * (RatioOn11[i] / (RatioOn11[i] + RatioOff11[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }
    //////////For Phase12
    if (phase11 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn12[i] * 60 + MinuteOn12[i] && (intHour * 60 + intMinute) - (HourOn12[i] * 60 + MinuteOn12[i]) <= 24 * (RatioOn12[i] / (RatioOn12[i] + RatioOff12[i])) * 60)
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
        } // if time condition is met
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
        }
      }
    }
    //////////For Phase13
    if (phase12 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn13[i] * 60 + MinuteOn13[i] && (intHour * 60 + intMinute) - (HourOn13[i] * 60 + MinuteOn13[i]) <= 24 * (RatioOn13[i] / (RatioOn13[i] + RatioOff13[i])) * 60)
        {
          if (light13[i] == 0 && dark13[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light13[i] == 0 && dark13[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light13[i] == 1 && dark13[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light13[i] == 0 && dark13[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light13[i] == 0 && dark13[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light13[i] == 1 && dark13[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        }
      }
    }
    //////////For Phase14
    if (phase13 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn14[i] * 60 + MinuteOn14[i] && (intHour * 60 + intMinute) - (HourOn14[i] * 60 + MinuteOn14[i]) <= 24 * (RatioOn14[i] / (RatioOn14[i] + RatioOff14[i])) * 60)
        {
          if (light14[i] == 0 && dark14[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light14[i] == 0 && dark14[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light14[i] == 1 && dark14[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light14[i] == 0 && dark14[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light14[i] == 0 && dark14[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light14[i] == 1 && dark14[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        }
      }
    }
    //////////For Phase15
    if (phase14 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn15[i] * 60 + MinuteOn15[i] && (intHour * 60 + intMinute) - (HourOn15[i] * 60 + MinuteOn15[i]) <= 24 * (RatioOn15[i] / (RatioOn15[i] + RatioOff15[i])) * 60)
        {
          if (light15[i] == 0 && dark15[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light15[i] == 0 && dark15[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light15[i] == 1 && dark15[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light15[i] == 0 && dark15[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light15[i] == 0 && dark15[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light15[i] == 1 && dark15[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        }
      }
    }
    //////////For Phase16
    if (phase15 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn16[i] * 60 + MinuteOn16[i] && (intHour * 60 + intMinute) - (HourOn16[i] * 60 + MinuteOn16[i]) <= 24 * (RatioOn16[i] / (RatioOn16[i] + RatioOff16[i])) * 60)
        {
          if (light16[i] == 0 && dark16[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light16[i] == 0 && dark16[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light16[i] == 1 && dark16[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light16[i] == 0 && dark16[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light16[i] == 0 && dark16[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light16[i] == 1 && dark16[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        }
      }
    }

    //////////For Phase17
    if (phase16 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn17[i] * 60 + MinuteOn17[i] && (intHour * 60 + intMinute) - (HourOn17[i] * 60 + MinuteOn17[i]) <= 24 * (RatioOn17[i] / (RatioOn17[i] + RatioOff17[i])) * 60)
        {
          if (light17[i] == 0 && dark17[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light17[i] == 0 && dark17[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light17[i] == 1 && dark17[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light17[i] == 0 && dark17[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light17[i] == 0 && dark17[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light17[i] == 1 && dark17[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        }
      }
    }
    //////////For Phase18
    if (phase17 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn18[i] * 60 + MinuteOn18[i] && (intHour * 60 + intMinute) - (HourOn18[i] * 60 + MinuteOn18[i]) <= 24 * (RatioOn18[i] / (RatioOn18[i] + RatioOff18[i])) * 60)
        {
          if (light18[i] == 0 && dark18[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light18[i] == 0 && dark18[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light18[i] == 1 && dark18[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light18[i] == 0 && dark18[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light18[i] == 0 && dark18[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light18[i] == 1 && dark18[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        }
      }
    }
    //////////For Phase19
    if (phase18 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn19[i] * 60 + MinuteOn19[i] && (intHour * 60 + intMinute) - (HourOn19[i] * 60 + MinuteOn19[i]) <= 24 * (RatioOn19[i] / (RatioOn19[i] + RatioOff19[i])) * 60)
        {
          if (light19[i] == 0 && dark19[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light19[i] == 0 && dark19[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light19[i] == 1 && dark19[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light19[i] == 0 && dark19[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light19[i] == 0 && dark19[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light19[i] == 1 && dark19[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        }
      }
    }
    //////////For Phase20
    if (phase19 == 1)
    {
      for (int i = 0; i < 10; i++)
      {
        if (intHour * 60 + intMinute >= HourOn20[i] * 60 + MinuteOn20[i] && (intHour * 60 + intMinute) - (HourOn20[i] * 60 + MinuteOn20[i]) <= 24 * (RatioOn20[i] / (RatioOn20[i] + RatioOff20[i])) * 60)
        {
          if (light20[i] == 0 && dark20[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
          if (light20[i] == 0 && dark20[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light20[i] == 1 && dark20[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
          }
        } // if time condition is met
        else
        {
          if (light20[i] == 0 && dark20[i] == 0)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light20[i] == 0 && dark20[i] == 1)
          {
            digitalWrite(DOut[i], LOW);
            LightFlag[i] = 0;
          }
          if (light20[i] == 1 && dark20[i] == 0)
          {
            digitalWrite(DOut[i], HIGH);
            LightFlag[i] = 1;
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
  for (int i = 0; i < 10; i++)
  {
    mPIR[i] = 0;
  }

  // per-second sampling
  for (int i = 0; i < 10; i++)
  {
    PIR[i] = digitalRead(DIn[i]);
  }

  // sensor value sampling for 1-min
  for (int i = 0; i < 990; i++)
  {
    for (int j = 0; j < 10; j++)
    {
      PIR[j] = PIR[j] + digitalRead(DIn[j]);
    }

    delay(60); // sampling 1000 times per minute
  }

  // 1-min summation
  for (int i = 0; i < 10; i++)
  {
    mPIR[i] = PIR[i];
  }

  // Outputs

  printTime();
  Serial.print(" ");

  for (int i = 0; i < 10; i++)
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
