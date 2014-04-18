Feature: Main header links
  In order to test the header links
  As a customer 
  I want to go to the correct link by clicking the appropriate header
  
  Background:
    Given I am on http://www.realestate.com.au
   
  Scenario Outline: Transferring successfully
    When I click the link <link name>
    Then I should be transferred to <as expected>
    Scenarios:
      | link name    | as expected                                           |         
      | Home ideas   | http://www.realestate.com.au/home-ideas/              |
      | Buy          | http://www.realestate.com.au/buy                      |    
      | Rent         | http://www.realestate.com.au/rent                     |
      | Invest       | http://www.realestate.com.au/invest                   |       
      | Sold         | http://www.realestate.com.au/sold                     |  
      | Share        | http://www.realestate.com.au/share                    |
      | New homes    | http://www.realestate.com.au/new-homes/               |
      | Retire       | http://www.realestate.com.au/retire                   |
      | Find agents  | http://www.realestate.com.au/find-agent               |
      | Blog         | http://www.realestate.com.au/blog/                    |
      | Commercial   | http://www.realcommercial.com.au/for-sale             | 
