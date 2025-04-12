

#________________________________________________IMPORTING MODULES___________________________________________________________________________________________

import os
from datetime import date
import mysql.connector as con
import sys as s
import time 

#____________________________________________________________________________________________________________________________________________________________

import mysql.connector as con
connection=con.connect(host="localhost",user='niyati',password='#Rosebasket123')
cur=connection.cursor()
cur.execute('create database if not exists moodlogger')
cur.execute('use moodlogger')
cur.execute('create table if not exists accounts(username varchar(40),password varchar(40) primary key)')

#________________________________________________CREATING FILES____________________________________________________________________________________________________________

#CHECKING IF THE FILE EXISTS

#IF NOT , CREATING FILE AND STORING DATA


if os.path.exists('happy')==False:    
    f=open('happy','w')             
    l=["""1. Beautiful Day – U2
2. Happy – Pharrell Williams
3. I Gotta Feeling – Black Eyed Peas
4. (I’ve Had) the Time of My Life – Bill Medley & Jennifer Warnes
5. Walking On Sunshine – Katrina and the Waves
6. Ain’t No Mountain High Enough – Marvin Gaye
7. I’m A Believer – The Monkees
8. Love Shack – The B52’s
9. I Will Survive – Gloria Gaynor
10. Party Rock Anthem – LMFAO
11. Lean On Me – Bill Withers
12. Fine By Me – Andy Grammer
13. Home – Edward Sharpe & the Magnetic Zeros
14. Hey Ya! – Outkast
15. Daylight – Matt and Kim
16. Good Life – OneRepublic
17. Dog Days Are Over – Florence and the Machine
18. Walking on a Dream – Empire of the Sun
19. Raise Your Glass – Pink
20. I’m Coming Out – Diana Ross"""]
    f.writelines(l)    
    f.close


if os.path.exists('depressed')==False:
    f=open('depressed','w')
    l=["""1. The Rolling Stones – “Paint It, Black”
2. Sia – “Breathe Me”
3. The Fray – “How To Save a Life”
4. Radiohead – “Give Up the Ghost”
5. Skylar Grey – “Dance Without You”
6. The National – “Sorrow”
7. Adele – “Hold On”
8. R.E.M. – “Everybody Hurts”
9. Coldplay – “Fix You”
10. Bon Iver – “re:stacks’”
11. Gnarls Barkley – “Just a Thought”
12. Avril Lavigne – “Nobody’s Home”
13. Ed Sheeran – “Save Myself”
14. Gary Jules – “Mad World”
15. Blink 182 – “Adam’s Song”
16. Eminem – “Stan”
17. Lady Gaga – “Til It Happens To You”
18. Johnny Cash – “Hurt”
19. Leonard Cohen – “Our Lady of Solitude”
20. The War on Drugs – “Red Eyes”"""]
    f.writelines(l)    
    f.close


if os.path.exists('sad')==False:
    f=open('sad','w')
    l=["""1. ‘Nothing Compares 2 U’ by Sinéad O’Connor
2. ‘Hurt’ by Johnny Cash
3. ‘Only Love Can Break Your Heart’ by Neil Young
4. ‘Teardrop’ by Massive Attack
5. ‘I Know It’s Over’ by The Smiths
6. ‘No Distance Left to Run’ by Blur
7. ‘The Boxer’ by Simon & Garfunkel
8. ‘No Name #5’ by Elliott Smith
9. ‘Tom Traubert’s Blues (Four Sheets to the Wind in Copenhagen)’ by Tom Waits
10. ‘Lazarus’ by David Bowie
11. ‘Strange Fruit‘ by Billie Holiday
12. ‘The River’ by Bruce Springsteen
13. ‘How to Disappear Completely’ by Radiohead
14. ‘Someone Great’ by LCD Soundsystem
15. ‘Disintegration’ by The Cure
16. ‘Famous Blue Raincoat’ by Leonard Cohen
17. ‘Re: Stacks’ by Bon Iver
18. ‘Boots of Spanish Leather’ by Bob Dylan
19. ‘Neither One of Us’ by Gladys Knight and the Pips
20. ‘Brick’ by Ben Folds Five"""]
    f.writelines(l)    
    f.close


if os.path.exists('moody')==False:
    f=open('moody','w')
    l=["""1. 'Am Fenster'-City
2'Columbia'-Oasis
3. 'Light my fire'-The Doors
4. 'My Propeller'-Arctic Monkeys
5. 'She Bangs the Drums-The Stone Roses
6. 'Time-Pink Floyd
7. 'Velvet Morning-The Verve
8. 'Parallel Universe-RHCP
9. 'My Mistakes Were Made For You-The Last Shadow Puppets
10. 'Kiss Off-Violent Femmes
11. 'Married with children-Oasis
12. 'History-The Verve
13. 'Fluorescent Adolescent-Arctic Monkeys
14. 'Blister in the Sun-Violent Femmes
15. 'Psycho Killer-Talking Heads
16. 'Pet Sematary-Ramones
17. 'Killer Queen-Queen
18. 'Begging You-The Stone Roses
19. 'Secret Door-Arctic Monkeys"""]
    f.writelines(l)    
    f.close


if os.path.exists('angry')==False:
     f=open('angry','w')
     l=["""1. Girls Just Want To Have Fun – Cindi Lauper
2. I’ve Got The World On A String – Frank Sinatra
3. Do Wah Diddy Diddy – Manfred Mann
4. Light My Fire – The Doors
5. My Girl – The Temptations
6. La Vie En Rose – Louis Armstrong
7. You Can’t Hurry Love – The Supremes
8. Three Little Birds – Bob Marley
9. Swim – Jack’s Mannequin
10. Man in the Mirror – Michael Jackson
11. Born This Way – Lady Gaga
12. Let It Be – The Beatles
13. The Only Living Boy In New York – Simon and Garfunkel
14. Say Hey (I Love You) – Michael Franti & Spearhead
15. Count On Me (Album Version) – Mat Kearney
16. Wonderwall – Oasis
17. Walking On Sunshine – Katrina and the Waves
18. What A Wonderful World – Louis Armstrong
19. Fun, Fun, Fun – The Beach Boys
20. Everyday – Dave Matthews Band"""]
     f.writelines(l)    
     f.close

