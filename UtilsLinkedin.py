import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.WebDriver(executable_path=ChromeDriverManager().install())
import logging
from urllib.parse import urlparse, urlunparse, parse_qs

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(ch)
def new_url(url, page=1):
    logger.info(f"Generating new URL for page {page}.")

    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        query_params['start'] = [str(page*25)]
        new_query_string = '&'.join([f"{k}={v[0]}" for k, v in query_params.items()])
        new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string, parsed_url.fragment))

        logger.info(f"New URL generated: {new_url}")
        return new_url
    except Exception as e:
        logger.error(f"Error generating new URL: {e}")
        raise
def start_linkedin(username, password) -> None:
    logger.info("Logging in... Please wait for a few seconds.")
    driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")

    try:
        user_field = driver.find_element("id", "username")
        pw_field = driver.find_element("id", "password")
        login_button = driver.find_element("xpath", '//*[@id="organic-div"]/form/div[3]/button')
        user_field.send_keys(username)
        user_field.send_keys(Keys.TAB)
        time.sleep(2)
        pw_field.send_keys(password)
        time.sleep(2)
        login_button.click()
        time.sleep(3)
    except TimeoutException:
        logger.error("TimeoutException! Username/password field or login button not found.")
        raise


def click_button_by_text(driver, text):
    selector = "button span[aria-hidden='true']:contains('{}')".format(text)
    try:
        element = driver.find_element_by_css_selector(selector).find_element_by_xpath('..')
        element.click()
        logger.info(f"Clicked button with text: {text}")
    except Exception as e:
        logger.error(f"Error clicking button with text '{text}': {e}")
        raise

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_into_every_job(job, location=""):    
    logger.info("Entering job and location information...")
    input_element = driver.find_element_by_xpath("//input[@aria-label='Chercher par intitulé de poste, compétence ou entreprise']")
    input_element.clear()
    input_element.send_keys(job)

    elements = driver.find_elements_by_xpath("//input[starts-with(@id, 'jobs-search-box-location-')]")
    for element in elements:
        element.clear()
        element.send_keys(location)

    input_element.send_keys(Keys.ENTER)

    button_text = "Recherche"
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space(.)='{button_text}']")))

    try:
        logger.info("Clicking the search button...")
        button.click()
    except Exception as e:
        logger.error(f"Error clicking the search button: {e}")
        raise

    
#ClickIntoEveryJob("","France")
#scrolling
def scroll_down():
    logger.info("Scrolling down the page...")

    script = """
    var elem = document.querySelector('.jobs-search-results-list');
    var height = elem.scrollHeight / 10;
    for (var i = 0; i < 9; i++) {
        elem.scrollTop += height;
        await new Promise(resolve => setTimeout(resolve, 100));
    }
    """

    try:
        driver.execute_script(script)
        logger.info("Page scrolled down successfully.")
    except Exception as e:
        logger.error(f"Error scrolling down the page: {e}")
        raise
def Newurl(url,page=1):
    url = driver.current_url
    from urllib.parse import urlparse, urlunparse, parse_qs
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params['start'] = [str(page*25)]

    
    new_query_string = '&'.join([f"{k}={v[0]}" for k, v in query_params.items()])
    new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string, parsed_url.fragment))

    print(new_url)
    return new_url
#Newurl(driver.current_url)
liste_python = [
    'python',
    'javascript','typescript','c++',"Django","Flask","Pyramid","FastAPI","Sanic","NumPy","SciPy","Pandas","Matplotlib","Seaborn","Scikit-learn","TensorFlow","PyTorch","Keras","NLTK","BeautifulSoup","Scrapy","PyInstaller","React","Angular","Vue.js","jQuery","Bootstrap","D3.js","Leaflet","Mapbox","React Native","Flutter"
]
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

def select_handler(value=None) -> None:
    logger.info("Selecting random options from dropdown menus...")
    selects = driver.find_elements(By.CSS_SELECTOR, 'select')
    for select in selects:
        options = Select(select).options[1:]
        random_option = random.choice(options)
        Select(select).select_by_visible_text(random_option.text)
    logger.info("Random options selected from dropdown menus successfully.")

def input_handler(value: str) -> None:
    logger.info(f"Entering '{value}' into input fields...")
    def set_value(element: WebElement) -> None:
        element.clear()
        element.send_keys(value)

    inputs = driver.find_elements(By.CSS_SELECTOR, 'input')
    for input in inputs:
        set_value(input)
    logger.info(f"'{value}' entered into input fields successfully.")

    
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

