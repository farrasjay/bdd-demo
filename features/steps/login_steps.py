from behave import given, when, then
from django.contrib.auth.models import User
from django.test import Client

@given('a registered user exists')
def step_impl(context):
    context.client = Client()
    User.objects.create_user(username='alice', password='password123')

@when('the user logs in with valid credentials')
def step_impl(context):
    context.response = context.client.post('/login/', {
        'username': 'alice',
        'password': 'password123'
    }, follow=True)

@then('they should see their dashboard page')
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Welcome, alice!" in context.response.content

@when('the user tries to log in with an incorrect password')
def step_impl(context):
    context.response = context.client.post('/login/', {
        'username': 'alice',
        'password': 'wrongpassword'
    }, follow=True)

@then('they should see an error message indicating invalid credentials')
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Invalid username or password" in context.response.content