import smtplib

my_email = 'shananatest@gmail.com'
password = 'N4A5f#cRX*bR$'


with smtplib.SMTP("smtp.gmail.com") as connection:  # We create a connection to smtp server (Simple Mail Transfer
    # Protocol)
    connection.starttls()  # Next we secure connection to the server through tls (Transport Layer Security)
    connection.login(user=my_email, password=password)  # Login to your mail
    connection.sendmail(
        from_addr=my_email, to_addrs='shananatest@yahoo.com',
        msg='Subject:Hello\n\nThis is the body of my test mail'
    )
# no need to close connection, 'with' will do that!
# lessen other app security, so it won't give you error




