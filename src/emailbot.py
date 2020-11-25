import imaplib, email 

user = 'thisisatestforanemailbot@gmail.com'
password = 'A123456&'
imap_url = 'imap.gmail.com'

def get_body(msg): 
	if msg.is_multipart(): 
		return get_body(msg.get_payload(0)) 
	else: 
		return msg.get_payload(None, True) 

def search(key, value, con): 
	result, data = con.search(None, key, '"{}"'.format(value)) 
	return data 

def get_emails(result_bytes, con): 
    msgs = []
    for num in result_bytes[0].split(): 
        typ, data = con.fetch(num, '(RFC822)') 
        msgs.append(data)
        con.store(num, '+FLAGS', '\\Deleted') 
    #con.expunge() may need to un-comment this before deploying, may cause inbox to be completely filled if not
    
    return msgs 

def record(filename):
    outfile = open(filename, 'a+')

    con = imaplib.IMAP4_SSL(imap_url) 
    con.login(user, password) 
    con.select('Inbox') 

    msgs = get_emails(search('FROM', 'donotreply@wordpress.com', con), con) 

    for msg in msgs[::-1]: 
        for sent in msg: 
            if type(sent) is tuple: 
                content = str(sent[1], 'utf-8') 
                data = str(content) 
                indexstart = data.find("ltr") 
                data2 = data[indexstart + 5: len(data)] 
                indexend = data2.find("</div>") 
                body = data2[0: indexend]

                namestrt = int(body.find('Name: '))
                emailstrt = int(body.find('Email: '))
                numstrt = int(body.find('Phone Number: '))
                timestrt = int(body.find('Time: '))
                timeend = int(body.find('IP Address: ')-2)
                ipstrt = int(body.find('IP Address: '))
                ipend = int(body.find('Contact Form URL: ')-1)

                name = body[namestrt:emailstrt-4] + ' '
                emailadd = body[emailstrt:numstrt-4] + ' '
                phonenum = body[numstrt:timestrt-12] + ' '
                timee = body[timestrt:timeend] + ' '
                ipadd = body[ipstrt:ipend]

                entry = name + emailadd + phonenum + timee + ipadd + '\n'

                outfile.write(entry) 
