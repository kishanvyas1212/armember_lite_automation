from src.cases.constants import *
from src.utilitises.get_element import get_element as ge

class validate:
    def verifyuser(drivers,username,desired_cookie,URL):
        if username in desired_cookie['value']:
        
            current_url =drivers.current_url
        
            if str(URL) == str(current_url):
                return 0

            else:    
                return 1
        else:
            return -1
    def registerformverification(drivers):
       
        # in this we can check only two field validation, username and user email, so need to check this two only
        # below code to check the error message
        try: 
            error_msg =  ge.wait_for_element_display(drivers,"arm-df__fc--validation__wrap")
            # print(type(error_msg))
            # print(error_msg)
        
        except: 
            
            print("no error is displayed it works properly")
            return 0, "no error is found"
        else: 
            return 1,error_msg
    def redirection_validation(drivers,expected_url):
        redirected_url = drivers.current_url
        if redirected_url == expected_url:
            print("it redirects properly, the redirection works properly")
            return 1, redirected_url
        else:
            print("redirection is not working properly")
            return 0, redirected_url