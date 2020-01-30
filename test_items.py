link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_busket_button(browser):
    browser.get(link)
    # checking that there is only one 'add to busket' button
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) == 1, "Number of 'add to busked' buttons is not 1"
