from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pytest
import random
import time

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")


link = "https://cart.onliner.by/"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    browser.delete_all_cookies()
    browser.quit()

class TestOnlinerCartPage():
    #Test case 1
    def test_onliner_link(self, browser):
        browser.get(link)
        element_1 = browser.find_element_by_css_selector("[href='https://www.onliner.by']")
        element_1.click()
        url_check = browser.current_url
        print("\nRedirected to the following link: " + url_check)
        assert url_check == 'https://www.onliner.by/', f"Redirected to a wrong link - {url_check}"
        print("\nUser is redirected to the home page")
        f = open("report.txt","w+")
        f.write("Test case 1 (TC-1) passed successfully")
        f.close()
        time.sleep(1)

    # Test case 2
    def test_login_link_interaction(self, browser):
        browser.get(link)
        text = "Войдите на сайт"
        element_2 = browser.find_element_by_partial_link_text(text)
        browser.execute_script("return arguments[0].scrollIntoView(true);", element_2)
        element_2.click()
        time.sleep(1)
        login_button = browser.find_element_by_css_selector("[type='submit']")
        close_button = browser.find_element_by_css_selector("[class='auth-form__close']")
        assert login_button.is_displayed(), "Authorization form is not available"
        assert login_button.is_enabled(), "Authorization form is not available"
        close_button.click()
        f=open("report.txt", "a+")
        f.write("\rTest case 2 (TC-2) passed successfully")
        f.close()
        print("\nAuthorization form is available")

    # Test case 3
    def test_login_positive(self, browser):
        browser.get(link)    
        text = "Войдите на сайт"
        element_2 = browser.find_element_by_partial_link_text(text)
        browser.execute_script("return arguments[0].scrollIntoView(true);", element_2)
        element_2.click()
        login_cart = browser.find_element_by_css_selector("[placeholder~='Ник']")
        login_cart.send_keys("Test_131220log@mail.ru")
        password_cart = browser.find_element_by_css_selector("[type='password']")
        password_cart.send_keys("Test_131220pass")
        login_button = browser.find_element_by_css_selector("[type='submit']")
        login_button.click()
        text = "Войдите на сайт"
        x = browser.find_elements_by_partial_link_text(text)
        assert len(x) == 0
        f=open("report.txt", "a+")
        f.write("\rTest case 3 (TC-3) passed successfully")
        f.close()
        print("\nUser has been successfully logged in")


    # Test case 4
    def test_login_negative(self, browser):
        browser.get(link)    
        text = "Войдите на сайт"
        element_2 = browser.find_element_by_partial_link_text(text)
        browser.execute_script("return arguments[0].scrollIntoView(true);", element_2)
        element_2.click()
        login_cart = browser.find_element_by_css_selector("[placeholder~='Ник']")
        login_cart.send_keys("invalid login")
        password_cart = browser.find_element_by_css_selector("[type='password']")
        password_cart.send_keys("invalid password")
        login_button = browser.find_element_by_css_selector("[type='submit']")
        login_button.click()
        x = browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/div[2]/div/form/div[3]/div")
        assert x.is_displayed()
        f=open("report.txt", "a+")
        f.write("\rTest case 4 (TC-4) passed successfully")
        f.close()
        print("\nValidation message is displayed. User is not logged in")


    # Test case 5
    def test_location_change_positive(self, browser):
        browser.get(link)
        city_list = ["Гродно", "Витебск", "Могилев", "Гомель", "Брест", "Минск"]
        new_city_value = random.choice(city_list)  
        city_button = browser.find_element_by_css_selector(".helpers_show_tablet + a")
        city_button.click()
        city_input = browser.find_element_by_css_selector("[type='text']")
        city_input.send_keys(new_city_value)
        time.sleep(1)
        drop_city = browser.find_element_by_class_name("auth-dropdown__item")
        drop_city.click()
        city_submit = browser.find_element_by_tag_name("button")
        city_submit.click()
        city_button_new = city_button.text
        assert city_button_new == new_city_value
        f=open("report.txt", "a+")
        f.write("\rTest case 5 (TC-5) passed successfully")
        f.close()
        print(f"Location has been changed successfully. New location is {new_city_value}")


    # Test case 6
    def test_location_change_negative(self, browser):
        browser.get(link)
        new_city_value = "invalid city"   
        city_button = browser.find_element_by_css_selector(".helpers_show_tablet + a")
        city_button.click()
        city_input = browser.find_element_by_css_selector("[type='text']")
        city_input.send_keys(new_city_value)
        city_submit = browser.find_element_by_tag_name("button")
        city_submit.click()
        validation_message = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div[2]/div[2]")
        assert "Укажите населенный пункт" == validation_message.text
        city_button_new = city_button.text
        assert city_button_new != new_city_value
        f=open("report.txt", "a+")
        f.write("\rTest case 6 (TC-6) passed successfully")
        f.close()
        print(f"Location has not been changed. Correct validation message is displayed")


    # Test case 7
    def test_add_item_to_cart(self, browser):
        browser.get(link)
        catalog_link = browser.find_element_by_css_selector("[href='https://catalog.onliner.by']")
        catalog_link.click()
        link_apple = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/ul/ul/li[2]")
        link_apple.click()
        item_iphone = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[12]/div[1]/div/div[3]/div[1]")
        item_iphone.click()
        item_iphone_12 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[12]/div[1]/div/div[3]/div[2]/div/a[1]/span/span[2]")
        item_iphone_12.click()
        item_x = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[4]/h1")
        item_name_full = item_x.text
        item_name = item_name_full[9:]
        add_to_cart = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/main/div/div/aside/div[1]/div[1]/div/div[1]/div/div[1]/a[2]")
        add_to_cart.click()
        time.sleep(2)
        cart_link = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[3]/div/div[2]/div[2]/div[3]/div/a")
        cart_link.click()
        cart_name_x = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div[3]/a")
        cart_name = cart_name_x.text 
        item_element = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]")
        assert item_element.is_displayed(), "Something went wrong. Test not passed"
        assert item_name == cart_name, "Something went wrong. Test not passed"
        f=open("report.txt", "a+")
        f.write("\rTest case 7 (TC-7) passed successfully")
        f.close()
        print(f"Item has been added to the cart\nCatalog name: ({item_name}) corresponds with name in cart: ({cart_name})")
        time.sleep(2)


    # Test case 8
    def test_remove_item_from_cart(self, browser):
        item_link = "https://catalog.onliner.by/mobile/apple/iphone12pro128gr"
        browser.get(item_link)
        add_to_cart = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/main/div/div/aside/div[1]/div[1]/div/div[1]/div/div[1]/a[2]")
        add_to_cart.click()
        time.sleep(2)
        cart_link = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[3]/div/div[2]/div[2]/div[3]/div/a")
        cart_link.click()
        mouse = ActionChains(browser)
        cart_remove = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[4]/div/div[1]/div/a")
        mouse.move_to_element(cart_remove).perform()
        cart_remove.click()
        time.sleep(1)
        confirm_button = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/a[2]")
        confirm_button.click()
        empty_cart_x = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div[2]")
        empty_cart = empty_cart_x.text
        assert empty_cart == "Ваша корзина пуста"
        f=open("report.txt", "a+")
        f.write("\rTest case 8 (TC-8) passed successfully")
        f.close()
        print("Item has been removed from the cart")


    # Test case 9
    def test_change_quantity_item_in_cart(self, browser):
        item_link = "https://catalog.onliner.by/mobile/apple/iphone12pro128gr"
        browser.get(item_link)
        add_to_cart = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/main/div/div/aside/div[1]/div[1]/div/div[1]/div/div[1]/a[2]")
        add_to_cart.click()
        cart_link = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[3]/div/div[2]/div[2]/div[3]/div/a")
        cart_link.click()
        time.sleep(2)
        mouse = ActionChains(browser)
        cart_add_item = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/a[2]")
        cart_remove_item = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/a[1]")
        cart_change_quantity = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[4]/div/div[2]/div/div[1]/div/input")
        mouse.move_to_element(cart_add_item).perform()
        for click1 in range(9): 
            cart_add_item.click()
        time.sleep(4)
        mouse.move_to_element(cart_remove_item).perform()
        for click2 in range(6): 
            cart_remove_item.click()
        time.sleep(4)
        cart_change_quantity.send_keys(2)
        f=open("report.txt", "a+")
        f.write("\rTest case 9 (TC-9) passed successfully")
        f.close()
        print("Item quantity in cart has been successfully changed")

    # Test case 10
    def test_order_confirmation(self, browser):
        item_link = "https://catalog.onliner.by/mobile/huawei/matexsb"
        browser.get(item_link)
        add_to_cart = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/main/div/div/aside/div[1]/div[1]/div/div[1]/div/div[1]/a[2]")
        add_to_cart.click()
        cart_link = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[3]/div/div[2]/div[2]/div[3]/div/a")
        cart_link.click()
        time.sleep(3)
        checkout_button = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div/div[3]/div/div[2]/div[2]/div/div/a")
        checkout_button.click()
        login_cart = browser.find_element_by_css_selector("[placeholder~='Ник']")
        login_cart.send_keys("Test_131220log@mail.ru")
        password_cart = browser.find_element_by_css_selector("[type='password']")
        password_cart.send_keys("Test_131220pass")
        login_button = browser.find_element_by_css_selector("[type='submit']")
        login_button.click()
        time.sleep(3)
        checkout2_button = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div/div/div[2]/div/div[4]/div/div[1]/div[3]/div/div[2]/div[2]/div/div/a")
        checkout2_button.click()
        time.sleep(3)
        payment_confirmation = browser.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[5]/button")
        mouse = ActionChains(browser)
        mouse.move_to_element(payment_confirmation).perform()
        assert payment_confirmation.is_enabled()
        url_check = browser.current_url
        assert url_check == 'https://cart.onliner.by/order'
        f=open("report.txt", "a+")
        f.write("\rTest case 10 (TC-10) passed successfully")
        f.close()
        print("Order confirmation is available")
        time.sleep(3)

