from behave import given, when, then
from django.contrib.auth.models import User
from django.test import Client

@given('I am a logged-in user')
def step_impl(context):
    context.client = Client()
    user = User.objects.create_user(username='david', password='password123')
    context.client.login(username='david', password='password123')

@when('I log out')
def step_impl(context):
    context.response = context.client.get('/logout/', follow=True)

@then('I should be redirected to the login screen')
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Login" in context.response.content

@given('I am not logged in')
def step_impl(context):
    context.client = Client()

@when('I attempt to access the logout page directly')
def step_impl(context):
    context.response = context.client.get('/logout/', follow=True)