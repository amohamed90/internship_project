from behave import given

@given('Open Reelly main sign-in page')
def open_main(context):
    context.app.main_page.open_main_page()


