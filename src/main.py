from src.compound import Compound#, PathNotFoundError
from src.run_class import HH, Superjob
from src.utils import sorting, get_top, get_hh_vacancies_list, get_sj_vacancies_list


def main():
    keyword = input('Ключевое слово? ')
    keyword = 'pYthon'
    hh_run = HH(keyword)
    print(hh_run)
    sj_run = Superjob(keyword)
    print(sj_run)
    path = "/hh_vacancies.json"
    #try:
    #hh_compound = Compound(path)
    #except PathNotFoundError:
    #    print(f"Директория {path} не найдена, записать невозможно")
    #    return
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
            sj_vacancies = sj_run.get_request().json()
            sj_items = sj_vacancies['objects']
            more = sj_vacancies['more']
            hh_compound. insert(sj_items)
    while True:
        hh_vacancies = get_hh_vacancies_list(hh_compound)
        sj_vacancies = get_sj_vacancies_list(sj_compound)
        sorted_vacancies = sorting(hh_vacancies + sj_vacancies)
        for vacancy in sorted_vacancies:
            print(vacancy)
            continue_run = input("Continue? y/n")
            if continue_run.lower() == n:
                break

main()
