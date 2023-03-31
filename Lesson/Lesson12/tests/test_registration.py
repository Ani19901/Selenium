from golem.actions import *
from Lesson12.pages.registration import create_account, fill_register_data

description = '''

'''

tags = ['registration']

pages = ['sign_up']


def setup(data):
    store('url', data.env.url)


def test(data):
    step('_____________Navigation_______________')
    navigate(data.url)
    # step('_____________Sign in_______________')
    # click_sign_in_button()

    step('_____________Create Account______________')
    create_account(data.EmailAddress)
    step('_____________Sign up_______________')
    fill_register_data(data.FirstName, data.LastName, data.Password, data.Address, data.City, data.State, data.ZipPostalCode, data.MobilePhone)

    step('_____________Assert account name_______________')
    #account.assert_account_name(data.account_name)


def teardown(data):
    step('_____________Sing out and check_______________')
    #account.user_logout_and_check()