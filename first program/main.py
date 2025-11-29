import smtplib

my_email = "adityabscit.2829@gmail.com"
password = "qwerty@123"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="abhibharti457@gmail.com",msg="dhbcsjkhlfiushjkcbsd.kcbsid")
connection.close()

