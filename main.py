"""
Вам будут нужны свой логин и пароль от Госуслуг
Написать скрипт, который авторизуется на Госуслугах
Создает папку в корневом каталоге скрипта и сохраняет паспортные данные в файл
Завершает успешное выполнение
—
если хотите продемонстрировать, высший пилотаж, то

В этой же сессии заказывает какой-нибудь документ
(Справка о наличии или отсутствии судимости, Справка о доходах клиента за последние 3 года (по форме 2-НДФЛ)),
справка выпускается 2-5 минут, при повторном запуске (или выход из таймаута) в папку сохраняется выпущенный файл

"""


"""

Данное 'ПО' создано для демонстрации,
производит авторизацию на Госуслугах,
создает папку в корневом каталоге скрипта и сохраняет паспортные данные в файл

"""
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from time import sleep

import requests
from bs4 import BeautifulSoup

# AutName = 'Имя: пользователя телефон или почта'
# AutPass = 'Пароль'
AutName = '+7'
AutPass = ''

class verification(object):


    def __init__(self):
        print("---------------------------------------------------------------------")
        print("                  Аутентификация портала ГосУслуг")
        print("---------------------------------------------------------------------")

        url = 'https://www.gosuslugi.ru'

        user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

        try:
            print('------------------- open site https://www.gosuslugi.ru ------------')
            EXE_PATH = 'driverChrom\chromedriver.exe'
            dr = webdriver.Chrome(EXE_PATH)

            dr.get(url)

            print(' zer good! ')
            print('-------------------------------------------------------------------')
            sleep(3)
        except:
            print(' no good..')
        try:
            print('------------------------ Enter lk ---------------------------------')
            lc = dr.find_element_by_link_text('Личный кабинет')
            lc.click()
            sleep(3)
        except:
            print(' no good..')
        try:
            print('------------------- Enter login and pass --------------------------')

            login = dr.find_element_by_id('login')
            login.send_keys(AutName)

            sleep(1)

            passw = dr.find_element_by_id('password')
            passw.send_keys(AutPass)
            passw.send_keys(Keys.ENTER)
            sleep(1)
            print(' zer good! ')
        except:
            print(' no good..')

        try:
            print('-------------------- Open menu ------------------------------------')
            show = dr.find_element_by_class_name('show')
            show.click()
            print(' zer good! ')
            sleep(1)
        except:
            print(' no good..')
        try:
            print('------------------- onClick Профиль -------------------------------')
            profil = dr.find_element_by_link_text('Профиль')
            profil.click()
            print(' zer good! ')
            sleep(3)
        except:
            print(' no good..')
        try:


            # FullName
            soup = BeautifulSoup(dr.page_source, 'lxml')
            name = soup.find_all('div', class_='name')
            fullName = name[1].text


            print('-------------------------------------------------------------------')
            print(' zer good! ')
        except:
            print(' no good..')
        try:
            print('-------------------- Open menu ------------------------------------')
            # menu
            show = dr.find_element_by_class_name('show')
            show.click()
            print(' zer good! ')
            sleep(1)
        except:
            print(' no good..')


        try:
            print('------------------- onClick Документы -----------------------------')

            documents = dr.find_element_by_xpath("/html/body/lk-root/header/lib-header/div/div/div[2]/div[2]/div["
                                                 "2]/lib-user-menu/div/div[1]/div/div[1]/ul[2]/li[4]/div/span")
            # documents = dr.find_element('text-plain',"Документы")
            documents.click()

            print(' zer good! ')
            sleep(3)
            print('-------------------------------------------------------------------')

        except:
            print(' no good..')


        # паспортные данные

        print('fullname =', fullName)


        soup = BeautifulSoup(dr.page_source, 'lxml')

        pasport = soup.find_all('h5', class_='title-h5')
        pasport = pasport[2].text
        print('pasport =', pasport)

        datapasport = soup.find_all('div', class_='mt-4')
        issued = datapasport[0].text
        print('issued = ', issued)

        department_code = datapasport[1].text
        print('department_code=', department_code)

        date_of_issue = datapasport[2].text
        print('date_of_issue = ', date_of_issue)

        addres = datapasport[3].text
        print('addres = ', addres)

        snils_inn = soup.find_all('h5', class_='title-h5')

        snils = snils_inn[1].text
        print('snils = ', snils)

        inn = snils_inn[2].text
        print('inn = ', inn)

        # запись в файл данных парсера
        if not os.path.exists('out'):
            os.mkdir('out')
        else:
            print("папка out существует")

        f = open('./out/pasport.txt', 'w')
        f.write(
            'Фамилия Имя Отчество:' + fullName + '\n'
                + 'Паспорт серия:' + pasport + '\n'
                + 'Кем выдан:' + issued + '\n'
                + 'Код подразделения:' + department_code + '\n'
                + 'Дата выдачи:' + date_of_issue + '\n'
                + 'Адрес:' + addres + '\n'
                + '\n'
                + 'Снилс:' + snils + '\n'
                + 'ИНН:' + inn + '\n')
        f.close()










if __name__ == '__main__':

    verification()
    # ver = verification()
    #
    # print("Name ", ver.get_user(), "Pass ", ver.get_pass())
