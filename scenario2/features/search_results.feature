
Feature: Main header links
  In order to test the header links
  As a customer 
  I want to go to the correct link by clicking the appropriate header
  
  Background:
    Given I am on http://www.realestate.com.au/buy
   
  Scenario: Verify correct number of results
    #When I click the State "Real estate Victoria"
    When I click the State "VIC"
    And I select "Richmond" as "Suburb"
    And I select "Apartment" as "Property Type"
    And I select "500,000" as "Max Price"
    And I click "Search"
    Then I should see the number of the result as "1083"

