import smtplib, re
from threading import Thread

def send_water_remainder_email(to,user_name):
    
    gmail_user = ''
    gmail_password = ''
    sent_from = gmail_user

    subject = 'Water Remainder'
    body = f"Hello {user_name}" + "\n\n" + \
           "This is your friendly reminder to drink a glass of water and keep yourself hydrated.\
            Staying hydrated helps you stay focused, energized, and healthy!" + "\n\n" + \
           "Take a moment now to grab some water." + "\n\n" + \
           "Stay healthy,,\nYour Water Reminder Team"

    email_text = f'Subject: {subject}' \
                 f'\n' \
                 f'\n' \
                 f'{body}'

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        return True
    except Exception:
        return False

def start_email_thread(recipients):
    
    try:
        for recipient in recipients:
            thread = Thread(target=send_water_remainder_email, args = [recipient.email, recipient.name])
            thread.daemon = True
            thread.start()
        return True
    except Exception as e:
        return False
    
def email_validator(email):
    
    if re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
        username = email.split('@')[0]
        domain = email.split('@')[1]
        domain_name = domain.split('.')[0]
        domain_type = domain.split('.')[1]
        if 3 <= len(username) <= 64:
            if 1 <= len(domain_name) <= 30:
                if 1 <= len(domain_type) <= 5:
                    return True
    else:
        return False
