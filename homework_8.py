import random
from datetime import datetime, timedelta


FIRST_NAMES = ('Аліна', 'Анастасія', 'Андрій', 'Анна', 'Артем', 'Богдан', 'Богдана', 'Валентина', 'Валерія', 'Василь', 'Владислав', 'Володимир', 
               'Віктор', 'Вікторія', 'Віра', 'Віталій','Галина', 'Ганна', 'Данило', 'Дмитро', 'Іван', 'Іванна', 'Ігор', 'Ірина', 'Катерина', 
               'Лариса', 'Леся', 'Людмила', 'Лідія', 'Лілія', 'Максим', 'Маргарита', 'Марина', 'Марта', 'Марта', 'Марія', 'Мирослава', 'Михайло', 
               'Надія', 'Назар', 'Наталя', 'Наталія', 'Ніна', 'Оксана', 'Олег', 'Олександр', 'Олексій', 'Олена', 'Олеся', 'Ольга', 'Петро', 
               'Роман', 'Руслан', 'Руслана', 'Світлана', 'Сергій', 'Софія', 'Тетяна', 'Христина', 'Юлія', 'Юрій', 'Яна', 'Ярослав', 'Ярослава')

LAST_NAMES = ('Яремчук', 'Зубенко', 'Ткаченко', 'Яворівський', 'Волошин', 'Жуковський', 'Зінченко', 'Сидорчук', 'Романченко', 'Онопченко', 
              'Ніколаєнко', 'Левченко', 'Тимченко', 'Грищенко', 'Жукович', 'Рибаченко', 'Старицький', 'Устименко', 'Семенчук', 'Шевель', 
              'Король', 'Романчук', 'Хоменюк', 'Павлюк', 'Хоменко', 'Назарчук', 'Черновол', 'Костенко', 'Сидоренко', 'Євдокименко', 'Васильчук',
              'Кравченюк', 'Терещенко', 'Борисенко', 'Яценко', 'Гончаренко', 'Самойленко', 'Усенко', 'Ярошенко', 'Павлюченко', 'Кравченко', 
              'Кузьмич', 'Харченко', 'Якименко', 'Мазур', 'Данилюк', 'Шаповаленко', 'Котляр', 'Федорович', 'Поліщук', 'Біленький', 'Русин', 
              'Марченко', 'Тарасюк', 'Українець', 'Тарасенко', 'Коцюбинський', 'Цибуленко', 'Павленко', 'Мельниченко', 'Сергієнко',  'Тимошенко',
              'Олексієнко', 'Савченко', 'Іванчук', 'Островський', 'Романюк', 'Литвинчук', 'Калінчук', 'Лазарчук', 'Шевченко', 'Бондаренко', 'Козак',
              'Ткачук', 'Іваненко', 'Федорчук', 'Хоменчук', 'Мельничук', 'Іванюк', 'Сагайдачний', 'Ковальчук', 'Василенчук', 'Яковенко', 'Руденко',
              'Панасюк', 'Нестеренко', 'Захарчук', 'Лисиченко', 'Цимбалюк', 'Даниленко', 'Шевчук', 'Журавченко', 'Демчук',  'Шелест', 'Олійник',
              'Вітренко', 'Кирик', 'Лисенко', 'Васильченко', 'Демченко', 'Харчук', 'Коваленко', 'Радченко', 'Онопко', 'Назаренко', 'Верещук',
              'Гордієнко', 'Міщенко', 'Семенюк', 'Бондарчук', 'Яременко', 'Дмитренко', 'Лазаренко', 'Новак', 'Журавчук', 'Литвиненко', 'Данильчук',
              'Поліщенко', 'Яковчук', 'Василенко', 'Іщенко', 'Головко', 'Гриценко', 'Головченко', 'Носаченко', 'Остапчук', 'Петренко', 
              'Мельник', 'Маслович', 'Завадський', 'Білич', 'Чернишенко', 'Жданович', 'Карпенко', 'Устимчук', 'Кузьменко', 'Григоренко', 
              'Заєць', 'Гуменюк', 'Орловчук', 'Федоренко', 'Шаповал', 'Білозерчук', 'Чорновіл', 'Фоменко')

