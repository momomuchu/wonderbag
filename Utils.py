import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.WebDriver(executable_path=ChromeDriverManager().install())
def NumberResult():
    div = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list__subtitle')
    import re
    # get the text inside the div element and extract the number from it
    num_str = div.text  # this should give you '2&nbsp;008 résultats'
    num_str = re.sub('[^0-9]', '', num_str)  # remove all non-numeric characters from the string
    num = int(num_str)  # convert the string to an integer

    # now you can use the 'num' variable as an integer
    return num
def start_linkedin(username, password) -> None:
    print("Logging in.....Please wait for a few seconds")
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
        print("TimeoutException! Username/password field or login button not found")
def ApplyOnJob(job):
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3120863207&f_AL=true&f_E=1%2C2&geoId=105015875&keywords=Machine%20learning&location=France&refresh=true&sortBy=R")
    ClickIntoEveryJob(job,"France")
    for page in range(0,40):
        time.sleep(1)
        
        newurl=Newurl(driver.current_url,page=page)
        if newurl=='NEXT':
            break
        driver.get(newurl)
        ApplyPage()
def ApplyPage():
        try:
            for i in range(3):
                scroll_down()
        except:
            pass
        divs = driver.find_elements(By.CSS_SELECTOR, 'div[data-job-id]')

        for div in divs:
            div.click()
            time.sleep(2.05)
            if True:
                try:
                    button = driver.find_elements_by_css_selector('button[data-job-id]')[0]
                    button.click()
                except:
                    continue
                try:
                    ApplyEasy()
                except:
                    try:
                        CancelApplication()
                    except:
                        pass
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
    try:
        button = driver.find_elements_by_css_selector('button[data-job-id]')[0]
        button.click()
    except:
        pass
    Stack=[]
    while True:
        try:
            button_handler()
        except:
            pass

        time.sleep(0.2)
        
        if True:
            if len(Stack)>3:
                print('In Stack handler')
                if Stack[-2]==Stack[-1] and Stack[-2]==Stack[-3]:
                    try:
                        new_input_handler()
                    except:
                        pass
                    try:
                        time.sleep(0.1)
                        select_handler()
                    except:
                        pass
                    try:
                        time.sleep(0.1)
                        checkbox_handler()
                    except:
                        pass
            if len(Stack)>7:
                ignorer_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Ignorer"]'))
            )
                ignorer_button.click()

            # click on the second button with data-control-name="discard_application_confirm_btn"
                confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]'))
            )
                confirm_button.click()
                print('ignore_application_confirm_btn')
                return
        from selenium.common.exceptions import NoSuchElementException


        try:
            span = driver.find_element(By.CSS_SELECTOR, 'span[role="note"]')
            Stack+=[span.text.strip()]
        except:
            sleep(1)
            print('Error %')
            
            try:
                button_handler()
                new_input_handler()
            except:
                pass
            try:
                time.sleep(0.1)
                select_handler()
            except:
                pass
            try:
                time.sleep(0.1)
                checkbox_handler()
            except:
                pass
            try:
                button_handler()
                sleep(1)
            except:
                print('error1')
            try:
                wait = WebDriverWait(driver, 4)
                element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-test-modal-close-btn]')))

                # Click on the element
                element.click()
            except:
                driver.execute_script("document.querySelector('button[data-test-modal-close-btn]').click()")
                sleep(1)
                driver.execute_script("document.querySelector('button[data-test-dialog-secondary-btn]').click()")
                
                print('error')

        try:
            if Stack[-1]=='100%':
                sleep(1)
                try:
                    button_handler()
                except:
                    pass
                sleep(1)
                try:
                    button_handler()
                    sleep(1)
                except:
                    print('error1')
                try:
                    wait = WebDriverWait(driver, 10)
                    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-test-modal-close-btn]')))

                    # Click on the element
                    element.click()
                except:
                    sleep(1)
                            
                        
                    print('error')
                    driver.execute_script("document.querySelector('button[data-test-modal-close-btn]').click()")
                return
        except:
            pass
def CancelApplication():
    ignorer_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Ignorer"]'))
            )
    ignorer_button.click()

            # click on the second button with data-control-name="discard_application_confirm_btn"
    confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]'))
            )
    confirm_button.click()
    print('ignore_application_confirm_btn')

        
def new_input_handler():
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

def new_input_handler():
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
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
def ClickIntoEveryJob(job,location=""):    
    sleep(1)
    input_element = driver.find_element_by_xpath("//input[@aria-label='Chercher par intitulé de poste, compétence ou entreprise']")
    sleep(1)
    # Click on the input element
    input_element.clear()
    input_element.send_keys(job)
    elements = driver.find_elements_by_xpath("//input[starts-with(@id, 'jobs-search-box-location-')]")
    sleep(1)
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

    
#ClickIntoEveryJob("","France")
def select_handler(value=None) -> None:
    selects = driver.find_elements(By.CSS_SELECTOR, 'select')
    for select in selects:
        options = Select(select).options[1:]
        random_option = random.choice(options)
        Select(select).select_by_visible_text(random_option.text)

liste_python = [
    'python',
    'javascript','typescript','c++',"Django","Flask","Pyramid","FastAPI","Sanic","NumPy","SciPy","Pandas","Matplotlib","Seaborn","Scikit-learn","TensorFlow","PyTorch","Keras","NLTK","BeautifulSoup","Scrapy","PyInstaller","React","Angular","Vue.js","jQuery","Bootstrap","D3.js","Leaflet","Mapbox","React Native","Flutter"
]
def input_handler(value: str) -> None:
    def set_value(element: WebElement) -> None:
        element.clear()
        element.send_keys(value)

    inputs = driver.find_elements(By.CSS_SELECTOR, 'input')
    for input in inputs:
        set_value(input)
def scroll_down():
    
    script = """
    var elem = document.querySelector('.jobs-search-results-list');
    var height = elem.scrollHeight / 10;
    for (var i = 0; i < 9; i++) {
        elem.scrollTop += height;
        await new Promise(resolve => setTimeout(resolve, 100));
    }
    """

    driver.execute_script(script)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

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

        if 'envoyer la candidature' in buttonText:
            try:
                driver.execute_script("document.getElementById('follow-company-checkbox').click()")
            except:
                pass
            time.sleep(0.1)
            button.click()
            button = driver.find_element(By.CSS_SELECTOR, 'button[data-test-modal-close-btn]')
            button.click()
            return
        if 'rifier' in buttonText or 'suivant' in buttonText:
            try:                    
                button.click()
            except:
                pass
            time.sleep(0.25)

def new_input_handler():
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
def Newurl(url,page=1):
    url = driver.current_url
    from urllib.parse import urlparse, urlunparse, parse_qs
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params['start'] = [str(page*25)]

    
    new_query_string = '&'.join([f"{k}={v[0]}" for k, v in query_params.items()])
    new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string, parsed_url.fragment))
    if page*25 > NumberResult():
        print('NEXT')
        return 'NEXT'
    print(new_url)
    return new_url