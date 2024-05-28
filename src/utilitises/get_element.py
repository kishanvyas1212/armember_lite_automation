from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class get_element:
    
    def action_perform(element, action,value):
        if action=='click':
            element.click()
        elif action=="send_keys":
            element.send_keys(value)
        return
        
        
    def findelement(driver, locator,locatorpath,action=1,value=1):
        try:
            if locator=="ID" or locator=="id":
                element = driver.find_element(By.ID, locatorpath )
                if action!="" or action!="1" or action=="click" or action=="send_keys":
                    get_element.action_perform(element,action,value)
                return element
            elif locator=="XPATH" or locator=="xpath":
                element = driver.find_element(By.XPATH,locatorpath)
                if action!="" or action!="1" or action=="click" or action=="send_keys":
                    get_element.action_perform(element,action,value)
                return element
            elif locator=="name" or locator=="NAME":
                element = driver.find_element(By.NAME,locatorpath)
                if action!="" or action!="1" or action=="click" or action=="send_keys":    
                    get_element.action_perform(element,action,value)
                return element
        except Exception as e:
            print("Element is not found so please retry to move to next case")
            driver.save_screenshot("screenshots/" + str(value) +".png")
            driver.quit()
            
    def wait_for_element_present(drivers,locator, timeout=2):
        try: 
            # try to find the element is located or not, if not then return None
            WebDriverWait(drivers, timeout).until(EC.presence_of_element_located((By.CLASS_NAME,locator)))
                
        except:
            pass
        return 
    def wait_for_element_display(driver, locator, timeout=10):
        elemenrt = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME,locator)))
        
        return elemenrt.text 
        # print(locator)
        # return drivers.find_elements(By.CLASS_NAME,locator)
    # locator = (By.XPATH,"test") pass the locator in this way for wait for element 