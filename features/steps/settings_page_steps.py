from behave import when

@when('Click on the Subscription & payments option')
def click_subscription_payment(context):
    context.app.settings_page.click_subscription_payment()