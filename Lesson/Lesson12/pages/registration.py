from golem import actions


#####  Locators  ########
btn_login_sign_in = ('xpath', "//a[contains(text(),'Sign in')]", 'Sign in button')

field_first_name = ('xpath', '//*[@id="firstname"]', 'First name input')
field_last_name = ('xpath', '//*[@id="lastname"]', 'Last name input')
field_address = ('xpath', '//*[@id="address1"]', 'Address field input')
field_password = ('xpath', '//*[@id="passwd"]', 'Password field input')
field_city = ('xpath', '//*[@id="city"]', 'City field input')
field_zip_code_postal = ('xpath', '//*[@id="postcode"]', 'Zip code input')
field_state = ('xpath', '//*[@id="id_state"]', 'State field input')
field_mobile_phone = ('xpath', '//*[@id="phone_mobile"]', 'Mobile Phone input')
btn_register = ('xpath', '//*[@id="submitAccount"]/span/text()', 'Register Button')

email_input = ('xpath', '//*[@id="email_create"]', 'Email Input')
btn_create_accout = ('xpath', '//*[@id="SubmitCreate"]', 'Create Account button')

field_my_account = ('xpath', '//*[@id="center_column"]/h1', 'My account input')



def click_sign_in_button():
    actions.click(btn_login_sign_in)


def create_account(email_field):
    actions.wait_for_element_present(email_input, 5)
    actions.send_keys(email_input, email_field)

    actions.wait_for_element_present(btn_create_accout)
    actions.click(btn_create_accout)


def fill_register_data(first_name, last_name, password, address, city, state, zip_code_postal, mobile_phone):
    try:
        actions.wait_for_element_present(field_first_name, 5)
        actions.send_keys(field_first_name, first_name)

        actions.wait_for_element_present(field_last_name)
        actions.send_keys(field_last_name, last_name)

       # actions.wait_for_element_present(field_address)
        actions.send_keys(field_address, address)

       # actions.wait_for_element_present(field_password)
        actions.send_keys(field_password, password)

        #actions.wait_for_element_present(field_city)
        actions.send_keys(field_city, city)

        #actions.wait_for_element_present(field_zip_code_postal)
        actions.send_keys(field_zip_code_postal, zip_code_postal)

       #actions.wait_for_element_present(field_state)
        actions.send_keys(field_state, state)

       # actions.wait_for_element_present(field_mobile_phone)
        actions.send_keys(field_mobile_phone, mobile_phone)

        actions.wait_for_element_present(btn_register)
        actions.click(btn_register)


    except Exception as e:
        print(e)
