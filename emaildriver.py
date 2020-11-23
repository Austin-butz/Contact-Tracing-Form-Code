import time, string, emailbot, os

while (1):
    fulltime = str(time.asctime(time.localtime(time.time())))
    if '00:00:00' in fulltime:
        print('Created New Contact Tracing List at: ')
        print(fulltime)
        emailbot.record(fulltime)