Feature: Tests access to sign in page

  Scenario: Verify user can access the sign in page
    Given Open target main page
    When Click on the Sign in button
    Then Click on the Sign in button in the right side nav menu
    Then Sign in form opened