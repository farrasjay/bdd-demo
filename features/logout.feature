Feature: User logout

  Scenario: Successful logout
    Given I am a logged-in user
    When I log out
    Then I should be redirected to the login screen

  Scenario: Logout attempt without active session
    Given I am not logged in
    When I attempt to access the logout page directly
    Then I should be redirected to the login screen