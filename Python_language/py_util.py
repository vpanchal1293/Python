
'''

html = '<html><table border="1"><tr><th>A</th><th>' + '</th><th>'.join(dict().keys()) + '</th></tr>'

for row in zip(*dict(fileNames).values()):
    print(row)
    m = '<tr><td>Object Name</td><td>' + '</td><td>'.join(row) + '</td></tr>' 
    print(m)
    html += m

html += '</table></html>'

file_ = open('result.html', 'w')
file_.write(html)
file_.close()
'''
import smtplib
sender = 'vp.panchal111@gmail.com'
receivers = ['jatin50790@gmail.com']
for i in range(1):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(sender, "Vipul12345!") 
    SUBJECT = "Hi Bbhura " + str(i) + 'th time'
    TEXT = "Message_you_need_to_send " + str(i) + 'th time'
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail(sender, receivers[0], message) 
    s.quit()
    print(i)