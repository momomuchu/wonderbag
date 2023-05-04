from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import argparse

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
# Create a Chrome Options instance
chrome_options = Options()

# Add the --headless argument
chrome_options.add_argument("--headless")

driver = webdriver.WebDriver(executable_path=ChromeDriverManager().install())

def button_handler():
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button')
    
    for button in buttons:
        buttonText = button.text.lower()

        if 'candidature' in buttonText:
            time.sleep(0.1)
            button.click()

            return
        if 'rifier' in buttonText or 'suivant' in buttonText:
            try:                    
                button.click()
            except:
                pass



def select_handler(value=None) -> None:
    selects = driver.find_elements(By.CSS_SELECTOR, 'select')
    for select in selects:
        options = Select(select).options[1:]
        random_option = random.choice(options)
        Select(select).select_by_visible_text(random_option.text)
def checkbox_handler() -> None:
    script = """
    function clickInputsInFieldsets() {
    function setChecked(element) {
        if (!element.checked) {
        element.click();
        }
    }

    var fieldsets = document.querySelectorAll('fieldset');
    for (var i = 0; i < fieldsets.length; i++) {
        var inputs = fieldsets[i].querySelectorAll('input[type="checkbox"], input[type="radio"]');
        for (var j = 0; j < inputs.length; j++) {
        setChecked(inputs[j]);
        }
    }
    }
    clickInputsInFieldsets();
    """

    driver.execute_script(script)
def button_handler():
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button')
    
    for button in buttons:
        buttonText = button.text.lower()

        if 'candidature' in buttonText:
            try:
                driver.execute_script("document.getElementById('follow-company-checkbox').click()")
            except:
                pass

            button.click()
            button = driver.find_element(By.CSS_SELECTOR, 'button[data-test-modal-close-btn]')
            button.click()
            return
        if 'continuer' in buttonText or 'suivant' in buttonText:
            try:                    
                button.click()
            except:
                pass

def new_input_handler():

    def set_value(element: WebElement) -> None:
        element.clear()
        element.send_keys('1')
        
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="number"]')
    for input in inputs:
        try:

            set_value(input)
        except:
            continue

def increment_all_number_inputs():
    """
    Increment the value of all number input fields by 1 using Selenium in Python.

    :param driver: A WebDriver instance to interact with the browser.
    """
    input_elements = driver.find_elements_by_xpath("//input[@type='number']")

    for input_element in input_elements:
        current_value = int(input_element.get_attribute('value') or 0)
        new_value = current_value + 1
        input_element.clear()
original_tab = driver.window_handles[0]
keywords = [
  # Data Science
  "Machine learning",
  "Deep learning",
  "Neural networks",
  "Natural language processing",
  "Data mining",
  "Data analysis",
  "Data visualization",
  "Statistics",
  "Predictive modeling",
  "Artificial intelligence",
  "Big data",
  "Business intelligence",
  "Hadoop",
  "Spark",

  "SQL",
  "Python",
  "Scikit-learn",
  "TensorFlow",
  "Keras",
  "PyTorch",
  "Pandas",
  "NumPy",
  "Matplotlib",
  "Seaborn",
  "NLTK",
  "SpaCy",
  "Gensim",
  "XGBoost",
  "LightGBM",
  "CatBoost",
  "AutoML",

  # Data Engineering
  "ETL",
  "Data warehousing",
  "Data pipelines",
  "Database administration",
  "Data architecture",
  "Data modeling",
  "Data integration",
  "Data quality",
  "data science",
  "data scientist",
  "data engineer",
  "data analyst",
  "Data governance",
  "Cloud computing",
  "AWS",
  "Azure",
  "Hadoop",
  "Spark",
  "SQL",
  "Python",

  # Web Development
  "HTML",
  "CSS",
  "JavaScript",
  "jQuery",
  "React",
  "AngularJS",
  "Node.js",
  "Express.js",
  "MongoDB",
  "MySQL",
  "PostgreSQL",
  "Django",
  "Flask",
  "Bootstrap",
  "RESTful APIs",
  "AWS",
  "Azure",
  "GCP",
  "React Native",
  "TypeScript",

  # Mobile Development
  "Kotlin",
  "Swift",
  "Objective-C",
  "iOS",
  "Android",
  "React Native",
  "Flutter",
  "Firebase",
  "RESTful APIs",
  "Mobile app development",
]

