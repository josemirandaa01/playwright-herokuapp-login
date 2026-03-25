from config import BASE_URL

class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")

    def get_success_message(self):
        self.page.wait_for_selector(".flash.success")
        return self.page.inner_text(".flash.success")

    def get_error_message(self):
        self.page.wait_for_selector(".flash.error")
        return self.page.inner_text(".flash.error")

    def get_current_url(self):
        return self.page.url