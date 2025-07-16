from behave import then

@then('Verify the right page opens')
def verify_page_opens(context):
    context.app.subscription_payments_page.verify_page_opens()

@then('Verify title “Subscription & payments” is visible')
def verify_text_visibility(context):
    context.app.subscription_payments_page.verify_text_visibility()

@then('Verify “back” and “upgrade plan” buttons are available')
def verify_buttons(context):
    context.app.subscription_payments_page.verify_upgrade_btn()
    context.app.subscription_payments_page.verify_back_btn()



