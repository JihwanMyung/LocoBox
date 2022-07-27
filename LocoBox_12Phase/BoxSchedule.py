


class PhaseSchedule:
    def __init__(self, hourOn, minOn, hourOff, minOff, dark, light):
        self.hourOn = hourOn
        self.minOn = minOn
        self.hourOff =  hourOff
        self.minOff = minOff
        self.dark = dark
        self.light = light

    
    def add_extra_parameters(self, date, month, year, hourFrom, minuteFrom):
       
        self.date = date
        self.month = month
        self.year = year 
        self.hourFrom = hourFrom
        self.minuteFrom = minuteFrom 

    def __str__(self):
        basic_parameters = "hourOn: " + str(self.hourOn) + " minOn: " + str(self.minOn) + " hourOff: " + str(self.hourOff) + " minOn: " + str(self.minOff) + " dark: " + str(self.dark) + " light: " + str(self.light)
        return basic_parameters

def getDarkLightValue(var):
    if var.get()==1:
        dark='0'
        light='0'
    if var.get()==2:
        dark='1'
        light='0'
    if var.get()==3:
        dark='0'
        light='1'
    return dark, light


class BoxSchedule:
    def __init__(self):
        self.pschedules = []


    def addPhase1(self,hourOn, minOn, hourOff, minOff, var):
        dark, light = getDarkLightValue(var)
        newSchedule = PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light)
        self.pschedules.append(newSchedule)
        

    def addPhase(self,hourOn, minOn, hourOff, minOff, var, date, month, year, hourFrom, minuteFrom ):
        dark, light = getDarkLightValue(var)
        newSchedule = PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light)
        newSchedule.add_extra_parameters(date, month, year, hourFrom, minuteFrom)
        self.pschedules.append(newSchedule)

    def printPhase(self, index):
        index = index -1 #the phases start from 1
        requested_schedule = self.pschedules[index]
        print(requested_schedule)