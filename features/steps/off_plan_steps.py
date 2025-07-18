from behave import when
from time import sleep

@when('Click on the settings option')
def click_settings(context):
    context.app.off_plan_page.click_settings()
    # For Sarafi testing
    sleep(10)