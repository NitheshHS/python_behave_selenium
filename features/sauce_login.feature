# Created by nhs at 27/04/25
Feature: Sauce Demo Login

  Scenario: Login to sauce demo with valid credentials
    Given navigate to url "https://www.saucedemo.com/v1/index.html"
    When enter username "standard_user" and password "secret_sauce"
    And click on login
    Then verify the home page title "Swag Labs"


  Scenario Outline: Login to sauce demo with all valid credentials
    Given navigate to url "https://www.saucedemo.com/v1/index.html"
    When enter username "<username>" and password "<password>"
    And click on login
    Then verify the home page title "Swag Labs"
    Examples:
      | username                | password     |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |

