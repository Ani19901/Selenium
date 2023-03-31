import random
import string

email = ''.join([random.choice(string.ascii_lowercase) for _ in range(10)]) + '@yopmail.com'
existing_username = "aaaaa@gmail.com"
existing_password = "123456"


url = 'http://automationpractice.com/index.php'
first_name = "Volo"
last_name = "Automation"
password = "Qwerty1234"
address_first_name = "Test"
address_last_name = "Automation"
address = "Lorrie drive"
zip_code_postal = "77025"
city = "houston"
state = "Texas"
country = "United States"
mobile_phone = "5127678889"
subject_heading = "customer service"
msg_contactus = "Hello, Thank you for your help"
login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
error_message = "The message cannot be blank."
order_ref = "my_tttt"
