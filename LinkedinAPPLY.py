import argparse
from UtilsLinkedin import *
# Create the argument parser
parser = argparse.ArgumentParser(description='Process login credentials')

# Add the username argument
parser.add_argument('username', type=str, help='the username')

# Add the password argument
parser.add_argument('password', type=str, help='the password')

# Parse the arguments
args = parser.parse_args()

# Access the username and password values
username = args.username
password = args.password
print(username, password)
start_linkedin(username, password)
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.CONTROL + '-')
ApplyOnJob('data engineer')

