import imaplib, email, time, os

outfile = open('anotheroutput.txt', 'a+')
readfile = open('anotheroutput.txt', 'r')

user = 'thisisatestforanemailbot@gmail.com'
password = 'A123456&'
imap_url = 'imap.gmail.com'

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)

def get_body(msg):
    if msg.is_multipart(): 
        return get_body(msg.get_payload(0)) 
    else: 
        return msg.get_payload(None, True)   

def main():
    entries = ['','','','','','','','','','']
    con.select('INBOX')
    for i in range (10):
        astring = '*-'
        astring += str(i)
        result, data = con.fetch('*', '(RFC822)')
        raw = email.message_from_bytes(data[0][-1])
        body = str(get_body(raw))

        namestrt = int(body.find('Name: '))
        emailstrt = int(body.find('Email: '))
        numstrt = int(body.find('Phone Number: '))
        timestrt = int(body.find('Time: '))
        timeend = int(body.find('IP Address: ')-4)
        ipstrt = int(body.find('IP Address: '))
        ipend = int(body.find('Contact Form URL: ')-4)
        name = body[namestrt:emailstrt-8] + ' '
        emailadd = body[emailstrt:numstrt-8] + ' '
        phonenum = body[numstrt:timestrt-20] + ' '
        timee = body[timestrt:timeend] + ' '
        ipadd = body[ipstrt:ipend]
        entry = name + emailadd + phonenum + timee + ipadd + '\n'
        if entry not in entries:
            entries[i] = entry

    lines = ['','','','','','','','','','']
    acc = 0
    with open('anotheroutput.txt') as f:
        for line in f:
            acc += 1
            lines[acc%10] = line
            pass
        #last_line = line

    print(entries)
    print(lines)
    for i in range (10):
        for g in range (10):
            if lines[i] == entries[g]:
                entries[g] = ''
    print(entries)
    

    #entry = name + emailadd + phonenum + timee + ipadd + '\n'

    #print("lastl: ", repr(last_line))
    #print("entry: ", repr(entry))
    #print("equal? ", last_line == entry)
    print('hi')

    for i in range (10):
        #if last_line != entry:
        if entries[i] != '':
            #outfile.write(entry)
            outfile.write(entries[i])

    outfile.flush()