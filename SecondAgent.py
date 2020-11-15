import win32com.client
import os
import time

while True:  
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo") 
    computer_name = os.getenv('COMPUTERNAME')
    qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\save-deleted"
    queue=qinfo.Open(1,0)   
    msg=queue.Receive()
    print("------------------------------------------/")
    print("Title:",msg.Label) 
    print("                                           ")
    print("Body:",msg.Body)
    print("-------------------------------------------")
    time.sleep(2)
    queue.Close()