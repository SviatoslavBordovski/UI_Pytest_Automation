#Constants
import inspect

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"
employeeNAME = "Charlie Carter"
newUSERNAME = "2021"
strongPASSWORD = "q1w2e3r4t5y6u7i8o9!~!"
forgotPassword = "Forgot your password?"
expectedInvalidCredentialsUrl = "https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials"
expectedInvalidCredentialsFlag = "Invalid credentials"

def whoami():
    return inspect.stack()[1][3]
