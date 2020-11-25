import time, string, emailbot, os, shutil

print('Press CTRL+C or CTRL+Z to stop the program')

while (1): 
    fulltime = str(time.asctime(time.localtime(time.time())))
    day = fulltime[0:fulltime.find(':')-3] + fulltime[fulltime.find(':')+6:len(fulltime)]
    if '00:00:00' in fulltime:
        print('Made new file:', day)
    if ':00 ' in fulltime:
        emailbot.record('../records/'+day)