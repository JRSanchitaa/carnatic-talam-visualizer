#suladi sapta talam generator
#menu options for a menu driven program
print()
print('This is a menu driven program that stores suladi sapta talam data and can fetch data for the users')

import random
import datetime
import time
import mysql.connector
import tkinter
import config
def talamdata():
    talams={'DHRUVA':['L','D','L','L'],
            'JAMPA':['L','A','D'],
            'MATYA':['L','D','L'],
            'TRIPUTA':['L','D','D'],
            'RUPAKA':['D','L'],
            'ATA':['L','L','D','D'],
            'EKA':['L'],}
    jathi={'CHATURASRA':4,'TISRA':3,'MISRA':7,'KANDA':5,'SANKEERNA':9}
    gathi={'CHATURASRA':4,'TISRA':3,'MISRA':7,'KANDA':5,'SANKEERNA':9}
    

    #to view talam structure(option 1)
    def view_structure():
        while True:
            try:
                print()
                tala=input('enter talam:DHRUVA,MATYA,RUPAKA,JAMPA,TRIPUTA,ATA,EKA')
                structure=talams[tala.upper()]
                print(tala.upper(),'talam')
                print('Its stucture is',structure)
                print()
                print('L denotes lagu , one beat followed by finger counts')
                print('D denotes drutham, one beat followed by reversing your palm')
                print('A denotes anudrutham, one beat')
                print()
                user=input('Enter yes if you would like to try again, else no').upper()
                if user=='YES':
                    continue
                else:
                    break
            except KeyError:
                print('Enter same spelling as input prompt')
                continue
    #akshara calculation
    
    def calcakshara(angavalue,structure):
        count=0
        for anga in structure:
            if anga=='L':
                count+=angavalue[anga]
            elif anga=='D':
                count+=angavalue[anga]
            elif anga=='A':
                count+=angavalue[anga]
        return count
    
    #matra calculation
    
    def calcmatra(gathi,akshara,GATHI):
        gathicount=gathi[GATHI]
        MATRA=akshara*gathicount
        return MATRA

    #to view akshara and matra of particular talam(option 2)
    def akshara_matra():
        while True:
            try:
                print()
                tala=input('enter talam:DHRUVA,MATYA,RUPAKA,JAMPA,TRIPUTA,ATA,EKA')
                structure=talams[tala.upper()]
                JATHIVAL=input('enter jathi :CHATURASRA,TISRA,MISRA,KANDA,SANKEERNA')
                value=jathi[JATHIVAL.upper()]
                angavalue={'L':value,'D':2,'A':1}
                gathival=input('enter gathi:CHATURASRA,TISRA,MISRA,KANDA,SANKEERNA')
                GATHI=gathival.upper()
                print()
                print('Talam name:',JATHIVAL,'jathi',gathival,'gathi',tala,'talam',)
                print()
                akshara=calcakshara(angavalue,structure)
                print('AKSHARA=',akshara)
                print()
                matra=calcmatra(gathi,akshara,GATHI)
                print('MATRA=',matra)
                print()
                user=input('Enter yes if you would like to try again, else no').upper()
                if user=='YES':
                    continue
                else:
                    break
            except KeyError:
                print('Enter same spelling as input prompt')
                continue
                
    
    #generation of 175 talas
    talamlist=[['TALAM NAME','AKSHARA','MATRA']]
    for tala in talams:
        for jati in jathi:
            for gati  in gathi:
                talamname=jati+' JATHI '+gati+' GATHI '+tala+' TALAM '
                value=jati.upper()
                angavalue={'L':value,'D':2,'A':1}
                angavalue['L']=jathi[jati]
                structure=talams[tala.upper()]
                akshara=calcakshara(angavalue,structure)
                matra=calcmatra(gathi,akshara,gati)
                talamlist.append([talamname,akshara,matra])


    #viewing all 175 tala with akshara and matra(option 3)
    def all_talas():
        while True:
            for i in range(1,len(talamlist)):
                print(talamlist[i][0])
                print()
                print('Akshara:',talamlist[i][1])
                print('Matra:',talamlist[i][2])
                print()
            user=input('Enter yes if you would like to try again, else no').upper()
            if user=='YES':
                continue
            else:
                break

    #adding all the data into mysql database into table talamname
    def talamdata(talamlist):
        mycon=mysql.connector.connect(user=config.DB_USER,host=config.DB_HOST,passwd=config.DB_PASSWORD,database=config.DB_NAME)
        cursor=mycon.cursor()
        st='select * from talamdata;'
        cursor.execute(st)
        count=len(cursor.fetchall())
        if count==0:
            for i in range (1,len(talamlist)):
                st='insert into talamdata values({},"{}",{},{});'.format(i,talamlist[i][0],talamlist[i][1],talamlist[i][2])
                cursor.execute(st)
        mycon.commit()
        mycon.close()
    talamdata(talamlist)

    #to filter data by talamname,jathi,gathi

    mycon=mysql.connector.connect(user=config.DB_USER,host=config.DB_HOST,passwd=config.DB_PASSWORD,database=config.DB_NAME)
    cursor=mycon.cursor()

    #to filter by talamname(option 4)
    def filter_talam():
        while True:  
            talam_name=input('Enter Talam :DHRUVA,MATYA,RUPAKA,JAMPA,TRIPUTA,ATA,EKA').upper()
            st='select*from talamdata where talam like "%{}%";'.format(talam_name,)
            cursor.execute(st)
            data=cursor.fetchall()
            if len(data) == 0:
                print("enter same spelling as input prompt")
                continue
            for row in data:
                print(row[1])
                print()
                print('Akshara:',row[2])
                print('Matra:',row[3])
                print()
            user=input('Enter yes if you would like to try again, else no').upper()
            if user=='YES':
                continue
            else:
                break
            
            
    #to filter by jathi(option 5)
    def filter_jathi():
        while True:
            jathi_name=input('Enter Jathi :CHATURASRA,TISRA,MISRA,KANDA,SANKEERNA').upper()
            st='select*from talamdata where talam like "%{}%";'.format(jathi_name+' JATHI',)
            cursor.execute(st)
            data=cursor.fetchall()
            if len(data) == 0:
                print("enter same spelling as input prompt")
                continue
            for row in data:
                print(row[1])
                print()
                print('Akshara:',row[2])
                print('Matra:',row[3])
                print()
            user=input('Enter yes if you would like to try again, else no').upper()
            if user=='YES':
                continue
            else:
                break

    #to filter by gathi(option 6)
    def filter_gathi():
        while True:
            gathi_name=input('Enter Gathi :CHATURASRA,TISRA,MISRA,KANDA,SANKEERNA').upper()
            st='select*from talamdata where talam like "%{}%";'.format(gathi_name+' GATHI',)
            cursor.execute(st)
            data=cursor.fetchall()
            if len(data) == 0:
                print("enter same spelling as input prompt")
                continue
            for row in data:
                print(row[1])
                print()
                print('Akshara:',row[2])
                print('Matra:',row[3])
                print()
            user=input('Enter yes if you would like to try again, else no').upper()
            if user=='YES':
                continue
            else:
                break

    #to filter by akshara(option 7)
    def filter_akshara():
        while True:
            try:
                akshara_val=int(input('Enter akshara value'))
                st='select*from talamdata where akshara={};'.format(akshara_val,)
                cursor.execute(st)
                data=cursor.fetchall()
                if len(data)==0:
                    print('There is no talam with akshara value',akshara_val)
                else:
                    for row in data:
                        print(row[1])
                        print()
                        print('Akshara:',row[2])
                        print('Matra:',row[3])
                        print()
                user=input('Enter yes if you would like to try again, else no').upper()
                if user=='YES':
                    continue
                else:
                    break
            except ValueError:
                print('enter valid input type, only integers')
                continue

    #to filter by matra(option 8)
    def filter_matra():
        while True:
            try:
                matra_val=int(input('Enter matra value'))
                st='select*from talamdata where matra={};'.format(matra_val,)
                cursor.execute(st)
                data=cursor.fetchall()
                if len(data)==0:
                    print('There is no talam with matra value',matra_val)
                else:
                    for row in data:
                        print(row[1])
                        print()
                        print('Akshara:',row[2])
                        print('Matra:',row[3])
                        print()
                user=input('Enter yes if you would like to try again, else no').upper()
                if user=='YES':
                    continue
                else:
                    break
            except ValueError:
                print('enter valid input type, only integers')
                continue

    #compare two talams(option 9)
    def compare():
        while True:
            try:
                print('enter talam in following format:jathi name jathi gathi name gathi talam name talam, eg=tisra jathi misra gathi eka talam')
                tala1=input('enter talam 1').upper()
                tala2=input('enter talam 2').upper()
                
                for row in talamlist:
                    if tala1 in row[0]:
                        a1=row[1]
                        m1=row[2]
                    if tala2 in row[0]:
                        a2=row[1]
                        m2=row[2]
                for i in talams:
                    if i in tala1:
                        s1=talams[i]
                    if i in tala2:
                        s2=talams[i]
                print()
                print('The structure of talam 1 is:',s1)
                print('The structure of talam 2 is:',s2)
                print()
                print('The akshara of talam 1 is:',a1)
                print('The akshara of talam 2 is:',a2)
                print()
                print('The matra of talam 1 is:',m1)
                print('The matra of talam 2 is:',m2)
                user=input('Enter yes if you would like to try again, else no').upper()
                if user=='YES':
                    continue
                else:
                    break
            except Exception:
                print('Enter valid talam name in same format as input prompt or recheck talam spelling')
                continue
        
        
    #talam of the day(option 10)
    def talam_of_day():
        print('The talam of the day is:')
        today_date=datetime.date.today()
        random.seed(str(today_date))
        sno=random.randint(1,175)
        st='select talam from talamdata where sno={};'.format(sno,)
        cursor.execute(st)
        data=cursor.fetchone()
        for row in data:
            print(row)
            

    #statistical data of talamdatabase(option 11)
    def statistics():
        print('There are 175 talams stored in this application')
        print()
        st='select talam,matra from talamdata order by matra desc;'
        cursor.execute(st)
        data=cursor.fetchone()
        for row in data:
            if type(row)==str:
                print('The talam with the highest matra is:',row)
            else:
                print('It has',row,'matras')
        data=cursor.fetchall()
        print()
        
        s='select talam,matra from talamdata order by matra asc;'
        cursor.execute(s)
        data=cursor.fetchone()
        for row in data:
            if type(row)==str:
                print('The talam with the lowest matra is:',row)
            else:
                print('It has',row,'matras')
        data=cursor.fetchall()
        print()
        

    #practice session(option 12)
    def practice():
        while True:
            count=0
            no=random.randint(1,2)
            if no==1:
                rno=random.randint(1,175)
                st='select talam from talamdata where sno={};'.format(rno,)
                cursor.execute(st)
                data=cursor.fetchone()
                for row in data:
                    practice_talam=row
                    print(row)
                t='True'
                while t=='True':
                    try:
                        structure_guess=list(input('Enter talam structure (d=drutham,a=anudhrutham,l=lagu eg:dl denote drutham followed by lagu)').upper())
                        akshara_guess=int(input('enter akshara'))
                        matra_guess=int(input('enter matra'))
                        for i in talams:
                            if i in practice_talam:
                                if talams[i]==structure_guess:
                                    print('The structure guessed is correct!')
                                    count+=1
                                else:
                                    print('The structure guessed is wrong')
                        for x in talamlist:
                            if practice_talam in x[0]:
                                if x[1]==akshara_guess:
                                    print('The akshara guessed is correct!')
                                    count+=1
                                else:
                                    print('The akshara guessed is wrong')
                                if x[2]==matra_guess:
                                    print('The matra guessed is correct!')
                                    count+=1
                                else:
                                    print('The matra guess is wrong')
                        if count==3:
                            t=='False'
                            break
                        else:
                            choice=input('Enter YES if you would like to try again else enter NO to reveal answer')
                            if choice.upper()=='NO':
                                for i in talams:
                                    if i in practice_talam:
                                        print('The correct structure is:',talams[i])
                                for x in talamlist:
                                    if practice_talam in x[0]:
                                        print('The correct akshara is:',x[1])
                                        print('The correct matra is:',x[2])
                                t=='False'
                                break
                            else:
                                t=='True'
                                continue
                    except ValueError:
                        print('enter valid input for matra and akshara, only integers')
                        continue
                
            if no==2:
                rno=random.randint(1,175)
                st='select talam from talamdata where sno={};'.format(rno,)
                cursor.execute(st)
                data=cursor.fetchone()
                for row in data:
                    practice_talam=row
                t='True'
                while t=='True':
                    for i in talams:
                        if i in practice_talam:
                            print('Guess the talam name from the given structure and akshara and matra')
                            print(talams[i])
                    for x in talamlist:
                        if practice_talam in x[0]:
                            print('The akshara is:',x[1])
                            print('The matra is:',x[2])
                    talam_guess=input('enter your guessed talam').upper()
                    if practice_talam.strip()==talam_guess.strip():
                        print('The talam guessed is correct!')
                        t='False'
                        break
                    else:
                        print('The guessed talam is wrong!')
                        choice=input('Enter YES if you would like to try again else enter NO to reveal answer')
                        if choice.upper()=='NO':
                            print('The talam is :',practice_talam)
                            t='False'
                            break
                        else:
                            continue
            user=input('Enter yes if you want to practice more, else no').upper()
            if user=='YES':
                continue
            else:
                break
    #talam metronome(option 13)
    def metronome():
        while True:

            root=tkinter.Tk()
            root.title('Talam Metronome')
            root.geometry('1600x1000')
            canvas=tkinter.Canvas(root,width=1600,height=1000)
            canvas.pack()
            space=0
            talam_prac=input('enter talam in following format:jathi name jathi gathi name gathi talam name talam, eg=tisra jathi misra gathi eka talam').upper()
            tala_name=talam_prac.split()
            for i in range(1,len(talamlist)):
                if talam_prac in talamlist[i][0]:
                    canvas.create_text(300,50+space,text=talamlist[i][0],font=('Arial',16,'bold'))
                    space+=20
                    for i in talams:
                        if i in talam_prac:
                            struc=talams[i]
                    base=350
                    shape=[]
                    matra_symbol=[]
                    for symbol in struc:
                        if symbol=='L':
                            count=jathi[tala_name[0]]
                            for i in range(count):
                                box=canvas.create_rectangle(base+i*30,80,base+((i+1)*30),110)
                                shape.append(box)
                            base+=count*30    
                        elif symbol=='D':
                            for i in range(2):
                                circle=canvas.create_oval(base+i*30,80,base+((1+i)*30),110)
                                shape.append(circle)
                            base+=60
                        elif symbol=='A':
                            triangle=canvas.create_polygon(base+15,80,base,110,base+30,110,fill='',outline='white')
                            shape.append(triangle)
                            base+=30

                    
                    canvas.create_rectangle(550,250,580,280)
                    canvas.create_text(750,265,text=": Lagu, one beat followed by finger counts",font=('Arial',16))
                    canvas.create_oval(550,300,580,330)
                    canvas.create_text(790,315,text=": Dhrutham, one beat followed by reversing your palm",font=('Arial',16))
                    canvas.create_polygon(565,350,550,380,580,380,fill='',outline='white')
                    canvas.create_text(690,365,text=": Anudhrutham, one beat",font=('Arial',16))
                    


                    #animating visuals
                    def get_positive_integer(prompt):
                        while True:
                            try:
                                value=int(input(prompt))
                                if value<=0:
                                    print('Please enter a number greater than zero')
                                    continue
                                
                                return value
                            except ValueError:
                                print('Please enter valid integer')

                              
                    bpm=get_positive_integer('enter bpm rate')
                    repeat=get_positive_integer('enter no of avartanas')
                    sec=60/bpm

                    dot_base=360
                    
                    canvas.create_text(250,275,text=f"BPM: {bpm}",font=('Arial',16))
                    av_text = canvas.create_text(270,325,text=f"Avartanas:   /{repeat}",font=('Arial',16))
                    root.update()
                    time.sleep(5)
    

                    for i in range(repeat):
                        for j in range(len(shape)):
                            canvas.itemconfig(av_text,text=f"Avartanas: {i+1}/{repeat}")
                            canvas.itemconfig(shape[j],fill='blue')
                            root.update()
                            dot=canvas.create_oval(dot_base+j*30,150,dot_base+10+j*30,160,fill='white')
                            root.update()
                            time.sleep(sec)
                            canvas.itemconfig(dot,fill='',outline='')      
                            root.update()
                            canvas.itemconfig(shape[j],fill='')
                            root.update()

                   
                        
            root.mainloop()
            user=input('Enter yes if you would like to try again, else no').upper()
            if user=='YES':
                continue
            else:
                break
        
    #menu of the program
    while True:
    
        print()
        print('choose option 1 to view structure of a talam',end='\n\n')
        print('choose option 2 to enter a particular talam having specific jathi and gathi and to know its matra and akshara',end='\n\n')
        print('choose option 3 to view all suladi sapta tala with their akshara and matra',end='\n\n')
        print('choose option 4 to filter talam by talam structure',end='\n\n')
        print('choose option 5 to filter talam by jathi',end='\n\n')
        print('choose option 6 to filter talam by gathi',end='\n\n')
        print('choose option 7 to filter talam by akshara',end='\n\n')
        print('choose option 8 to filter talam by matra',end='\n\n')
        print('choose option 9 to compare two talam by akshara and matra',end='\n\n')
        print('choose option 10 to know the talam of the day',end='\n\n')
        print('choose option 11 to know the statistics of stored talam',end='\n\n')
        print('choose option 12 to enter practice mode',end='\n\n')
        print('choose option 13 to access visual metronome',end='\n\n')
        print()
        try:
            option=int(input('choose your option'))
        except ValueError:
            print('enter valid option:an integer between 1 to 13')
            continue
        print()
        if option==1:
            view_structure()
        elif option==2:
            akshara_matra()
        elif option==3:
            all_talas()
        elif option==4:
            filter_talam()
        elif option==5:
            filter_jathi()
        elif option==6:
            filter_gathi()
        elif option==7:
            filter_akshara()
        elif option==8:
            filter_matra()
        elif option==9:
            compare()
        elif option==10:
            talam_of_day()
        elif option==11:
            statistics()
        elif option==12:
            practice()
        elif option==13:
            metronome()
        else:
            print('Invalid option. Try again')
            continue
            
        exit=input('Enter yes if you would like to explore other features, if not enter exit').upper()
        if exit=='YES':
            continue
        else:
            print('Thank you for using the suladi sapta talam application!!')
            break
        
    
    mycon.close()

talamdata()

