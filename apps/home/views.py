import time

from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your views here.


def home_page(request):
    template_name = 'home_page.html'
    url = 'https://mercadolivre.com.br/'
    term = request.GET.get('term', None)
    if term:
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=options)
        browser.get(url)
        # Aceita os cookies
        browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]').click()
        # Campo de busca
        search_field = browser.find_element(By.XPATH, '//*[@id="cb1-edit"]')
        search_field.send_keys(term)
        browser.find_element(By.XPATH, '/html/body/header/div/form/button').click()
        time.sleep(5)
        # Clique ordenação
        browser.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[1]/div/div/div/div[2]/div/div/button/span').click()
        time.sleep(5)
        # Ordenar pelo menor preço
        browser.find_element(By.XPATH, '//*[@id="andes-dropdown-mais-relevantes-list-option-price_asc"]/div/div/span').click()
    return render(request, template_name, {})