START_DATE = (1970, 1, 1)
END_DATE = (2005, 12, 31)


def generate_random_date(start_date: tuple[int]=START_DATE, end_date: tuple[int]=END_DATE) -> datetime:
    """
    Generates a random date within the specified range.

    Arguments:
    start_date (tuple): A tuple with three values (year, month, day) representing the start date.
    end_date (tuple): A tuple with three values (year, month, day) representing the end date.

    Returns:
    datetime: A datetime object with a random date within the specified range.
    """

    start_date = datetime(*start_date)
    end_date = datetime(*end_date)

    delta = end_date - start_date 
    random_days = random.randint(0, delta.days)   
    random_date = start_date + timedelta(days=random_days)

    return random_date


def generate_users_list(number_of_users: int, start_date: tuple[int]=START_DATE, end_date: tuple[int]=END_DATE) -> list[dict[str, object]]:
    """
    Generates a list of random users with their names and birthdays.

    Arguments:
    number_of_users (int): The desired number of users to generate.
    start_date (tuple, optional): A tuple with three values (year, month, day) representing the start date range for birthdays.
        Defaults to START_DATE.
    end_date (tuple, optional): A tuple with three values (year, month, day) representing the end date range for birthdays.
        Defaults to END_DATE.

    Returns:
    list[dict[str, object]]: A list of dictionaries, where each dictionary represents a user with "name" and "birthday" keys.
    """

    users = []

    while len(users) < number_of_users:
        full_name = f'{random.choice(LAST_NAMES)} {random.choice(FIRST_NAMES)}'
        if full_name in users:
            continue
        users.append({"name": full_name, "birthday": generate_random_date(start_date, end_date)})

    return users


def get_birthday_celebration(birthdate: datetime, current_date=datetime.now()) -> datetime:
    """
    Gets the date of birthday celebration for a given the user's date of birth in the current year.

    Arguments:
    birthdate (datetime): The birthdate of the user.
    current_date (datetime, optional): The current date. Defaults to the current system date.

    Returns:
    datetime: The date of the birthday celebration. If the birthdate is on February 29 and the current year is not a leap year,
            the celebration is on March 1. Otherwise, the celebration is on the same day and month as the birthdate.
    """

    current_year = current_date.year
    is_leap_year = True if current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0) else False
    if birthdate.day == 29 and birthdate.month == 2 and not is_leap_year:
        celebration_day = 1
        celebration_month = 3
    else:
        celebration_day = birthdate.day
        celebration_month = birthdate.month 

    birthday_celebration = datetime(current_year, celebration_month, celebration_day) 

    return birthday_celebration


def generate_users_birthday_list(users: list[dict[str, object]], current_date=datetime.now()) -> None:
    """ 
    Prints a list of users who have their birthday celebrations in the current week.

    Arguments:
    users (list[dict[str, object]]): A list of dictionaries representing users with "name" and "birthday" keys.
    current_date (datetime, optional): The current date. Defaults to the current system date.

    Returns: 
    None: Prints the output to the console.
    """

    current_date = datetime(current_date.year, current_date.month, current_date.day) 
    current_weekday = current_date.weekday()

    if current_weekday:
        start_date = current_date
        end_date = current_date + timedelta(days=7) 
    else:
        start_date = current_date - timedelta(days=2)
        end_date = current_date + timedelta(days=5)         

    users_birthday_list = {}

    for user in users:         
        user_birthday = get_birthday_celebration(user["birthday"], current_date)

        if user_birthday - start_date < timedelta(days=7) and end_date - user_birthday < timedelta(days=8):            
            if user_birthday.weekday() in (5, 6):
                user_weekday = 0
            else:
                user_weekday = user_birthday.weekday()
          
            users_birthday_list.setdefault(user_weekday, []).append(user["name"])

    weekday_names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    for weekday, users in sorted(users_birthday_list.items()):
        print(f"{weekday_names[weekday]}: {', '.join(users)}")


if __name__ == '__main__':

    generate_users_birthday_list(generate_users_list(1000))


    
