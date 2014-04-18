Feature: Sendgrid mail api method
   fill out the forms
   sender receives the mail correctly

   Scenario: sending mail
      Given I am at "http://sendgrid.com/docs/api_workshop.html"
      When I enter username as "comc49"
      #And I enter password as "sendgridcodetest"
      And I click "Expand Methods" for mail api method
      And I fill in parameter "to" as "bkoo004@ucr.edu"
      And I fill in parameter "toname" as "Bob"
      And I fill in parameter "x-smtpapi" as '{ "category": "newuser" }'
      And I fill in parameter "from" as "comc49@gmai.com "
      And I fill in parameter "fromname" as "Brian"
      And I fill in parameter "subject" as "testing"
      And I fill in parameter "text" as "hi this is a test mail"
      And I fill in parameter "html" as "sup"
      And I fill in parameter "bcc" as "comc39@naver.com"
      And I fill in parameter "date" as "Thu, 17 Apr 2014 20:51:52 -0700"
      And I fill in parameter "headers" as '{“X-Accept-Language”: “en”, “X-Mailer”: “MyApp”}'
      And I fill in parameter "files" as "files[file1.doc]=example.doc"
      And I click "Try it!" button
      Then I should see "success" in the response body
