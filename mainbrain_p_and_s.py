from body.speak import speak
import webbrowser
from tkinter import *
import os
import subprocess
from webextractors.weather import get_temp,get_sky,get_otherdata
from automation.sendmail import send_mail
from automation.whatsapp import send_wh_msg
from body.speak import speak
from schedule.alarm import set_alarm
from time import sleep
from schedule.alarm import check_alarm
import time
from other.screenshot import take_screenshot
from brains.Primarybrain import PrimaryBrain
from other.screenrecorder import screenre
from englisttohindi.englisttohindi import EngtoHindi
from automation.openapp import openapp



def get_response_txt(query,screenshotloc,screenreloc,web,apipath):
    try:

    
        check_alarm()
        alarm=["set alarm","set an alarm","wake me up at","wake me up","wake me"]

        vs=["open vs code","open vs editor","open vs","open" and "vs","I need to code","I have to code"]

        a=["i will give input by speech","i will give input by speaking","switch to voice input","i will command you by voice","i will give you command by voice"]




    
        if query==None:
            query=''

        elif query=='':
            query==''

        elif "open" and 'software' in query:
            query=str(query)
            query=query.replace("open","")        
            query=query.replace("software","")
            speak("opening "+query)
            openapp(query)
            sleep(1)
            speak(query+" opened")


        

        elif "write" and "code" in query:        
            win=Tk()

            def copy():
                win.clipboard_clear()
                win.clipboard_append(code)
                win.update()

            speak("With pleasure Sir")
            sleep(0.7)
            win.title("code")
            try:

                code=PrimaryBrain(apipth=apipath,question=query)

            except Exception as er:
                print(er)
                speak("Problem Printed . Contact Tushar about that !")
            Button(text="Copy Code",command=copy).pack()

            Label(text=code).pack()
            win.mainloop()





        elif "google search" in query:
            query=query.replace("google search","")
            webbrowser.open("https://www.google.com/search?q="+query)

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")



        
        


        elif "open" and "file explorer" in query:
            speak("opening file explorer")
            subprocess.run(["explorer", ","])
            query=''


       
        elif query in vs:
            speak("Okay Sir. Opening v s code . Happy Coding")
            os.startfile("D:/max assistant/Visual Studio Code")
            query=''

        elif "send mail" in query:
            speak("okay Sir. Please tell me the following details")
            
            time.sleep(2)
            re=input("reciever: ")
            sub=input("subject: ")
            bo=input("body: ") 
            time.sleep(2)
            send_mail(re,sub,bo,web) 
            time.sleep(2)
            speak("mail sent to "+re) 

        elif query in alarm:
            speak("okay Sir .")
            sleep(1)
            speak("please input the time in the following format")
            print("Hours:Minutes:Seconds")
            
            print("example -> 10:30:50")
            a=input("time: ")
            set_alarm(a)
            speak("alarm set")



        elif "tell weather of"  in query :
            query=str(query)
            c=query.replace("tell weather of","")
            


          #  c=input("Please input the city: ")
              

            try:
                print("The temperature of "+c+" is "+get_temp(c))          
                speak("The temperature of "+c+" is "+get_temp(c))        
            
                print("sky conditions of "+c+" are "+get_sky(c))         
                speak("sky conditions of "+c+" are "+get_sky(c))        
            
                print("some other data about "+c+" is "+get_otherdata(c))




                speak("some other data about "+c+" is "+get_otherdata(c))            
                query=''


            except Exception as e:
                print(e)
                speak(e)


                query=''

        elif query=="":
            query=''
            pass






        else:
            try:
                
                ans=PrimaryBrain(question=query,apipth=apipath)
            
                query=''
                if 'I am not able to take a screenshot' in ans:
                    speak("Taking screenshot after five seconds")
                    sleep(1)
                    speak("one")
                    sleep(1)
                    speak("two")
                    sleep(1)
                    speak("Three")
                    sleep(1)
                    speak("four")
                    sleep(1)
                    speak("five")
                    sleep(1)
                    take_screenshot(screenshotloc)
                    speak("Screenshot taken sir")

                elif "I am not able to do a screen recording" in ans:
                    speak("Starting screen recording after 5 seconds")     

                    sleep(1.3)
                    speak("one")
                    sleep(1.4)
                    speak("two")
                    sleep(1.3)
                    speak("Three")
                    sleep(1.4)
                    speak("four")
                    sleep(1.5)
                    speak("five")
                    sleep(1.3)
                    speak("starting screen recording")
                    screenre(screenreloc)
                    
                    speak("Screen recording stopped ")
                else:   
                    print(ans)
                    speak(ans)

            except Exception as e:
                print(e)
                speak("problem printed . Contact Tushar about that")

  
    except Exception:
        print(e)
        speak("problem printed . Contact Tushar about that")

        

       












