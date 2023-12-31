
"""    РАБОТА С ВАКАНСИЯМИ    """


class Vacancy:
    __slots__ = {"title", "link", "description", "salary"}
    def __init__(self, title, link, description, salary):

        self.title = title
        self.link = link
        self.description = description
        self.salary = salary


    def __repr__(self):
        return f"vacancy(title = '{self.title}', link = '{self.link}', description = '{self.description}', salary = {self.salary}"


    def __str__(self):
        return self.title


    def __gt__(self,other):
        return self.salary > other.salary



    def __lt__(self,other):
        if other.salary is None:
            return False
        if self.salary is None:
            return True


class CountMixin:
    @property

    def get_count_vacancy(self):
        pass


class HHVacancy(Vacancy, CountMixin):
    def __str__(self):
        return f"HH:{self.title}, зарплата: {self.salary} руб.мес"


class SJVacancy(Vacancy, CountMixin):
    def __str__(self):
        return f"SJ:{self.title}, зарплата: {self.salary} руб.мес"