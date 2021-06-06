import os
import pyautogui
import time
import random
import subprocess
import datetime
import psutil
import sys
import win32gui
import win32con

class SAMPFARM(object):

    ''' TO DO LIST:
        Revise method: Log in at random times, for a total of 19 minutes, log in at 57-59 to cash
    '''
    chatlog=r'C:/Users/Stratos/Documents/GTA San Andreas User Files/SAMP/chatlog.txt'
    game_folder=r"D:\Program Files (x86)\Rockstar Games\GTA San Andreas\samp.exe"
    password='&&&&&&&&'
    
    gta_sa_window=None    
    def login(self, e=1): #Log in on LS:RP from SAMP main page
        attempt=e
        if attempt==10:
            print('failed to log in')
            sys.exit(0)
        open(self.chatlog, 'w').close()
        p = subprocess.Popen([self.game_folder, "server.ls-rp.io:7777"],stdout=subprocess.PIPE)
        print('mpainw sto samp')
        while(1):
            f=open(self.chatlog)
            print('psaxnw epiveveosi sindesis ston LS:RP')
            for line in f:
                if(line[11:23]=="Connected to"): #successful connection
                    print('sindesi epiveveothike')
                    time.sleep(5)          #wait until password pop up appears
                    pyautogui.typewrite(self.password) # Password field  
                    time.sleep(1)
                    pyautogui.press('enter')    
                    time.sleep(1)
                    pyautogui.moveTo(800, 423) #left character?
                    time.sleep(0.3)
                    pyautogui.click(clicks=1)
                    self.gta_sa_window=win32gui.GetForegroundWindow()
                if(line[11:17]=="SERVER"): #successful login
                    self.writeLogs('Successfully logged in')
                    p.kill()
                    return 1 #gia ta logs isws "login successful" na kanei return
                if(('ERROR:' in line) or ('Server clo' in line)):
                    print("couldn't log in")
                    self.quitGame()
                    self.forceCrash()
                    attempt+=1
                    print("retrying")
                    self.login(attempt)
                    return 0
            time.sleep(1)
            
   
    def checkTime(self, e=1): # Needs to be readjusted to separate time into groups and calculate for how much time user needs to remain signed in before leaving.
        r = random.randrange(3, 31)
        print("chosen random login time:",r)
        self.writeLogs('Chosen random login time: '+str(r))
        while(1):
            now = datetime.datetime.now()
            if(now.minute>=3 and now.minute<32 or now.minute==r): 
                time.sleep(random.randrange(0,3))
                self.login()
                return 1
            if(now.minute<r or now.minute>r):               
                currentTime=now.minute
                if(currentTime>r):
                    wait=60-currentTime+r
                    print ('waiting for',(wait),'minutes')
                    self.writeLogs('waiting for '+str(wait))
                    time.sleep(wait*60)
                else:
                    wait=r-currentTime
                    print('waiting for',(wait),'minutes')
                    self.writeLogs('waiting for '+str(wait))
                    time.sleep(wait*60)
                    
        
    
    def antiKick(self, e=1): # Logic: Random movements & force crash upon PM or /b & /q upon paycheck.
        lastMove=0
        y=0
        pyautogui.FAILSAFE = False # important
        started = (datetime.datetime.now()).minute
        while(1):
            current = (datetime.datetime.now()).minute
            z=self.receivedPaycheck()
            if (z==-1):
                break
            if(z==1):
                return 1; #received paycheck, close.
            if(current==started+20):
                time.sleep(random.randrange(40,120))
                self.minmaxGTA('max')
                time.sleep(random.randrange(1,3))
                self.quitGame()
                self.writeLogs("Done time, waiting for :59")
                return 0
            number = random.randint(1,3) #how many moves?
            r = random.randint(4, 8) #time between moves in minutes
            if(current==lastMove+r or y==0 or current==1): #if current ==1 it means that hour has passed.
                self.minmaxGTA('max')
                time.sleep(random.randrange(1,3))
                z=self.receivedPaycheck()
                if(z==-1):
                    break
                if(z==1):
                    self.writeLogs("Somehow received a paycheck, don't ask")
                    return 1; #received paycheck OR reached 20 minutes of afk'ing.
                if(current>=started+20):
                    self.quitGame()
                    self.writeLogs("Done time, waiting for :59")
                    return 0
                print("Moving")
                self.writeLogs('Initiating new movement sequence: '+ str(number))
                y=1
                lastMove=(datetime.datetime.now()).minute
                for _ in range(number):
                    whatever = random.randint(1,6)
                    if(whatever==1):
                        pyautogui.mouseDown(button='right')
                        pyautogui.keyDown('shift')
                        time.sleep(0.5)
                        pyautogui.mouseUp(button='right')
                        pyautogui.keyUp('shift')
                    if(whatever==2):
                        pyautogui.keyDown('alt')
                        pyautogui.keyDown('w')
                        pyautogui.keyDown('a')
                        time.sleep(0.5)
                        pyautogui.keyUp('w')
                        pyautogui.keyUp('a')
                        pyautogui.keyUp('alt')
                    if(whatever==3):
                        pyautogui.keyDown('s')
                        pyautogui.keyDown('a')
                        time.sleep(0.5)
                        pyautogui.keyUp('s')
                        pyautogui.keyUp('a')
                    if(whatever==4):
                        pyautogui.keyDown('d')
                        pyautogui.keyDown('s')
                        time.sleep(0.5)
                        pyautogui.keyUp('d')
                        pyautogui.keyUp('s')
                    if(whatever==5):
                        pyautogui.keyDown('alt')
                        pyautogui.keyDown('w')
                        pyautogui.keyDown('d')
                        time.sleep(0.5)
                        pyautogui.keyUp('w')
                        pyautogui.keyUp('d')
                        pyautogui.keyUp('alt')
                self.minmaxGTA('min')
                pyautogui.keyUp('alt')
        time.sleep(5)

