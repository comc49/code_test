require 'watir'

$browser = Watir::Browser.new
#Given /^I am on ([\w]+.{3}[\w]+.[\w]+.[\w]+.[\w]+)$/ do |url|
Given /^I am on (.+)$/ do |url|
   #$browser = Watir::Browser.start("#{url}")
   $browser.goto("#{url}")
   $website = url 
end

When /^I click the link ([\w]+[\s]?[\w]*)$/ do |link_name|
   $browser.link(:text => "#{link_name}").when_present.click
   $clicked_link = "#{link_name}".downcase
end

Then /^I should be transferred to (.+)$/ do |name|
  $new_browser = $browser.windows.last
  @base_url = /(.+au\/.+\/)|(.+au\/.+$)/.match($new_browser.url)
  if "#{@base_url}" != "#{name}"
     fail "wrong url"
  else
    puts "correct URL"
  end
end