if os.path.exists('quotes')==False:
     f=open('quotes','w')
     l=["""'The best revenge is massive success.' – Frank Sinatra
'Act as if what you do makes a difference. It does.' – William James
'All our dreams can come true if we have the courage to pursue them.' – Walt Disney
'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.' – Swami Vivekananda
'The only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle.' – Steve Jobs
'I can’t change the direction of the wind, but I can adjust my sails constantly to reach my destination.' – Jimmy Dean
'What lies behind us and what lies before us are tiny matters compared to what lies within us.' – Ralph Waldo Emerson
'The more difficulties one encounters, the stronger one becomes. '– Napoleon Hill
'Great works are performed not by strength but by perseverance. '– Samuel Johnson
'Life isn’t about getting and having; it’s about giving and being.' – Kevin Kruse
'To be idle is a short road to death and to be diligent is a way of life; foolish people are idle, wise people work.'– Buddha
'You can never quit. Winners never quit, and quitters never win.' – Unknown
'Be yourself; everyone else is already taken.' – Oscar Wilde
'Fall seven times, stand up eight.' – Japanese Proverb"""]
     f.writelines(l)
     f.close()

if os.path.exists('lyrics')==False:
    f=open('lyrics','w')
    l1=['''\n\n    Maybe it's the way you say my name
    Maybe it's the way you play your game
    But it's so good, I've never known anybody like you
    But it's so good, I've never dreamed of nobody like you

    And I've heard of a love that comes once in a lifetime
    And I'm pretty sure that you are that love of mine

    'Cause I'm in a field of dandelions
    Wishing on every one that you'd be mine, mine
    And I see forever in your eyes
    I feel okay when I see you smile, smile

    Wishing on dandelions all of the time
    Praying to God that one day you'll be mine
    Wishing on dandelions all of the time, all of the time +1
        ''']
    f.writelines(l1)


    f.write('\n\nNIGHT CHANGES- HARRY STYLES\n')
    f.write("_"*30)
    l2=['''\n\n    Goin' out tonight, changes into something red
    Her mother doesn't like that kind of dress
    Everything she never had, she's showing off
    Driving too fast, moon is breaking through her hair
    She's heading for something that she won't forget
    Having no regrets is all that she really wants

    [Chorus: All, Harry]
    (Ooh) We're only getting older, baby
    (Ooh) And I've been thinking about it lately
    (Ooh) Does it ever drive you crazy
    (Ah-ah-ah) Just how fast the night changes?
    (Ooh) Everything that you've ever dreamed of
    (Ooh) Disappearing when you wake up
    (Ooh) But there's nothing to be afraid of
    (Ah-ah-ah) Even when the night changes
    (Ooh) It will never change me and you +2''']
    f.writelines(l2)


    f.write('\n\nBELIEVER - IMAGINE DRAGONS\n')
    f.write("_"*30)
    l3=['''\n\n    First things first
    I'ma say all the words inside my head
    I'm fired up and tired of the way that things have been, oh ooh
    The way that things have been, oh ooh

    Second things second
    Don't you tell me what you think that I could be
    I'm the one at the sail, I'm the master of my sea, oh ooh
    The master of my sea, oh ooh

    I was broken from a young age
    Taking my sulking to the masses
    Writing my poems for the few
    That look at me, took to me, shook to me, feeling me
    Singing from heartache from the pain
    Taking my message from the veins
    Speaking my lesson from the brain
    Seeing the beauty through the...

    Pain!
    You made me a, you made me a believer, believer
    Pain!
    You break me down, you build me up, believer, believer
    Pain!
    Oh let the bullets fly, oh let them rain
    My life, my love, my drive, it came from...
    Pain!
    You made me a, you made me a believer, believer +3
    ''']
    f.writelines(l3)


    f.write('\n\nLOVELY - BILLIE EILISH\n')
    f.write("_"*30)
    l4=['''\n\n    Thought I found a way
    Thought I found a way out (Found)
    But you never go away (Never go away)
    So I guess I gotta stay now

    [Pre-Chorus: Billie Eilish & Khalid]
    Oh, I hope some day I'll make it out of here
    Even if it takes all night or a hundred years
    Need a place to hide, but I can't find one near
    Wanna feel alive, outside I can't fight my fear

    Isn't it lovely, all alone?
    Heart made of glass, my mind of stone
    Tear me to pieces, skin to bone
    Hello, welcome home\n\n+4''']
    f.writelines(l4)

    f.write('RUNNING UP THAT HILL - KATE BUSH\n')
    f.write("_"*40)
    l5=['''\n\n[Verse 1]
    It doesn't hurt me (Yeah, yeah, yo)
    Do you wanna feel how it feels? (Yeah, yeah, yo)
    Do you wanna know, know that it doesn't hurt me? (Yeah, yeah, yo)
    Do you wanna hear about the deal that I'm makin'? (Yeah, yeah, yo)

[Pre-Chorus]
    You
    It's you and me

[Chorus]
    And if I only could
    I'd make a deal with God
    And I'd get him to swap our places
    Be runnin' up that road
    Be runnin' up that hill
    Be runnin' up that buildin'
    Say, if I only could, oh +5''']    
    f.writelines(l5)
    f.close()




#_________________________________________________FIRST FUNCTION______________________________________________________________________________________________

