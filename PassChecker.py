import re
import tkinter as tk
from tkinter import messagebox
def password_checking(password):

    length_error=len(password)>=8
    upper_case_error=bool(re.search(r"[A-Z]",password ))
    lower_case_error=bool(re.search(r"[a-z]",password))
    digit_error=bool(re.search(r"[0-9]",password))
    special_char_error=bool(re.search(r"[!@#$%^&*]",password))
    
    score=sum([length_error,upper_case_error,lower_case_error,digit_error,special_char_error])

    if score==5:
        strength="Password is strong"
    elif score <= 2:
        strength="Password is medium"
    else:
        strength="Password is weak"


    missing=[]

    if not length_error:
        missing.append("Should be at least 8 character long")
    if not upper_case_error:
        missing.append("Should have at least one uppercase letter")
    if not lower_case_error:
        missing.append("Should have at least one lowercase letter")
    if not digit_error:
        missing.append("Should have at least one digit")
    if not special_char_error:
        missing.append("Should have at least one special character from !@#$%^&*")

    feedback=""
    if missing:
        feedback= ", ".join(missing) + "."
    return strength + ("\n" + feedback if feedback else "")

# GUI Implementation

root=tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

tk.Label(root,text="Please enter your password:").pack(pady=10)
password_entry=tk.Entry(root,show="*")
password_entry.pack(pady=5)

def check_password():
    password=password_entry.get()
    result=password_checking(password)
    messagebox.showinfo("Password Strength",result) 

check_button=tk.Button(root,text="Check Password",command=check_password)
check_button.pack(pady=10)
root.mainloop()

password=input("Enter a password : ")
print(password_checking(password)) 