def button_handler():
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button')
    
    for button in buttons:
        buttonText = button.text.lower()
        print(buttonText)
        if 'candidature' in buttonText:
            time.sleep(0.01)
            button.click()

            return
        if 'tinuer' in buttonText or 'suivant' in buttonText:
            try:                    
                button.click()
            except:
                pass
def ApplyEveryTab(driver,original_tab):
    driver.switch_to.window(original_tab)
    tabs=driver.window_handles
    for i in range(8):
        
        for tab in tabs:
            if tab!=original_tab:
                
                driver.switch_to.window(tab)
                try:
                    increment_all_number_inputs()

                except:
                    pass
                try:
                    button_handler()
                except:
                    pass
                try:
                    new_input_handler()
                except:
                    pass
                try:
                    select_handler()
                except:
                    pass
                try:
                    checkbox_handler()
                except:
                    pass
                try:
                    checkbox_and_radio_inputs = driver.find_elements(By.XPATH, "//input[@type='checkbox'] | //input[@type='radio']")

                    for input_element in checkbox_and_radio_inputs:
                        input_element.click()
                except:
                    pass
                time.sleep(1)

#ApplyEveryTab(driver,original_tab)
driver.get('https://fr.indeed.com/jobs?q=développeur&l=&from=searchOnHP&vjk=4746db09ee7ac3f9')
import time

def login( email, password):
    driver.get('https://secure.indeed.com/account/login')
    time.sleep(1)
    print(driver.current_url)
    time.sleep(1)
    
    email_input = driver.find_element_by_css_selector('input[type="email"]')
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(0.1)

    submit_button = driver.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()
    time.sleep(1)

    fallback_link = driver.find_element_by_css_selector('a[data-tn-element="auth-page-google-password-fallback"]')
    fallback_link.click()
    time.sleep(1)

    password_input = driver.find_element_by_css_selector('input[type="password"]')
    password_input.send_keys(password)
    time.sleep(0.1)

    signin_button = driver.find_element_by_css_selector('button[data-tn-element="auth-page-sign-in-password-form-submit-button"]')
    signin_button.click()

login(username,password)

from time import sleep
original_tab = driver.window_handles[0]
driver.switch_to.window(original_tab)
index_emploi=0
driver.get('https://fr.indeed.com/jobs?q='+keywords[index_emploi])
while True:
    
    driver.switch_to.window(original_tab)
    
    length = driver.execute_script("return document.querySelectorAll('.jcs-JobTitle.css-jspxzf.eu4oa1w0').length")

    for index in range(0,length):
        try:
            driver.execute_script(f'document.querySelectorAll(".jcs-JobTitle.css-jspxzf.eu4oa1w0")[{index}].click();')
            sleep(3)
            if driver.execute_script("return document.querySelectorAll('.jobsearch-IndeedApplyButton-newDesign.css-1hjxf1u.eu4oa1w0').length > 0"):
                driver.execute_script("document.querySelectorAll('.jobsearch-IndeedApplyButton-newDesign.css-1hjxf1u.eu4oa1w0')[1].click();")
        except:
            pass
    try:
        ApplyEveryTab(driver=driver,original_tab=original_tab)
    except:
        continue

    tabs = driver.window_handles

    for tab in tabs:
        try:
            if tab != original_tab:
                driver.switch_to.window(tab)

                driver.close()
        except:
            pass
    driver.switch_to.window(original_tab)
    try:
        driver.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]').click()
    except:
        index_emploi+=1
        driver.get('https://fr.indeed.com/jobs?q='+keywords[index_emploi])

