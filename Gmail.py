import smtplib
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = "ssteja2946@gmail.com"
    sender_password = "ucvd fsrt pkoi lojf"
    receiver_email = receiver_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)
    if not sender_email or not sender_password or not receiver_email or not subject or not message.strip():
        messagebox.showwarning("Validation Error", "All fields must be filled out.")
        return
    full_message = f"Subject: {subject}\n\n{message}"
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, sender_password)
        s.sendmail(sender_email, receiver_email, full_message)
        s.quit()
        messagebox.showinfo("Success", "Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Authentication Error", "Failed to authenticate. Check your email and password.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email.\n{e}")
root = tk.Tk()
root.title("Email Sender")
#tk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5)
#sender_email_entry = tk.Entry(root, width=40)
#sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

# tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
# password_entry = tk.Entry(root, show="*", width=40)
# password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="To").grid(row=2, column=0, padx=10, pady=5)
receiver_email_entry = tk.Entry(root, width=40)
receiver_email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Subject").grid(row=3, column=0, padx=10, pady=5)
subject_entry = tk.Entry(root, width=40)
subject_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Message").grid(row=4, column=0, padx=10, pady=5)
message_text = tk.Text(root, height=10, width=40)
message_text.grid(row=4, column=1, padx=10, pady=5)

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=5, column=1, padx=10, pady=10)
root.mainloop()
