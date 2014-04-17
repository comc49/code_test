require 'watir'

$browser = Watir::Browser.new
Given /^I am on (.+)$/ do |url|
   $browser.goto("#{url}")
   $website = url 
end

When /^I click the State "(.+)"$/ do |state_name|
   $browser.area(:id => "area_#{state_name}").when_present.click
end

And /^I select "(.+)" as "Suburb"$/ do |suburb_choice|
   $browser.select_list(:id => /.*suburbSelect.*/).option(:text =>"#{suburb_choice}").when_present.select
end

And /^I select "(.+)" as "Property Type"$/ do |p_type|
   $browser.button(:id => "state_propertyType").click
   $browser.checkbox(:id => "ddCb_state_propertyType_3").when_present.set
end
And /^I select "(.+)" as "Max Price"$/ do |max_price|
   $browser.button(:id => "state_maxPrice").click
   $browser.div(:id => "LMIDD_state_maxPrice").dd(:text => "#{max_price}").when_present.click
end

And /^I click "(.+)"$/ do |search_button|
  $browser.button(:id => "state_searchBtnState").click  
end

Then /^I should see the number of the result as "([\d]+)"$/ do |num_of_result|
   @result_line = $browser.div(:id => "resultsInfo").p.text
   @result_num = @result_line.match /([\d]+) Total/
   #puts "#{@result_num[1]}"
   #puts "#{num_of_result}"
   if "#{@result_num[1]}" == "#{num_of_result}"
      puts "Correct result"
   else
      fail "Wrong result"
   end
end
