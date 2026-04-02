# import smtplib
# hostname = 'smtp.gmail.com'
# email = 'muhammadshahbazkhan199@gmail.com'
# password = 'pnod ddam nbnw btqm'  # use Gmail App Password

# with smtplib.SMTP(host=hostname, port=587) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs=email,
#         msg='Subject: Test Email\n\nHi Shahbaz Khan!'
#     )
import smtplib
import tkinter as tk
from tkinter import messagebox

# Function to send email
def send_email():
    hostname = 'smtp.gmail.com'
    port = 587
    email = sender_email.get()
    password = sender_password.get()
    recipient = recipient_email.get()
    subject = email_subject.get()
    body = email_body.get("1.0", tk.END)

    msg = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP(host=hostname, port=port) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=recipient,
                msg=msg
            )
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Python Email Sender")
root.geometry("400x400")

# Sender Email
tk.Label(root, text="Your Email:").pack(pady=2)
sender_email = tk.Entry(root, width=50)
sender_email.pack()

# Password
tk.Label(root, text="App Password:").pack(pady=2)
sender_password = tk.Entry(root, width=50, show="*")
sender_password.pack()

# Recipient Email
tk.Label(root, text="Recipient Email:").pack(pady=2)
recipient_email = tk.Entry(root, width=50)
recipient_email.pack()

# Subject
tk.Label(root, text="Subject:").pack(pady=2)
email_subject = tk.Entry(root, width=50)
email_subject.pack()

# Body
tk.Label(root, text="Body:").pack(pady=2)
email_body = tk.Text(root, height=10, width=50)
email_body.pack()

# Send Button
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack(pady=10)

root.mainloop()