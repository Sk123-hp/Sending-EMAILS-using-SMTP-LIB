import smtplib
hostname = 'smtp.gmail.com'
email = 'muhammadshahbazkhan199@gmail.com'
password = 'pnod ddam nbnw btqm'  # use Gmail App Password

with smtplib.SMTP(host=hostname, port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg='Subject: Test Email\n\nHi Shahbaz Khan!'
    )