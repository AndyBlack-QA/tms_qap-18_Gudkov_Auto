from HW20.pages.home_page import HomePage
from HW20.elements.header_elements import HeaderElement
from HW20.pages.search_results_page import SearchResultsPage


def test_oz_icon_on_main_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    header_elements = HeaderElement(driver)
    assert header_elements.find_oz_icon().is_displayed()


def test_search_results(driver):
    home_page = HomePage(driver)
    home_page.open()
    header_elements = HeaderElement(driver)
    header_elements.search_field_click("Библия")
    header_elements.search_button_click()
    search_results_page = SearchResultsPage(driver)
    assert header_elements.search_field_get_text() in search_results_page.book_title_bible_request_text()




