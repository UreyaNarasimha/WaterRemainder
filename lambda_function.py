import smtplib

def lambda_handler(event, context):

    gmail_user = ''
    gmail_password = ''
    sent_from = gmail_user

    subject = 'Water Remainder'
    body = "Hello User" + "\n\n" + \
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

        emails_list = []

        for email in emails_list:
            try:
                smtp_server.sendmail(sent_from, email, email_text)
                print(f"Email sent to {email}")
            except Exception as e:
                print(f"Failed to send email to {email}: {e}")
        smtp_server.close()
        return True
    except Exception as ex:
        print("Something went wrong….", ex)
        return False