#TODO FIX:
          
    def minmaxGTA(self, mode):
        time.sleep(0.5)
        if(mode=='min'):
            self.writeLogs('Minimizing Window')
            win32gui.ShowWindow(self.gta_sa_window, win32con.SW_FORCEMINIMIZE)
            time.sleep(1.5)
            return 1
        elif(mode=='max'):
            self.writeLogs('Maximizing Window')
            win32gui.ShowWindow(self.gta_sa_window, win32con.SW_RESTORE)
            time.sleep(1.5)
            return 1
        
        
    def receivedPaycheck(self, e=1): #Logic: The moment you receive paycheck /q, the moment you receive an ooc message force crash.
        f=open(self.chatlog)
        for line in f:
            current = (datetime.datetime.now()).minute
            if(line[11:13]=="(("): #ooc message
                orig=line
                line2=line.split('{')
                line2=line[1].split('}')
                if(line2[0]=='FF9900'): #admin
                    try:
                        print('force crashing because of admin!') #initiate force crash method
                        g = orig.split(':')            #experimental for auto /pm before force crash
                        ID = g[3].replace(")", "")
                        say = random.choice([' sup',' yo',' wassup',' hey'])
                        time.sleep(random.randrange(2, 5))
                        pyautogui.typewrite('t/pm'+ID+say)
                        time.sleep(0.5)
                        pyautogui.press('enter')
                        time.sleep(1)
                        self.forceCrash()
                        self.writeLogs('Had to force crash because of '+orig)
                        print(orig)
                        '''time.sleep(10800)
                        return 1''' #se periptwsi pou thelw na ksanampei se 3 wres anti gia full termination.
                        sys.exit()
                    except:
                        self.forceCrash()
                        sys.exit()
                elif(line[14]=="["): #/b
                    print('force crashing because of a \/b')
                    self.forceCrash()
                    self.writeLogs('Had to force crash because of '+orig)
                    sys.exit()
            if(line[16:20]=="BANK"): #received paycheck
                print('new paycheck')
                self.writeLogs('Received new paycheck')
                r = random.uniform(1.5, 5.1)
                time.sleep(r)
                self.quitGame()
                return 1
            if(line[11:19]=="Server c"): #Kicked from server
                print('kicked from the server')
                self.forceCrash()
                self.writeLogs('Kicked from the server')
                sys.exit()
            if(line[11:21]=="The server"): #server restarting
                print('server is restarting, detected The server msg')
                self.forceCrash()
                self.writeLogs('we either lost connection or server restarted')
                return -1
#You have been teleported
            if(line[11:24]=="You have been"):
                print('teleported')
                time.sleep(0.5)
                self.forceCrash()
                #open(self.chatlog, 'w').close()
                self.writeLogs("Had to force crash because of teleport")
                self.writeLogs(line)
                sys.exit()
    
    def forceCrash(self, e=1): #Logic: Finds the process named gta_sa.exe and kills it thus causing a crash.
        PROCNAME = "gta_sa.exe"
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()
                self.writeLogs('Successfully force-crashed')
                
    def quitGame(self,e=1): #Logic: logs out of the game.
        time.sleep(0.5)
        pyautogui.typewrite('t/q')
        time.sleep(random.random()*2)
        pyautogui.press('enter')
        self.writeLogs('Successfully quit the game')
        time.sleep(2)
        try:
            self.forceCrash()
        except:
            pass
        
    def writeLogs(self, text):
        try:
            f= open('logs.txt', 'a')
            time=(str)(datetime.datetime.now())
            f.write(time+" "+ r"||" + " " + text+"\n")
            f.close()
            return 1
        except:
            print('failed to write')
            return 0
#MAIN
a=SAMPFARM()
while(1):
   a.checkTime()
   suc=a.antiKick()
   if(suc==0):
       whenToLogin=random.randint(56,58)
       print('I am going to log back at :'+str(whenToLogin))
       time.sleep((whenToLogin-(datetime.datetime.now()).minute)*60)
       a.login()
       while(1):
           y=a.receivedPaycheck()
           if y==-1:
               break
           if(y==1 or datetime.datetime.now().minute==4):
               a.forceCrash()
               break
           time.sleep(1)
   time.sleep(5)