def checkbox_handler() -> None:
    logger.info("Selecting checkboxes and radio buttons...")
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
    try:
        driver.execute_script(script)
        logger.info("Checkboxes and radio buttons selected successfully.")
    except Exception as e:
        logger.error(f"Error selecting checkboxes and radio buttons: {e}")
        raise
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

# Create logger
logger = logging.getLogger(__name__)

def button_handler():
    logger.info("Clicking buttons...")
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button')
    
    for button in buttons:
        buttonText = button.text.lower()

        if 'envoyer la candidature' in buttonText:
            try:
                driver.execute_script("document.getElementById('follow-company-checkbox').click()")
            except:
                pass
            time.sleep(0.1)
            button.click()
            button = driver.find_element(By.CSS_SELECTOR, 'button[data-test-modal-close-btn]')
            button.click()
            logger.info("Button clicked successfully.")
            return
        if 'rifier' in buttonText or 'suivant' in buttonText:
            try:                    
                button.click()
            except:
                pass
            time.sleep(0.25)
            logger.info("Button clicked successfully.")

def new_input_handler():
    logger.info("Entering values into input fields...")
    form= driver.find_elements(By.CSS_SELECTOR, 'form')[0]
    buttons = form.find_elements(By.CSS_SELECTOR, 'button')

    def set_value(element: WebElement) -> None:
        element.clear()
        element.send_keys('1')
        
    inputs = form.find_elements(By.CSS_SELECTOR, 'input')
    for input in inputs:
        try:
            time.sleep(0.1)
            set_value(input)
        except:
            continue
    logger.info("Values entered into input fields successfully.")

def Newurl(url,page=1):
    logger.info("Generating new URL...")
    url = driver.current_url
    from urllib.parse import urlparse, urlunparse, parse_qs
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params['start'] = [str(page*25)]

    new_query_string = '&'.join([f"{k}={v[0]}" for k, v in query_params.items()])
    new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string, parsed_url.fragment))
    if page*25 > NumberResult():
        logger.info("Next page found.")
        return 'NEXT'
    logger.info("New URL generated successfully.")
    return new_url

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


def ApplyEasy():
    logger.info("Starting ApplyEasy function...")
    try:
        button = driver.find_elements_by_css_selector('button[data-job-id]')[0]
        button.click()
    except:
        pass
    Stack=[]
    while True:
        try:
            logger.info("Calling button_handler function...")
            button_handler()
        except:
            pass

        time.sleep(0.2)

        if True:
            if len(Stack)>3:
                logger.info("In Stack handler...")
                if Stack[-2]==Stack[-1] and Stack[-2]==Stack[-3]:
                    try:
                        logger.info("Calling new_input_handler function...")
                        new_input_handler()
                    except:
                        pass
                    try:
                        time.sleep(0.1)
                        logger.info("Calling select_handler function...")
                        select_handler()
                    except:
                        pass
                    try:
                        time.sleep(0.1)
                        logger.info("Calling checkbox_handler function...")
                        checkbox_handler()
                    except:
                        pass
            if len(Stack)>7:
                logger.info("Clicking on 'Ignorer' button...")
                ignorer_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Ignorer"]'))
            )
                ignorer_button.click()

                logger.info("Clicking on 'discard_application_confirm_btn' button...")
                # click on the second button with data-control-name="discard_application_confirm_btn"
                confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]'))
            )
                confirm_button.click()
                logger.info("Application discarded successfully.")
                return
        from selenium.common.exceptions import NoSuchElementException


        try:
            span = driver.find_element(By.CSS_SELECTOR, 'span[role="note"]')
            Stack+=[span.text.strip()]
        except:
            sleep(1)
            logger.error("Error occurred while getting text from span element.")

            try:
                logger.info("Calling button_handler function...")
                button_handler()
                logger.info("Calling new_input_handler function...")
                new_input_handler()
            except:
                pass
            try:
                time.sleep(0.1)
                logger.info("Calling select_handler function...")
                select_handler()
            except:
                pass
            try:
                time.sleep(0.1)
                logger.info("Calling checkbox_handler function...")
                checkbox_handler()
            except:
                pass
            try:
                logger.info("Calling button_handler function...")
                button_handler()
                sleep(1)
            except:
                logger.error("Error occurred while calling button_handler function.")
            try:
                wait = WebDriverWait(driver, 4)
                element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-test-modal-close-btn]')))

                # Click on the element
                element.click()
            except:
                logger.error("Error occurred while closing modal window.")
                driver.execute_script("document.querySelector('button[data-test-modal-close-btn]').click()")
                sleep(1)
                driver.execute_script("document.querySelector('button[data-test-dialog-secondary-btn]').click()")

                print('error')

        try:
            if Stack[-1]=='100%':
                sleep(1)
                try:
                    logger.info("Calling button_handler function...")
                    button_handler()
                except:
                    pass
                sleep(1)
                try:
                    logger.info("Calling button_handler function...")
                    button_handler()
                    element.click()
                    logger.info("Modal window closed successfully.")
                except:
                    sleep(1)
                            
                        
                    logger.error("Error occurred while closing modal window.")
                    driver.execute_script("document.querySelector('button[data-test-modal-close-btn]').click()")
                return
        except:
            pass

        logger.info("ApplyEasy function finished successfully.")