def write(file):       #function to write about todays events and save it into a file          
    print('*'*40)
    print('\nHey user , what all happened with you today ?')
    print("_"*40)
    print('\n',date.today())
    print('_'*40)
    lines=[]
    print('ENTER 0 TO STOP WRITING')
    while True:
        line=input('\n')
        lines.append(line)
        if lines[-1]=='0':
            break
        else:
            continue
    print('_'*40)
    print('\nThese are your lines\n','\n',lines)
    fr=open(file,'a')       
    fr.write('\n')
    for i in lines:
        fr.write('\n')        
        fr.write(i)
        fr.write('\n')
    fr.write('\n')
    fr.close()
    

#_________________________________________________SECOND FUNCTION______________________________________________________________________________________________

def mood(m='happy'):     #function that opens file that has music that matches the mood
    print('\nDo you want to see our exclusive',m,'mood songs to lift your mood more ?\n')
    hear=input('1.Yes\n2.No\nEnter your choice: ')
#if user wants songs
    if hear=='Yes' or hear=='yes' or hear=='1':
        f=open(m,'r')        
        time.sleep(1)
        print('\nThese are our collection , Hope it makes your mood much better :) \n')        
        fr=f.readlines()
        for i in fr:
            for j in i:
                if j=='\n':
                    i.replace(j, '')
        print('_'*50)
        for i in fr:
            print(i)        
    if hear=='2' or hear=='no' or hear=='No':
        print('\nNo problem\n')
    global name
    fr=open('happy','a')
    fr.write(str(date.today()))
    fr.write('\n')
    fr.write('_'*10)
    fr.write('\n')    
    fr.write('\nMood:\n')
    fr.write(m.upper())
    fr.write('\n')
    fr.write('\n')
    fr.close() 

#__________________________________________________THIRD FUNCTION_______________________________________________________________________________________________


def checkuser(name):       #function that checks if there is another user with same username
    connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
    sql_select_Query = "select * from accounts"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    l=[]
    for row in records:
        l.append(row[0])
    for i in l:
        if i==name:
            print('such user name already exists , Please try again')
        else:
            global flag
            flag='1'
#_________________________________________________USER FUNCTION________________________________________________________________________________________________

