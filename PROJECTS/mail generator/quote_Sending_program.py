import datetime as dt
import random
import smtplib

my_email="ayushmaurya21806@gmail.com"
passw="kbeg kpfx pceu vyqa"

now=dt.datetime.now()
weekday=now.isoweekday()
if weekday== 1:
    with open("quotes.txt","r") as file:
        all_quotes=file.readlines()
        quote=random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email,password=passw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=["mauryaastha339@gmail.com", "gokuthesaiyan370@gmail.com","aslamkhan809442@gmail.com"],
            msg=f"subject:Quote of the day\n\n{quote}"
        )

    


