from behave import given, when, then
from django.test import Client
from django.contrib.auth.models import User

@given('I am a new visitor')
def step_impl(context):
    context.client = Client()

@when('I register with a valid username and password')
def step_impl(context):
    context.response = context.client.post('/register/', {
        'username': 'bob',
        'password': 'password123',
        'confirm': 'password123'
    }, follow=True)

@then('I should be redirected to the login page')
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Login" in context.response.content
    assert User.objects.filter(username='bob').exists()

@when('I register with non-matching passwords')
def step_impl(context):
    context.response = context.client.post('/register/', {
        'username': 'charlie',
        'password': 'password123',
        'confirm': 'differentpassword'
    }, follow=True)

@then('I should see an error message about password mismatch')
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Passwords do not match" in context.response.content
    assert not User.objects.filter(username='charlie').exists()