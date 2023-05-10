import requests
import time
import smtplib, ssl
import datetime
import json

# Part 0: Load user input
f = open('input.json')
user_input = json.load(f)
zipcode = user_input["zipcode"]
sender_email = user_input["sender_email"]
receiver_emails = user_input["receiver_emails"]
password = user_input["password"]
rate = user_input["rate"]
f.close()

# Part 1: Scrape the data
url = "https://my.uscis.gov/appointmentscheduler-appointment/field-offices/zipcode/" + user_input["zipcode"]

def check_availability():
    r = requests.get(url)
    json_data = r.json()
    time_slots = json_data[0]["timeSlots"]
    return (len(time_slots) > 0), r.text

# Part 2: Send email if available
def send_email():
    port = 465
    context = ssl.create_default_context()
    message = """\
    Subject: USCIS Appointment Available

    There is an appointment available at the USICS Office.

    Please go to this url: https://my.uscis.gov/appointmentscheduler-appointment/ca/en/office-search
    and type 98033 or Washington to find the office """
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login(sender_email, password)
        for receiver_email in receiver_emails:
            server.sendmail(sender_email, receiver_email, message)

def write_log(data):
    f = open("log.txt", "a")
    log = "Time: {time}, Data: {data}\n".format(time = datetime.datetime.now(), data = data)
    f.write(log)
    f.close()

def main():
    log_count = 0
    while True:
        available, data = check_availability()
        if available:
            print("Got em! Sending email now... at ", datetime.datetime.now())
            send_email()
            break
        else:
            print("Fuck! Sleeping", rate, "seconds and try again: ", datetime.datetime.now())
            if log_count % 10 == 0:
                write_log(data)
            time.sleep(rate)
        log_count += 1


if __name__ =="__main__":
    main()
