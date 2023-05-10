# USCIS Appointment Checker

Automate checking USCIS ACS appointment and get email notification upon availability

Example json:
```
{
    "sender_email": "example@gmail.com",
    "receiver_emails": [
        "example1@gmail.com",
        "example2@gmail.com"
    ],
    "zipcode": "12345",
    "rate": 10,
    "password": "abcde"
}
```

`sender_email`: the email used to send notification

`receiver_emails`: a list of emails to receive notification

`zipcode`: the zipcode of the offices you want to check

`rate`: sleep seconds between each GET requests

`password`: password to login to sender_email

Run:
```
py main.py
```