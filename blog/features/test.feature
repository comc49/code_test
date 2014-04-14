Feature: Main header links
  In order to test the header links
  As a customer 
  I want to go to the correct link by clicking the appropriate header
  
  Scenario: clicks the link header
    When I click the link Buy
    Given I have link header called Buy 
    Then I should be tranferred to "realestate.com/au/buy"

