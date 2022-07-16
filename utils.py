import json

SOURCE = "candidates.json"


def load_candidates() -> list:
    """Загружает данные из локального файла в список"""

    with open(SOURCE, mode='r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    return candidates_list


def get_candidate(candidate_id, all_candidates):
    if candidate_id == 0:
        return '<h2>Введите выше номер необходимого кандидата</h2>'
    elif candidate_id <= len(all_candidates):
        for candidate in all_candidates:
            if candidate['pk'] == candidate_id:
                return candidate
    else:
        return f'<h2>Извините в нашей базе нет страницы кандидата с номером <font color="red">{candidate_id}</h2>'


def find_skill(skill):
    """Осуществялет поиск по всем навыкам всех сотрудников и возвращает bool"""

    all_skills = []
    candidates = load_candidates()
    for i in candidates:
        for value in i['skills'].lower().split(' '):
            all_skills.append(value.strip(','))

    if skill.lower().strip() in all_skills:
        return True
    else:
        return False


def find_name(name):
    """Осуществялет поиск по всем именам всех сотрудников и возвращает bool"""

    all_name = []
    candidates = load_candidates()
    for i in candidates:
        for value in i['name'].lower().split(' '):
            all_name.append(value)

    if name.lower().strip() in all_name:
        return True
    else:
        return False


def get_candidates_by_skill(skill, all_candidates):
    list_skill = []
    if skill == '0':
        return "<h2>Введите искомый навык выше</h2>"
    elif find_skill(skill):
        for i in all_candidates:
            for value in i['skills'].lower().split(' '):
                if skill.lower().strip() == value.strip(','):
                    list_skill.append([i['name'], i['pk']])
        return list_skill
    else:
        return f'<h2>Извините в нашей базе нет кандидатов с навыком <font color="red">{skill}'


def get_candidates_by_name(name, all_candidates):
    list_name = []
    if name == '0':
        return "<h2>Введите искомое имя выше</h2>"
    elif find_name(name):
        for i in all_candidates:
            for value in i['name'].split(' '):
                if name.lower().strip() == value.lower():
                    list_name.append([i['name'], i['pk']])
        return list_name
    else:
        return f'<h2>Извините в нашей базе нет кандидатов с именем <font color="red">{name}'
