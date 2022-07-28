

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

def inverseDarkLightValue(dark, light):
    if (dark=='0' ) and (light=='0'):
        temp_var = 1
    elif (dark=='1') and (light=='0'):
        temp_var = 2
    elif (dark=='0') and (light=='1'):
        temp_var = 3

    return temp_var


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


    def assignPhase1(self,spin_A,spin_B,spin_C ,spin_D,var):
        #spin1_A_1.get(),spin1_B_1.get(),spin1_C_1.get(),spin1_D_1.get(), var1_1
        spin_A.delete(0,'end')
        spin_A.insert(0,self.hourOn)
        spin_B.delete(0,'end')
        spin_B.insert(0,self.minOn)
        spin_C.delete(0,'end')
        spin_C.insert(0,self.hourOff)
        spin_D.delete(0,'end')
        spin_D.insert(0,self.minOff)
        temp_var = inverseDarkLightValue(self.dark, self.light)
        var.set(temp_var)



    def assignSchedule(self,spin_A,spin_B,spin_C ,spin_D, var, spin_E, spin_F, date_entry, month_entry, year_entry ):
        self.assignPhase1(spin_A,spin_B,spin_C ,spin_D, var)
        spin_E.delete(0,'end')
        spin_E.insert(0,self.hourFrom)
        spin_F.delete(0,'end')
        spin_F.insert(0,self.minuteFrom)
        date_entry.delete(0,'end')
        date_entry.insert(0, self.date)
        month_entry.delete(0,'end')
        month_entry.insert(0, self.month)
        year_entry.delete(0,'end')
        year_entry.insert(0, self.year)
        







class BoxSchedule:
    def __init__(self):
        self.phase_sched = []


    


    def addPhase1(self,hourOn, minOn, hourOff, minOff, var):
        dark, light = getDarkLightValue(var)
        newSchedule = PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light)
        self.phase_sched.append(newSchedule)
        

    def addPhase(self,hourOn, minOn, hourOff, minOff, var, date, month, year, hourFrom, minuteFrom ):
        dark, light = getDarkLightValue(var)
        newSchedule = PhaseSchedule(hourOn, minOn, hourOff, minOff, dark, light)
        newSchedule.add_extra_parameters(date, month, year, hourFrom, minuteFrom)
        self.phase_sched.append(newSchedule)

    def printPhase(self, index):
        index = index -1 #the phases start from 1
        requested_schedule = self.phase_sched[index]
        print(requested_schedule)

    def pasteSchedule(self, box_index, global_mat):
        box_index = box_index -1
        #print(global_mat)
        
        spin_A = global_mat[box_index, 0, 0 ]
        spin_B =  global_mat[box_index, 0, 1 ]
        spin_C = global_mat[box_index, 0, 2 ]
        spin_D = global_mat[box_index, 0, 3 ]
        var = global_mat[box_index,0, 4 ]

        self.phase_sched[0].assignPhase1(spin_A,spin_B,spin_C ,spin_D,var)
        
        
        for phase_ind, phase in enumerate(self.phase_sched[1:], start=1):
            print(global_mat[box_index, phase_ind ])
            phase.assignSchedule(*global_mat[box_index, phase_ind ])

