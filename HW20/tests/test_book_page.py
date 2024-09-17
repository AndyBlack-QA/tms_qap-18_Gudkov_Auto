from HW20.pages.book_page import BookPage
from HW20.pages.home_page import HomePage


def test_add_product_turns_in_shipping_cart(driver):
    book_page = BookPage(driver)
    book_page.open()
    book_page.put_to_the_shopping_cart()
    assert book_page.in_shopping_cart().is_displayed()


def test_validate_book_title(driver):
    order_of_the_book = 1
    home_page = HomePage(driver)
    home_page.open()

    home_book_title = home_page.get_book_title(order_of_the_book)

    home_page.open_book(order_of_the_book)

    book_page = BookPage(driver)
    book_title = book_page.get_title()

    assert home_book_title == book_title
