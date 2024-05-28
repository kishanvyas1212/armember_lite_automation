import time
from selenium import webdriver #by this we can access the webdriver which is inbuild method of selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from src.cases.constants import *
from src.utilitises.get_element import get_element as ge
from src.utilitises.validate import validate



def testcase_1(drivers):
    # Correct username, wrong password
    drivers.get(BASE_URL+"/login")
    usernamef = ge.findelement(drivers,"NAME","user_login","send_keys",right_username) 
    pwd = ge.findelement(drivers,"NAME","user_pass","send_keys","test")   
    beforelogin = drivers.get_cookies()
    login = ge.findelement(drivers,"NAME","armFormSubmitBtn","click")
    time.sleep(3)
    error_message = drivers.find_element(By.CSS_SELECTOR, "div.arm-df__fc--validation__wrap")
    
    if WRONG_PASS_ERROR in error_message.text:
        actual_result = f"Case is passed, and displayed error message is {error_message.text}"
        status = "pass"
    else:
        actual_result = f"Case is failed, and displayed error message is {error_message.text}"
        status ="Failed"
    
    return actual_result,status
def testcase_2(drivers):
    # wrong username, wrong password
    drivers.get(BASE_URL+"/login")
    usernamef = ge.findelement(drivers,"NAME","user_login","send_keys","afdmin") 
    pwd = ge.findelement(drivers,"NAME","user_pass","send_keys","test")   
    beforelogin = drivers.get_cookies()
    login = ge.findelement(drivers,"NAME","armFormSubmitBtn","click")
    time.sleep(3)
    error_message = drivers.find_element(By.CSS_SELECTOR, "div.arm-df__fc--validation__wrap")
    
    if NO_USER_EXIST in error_message.text:
        actual_result = f"Case is passed, and displayed error message is {error_message.text}"
        status = "pass"
    else:
        actual_result = f"Case is failed, and displayed error message is {error_message.text}"
        status ="Failed"
    
    return actual_result,status
    
    
def testcase_3(drivers):
    # Login with right creds
    drivers.get(BASE_URL+"/login")
    usernamef = ge.findelement(drivers,"NAME","user_login","send_keys",right_username) 
    pwd = ge.findelement(drivers,"NAME","user_pass","send_keys",right_username)   
    beforelogin = drivers.get_cookies()
    login = ge.findelement(drivers,"NAME","armFormSubmitBtn","click")
    time.sleep(10)
    loggedin_cookies = drivers.get_cookies()
# Find the dictionary that matches the specified name
    desired_cookie = next((cookie for cookie in loggedin_cookies if cookie['name'] == COOKIE), None)
    if right_username in desired_cookie['value']:
        
        current_url =drivers.current_url
        
        if str(LOGIN_REDIRECTS_URL) == str(current_url):
            actual_result = "Case is passed, login and user redirect success fully"
            
        else:    
            actual_result = f"Case is passed, but not redirected successfully redirected to {current_url}"
        status = "pass"
    else:
        actual_result ="Case failed, user can not logged in"
        status="failed"
    return actual_result,status
    
    
def testcase_4(drivers):
    # Login with right creds
    drivers.get(BASE_URL+"/register")
    ge.findelement(drivers,"NAME","user_login","send_keys",Create_username)
    ge.findelement(drivers,"NAME","first_name","send_keys",f_name)
    ge.findelement(drivers,"NAME","last_name","send_keys",l_name)
    ge.findelement(drivers,"NAME","user_email","send_keys",u_email)
    ge.findelement(drivers,"NAME","user_pass","send_keys",password)
    
    validation = validate.registerformverification(drivers)
    if validation[0] == 0:
        
        submit_form = ge.findelement(drivers,"NAME","armFormSubmitBtn","click")
        time.sleep(10)
        loggedin_cookies = drivers.get_cookies()
# Find the dictionary that matches the specified name
        if loggedin_cookies != "none" or loggedin_cookies != "":
            desired_cookie = next((cookie for cookie in loggedin_cookies if cookie['name'] == COOKIE), None)
        else:
            time.sleep(5)
            loggedin_cookies=drivers.get_cookies()
            desired_cookie = next((cookie for cookie in loggedin_cookies if cookie['name'] == COOKIE), None)
         
        response = validate.verifyuser(drivers,Create_username,desired_cookie,register_redirect_url)
        
        if response == 0:
            actual_result = f"User register properly and user redirected to set url{drivers.current_url}"
            status ="Pass"
        elif response == 1:
            actual_result = f"User register properly but user not redirected to set url{register_redirect_url} instead it redirected to {drivers.current_url}"
            status ="Pass"
            
    else: 
        actual_result =validation[1]
        status = "failed"
    return actual_result,status
    


def link_checker(driver):
    driver.get("https://www.sociamonials.com")
    
    links = driver.find_elements(By.TAG_NAME,'a')
    use_full_links = []
    broken_links = []
    same_domain_link=[]
    for link in links:
        url = link.get_attribute('href')
        if url and url !="#" and "https" in url:
            use_full_links.append(url)
            response = requests.get(url)
            if response.status_code == 400 or response.status_code == 404:
                broken_links.append(url)
            elif "sociamonials.com" in url:
                same_domain_link.append(url)
        else:
            continue                        
    
    return use_full_links,broken_links