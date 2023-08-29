
from src.compound import Compound#, PathNotFoundError
from src.run_class import HH, Superjob
from src.utils import sorting, get_top, get_hh_vacancies_list, get_sj_vacancies_list
import requests
import os

"""  ПО ЗАЯВКЕ РАБОТАЕМ С ВАКАНСИЯМИ НН И СУПЕРДЖОБ  """

def main():
    keyword = input(' ВВЕДИТЕ КЛЮЧЕВОЕ СЛОВО   ')
    hh_run = HH(keyword)
    sj_run = Superjob(keyword)
    hh_compound = Compound("hh_vacancies.json")
    sj_compound = Compound("sj_vacancies.json")
    page = 0
    hh_pages = 1
    hh_close = False
    more = True

    while not hh_close and more:
        if page < hh_pages:
            hh_run.params['page'] = page
            page +=1
            hh_vacancies = hh_run.get_request().json()
            hh_pages = hh_vacancies['pages']
            hh_items = hh_vacancies['items']
            hh_compound.insert(hh_items)
        else:
            hh_close = True
        if more:

            sj_run.params['page'] = sj_run.params['page'] + 1
            """  Прищлось напрямую, так и не смог  через 'sj_run.get_requests().json()"""
            headers = {"X-Api-App-Id": os.environ.get("SUPER_JOB_KEY")}
            params = {"text": keyword, "page": page, "per_page": 50}
            sj_vacancies = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=headers, params = params)#sj_run.get_request().json()
            sj_items = sj_vacancies.json()['objects']
            more = sj_vacancies.json()['more']
            sj_compound.insert(sj_items)
    while True:
        give = input('Сортировать все или по определенному количеству "a" or "c"').lower()
        if give == 'a':
            hh_vacancies = get_hh_vacancies_list(hh_compound)
            sj_vacancies = get_sj_vacancies_list(sj_compound)
            sorted_vacancies = sorting(hh_vacancies + sj_vacancies)
            for vacancy in sorted_vacancies:
                print(vacancy)
        elif give =='c':
            hh_vacancies = get_hh_vacancies_list(hh_compound)
            sj_vacancies = get_sj_vacancies_list(sj_compound)
            all_vacancies = hh_vacancies + sj_vacancies
            top_count = int(input('Введите количество вакансии для вывода - '))
            top_vacancies = get_top(all_vacancies, top_count)
            for vacancy in  top_vacancies:
                print(vacancy)
        else:
            print('Неправильный ввод!')
        continue_run = input("Continue? y/n")
        if continue_run.lower() == 'n':
            break

main()