import logging

def CancelApplication():
    logger.info('Attempting to ignore application.')
    ignorer_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Ignore"]'))
            )
    ignorer_button.click()

    # click on the second button with data-control-name="discard_application_confirm_btn"
    confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]'))
            )
    confirm_button.click()
    logger.info('Application ignored successfully.')

#pplyEasy()
import logging

def ApplyPage():
    try:
        for i in range(3):
            scroll_down()
    except Exception as e:
        logger.error(f'Error scrolling down: {e}')
    divs = driver.find_elements(By.CSS_SELECTOR, 'div[data-job-id]')

    for div in divs:
        div.click()
        time.sleep(2.05)
        try:
            button = driver.find_elements_by_css_selector('button[data-job-id]')[0]
            button.click()
            logger.info('Clicked on apply button.')
            try:
                ApplyEasy()
                logger.info('Application submitted successfully.')
            except Exception as e:
                logger.error(f'Error submitting application: {e}')
                try:
                    CancelApplication()
                    logger.info('Application ignored successfully.')
                except Exception as e:
                    logger.error(f'Error ignoring application: {e}')
        except Exception as e:
            logger.error(f'Error clicking on apply button: {e}')
            continue
def ClickIntoEveryJob(job,location=""):    
    sleep(1)
    input_element = driver.find_element_by_xpath("//input[@aria-label='Chercher par intitulé de poste, compétence ou entreprise']")
    sleep(1)
    # Click on the input element
    input_element.clear()
    input_element.send_keys(job)
    elements = driver.find_elements_by_xpath("//input[starts-with(@id, 'jobs-search-box-location-')]")
    sleep(1)
    logger.info('clicking on location')
# Loop through the elements and find the one with the exact id you want
    for element in elements:
        element.clear()
        element.send_keys(location)
    input_element.send_keys(Keys.ENTER)
    button_text = "Recherche"

# Wait for the button to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[normalize-space(.)='{button_text}']")))
    
    # Click the button
    button.click()
def ApplyOnJob(job):
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3120863207&f_AL=true&f_E=1%2C2&geoId=105015875&keywords=Machine%20learning&location=France&refresh=true&sortBy=R")
    ClickIntoEveryJob(job,"France")
    for page in range(0,40):
        time.sleep(1)
        
        newurl=Newurl(driver.current_url,page=page)
        if newurl=='NEXT':
            break
        driver.get(newurl)
        logger.info(f'Starting application process on page {page}.')
        ApplyPage()


keywords = [
  # Data Science

  "Spark",
  "Tableau",
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
  "Plotly",
  "NLTK",
  "SpaCy",
  "Gensim",
  "XGBoost",
  "LightGBM",
  "CatBoost",
  "AutoML",

  # Data Engineering

  "AWS",
  "Azure",
  "GCP",
  "Hadoop",
  "Spark",
  "Kafka",
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
  "Vue.js",
  "Next.js",
  "Nuxt.js",
  "Webpack",
  "Babel",
  "TypeScript",
  "GraphQL",
  "Apollo",
  "Jest",
  "Enzyme",
  "Cypress",
  "Storybook",

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
  "Mobile UX/UI design",

]
def NumberResult():
    div = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list__subtitle')
    import re
    # get the text inside the div element and extract the number from it
    num_str = div.text  # this should give you '2&nbsp;008 résultats'
    num_str = re.sub('[^0-9]', '', num_str)  # remove all non-numeric characters from the string
    num = int(num_str)  # convert the string to an integer

    # now you can use the 'num' variable as an integer
    return num