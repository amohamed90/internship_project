Feature: Tests for Subscription and Payments verifications


  Scenario: User can open Subscription & payments page
    Given Open Reelly main sign-in page
    When Log in to the page
    And Click on the settings option
    And Click on the Subscription & payments option
    Then Verify the right page opens
    And Verify title “Subscription & payments” is visible
    And Verify “back” and “upgrade plan” buttons are available