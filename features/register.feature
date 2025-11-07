Feature: User registration

  Scenario: Successful registration
    Given I am a new visitor
    When I register with a valid username and password
    Then I should be redirected to the login page

  Scenario: Failed registration due to password mismatch
    Given I am a new visitor
    When I register with non-matching passwords
    Then I should see an error message about password mismatch