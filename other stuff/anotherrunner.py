import time, string, combine

while (1):
    fulltime = str(time.asctime(time.localtime(time.time())))
    if '23:59:59' in fulltime:
        outfile = open(fulltime, 'w+')
        combine.main()