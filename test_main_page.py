#from selenium.webdriver.common.by import By
#import time

#def test_guest_should_see_add_to_basket_button(browser):
    # Переход на страницу товара
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"#   browser.get(link)
    
    # Ждем 30 секунд для визуальной проверки
#    time.sleep(30)
    
    # Поиск кнопки добавления в корзину
#   button = browser.find_element("css selector", ".btn-add-to-basket")
    
    # Проверка, что кнопка присутствует на странице
#    assert button is not None, "Кнопка добавления в корзину не найдена"

from selenium import webdriver
from selenium.webdriver.common.by import By

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    browser.get(link)
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()
    
    
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина