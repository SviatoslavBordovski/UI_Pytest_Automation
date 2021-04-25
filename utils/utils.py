#Constants
import inspect

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"
employeeNAME = "Charlie Carter"
newUSERNAME = "qwerty2016"
strongPASSWORD = "q1w2e3r4t5y6u7i8o9!~!"

def whoami():
    return inspect.stack()[1][3]