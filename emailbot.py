import imaplib, email, time, os

outfile = open('output.txt', 'a+')
readfile = open('output.txt', 'r')

user = 'thisisatestforanemailbot@gmail.com'
password = 'A123456&'
imap_url = 'imap.gmail.com'

def get_body(msg):
    if msg.is_multipart(): 
        return get_body(msg.get_payload(0)) 
    else: 
        return msg.get_payload(None, True)   

def main(): 
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    con.select('INBOX')
    result, data = con.fetch(b'*', '(RFC822)')
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

    with open('output.txt') as f:
        for line in f:
            pass
        last_line = line

    entry = name + emailadd + phonenum + timee + ipadd + '\n'

    print("lastl: ", repr(last_line))
    print("entry: ", repr(entry))
    print("equal? ", last_line == entry)


    if last_line != entry:
        outfile.write(entry)

    outfile.flush()