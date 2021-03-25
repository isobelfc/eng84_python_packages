# Python requests package
# Let's connect to live web using Python requests api
# We will connect to www.bbc.com and check if the web is live
import requests

# responses = requests.get("http://www.bbc.co.uk/")

# if responses.status_code == 200:
#     print(f"The website is up and running. Status code is {responses.status_code}")
# else:
#     print(f"Oops, something went wrong. Status code is {responses.status_code}")
# # status 200 which is a success means the website is live running
# # status 400 or 404 means not working

# Create a function called status code check
# Function should return status code with appropriate message
# DRY

# def status_code_check(url):
#     responses = requests.get(url)
#     if responses.status_code == 200:
#         print(f"The website is up and running. Status code is {responses.status_code}")
#     else:
#         print(f"Oops, something went wrong. Status code is {responses.status_code}")
#
# status_code_check("http://bbc.co.uk/")

def check_status(url):
    response = requests.get(url)
    if response:  # the condition was True
        print("success and the status code was " + str(response.status_code))
    else:
        print("failure, status code " + str(response.status_code))
# requests goes one step further in simplifying this process for us
# if you use response instance in a condition expression
# it will evaluate to True if the status code was between 200 and 400, False otherwise
# therefore you can simplify the last example by rewriting

check_status("http://www.bbc.co.uk/")
check_status("http://www.bbc.co.uk/n")
