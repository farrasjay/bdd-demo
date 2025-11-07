Feature: User login

  Scenario: Successful login
    Given a registered user exists
    When the user logs in with valid credentials
    Then they should see their dashboard page

  Scenario: Failed login with wrong password
    Given a registered user exists
    When the user tries to log in with an incorrect password
    Then they should see an error message indicating invalid credentials