        # phase 3
    phaseLabel1_3 = Label(tab1, text='Phase 3')
    fromLabel1_3 = Label(tab1, text='From:')
    fromLabel1_3.grid(column=1,row=4+row_adj)
    space1_3 = Label(tab1, text=' ')
    space1_3_2 = Label(tab1, text=' ')
    spin1_E_3 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_F_3 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_E_3.delete(0,'end')
    spin1_E_3.insert(0,'07')
    spin1_F_3.delete(0,'end')
    spin1_F_3.insert(0,'00')
    label1_h0_3 = Label(tab1, text=':')
    label1_m0_3 = Label(tab1, text='')
    date1_3_entry = Spinbox(tab1, from_=00, to=31, width=3, format='%02.0f')
    month1_3_entry = Spinbox(tab1, from_=00, to=12, width=3, format='%02.0f')
    year1_3_entry = Spinbox(tab1, from_=2018, to=2030, width=5)
    today=datetime.date.today() # today
    day_phase3 = day_phase2 + datetime.timedelta(days=7) # calculate dates for 14 days after recording initiation
    date1_3_entry.delete(0,'end')
    date1_3_entry.insert(0,'{:02d}'.format(day_phase3.day))
    month1_3_entry.delete(0,'end')
    month1_3_entry.insert(0,'{:02d}'.format(day_phase3.month))
    year1_3_entry.delete(0,'end')
    year1_3_entry.insert(0,day_phase3.year)
    label1_d_3 = Label(tab1, text= '/')
    label1_m_3 = Label(tab1, text= '/')
    rad1_A_3 = Radiobutton(tab1, text='LD', variable=var1_3, value=1)
    lbl1_A_3 = Label(tab1, text= 'On:')
    spin1_A_3 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_B_3 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_A_3.delete(0,'end')
    spin1_A_3.insert(0,'07')
    spin1_B_3.delete(0,'end')
    spin1_B_3.insert(0,'00')
    label1_h1_3 = Label(tab1, text=':')
    label1_m1_3 = Label(tab1, text='')
    lbl1_B_3 = Label(tab1, text= 'Off:')
    spin1_C_3 = Spinbox(tab1, from_=00, to=24, width=3, format='%02.0f')
    spin1_D_3 = Spinbox(tab1, from_=00, to=59, width=3, format='%02.0f')
    spin1_C_3.delete(0,'end')
    spin1_C_3.insert(0,'19')
    spin1_D_3.delete(0,'end')
    spin1_D_3.insert(0,'00')
    label1_h2_3 = Label(tab1, text=':')
    label1_m2_3 = Label(tab1, text='')
    rad1_B_3 = Radiobutton(tab1, text='DD', variable=var1_3, value=2)
    rad1_C_3 = Radiobutton(tab1, text='LL', variable=var1_3, value=3)
    phaseLabel1_3.grid(column=0, row=4+row_adj, padx=15, pady=5)
    spin1_E_3.grid(column=2,row=4+row_adj)
    label1_h0_3.grid(column=3,row=4+row_adj)
    spin1_F_3.grid(column=4,row=4+row_adj)
    label1_m0_3.grid(column=5,row=4+row_adj)
    space1_3.grid(column=6,row=4+row_adj)
    date1_3_entry.grid(column=11, row=4+row_adj)
    label1_d_3.grid(column=8,row=4+row_adj)
    month1_3_entry.grid(column=9, row=4+row_adj)
    label1_m_3.grid(column=10,row=4+row_adj)
    year1_3_entry.grid(column=7, row=4+row_adj) # ISO format
    space1_3_2.grid(column=12,row=4+row_adj,padx=5)
    rad1_A_3.grid(column=13, row=4+row_adj, pady=5)
    lbl1_A_3.grid(column=14, row=4+row_adj, pady=5)
    spin1_A_3.grid(column=15,row=4+row_adj, pady=5)
    label1_h1_3.grid(column=16,row=4+row_adj, pady=5)
    spin1_B_3.grid(column=17,row=4+row_adj, pady=5)
    label1_m1_3.grid(column=18,row=4+row_adj, pady=5)
    lbl1_B_3.grid(column=19, row=4+row_adj, pady=5)
    spin1_C_3.grid(column=20,row=4+row_adj, pady=5)
    label1_h2_3.grid(column=21,row=4+row_adj, pady=5)
    spin1_D_3.grid(column=22,row=4+row_adj, pady=5)
    label1_m2_3.grid(column=23,row=4+row_adj, pady=5)
    rad1_B_3.grid(column=24, row=4+row_adj, padx=15, pady=5)
    rad1_C_3.grid(column=25, row=4+row_adj, pady=5)