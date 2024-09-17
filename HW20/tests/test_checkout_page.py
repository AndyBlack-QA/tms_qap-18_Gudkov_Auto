import time

from HW20.pages.book_page import BookPage
from HW20.pages.home_page import HomePage
from HW20.pages.checkout_page import CheckoutPage
from HW20.elements.header_elements import HeaderElement


def test_checkout_open_by_header_icon(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.cookie_accept()
    header_elements = HeaderElement(driver)
    header_elements.checkout_click()
    assert driver.current_url == "https://oz.by/checkout/"


def test_checkout_empty_by_default(driver):
    home_page = HomePage(driver)
    home_page.open()
    header_elements = HeaderElement(driver)
    header_elements.checkout_click()
    checkout_page = CheckoutPage(driver)
    assert checkout_page.get_checkout_emptiness_text() == ('В корзине пусто. Чтобы найти товары, используйте поиск '
                                                           'или выберите товары из просмотренных ранее:')


def test_added_item_get_into_shipping_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_book(1)
    book_page = BookPage(driver)
    first_book_title = book_page.get_title()
    book_page.put_to_the_shopping_cart()
    time.sleep(1)
    header_elements = HeaderElement(driver)
    header_elements.checkout_click()
    checkout_page = CheckoutPage(driver)
    assert first_book_title == checkout_page.get_first_book_title()


def test_delete_item_from_checkout(driver):
    book_page = BookPage(driver)
    book_page.open()
    book_page.put_to_the_shopping_cart()
    time.sleep(1)
    header_elements = HeaderElement(driver)
    header_elements.checkout_click()
    checkout_page = CheckoutPage(driver)
    checkout_page.check_first_book_checkbox()
    checkout_page.delete_item_button_click()
    checkout_page.delete_confirmation_yes_click()
    assert checkout_page.get_checkout_emptiness_text()


def test_cancel_deleting_item_from_checkout(driver):
    book_page = BookPage(driver)
    book_page.open()
    book_page.put_to_the_shopping_cart()
    time.sleep(1)
    header_elements = HeaderElement(driver)
    header_elements.checkout_click()
    checkout_page = CheckoutPage(driver)
    checkout_page.check_first_book_checkbox()
    checkout_page.delete_item_button_click()
    checkout_page.delete_confirmation_cancel_click()
    assert checkout_page.get_first_book_title()


def test_list_of_first_item_quantity_appears_after_click(driver):
    book_page = BookPage(driver)
    book_page.open()
    book_page.put_to_the_shopping_cart()
    time.sleep(1)
    header_elements = HeaderElement(driver)
    header_elements.checkout_click()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_quantity_of_the_first_item()
    assert checkout_page.list_of_quantity_first_item()









