import time, string, emailbot, os

print('Welcome, please select a time interval for recording contact tracing files')
print('1: Hourly')
print('2: Every 12 hours')
print('3: Daily')
print('q: Quit')
input1 = input()

while input1 not in ['1', '2', '3', '4', 'q', 'Q', 't', 'T']:#T = test
    print('Invalid response, please type one of the following options')
    print('1: Hourly')
    print('2: Every 12 hours')
    print('3: Daily')
    print('q: Quit')
    input1 = input()

if input1 not in ['q', 'Q', 't', 'T']:
    print('Running, press CTRL+Z to stop')

if input1 == '1':
    while (1):
        fulltime = str(time.asctime(time.localtime(time.time())))
        if ':00:00 ' in fulltime:
            print('Created New Contact Tracing List:', fulltime)
            emailbot.record(fulltime)
            time.sleep(1)

elif input1 == '2':
    while (1):
        fulltime = str(time.asctime(time.localtime(time.time())))
        if '12:00:00' in fulltime or '00:00:00' in fulltime:
            print('Created New Contact Tracing List:', fulltime)
            emailbot.record(fulltime)
            time.sleep(1)

elif input1 == '3':
    while (1):
        fulltime = str(time.asctime(time.localtime(time.time())))
        if '00:00:00' in fulltime:
            print('Created New Contact Tracing List:', fulltime)
            emailbot.record(fulltime)
            time.sleep(1)

elif input1 == 't' or 'T':
    while (1):
        fulltime = str(time.asctime(time.localtime(time.time())))
        if '12:00:00' in fulltime or '12:55:30' in fulltime:
            print('Created New Contact Tracing List:', fulltime)
            emailbot.record(fulltime)  
            time.sleep(1)

elif input1 == 'q' or 'Q':
    print('Quitting')
    quit()

