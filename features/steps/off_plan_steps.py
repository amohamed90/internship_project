from behave import when

@when('Click on the settings option')
def click_settings(context):
    context.app.off_plan_page.click_settings()