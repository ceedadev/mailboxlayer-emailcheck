from keys import APIKEY
import requests
# import os
import time

#define Verification Class Logic
class Verify:
    def __init__(self,emails):
        self.emails = emails

        i = 0
        for email in self.emails:
            #checking per email
            r = requests.get(f'https://apilayer.net/api/check?access_key={APIKEY}&email={email}')
            print(r.status_code)
            print(r.json())

            #sleep for 1 sec for every 5 requests
            i += 1
            if i % 5 == 0:
                time.sleep(1)

#welcome message
print("Email Validator app")
print("Do you want to check single email address or bulk email address ?")
#get email address
mode = input('S for Single, B for Bulk : ')
if mode == 'S':
    #single email address
    emails = [input('Email Address : '),]
    Verify(emails)

elif mode == 'B':
    #bulk email address logic
    txt_path = input('Enter filepath for the txt file : ')
    file = open(txt_path, 'r')
    lines = file.readlines()
    emails = [line.strip() for line in lines]
    Verify(emails)

else:
    raise ValueError('Wrong input, Please Enter Either S or B, case sensitive')