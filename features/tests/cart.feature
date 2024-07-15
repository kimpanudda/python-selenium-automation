Feature: Tests for Cart functionality

  Scenario: Verify empty cart message
    Given Open target main page
    When Click on Cart icon
    Then Verify cart is empty
