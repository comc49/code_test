require 'watir'

$browser = Watir::Browser.new    #opens new browser
Given /^I am on (.+)$/ do |url|  #parses through my Given statement and finds the url
   $browser.goto("#{url}")
   $website = url                #saves the url to a global variable
end

When /^I click the link ([\w]+[\s]?[\w]*)$/ do |link_name|
   $browser.link(:text => "#{link_name}").when_present.click   #clicks the link header
   $clicked_link = "#{link_name}".downcase                     #saves the name of link
end

Then /^I should be transferred to (.+)$/ do |name|
  $new_browser = $browser.windows.last       #go to the new window if created by clicking the link
  @base_url = /(.+au\/.+\/)|(.+au\/.+$)/.match($new_browser.url)  #parse through the url
  if "#{@base_url}" != "#{name}"    #checks if url is not correct
     fail "wrong url"
  else
    puts "correct URL"
  end
end
