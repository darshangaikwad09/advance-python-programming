import re

text = input("Enter a text: ")

pattern = r'\w+@\w+\.\w+'

emails = re.findall(pattern, text)

if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email address found.")

'''
Input: Contact me at darshan@gmail.com or friend123@outlook.com

Output:
Email addresses found:
darshan@gmail.com
friend123@outlook.com

'''
