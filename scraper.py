import requests
from bs4 import BeautifulSoup
import smtplib 
import time

URL = ""
COMPARE = 0
SEARCH = False
 

user_agents_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

def send_mail():
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login("ritik.raina2005@gmail.com", <password>) 
    # message to be sent 
    message = "Price has dropped on product!" + str(URL)
    # sending the mail 
    s.sendmail("ritik.raina2005@gmail.com", "rraina@ucsd.edu", message) 
    # terminating the session 
    s.quit()  

def check_price():
    if len(URL) == 0: 
        initialization()
    else:
        page = requests.get(URL, headers = user_agents_header)
        initial = BeautifulSoup(page.content, "html.parser")
        soup = BeautifulSoup(initial.prettify(), "html.parser")
        price = soup.find(id = "priceblock_dealprice").get_text().strip()[1:]
        print(price)
        if (float(price) < float(COMPARE)):
            global SEARCH
            send_mail()
            print("Email sent!")
            SEARCH = True
        print("Search over!")

def initialization():
    global URL
    global COMPARE
    URL = input("Enter the website URL: ") 
    COMPARE = input("Enter the comparison amount: ")
    while(type(COMPARE) != int or len(str(COMPARE)) == 0 or COMPARE <= 0):
        try:
            COMPARE = float(COMPARE)
        except:
            print("Your comparison amount was an error! PLease input again")
            COMPARE = input("Enter the comparison amount: ")

while(SEARCH == False):
    check_price()
