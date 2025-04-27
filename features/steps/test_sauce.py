from behave import *

from features.pages.login_page import LoginPage
from features.pages.product_page import ProductPage


@given(u'navigate to url "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@when(u'enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page = context.page_factory.get_login_page()
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    # context.driver.find_element(By.ID, 'user-name').send_keys(username)
    # context.driver.find_element(By.ID, 'password').send_keys(password)


@when(u'click on login')
def step_impl(context):
    context.login_page.click_login_button()
    # context.driver.find_element(By.ID, 'login-button').click()


@then(u'verify the home page title "{home_page_title}"')
def step_impl(context, home_page_title):
    page_title = context.driver.title
    assert page_title == home_page_title

@when(u'in home page get all product name')
def step_impl(context):
    context.product_page = context.page_factory.get_product_page()
    context.product_name_list = sorted([product.text for product in context.product_page.get_all_products()])
    # inventory_elements=context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
    # context.product_list=[]
    # for element in inventory_elements:
    #     context.product_list.append(element.text)
    # context.product_list.sort()


@then(u'verify all the product name')
def step_impl(context):
    expected_products=['Sauce Labs Backpack', 'Sauce Labs Bike Light',
                       'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket',
                       'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)  ']
    expected_products.sort()
    assert expected_products == context.product_name_list, f"expected {expected_products} got {context.product_name_list}"

