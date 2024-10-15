from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверяем, что в текущем URL есть подстрока "login"        
#        assert "login" in self.browser.current_url, "Login URL is incorrect"
#        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login URL is incorrect" 
#        assert True
        print(f"Current URL: {self.browser.current_url}")  # Вывод текущего URL для отладки
        assert "login" in self.browser.current_url, "Login URL is incorrect"
        
    def should_be_login_form(self):
        # Проверяем, что присутствует форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        # Проверяем, что присутствует форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
        assert True