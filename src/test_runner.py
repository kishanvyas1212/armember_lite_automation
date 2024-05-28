from .excel_utils import read_test_cases, update_test_case_status
from config.settings import EXCEL_FILE_PATH
import logging
from src.cases.test_case import * 

from selenium import webdriver #by this we can access the webdriver which is inbuild method of selenium
from selenium.webdriver.chrome.service import Service   #This is selenium 4 new feature in which we import service 

# test
def driver_initlise():
    logging.info("Initiating the wev driver")
    ser_Obj = Service("C:\\Users\\91635\\Desktop\\drivers\\chrome\\chromedriver.exe")
    drivers = webdriver.Chrome(service= ser_Obj)
    drivers.implicitly_wait(60)
    
    return drivers


def run_tests():
    logging.info("reading test cases from excel file")
    test_cases = read_test_cases(EXCEL_FILE_PATH)

    for cases in test_cases['TestCaseID']:
        logging.info(f"executing the case id : {cases}" )
        function_name = f"testcase_{cases}"
        
        if function_name in globals() and callable(globals()[function_name]):
            driver = driver_initlise()
            logging.info(f"calling function according the test casse id: {cases}" )
            function_to_call = globals()[function_name]
            actual_result,status = function_to_call(driver)
            update_test_case_status(EXCEL_FILE_PATH, cases-1, status, actual_result)
            
            driver.quit()
        else:
            print(f"Function {function_name} does not exist or is not callable.")
            logging.info(f"Function {function_name} does not exist or is not callable.")