def USER():
    

    time.sleep(2)
    print('\n\n\n')
    print('\t'*5,'DAILY MOOD LOGGER')   #introduction
    print('\t'*5,'_'*17)
    print('\n')
    print('What is your name user?\n')
    time.sleep(2)
    n=input('')
    print('\nHey',n,'Do you have an account in daily mood logger?\n1.Yes\n2.No\n')
    ch=input('Please enter your choice:\n\n')

    #________________________IF USER HAS NO ACCOUNT__________________________


    if ch=='2' or ch=='No' or ch=='no':                 #Whenever a new user logs in a file and a record(username, password) will be created on their name
        t=True
        while t==True:
            name=input("\nPlease enter a username:\n\n")
            passwords=input('\nEnter a password:\n\n')
            t=os.path.exists(name)
            if t==True:
                print('\nSuch username already exists ,  DO you want to try again ?')
                y=input('1.yes\n2.no\n\nEnter your choice:\n\n')
                while True:
                    if y=='yes'or y=='Yes' or y=='1':
                        continue
                        break
                    else:
                        s.exit('Exitting the Programe')                 
            if t==False:
                print('\nYou have successfully created an account in daily mood logger :) \n\n')
                connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                sql_select_Query = "insert into accounts(username,password)values(%s,%s)"
                val=(name,passwords)
                cursor = connection.cursor()
                cursor.execute(sql_select_Query,val)
                connection.commit()
                fr=open(name,'w')
                fr.close()
                break
        print("_"*40)
        print('\nHey' ,name, ''' , Welcome to Daily Mood Logger\n\nhow do you feel today ?\n\nPlease select your mood:
              \n1.HAPPY :)\n2.MOODY -_-\n3.SAD :(\n4.DEPRESSED *_*\n5.ANGRY ¬_¬"\n6.ANY OTHER MOOD ‾◡◝''')

       #Asking for moods

        feel=input('\nEnter your mood: \n\n')

        if feel=='2' or feel.lower=='moody':
            mood('moody')
           
        elif feel=='4' or feel.lower=='depressed':
            mood('depressed')
             
        elif feel=='6' or feel.lower=='any other mood':
            print('\nEnter your mood :  ')
            m=input('\n')
            fr=open(name,'a')
            fr.write(str(date.today()))
            fr.write('\n')
            fr.write('_'*10)
            fr.write('\nMood:\n')
            fr.write(m.upper())
            fr.write('\n')
            fr.write('\n')
            fr.close() 
             
        elif feel=='3' or feel.lower=='sad':
            mood('sad')
            
           
        elif feel=='5' or feel.lower=='angry':
            mood('angry')
            
        else:
            mood('happy')
            

        #*****************************MOOD LOGGER OPTIONS***************************************
            
        print('_'*50)
        print('\nWhat would you like to do',name,'?')
        c= True
        while c==True:
            print('''\n1.READ GOOD QUOTES\n2.HEAR GOOD SONGS\n3.READ LYRICS\n4.JOT DOWN ABOUT TODAY
\n5.READ MY PREVIOUS ENTRIES\n6.CHANGE USERNAME\n7.DELETE ACCOUNT\n8.EXIT\n''')
            want=input('\nEnter Your Choice: ')

            if want=='8' or want=='Exit' or want=='exit':
                s.exit()

            elif want=='6' or want=='Change username' or want=='change username':            
                flag='0'
                t=True
                while t==True:
                    cname=input('\nPlease enter your user name:\n\n')
                    cpasswords=input('\nplease enter your password:\n\n')
                    if cname==name and cpasswords==passwords:
                        while True:
                            newname=input("\nplease enter your new username:\n\n")
                            checkuser(newname)
                            if flag=='1':  #no such username
                                print('\nYour old username',name,'has been changed to :',newname)                    
                                connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                                cur=connection.cursor()
                                query="delete from accounts where username=%s "                    
                                val=(name,)
                                cur.execute(query,val)
                                connection.commit()                    
                                query = "insert into accounts(username,password)values(%s,%s)"
                                value=(newname,passwords)                   
                                cur.execute(query,value)
                                connection.commit()
                                os.rename(name,newname)
                                name=newname
                                t=False                            
                                break                           
                            if flag=='0':
                                print("\nDo you want to try again?")
                                u=input('1.yes\n2.no :\n')
                                if u=='yes' or u=='1':
                                    continue
                                else:
                                    break
                    else:
                        print("\nDo you want to try again?")
                        u=input('1.yes\n2.no :\n')
                        if u=='yes' or u=='1':
                            continue
                        else:
                            break
                    
                        

            elif want=='5' or want=='Read my previous entries':
                print('\n\n\t"No previous entries"')
                continue

            elif want=='4' or want=='Jot down about today' or want=='jot down about today':
                write(name)            

            elif want=='2' or want=='Hear good songs' or want=='hear good songs':
                fr=open("happy",'r')
                time.sleep(1)
                print('\nThese are our collection , Hope it makes your day much better :) \n')
                f=fr.readlines()
                for i in f:
                    for j in i:
                        if j=='\n':
                            i.replace(j, '')
                print('_'*50,'\n')
                for i in f:
                    print(i)
                print('_'*50)
                fr.close()

            elif want=='1' or want=='Read good quotes' or want=='read good quotes':
                fr=open("quotes",'r')
                time.sleep(1)
                print('\nThese are our collection , Hope it makes your day much better :) \n')
                f=fr.readlines()
                for i in f:
                    for j in i:
                        if j=='\n':
                            i.replace(j, '')
                print('_'*50)
                for i in f:
                    print(i)
                print('_'*50)
                fr.close()

            elif want=='7' or want=='delete my account' or want=='Delete my account':
                print('ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT AFTER DELETING THIS PROGRAM WILL END\nTHIS STEP CANNOT BE REVERSED\n1.Yes\n2.No')
                n=input('\n')
                if n==1 or n.lower=='yes':
                    while True:
                        dname=input('\nPlease enter your user name:\n\n')
                        dpasswords=input('\nplease enter your password:\n\n')
                        if dname==name and dpasswords==passwords:
                            connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                            cur=connection.cursor()
                            query="delete from accounts where username=%s"
                            val=name,
                            cur.execute(query,val)
                            connection.commit()                        
                            os.remove(name)
                            print('YOU ACCOUNT HAS BEEN DELETED..............\n\n\nByee')
                            s.exit
                        else:
                            y=input('Wrong Username or Password..... \nDo you want to try again?\n1.yes\n2.no :\n\n')
                            if y=='yes' or y=='1':
                                continue
                            else:
                                break
                else:
                    print('Good Choice ;)')
                    continue
                    
            

            elif want=='3' or want.lower()=='read lyrics':
                f=open('lyrics','r')
                print('\n\n','_'*70,f.read(),"_"*70)

            else:
                continue
            
            
            
            
    #______________________________________IF USER ALREADY HAS AN ACCOUNT_____________________________________________

    else:
        c=True
        while c==True:
            name=input('\nPlease enter your user name:\n\n')
            passwords=input('\nplease enter your password:\n\n')
            connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
            sql_select_Query = "select * from accounts"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)   
            records = cursor.fetchall()
            l=[name,passwords]
            l2=[]
            flag='0'
            for row in records:
                l2.append([row[0],row[1]])        
            if l not in l2:
                print('\nWrong username or password , please try again\n')
                flag='1'            
            if l in l2:
                print('\nYou have succesfully logged into your account\n')                
                break
                flag='0'
            if flag=='1':
                y=input('Do you want to try again?\n1.yes\n2.no :\n\n')
                if y=='yes' or y=='1':
                    continue
                else:
                    s.exit('Exitting the program')
            

    #_____________________________________________________________________________________________________________

        time.sleep(1)
        print("_"*40)
        print('\nHey' ,name, ''' , Welcome back to Daily Mood Logger\n\nhow do you feel today ?\n\nPlease select your mood:
              \n1.HAPPY :)\n2.MOODY -_-\n3.SAD :(╰\n4.DEPRESSED *_*\n5.ANGRY ¬_¬"\n6.ANY OTHER MOOD‾◡◝''')

    #Asking for moods
        
        feel=input('\nEnter your mood: \n\n')

        if feel=='2' or feel=='Moody' or feel=='moody':
            mood('moody')

        elif feel=='4' or feel=='depressed' or feel=='Depressed':
            mood('depressed')

        elif feel=='6' or feel.lower=='any other mood':
            print('\nEnter your mood :  ')
            m=input('\n')
            fr=open(name,'a')
            fr.write(str(date.today()))
            fr.write('\n')
            fr.write('_'*10)
            fr.write('\nMood:\n')
            fr.write(m.upper())
            fr.write('\n')
            fr.write('\n')
            fr.close() 

        elif feel=='3' or feel=='sad' or feel=='Sad':
            mood('sad')

        elif feel=='5' or feel=='Angry' or feel=='angry':
            mood('angry')

        else:
            mood('happy')

    #************************************MOOD LOGGER OPTIONS*************************************
                
        print('_'*50)
        print('\nWhat would you like to do',name,'?')
        c= True
        while c==True:
            print('''\n1.READ GOOD QUOTES\n2.HEAR GOOD SONGS\n3.READ LYRICS\n4.JOT DOWN ABOUT TODAY
\n5.READ MY PREVIOUS ENTRIES\n6.CHANGE USERNAME\n7.DELETE ACCOUNT\n8.EXIT\n''')
            want=input('\nEnter Your Choice: ')

            if want=='8' or want=='Exit' or want=='exit':
                s.exit()

            elif want=='6' or want=='Change username' or want=='change username':            
                flag='0'
                t=True
                while t==True:
                    cname=input('\nPlease enter your user name:\n\n')
                    cpasswords=input('\nplease enter your password:\n\n')
                    if cname==name and cpasswords==passwords:
                        while True:
                            newname=input("\nplease enter your new username:\n\n")
                            checkuser(newname)
                            if flag=='1':  #no such username
                                print('\nYour old username',name,'has been changed to :',newname)                    
                                connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                                cur=connection.cursor()
                                query="delete from accounts where username=%s "                    
                                val=(name,)
                                cur.execute(query,val)
                                connection.commit()                    
                                query = "insert into accounts(username,password)values(%s,%s)"
                                value=(newname,passwords)                   
                                cur.execute(query,value)
                                connection.commit()
                                os.rename(name,newname)
                                name=newname
                                t=False                            
                                break                           
                            if flag=='0':
                                print("\nDo you want to try again?")
                                u=input('1.yes\n2.no :\n')
                                if u=='yes' or u=='1':
                                    continue
                                else:
                                    break
                    else:
                        print("\nDo you want to try again?")
                        u=input('1.yes\n2.no :\n')
                        if u=='yes' or u=='1':
                            continue
                        else:
                            break
            
            elif want=='5' or want=='Read my previous entries':
                f=open(name,'r')
                print(f.read())
                f.close()

            elif want=='4' or want=='Jot down about today' or want=='jot down about today':
                write(name)

            elif want=='2' or want=='Hear good songs' or want=='hear good songs':
                fr=open("happy",'r')
                time.sleep(1)
                print('\nThese are our collection , Hope it makes your day much better :) \n')
                f=fr.readlines()
                for i in f:
                    for j in i:
                        if j=='\n':
                            i.replace(j, '')
                print('_'*50,'\n')
                for i in f:
                    print(i)
                print('_'*50)
                fr.close()

            elif want=='1' or want=='Read good quotes' or want=='read good quotes':
                fr=open("quotes",'r')
                time.sleep(1)
                print('\nThese are our collection , Hope it makes your day much better :) \n')
                f=fr.readlines()
                for i in f:
                    for j in i:
                        if j=='\n':
                            i.replace(j, '')
                print('_'*50)
                for i in f:
                    print(i)
                print('_'*50)

            elif want=='7' or want=='delete my account' or want=='Delete my account':
                print('ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT , THE PROGRAM WILL END AFTER DELETION\nTHIS STEP CANNOT BE REVERSED\n1.Yes\n2.No\n')
                n=input('\n')
                if n==1 or n.lower=='yes':
                    while True:
                        dname=input('\nPlease enter your user name:\n\n')
                        dpasswords=input('\nplease enter your password:\n\n')
                        if dname==name and dpasswords==passwords:
                            connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                            cur=connection.cursor()
                            query="delete from accounts where username=%s"
                            val=name,
                            cur.execute(query,val)
                            connection.commit()                        
                            os.remove(name)
                            print('YOU ACCOUNT HAS BEEN DELETED..............\n\n\nByee')
                            s.exit()
                        else:
                            y=input('Wrong Username or Password..... \nDo you want to try again?\n1.yes\n2.no :\n\n')
                            if y=='yes' or y=='1':
                                continue
                            else:
                                break
                else:
                    print('\nGood Choice ;)')
                    continue
            elif want=='3' or want.lower()=='read lyrics':
                f=open('lyrics','r')
                print('\n\n','_'*70,f.read(),"_"*70)

            else:
                continue


