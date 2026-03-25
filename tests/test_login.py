from pages.login_page import LoginPage
from config import BASE_URL

class TestLogin:

    # Test Case 1: Successful login
    def test_successful_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login("tomsmith", "SuperSecretPassword!")

        assert "/secure" in login.get_current_url()
        assert "You logged into a secure area!" in login.get_success_message()

    # Test Case 2: Login with invalid username
    def test_invalid_username(self, page):
        login = LoginPage(page)
        login.open()
        login.login("invalid_username", "SuperSecretPassword!")

        assert "Your username is invalid!" in login.get_error_message()
        assert BASE_URL in login.get_current_url()

    # Test Case 3: Login with invalid password
    def test_invalid_password(self, page):
        login = LoginPage(page)
        login.open()
        login.login("tomsmith", "invalid_password")

        assert "Your password is invalid!" in login.get_error_message()
        assert BASE_URL in login.get_current_url()
