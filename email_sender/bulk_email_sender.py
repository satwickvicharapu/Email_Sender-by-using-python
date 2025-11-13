from single_email_sender import singleEmailSender




#bulk email send function defination
def bulkEmailSender(list_of_emails:list[str],subject:str,body:str):
    for email in list_of_emails:
        try:
            
#calling single email sender
            singleEmailSender(to_email=email, subject=subject, body=body)
            print(f"{email} to email send successfully")
        except Exception as e:
            print(f"{email} to email send field")
