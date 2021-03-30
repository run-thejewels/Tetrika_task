import requests
from bs4 import BeautifulSoup


def task(array):
    for i in range(len(array)):
        if array[i] == "0":
            return i
    return "Not found"


def animals():
    """функция перебирает примерно 100 страниц поэтому прошу проявить терпение"""
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    page = requests.get(url).text
    list_all_animals = {"А": [], "Б": [], "В": [], "Г": [], "Д": [], "Е": [], "Ё": [], "Ж": [], "З": [], "И": [],
                        "Й": [], "К": [], "Л": [], "М": [], "Н": [], "О": [], "П": [], "Р": [], "С": [], "Т": [],
                        "У": [], "Ф": [], "Х": [], "Ц": [], "Ч": [], "Ш": [], "Щ": [], "Э": [], "Ю": [], "Я": []}
    while True:
        soup = BeautifulSoup(page, 'lxml')
        for div in soup.find_all('div', class_='mw-category-group'):
            for name in div.find_all('a'):
                if name.text[0] in list_all_animals:
                    list_all_animals[name.text[0]].append(name.text)
                if name.text[0] == "A":
                    for lists in list_all_animals:
                        print(f"{lists}: {len(list_all_animals[lists])}")
                    exit()
        links = soup.find('div', id='mw-pages').find_all('a')
        for a in links:
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                page = requests.get(url).text


def time_management(time_list, a, b, i, j):
    """обработка 6 возможных сочетаний 2 временных отрезков"""
    if a[i] < b[j]:
        if a[i + 1] < b[j]:
            return time_list
        else:
            time_list.append(b[j])
        if a[i + 1] > b[j + 1]:
            time_list.append(b[j + 1])
        else:
            time_list.append(a[i + 1])
    else:
        if a[i] > b[j + 1]:
            return time_list
        else:
            time_list.append(a[i])
        if a[i + 1] > b[j + 1]:
            time_list.append(b[j + 1])
        else:
            time_list.append(a[i + 1])
    return time_list


def appearance(intervals):
    pupil_on_lesson = []
    tutor_on_lesson = []
    cupple_time = []
    time_lesson = intervals["lesson"]
    time_pupil = intervals["pupil"]
    time_tutor = intervals["tutor"]
    time = 0
    for i in range(0, len(time_pupil), 2):
        time_management(pupil_on_lesson, time_pupil, time_lesson, i, 0)
    for i in range(0, len(time_tutor), 2):
        time_management(tutor_on_lesson, time_tutor, time_lesson, i, 0)
    for i in range(0, len(pupil_on_lesson), 2):
        for j in range(0, len(tutor_on_lesson), 2):
            time_management(cupple_time, pupil_on_lesson, tutor_on_lesson, i, j)
    for i in range(0, len(cupple_time), 2):
        time += cupple_time[i + 1] - cupple_time[i]
    return  time


if __name__ == '__main__':
    tests = [
        {'data': {'lesson': [3200, 6800],
                  'pupil': [3340, 3389, 3390, 3395, 3396, 6472],
                  'tutor': [3290, 3430, 3443, 6473]},
         'answer': 3117
         },
        {'data': {'lesson': [1594702800, 1594706400],
                  'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                            1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                            1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                            1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                  'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
         'answer': 3577
         },
        {'data': {'lesson': [1594692000, 1594695600],
                  'pupil': [1594692033, 1594696347],
                  'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
         'answer': 3565
         },
    ]
    print("Task 1:")
    print(task("111111111111111111111111100000000"))
    print("Task 2:")
    animals()
    print("Task 3:")
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