#________________________________________________________________ADMIN FUNCTION__________________________________________________________________


def ADMIN():
    print('_'*70)
    print('\n\nHey there admin , how are you?\n')
    feel=input('')
    while True:
        print('\nWhat would you like to do?\n')
        print('*******MENU*******')
        print('_'*20)
        print('\n1.INSERT\n2.UPDATE\n3.SEARCH\n4.DELETE\n5.DISPLAY\n6.EXIT\n')
        print('_'*20)
        ch=input("\nEnter your choice:\n\n")

        if (ch=='6' or ch.lower()=='exit'):
            print('_'*70,'\n','\nTHANKYOU!!!\n','_'*70)
            time.sleep(2)
            s.exit()
  #______________________________DELETING_______________________________________

        elif (ch=='4' or ch.lower()=='delete'):

            while True:
                print('\nWhat Do You Want To Delete?\n')
                print('_'*20)
                print('\n1.SONG\n2.LYRICS\n3.QUOTE\n4.USER\n5.FILE\n6.Exit')
                print('_'*20)
                ch2=input('\n\nEnter Your Choice: ')

                if (ch2=='6' or ch2.lower()=='exit'):
                    break

                elif (ch2=='5' or ch2.lower()=='file'):
                    file2=input('\nEnter the name of the file you want to delete:\n\n[THIS PROCESS CANNOT BE REVERSED]\n\nFILENAME: ')
                    if (os.path.exists(file2)==True):
                        print('\nDELETING THE FILE.........')
                        time.sleep(2)
                        connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                        cur=connection.cursor()
                        query='select username from accounts'
                        cur.execute(query)
                        records=cur.fetchall()
                        if os.path.exists(file2):
                            os.remove(file2)
                        if file2 in records:
                            query="delete from accounts where username=%s"
                            val=file2,
                            cur.execute(query,val)
                            connection.commit()  
                        print('\nFILE DELETED\n')
                    else:
                        print("Such file doesn't exists , Please try again")

                elif (ch2=='4' or ch2.lower()=='user'):
                    name1=input('\nEnter the name of the user you want to delete [THIS PROCESS CANNOT BE REVERSED]\n\nUSERNAME: ')
                    if (os.path.exists(name1)==True):
                        print('\nDELETING THE USER.........')
                        connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                        cur=connection.cursor()
                        query="delete from accounts where username=%s"
                        val=name1,
                        cur.execute(query,val)
                        connection.commit()                        
                        os.remove(name1)
                        time.sleep(2)
                        print('\nUSER DELETED\n')
                    else:
                        print("Such username doesn't exists , Please try again")

                elif (ch2=='3' or ch2.lower()=='quote'):
                    fr=open("quotes",'r')
                    time.sleep(1)
                    print('\nThese are the current quotes in our collection\n')
                    f=fr.readlines()
                    for i in f:
                        for j in i:
                            if j=='\n':
                                i.replace(j, '')
                    print('_'*50)                    
                    for i in f:
                        print(i)
                    print('_'*50)
                    no=input('\nHOW MANY QUOTES YOU WANT TO DELETE:\n\n')
                    for i in range(no):
                        quote=input("Enter the quote you want to delete:\n\n")
                        if quote in fr:
                            fr.remove(quote)
                        else:
                            print('NO MATCHING QUOTE , TRY AGAIN')
                    
            
                elif (ch2=='2' or ch2.lower()=='lyrics'):                    
                        sname=input("Enter the name of the song whose lyrics you want to delete:\n\n")
                        f=open('lyrics','r')
                        fr=f.readlines()
                        for i in fr:
                            if sname.upper() in i:
                                fr.remove(i)
                            else:
                                print('\nNo such song name\n')
                        f.close()

                elif (ch2=='1' or ch2.lower()=='song'):
                    print('SONGS IN WHICH MOOD CATEGORY DO YOU WANT TO DELETE ?')
                    print('\n1.HAPPY\n2.MOODY\n3.SAD\n4.DEPRESSED\n5.ANGRY\n')
                    if feel=='2' or feel.lower=='moody':
                        delsong('moody')
           
                    elif feel=='4' or feel.lower=='depressed':
                        delsong('depressed')
                         
                    elif feel=='3' or feel.lower=='sad':
                        delsong('sad')
                                           
                    elif feel=='5' or feel.lower=='angry':
                        delsong('angry')
                        
                    elif feel=='1' or feel.lower=='happy':
                        delsong('happy')                
                    else:
                        print('WRONG CHOICE , PLEASE TRY AGAIN......')

   #____________________________________SEARCHING_________________________________________
                    
                    
        elif (ch=='3' or ch.lower()=='search'):

            while True:
                print('\nWhat Do You Want To Search?\n')
                print('_'*20)
                print('\n1.SONG\n2.LYRICS\n3.QUOTE\n4.USER\n5.FILE\n6.Exit')
                print('_'*20)
                ch3=input('\n\nEnter Your Choice: \n')

                if (ch3=='6' or ch3.lower()=='exit'):
                    break

                elif (ch3=='5' or ch3.lower()=='file'):
                    fname=input('\nEnter a file name to search: ')
                    if os.path.exists(fname)==True:
                        print('\nFILE FOUND!!')
                    else:
                        print('FILE NOT FOUND...\n')

                elif (ch3=='4' or ch3.lower()=='user'):
                    uname=input('\nEnter username to search: ')
                    if os.path.exists(uname)==True:
                        print('\nUSER FOUND')
                    else:
                        print('USER NOT FOUND\n')

                elif (ch3=='3' or ch3.lower()=='quote'):
                    fr=open("quotes",'r')
                    f=fr.read()
                    fr.seek(0)
                    quote=input("Enter the quote you want to search:\n\n")
                    if quote in f and quote!='' :
                        print('\nQUOTE FOUND!!\n')
                    else:
                        print('\nQUOTE NOT FOUUND....\n')
                    fr.close()

                elif (ch3=='2' or ch3.lower()=='lyrics'):
                    sname=input("Enter the name of the song whose lyrics you want to search :\n\n")
                    f=open('lyrics','r')
                    fr=f.read()
                    f.seek(0)
                    if sname.upper() in fr:
                        print('\nLYRICS FOUND!!!')
                    else:
                        print('\nLYRICS NOT FOUND.....')

                    f.close()

                elif (ch3=='1' or ch3.lower()=='song'):
                    nsong=input('\nWhich mood song do you want to search : ')
                    song=input('\nEnter the name of the song you want to search: ')
                    if os.path.exists(nsong)==True:
                        f=open(nsong,'r')
                        fr=f.read().split()
                        l=[]
                        for i in fr:
                            l.append(i.lower())                                            
                        if song in l:
                            print('\nSONG FOUND!!!!!')
                        else:
                            print('\nSONG NOT FOUND...')
                    else:
                        print('\nNO SUCH MOOD..')

                    f.close()


   #____________________________________UPDATE_______________________________________________
                    
                    
        elif (ch=='2' or ch.lower()=='update'):

            while True:
                print('\nWhat Do You Want To UPDATE?\n')
                print('_'*20)
                print('\n1.SONG\n2.LYRICS\n3.QUOTE\n4.USER\n5.FILE\n6.Exit')
                print('_'*20)
                ch4=input('\n\nEnter Your Choice: ')

                if (ch4=='6' or ch4.lower()=='exit'):
                    break

                elif (ch4=='5' or ch4.lower()=='file'):
                    foname=input('\nEnter current file name: ')
                    if os.path.exists(foname)==True:
                        fnname=input('Enter new file name to update: ')
                        print('\nFILE NAME UPDATE SUCCESFULLY!!!\n')
                        os.rename(foname,fnname)
                    else:
                        print('NO SUCH FILE FOUND , PLEASE TRY AGAIN........')

                elif (ch4=='4' or ch4.lower()=='user'):
                    uoname=input('\nEnter current username: ')
                    if os.path.exists(uoname)==True:
                        unname=input('Enter new user name to update: ')
                        if os.path.exists(unname)==False:
                            checkuser(newname)
                            if flag=='1':  #no such username
                                                  
                                connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                                cur=connection.cursor()
                                query="delete from accounts where username=%s "                    
                                val=(name,)
                                cur.execute(query,val)
                                connection.commit()                    
                                query = "insert into accounts(username,password)values(%s,%s)"
                                value=(newname,passwords)                   
                                cur.execute(query,value)
                                connection.commit()
                                os.rename(name,newname)

                        else:
                            print('\nSUCH USERNAME IS ALREADY IN USE PLEASE TRY AGAIN\n')
                        print('\nUSERNAME UPDATED SUCCESFULLY')
                    else:
                        print('\nUSER NOT FOUND\n')

                
                elif (ch4=='3' or ch4.lower()=='quote'):
                    fr=open("quotes",'r')
                    f=fr.readlines()
                    for i in f:
                        for j in i:
                            if j=='\n':
                                i.replace(j, '')
                    
                    oquote=input("Enter the quote you want update:\n\n")
                    if quote in fr:
                        nquote=input('Enter new quote: ')
                        fr.replace(oquote,nquote+'\n')
                        print('QUOTE UPDATED!!')
                    else:
                        print('QUOTE NOT FOUUND....')
                    fr.close()
                    

                elif (ch4=='2' or ch4.lower()=='lyrics'):
                    soname=input("Enter the name of the song whose lyrics you want to update:\n\n")
                    fr=open('lyrics','r')
                    f=fr.readlines()
                    for i in f:
                        for j in i:
                            if j=='\n':
                                i.replace(j, '')
                    for i in f:
                        if soname.upper() in i==True:
                            flag=1                              
                        else:
                            flag=0                            
                    if flag==1:
                        sname=input("\nEnter the new song name: ").upper() 
                        snname=input('\nEnter new lyrics: \n\n')
                        f.replace(i,sname+snname+'\n')
                        print('\nLYRICS UPDATED!!!\n')
                    elif flag==0:
                        print('\nNO SUCH SONG NAME....\n')
                    fr.close()


                elif (ch4=='1' or ch4.lower()=='song'):
                    nsong=input('\nWhich mood song do you want to update : ')
                    song=input('\nEnter the name of the song you want to update: ')
                    flag=0
                    if os.path.exists(nsong)==True:
                        fr=open(nsong,'r')
                        f=fr.read()
                        if song in f:
                            flag=1                                
                        else:                                
                            flag=0
                        if flag==1:
                            newsong=input('\nEnter the new song: ')
                            f.replace(song,newsong+'\n')
                            print('\nSONG UPDATED.....')
                        elif flag==0:
                            print('\nSONG NOT FOUND...\n')                            
                    else:
                        print('NO SUCH MOOD.....')

                    fr.close()


    #____________________________________INSERT_____________________________________
                    

        elif (ch=='1' or ch.lower()=='insert'):
        

            while True:
                print('\nWhat Do You Want To insert?\n')
                print('_'*20)
                print('\n1.SONG\n2.LYRICS\n3.QUOTE\n4.USER\n5.FILE\n6.EXIT')
                print('_'*20)
                ch4=input('\n\nEnter Your Choice: \n')

                if (ch4=='6' or ch4.lower()=='exit'):
                    break

                elif (ch4=='5' or ch4.lower()=='file'):
                    file3=input('\nEnter The File Name: ')
                    fr=open(file3,'w')
                    fr.close()

                elif (ch4=='4' or ch4.lower()=='user'):
                    t=True
                    while t==True:
                        name=input("\nPlease enter a username:\n\n")
                        passwords=input('\nEnter a password:\n\n')
                        t=os.path.exists(name)
                        if t==True:
                            print('\nSuch username already exists ,  DO you want to try again ?')
                            y=input('1.yes\n2.no\n\nEnter your choice:\n\n')
                            while True:
                                if y=='yes'or y=='Yes' or y=='1':
                                    continue
                                    break
                                else:
                                    s.exit('Exitting the Programe')                 
                        if t==False:
                            print('\nACCOUNT CREATED!!!')
                            connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                            sql_select_Query = "insert into accounts(username,password)values(%s,%s)"
                            val=(name,passwords)
                            cursor = connection.cursor()
                            cursor.execute(sql_select_Query,val)
                            connection.commit()
                            fr=open(name,'w')
                            fr.close()

                elif (ch4=='3' or ch4.lower()=='quote'):
                    fr=open('quotes','a')
                    quote1=input('\n\nEnter The Quote: \n\n')
                    
                    fr.write(quote1)
                    print('\n\nTHE QUOTE HAS BEEN SAVED!!!')
                    fr.close()

                elif (ch4=='2' or ch4.lower()=='lyrics'):
                    fr=open('lyrics','a')
                    songname=input('Enter the song name: \n\n')
                    print('_'*30+'\n')
                    print('ENTER 0 TO STOP WRITING')
                    lyrics=[]
                    while True:
                        lyric=input('\n')
                        if lyric!='0':
                            lyrics.append(lyric)
                        elif lyric=='0':
                            break
                    fr.write(songname.upper())
                    fr.write('\n')
                    fr.write('_'*30)
                    fr.writelines(lyrics)
                    print('\n\nTHE LYRICS HAS BEEN SAVED!!!\n\n')

                
                elif (ch4=='1' or ch4.lower()=='song'):
                    mood1=input('\nEnter The Mood Of The Song: ')
                    if os.path.exists(mood1)==True:
                        fr=open(mood1,'a')
                        song2=input('\nEnter The Song: \n\n')
                        l=[song2]
                        fr.writelines(l)
                        fr.close()
                        print('\nTHE SONG HAS BEEN SAVED!!!')
                    else:
                        time.sleep(2)
                        print('\n\nNO SUCH MOOD.......\n\nPLEASE TRY AGAIN')

    #_______________________________________DISPLAY________________________________________
                            
        elif (ch=='5' or ch.lower()=='display'):
            while True:
                print('\nWhat Do You Want To See?\n')
                print('_'*20)
                print('\n1.SONG\n2.LYRICS\n3.QUOTE\n4.USER\n5.FILE\n6.EXIT')
                print('_'*20)
                ch7=input('\n\nEnter Your Choice: \n')

                if (ch7=='6' or ch7.lower()=='exit'):
                    break

                elif (ch7=='5' or ch7.lower()=='file'):
                    print('\n\nTHESE ARE THE FILES IN YOUR CWD:\n')
                    files=os.listdir(str(os.getcwd()))
                    print('_'*20)
                    for file in files:
                        print('\n'+file)
                    print('\n'+'_'*20)

                elif (ch7=='4' or ch7.lower()=='user'):
                    connection=con.connect(host="localhost",database='moodlogger',user='niyati',password='#Rosebasket123')
                    cur=connection.cursor()
                    cur.execute('select username from accounts')
                    record=cur.fetchall()
                    print('\nTHESE ARE THE USERNAME OF USERS CURRENTLY LOGGED IN DAILY MOOD LOGGER: \n')
                    print('_'*20)
                    for i in record:
                        for j in i:
                            print('\n'+j)
                    print('\n'+'_'*20)

                elif (ch7=='3' or ch7.lower()=='quote'):
                    fr=open("quotes",'r')
                    time.sleep(1)
                    print('\nTHESE ARE THE CURRENT QUOTES IN THE FILE\n')
                    f=fr.readlines()
                    for i in f:
                        for j in i:
                            if j=='\n':
                                i.replace(j, '')
                    print('_'*50)
                    for i in f:
                        print(i)
                    print('_'*50)

                elif (ch7=='2' or ch7.lower()=='lyrics'):
                    f=open('lyrics','r')
                    print('\n\n','_'*70,f.read(),+'\n'+"_"*70)


                elif (ch7=='1' or ch7.lower()=='song'):
                    print('\nSONGS IN WHICH MOOD CATEGORY DO YOU WANT TO SEE ?')
                    print('\n1.HAPPY\n2.MOODY\n3.SAD\n4.DEPRESSED\n5.ANGRY\n')
                    if feel=='2' or feel.lower=='moody':
                        f=open('moody','read')
                        time.sleep(1)
                        print('\nTHESE ARE THE CURRENT SONGS IN THE FILE \n')        
                        fr=f.readlines()
                        for i in fr:
                            for j in i:
                                if j=='\n':
                                    i.replace(j, '')
                        print('_'*50+'\n')
                        for i in fr:
                            print(i)
                        print('\n'+'_'*50)
                    elif feel=='4' or feel.lower=='depressed':
                        f=open('depressed','r')
                        time.sleep(1)
                        print('\nTHESE ARE THE CURRENT SONGS IN THE FILE \n')         
                        fr=f.readlines()
                        for i in fr:
                            for j in i:
                                if j=='\n':
                                    i.replace(j, '')
                        print('_'*50+'\n')
                        for i in fr:
                            print(i)
                        print('\n'+'_'*50)
                                 
                    elif feel=='3' or feel.lower=='sad':
                        f=open('sad','r')
                        time.sleep(1)
                        print('\nTHESE ARE THE CURRENT SONGS IN THE FILE \n')         
                        fr=f.readlines()
                        for i in fr:
                            for j in i:
                                if j=='\n':
                                    i.replace(j, '')
                        print('_'*50+'\n')
                        for i in fr:
                            print(i)
                        print('\n'+'_'*50)
                                                       
                    elif feel=='5' or feel.lower=='angry':
                        f=open('angry','r')
                        time.sleep(1)
                        print('\nTHESE ARE THE CURRENT SONGS IN THE FILE \n')         
                        fr=f.readlines()
                        for i in fr:
                            for j in i:
                                if j=='\n':
                                    i.replace(j, '')
                        print('_'*50+'\n')
                        for i in fr:
                            print(i)
                        print('\n'+'_'*50)
                                
                    elif feel=='1' or feel.lower=='happy':
                        f=open('happy','r')
                        time.sleep(1)
                        print('\nTHESE ARE THE CURRENT SONGS IN THE FILE \n')        
                        fr=f.readlines()
                        for i in fr:
                            for j in i:
                                if j=='\n':
                                    i.replace(j, '')
                        print('_'*50+'\n')
                        for i in fr:
                            print(i)
                        print('\n'+'_'*50)                
                    else:
                        print('WRONG CHOICE , PLEASE TRY AGAIN......')
                       
                     
                    
                                        
                                        

                    

#______________________________________________________________MAIN PROGRAME_____________________________________________________________________


print('\n\n\n')
print('\t'*5,'DAILY MOOD LOGGER')   #introduction
print('\t'*5,'_'*17)
print('\n')
while True:
    print('\nARE YOU AN ADMIN OR A USER?\n(enter 0 to quit)')
    uad=input('\n\n')
    if uad.lower()=='admin':
        passwd=input('\n\nPLEASE ENTER YOUR PASSWORD: ')
        if passwd=='windows':
            print('\n\nCORRECT PASSWORD!!!!')
            time.sleep(3)
            ADMIN()
            break
        else:
            print('\n\nWRONG PASSWORD PLEASE TRY AGAIN........\n\n')
    elif uad.lower()=='user':
        time.sleep(2)
        USER()
    elif uad==0:
        time.sleep(2)
        s.exit()
    else:
        print('WRONG CHOICE')
                            
#____________________________________________________________________THE END_______________________________________________________________________________
           

#3554 LINES























