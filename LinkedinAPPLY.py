import argparse
from UtilsLinkedin import *
# Create the argument parser
from job import *


username = "@gmail.com"
password = ""
print(username, password)
start_linkedin(username, password)
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.CONTROL + '-')
sleep(10)
while True:
    for job in keywords:
        try:
            ApplyOnJob(job)
            ApplyOnJob(f"'{job}'")
        except:
            continue

