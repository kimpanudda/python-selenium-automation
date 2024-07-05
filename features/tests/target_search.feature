Feature: Target main page search tests

  Scenario: User can search for a product on target
    Given Open target main page
    When Search for product
    Then Verify search worked


  Scenario: Verify empty cart message
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty


  Scenario: Logged out user can navigate to Sign In
    Given Open target main page
    When Click sign in
    And Click sign in from right side
    Then Verify sign in form opened