from time import sleep
from behave import when

@when('Log in to the page')
def login(context):
    context.app.sign_in_page.input_username()
    context.app.sign_in_page.input_password()
    context.app.sign_in_page.click_continue()
    # sleep is needed for Safari testing browser
    sleep(10)