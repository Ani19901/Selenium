from golem import actions

account_name_span = ('xpath', './/*[@class="account"]/span', 'Account name')
logout_btn = ('xpath', './/*[@class="logout"]', 'Logout button')
sign_in_btn = ('xpath', './/*[@id="SubmitLogin"]', 'Sign in button')


def assert_account_name(name):
    actions.assert_element_text(account_name_span, name)



def user_logout_and_check():
    if actions.get_browser().element_is_present(logout_btn):
        actions.click(logout_btn)
        actions.wait_for_element_present(sign_in_btn)