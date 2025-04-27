Feature: Sauce Product Page


  Scenario: Verify all product displayed in product page
    Given navigate to url "https://www.saucedemo.com/v1/index.html"
    When enter username "standard_user" and password "secret_sauce"
    And click on login
    And in home page get all product name
    Then verify all the product name