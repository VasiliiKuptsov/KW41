from src.jobs_class import Vacancy, HHVacancy, SJVacancy


def sorting(vacancies:list[Vacancy]) -> list(Vacancy):
    return sorted(vacancies)


def get_top (vacancies:list[vacancy], top-count:int) -> list[vacancy]:
    return list(sorted(vacancies, reverse=True)[:top_count])


def get_hh_vacancies_list(compound) -> list[HHVacancy]:
    vacancies = [
        HHVacancy(
            title = vacancy['name'],
            link = vacancy['alternat_url'],
            description = vacancy['snippet'],
            salary = vacancy['salary']['from']if vacancy['salary'] else None)
        for vacancy in compound.select({})]
    return vacancies


def get_sj_vacancies_list(compound) -> list[SJVacancy]:
    vacancies = [
        SJVacancy(
            title=vacancy['profession'],
            link=vacancy['link'],
            description=vacancy['candidat'],
            salary=vacancy['payment_from'])
        for vacancy in compound.select({})]
    return vacancies
