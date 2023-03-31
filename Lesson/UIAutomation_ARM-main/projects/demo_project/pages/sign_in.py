from golem import actions

email_address_input = ('xpath', './/*[@id="email"]', 'Email address input')
password_input = ('xpath', './/*[@id="passwd"]', 'Password input input')
sign_in_btn = ('xpath', './/*[@id="SubmitLogin"]', 'Sign in button')


def login_as_a_user_by_name_and_pass(name, password):
    actions.wait_for_element_present(email_address_input, 5)
    actions.send_keys(email_address_input, name)
    actions.wait_for_element_present(password_input)
    actions.send_keys(password_input, password)
    actions.wait_for_element_present(sign_in_btn)
    actions.click(sign_in_btn)