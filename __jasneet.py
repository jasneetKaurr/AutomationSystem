"""
__jasneet.py:design and build an automation system using python stubs
             submitted by:jasneet kaur
             student_id:c0750018
"""

#-----------------imports------------------------------------------
import schedule
import time
import datetime
import smtplib
import ssl


#-------------sending emails----------------------------------------
server=smtplib.SMTP('smtp.gmail.com',587)             #Create SMTP session
server.ehlo()
server.starttls()                                     #Start TLS fro security

server.login("jasneet2805@gmail.com","Jaiveer10!")    #Authentication

msg="Hello, have a good day"                           #Message to send
server.sendmail("jasneet2805@gmail.com","jasneetk873@gmail.com",msg)  #Sending the email
server.quit()                                          #Terminating the session


#---------------------------------------------------------------------
Var = 0

print(datetime.datetime.now()," Stubs Starting...")

      

#-------------------Stubs for the tasks which print the task it is supposed to do------------------------------------------

def start_machine():

    global Var
    Var += 1
    print(datetime.datetime.now(),"Time to start the washing machine", Var) 



def playbigben():

    global Var
    Var += 1
    print(datetime.datetime.now(),"Time to play big ben sound", Var)

def webchecking():

    global Var
    Var += 1
    print(datetime.datetime.now(),"Time to chek if servers are online", Var)


def wakeup():
    global Var
    Var +=1
    print(datetime.datetime.now(),"Time to wake up now",Var)


def bowling():
    global Var
    Var +=1
    print(datetime.datetime.now(),"It's bowling time",Var)

def classtime():
    global Var
    Var +=1
    print(datetime.datetime.now(),"It's time to goto python class and learn the power of python",Var)


def send_email():
    global Var
    Var +=1
    print(datetime.datetime.now(),"Time to send email to javy with inspirational quotes",Var)



#A list of tasks that should be implemented with automation system
#----------------Task scheduling----------------------------------

#Every 10 minutes check that the web servers are online
schedule.every(10).minutes.do(webchecking)

#Play a Big Ben sound at the start of each hour. Except between 22:00 and 7:00
schedule.every().hour.do(playbigben).cancel_job().at("22:00","07:00")

#19:00 say that it is time to start the washing machine
schedule.every().day.at("19:00").do(start_machine)

#Wake you up at 7:30 every  morning
schedule.every().day.at("07:30").do(wakeup)

#Every Wednesday and Friday remind you that you have a Python Class (at 8:00)
schedule.every().wednesday.friday.at("08:00").do(classtime)

#Every Friday evening at 18:00 say that you have bowling
schedule.every().friday.at("18:00").do(bowling)

#Send an email to your favourite person every day with a quote from http://wisdomquotes.com/friendship-quotes/
schedule.every().day.do(send_email)



#Loop to keep the scheduling task running all the time
while True:
    schedule.run_pending()#Check if the scheduled task is pending to run or not
    time.sleep(1)

#Assignment requirements-------------------------------------------
#Here is a task list that should be implemented with your automation system:
##
##Every 10 minutes check that the web servers are online
##
##Play a Big Ben sound at the start of each hour. Except between 22:00 and 7:00
##
##At 19:00 say that it is time to start the washing machine
##
##Wake you up at 7:30 every  morning
##
##Every Wednesday and Friday remind you that you have a Python Class (at 8:00)
##
##Every Friday evening at 18:00 say that you have bowling 
##
##Send an email to your favourite person every day with a quote from http://wisdomquotes.com/friendship-quotes/









