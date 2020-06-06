from time import sleep
import secrets # importing the secret.py module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # accessing to keyboad LOOOL

# paths for all elements to access to github
github_url = 'https://github.com/login'
login_field = '//*[@id="login_field"]'
password_field = '//*[@id="password"]'
login_btn = '//*[@id="login"]/form/div[4]/input[9]'
email = secrets.email # email value fro the secret.py module
username = secrets.username # username value fro the secret.py module
password = secrets.password # password value fro the secret.py module

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
driver.get(github_url) # Opening GitHub

def login():
    """login function"""
    assert (email != None or username!= None and password != None),('Please check the data')
    print('Logging ...')
    # Let's write some commands to logging in !
    driver.find_element_by_xpath(login_field).send_keys(email)
    driver.find_element_by_xpath(password_field).send_keys(password)
    driver.find_element_by_xpath(login_btn).click()
    if driver.current_url == 'https://github.com/sessions/verified-device':
        # Sometimes is required to write a code that GitHub sends to your email
        verify_field = '//*[@id="otp"]'
        print('Waiting fill in the verification code')
        print('You have 10 seconds...')
        sleep(10)
        code = input('Please write the code right here: ')
        driver.find_element_by_xpath(verify_field).send_keys(code, Keys.ENTER)
    else:
        # If auth-code is not required just pass that !
        pass
    print('Log went succefully')

def profile():
    """function to opening your profile"""
    print('Opening your profile')
    try:
        header = '/html/body/div[1]/header/div[7]'
        driver.find_element_by_xpath(header).click()
        profile_choice = '/html/body/div[1]/header/div[7]/details/details-menu/a[1]'
        driver.find_element_by_xpath(profile_choice).click()
        count_contributions = '//*[@id="js-pjax-container"]/div/div[3]/div[3]/div[2]/div[1]/div/h2'
        contributions = driver.find_element_by_xpath(count_contributions).text
        print(contributions)
        followers = '//*[@id="js-pjax-container"]/div/div[3]/div[2]/nav/a[6]'
        followersCount = driver.find_element_by_xpath(followers).text
        print('You have {} followers :)'.format(followersCount.split()[1]))
    except Exception as e:
        # If the browser is not in full screen that gets an error
        print('Be sure that the browser takes full screen')
        print(e)

def logout():
    """logout function"""
    header = '/html/body/div[1]/header/div[7]'
    driver.find_element_by_xpath(header).click()
    sign_out = '/html/body/div[1]/header/div[7]/details/details-menu/form/button'
    driver.find_element_by_xpath(sign_out).click()
    print('You signed out !')


if __name__=='__main__':
    login()
