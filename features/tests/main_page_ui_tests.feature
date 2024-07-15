Feature: Tests for main page UI

#  Scenario: Verify header in shown
#    Given Open Target main page
#    Then Verify header in shown
#
#  Scenario: Verify header has correct amount links
#    Given Open Target main page
#    Then Verify header has 6 links

  Scenario: Verify benefit cells has correct amount links
    Given Open Target main page
    When Click on Target Circle link
    Then Verify benefit cells has 10 links