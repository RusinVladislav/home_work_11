import json

SOURCE = "candidates.json"


def load_candidates() -> list:
    """Загружает данные из локального файла в список"""

    with open(SOURCE, mode='r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    return candidates_list


def get_candidate(candidate_id, all_candidates):
    """Возвращает данные кандидата по его номеру pk"""

    if candidate_id == 0:
        return '<h2>Введите выше номер необходимого кандидата</h2>'
    elif candidate_id <= len(all_candidates):
        for candidate in all_candidates:
            if candidate['pk'] == candidate_id:
                return candidate
    else:
        return f'<h2>Извините в нашей базе нет страницы кандидата с номером <font color="red">{candidate_id}</h2>'


def get_candidates_by_skill(skill, all_candidates):
    """Возвращает список кандидатов по нужному навыку"""

    list_skill = []
    if skill == '0':
        return "<h2>Введите искомый навык выше</h2>"
    for i in all_candidates:
        for value in i['skills'].lower().split(' '):
            if skill.lower().strip() == value.strip(','):
                list_skill.append([i['name'], i['pk']])
    if list_skill:
        return list_skill
    else:
        return f'<h2>Извините в нашей базе нет кандидатов с навыком <font color="red">{skill}'


def get_candidates_by_name(name, all_candidates):
    """Возвращает список кандидатов по нужному имени"""

    list_name = []
    if name == '0':
        return "<h2>Введите искомое имя выше</h2>"
    for i in all_candidates:
        for value in i['name'].split(' '):
            if name.lower().strip() == value.lower():
                list_name.append([i['name'], i['pk']])
    if list_name:
        return list_name
    else:
        return f'<h2>Извините в нашей базе нет кандидатов с именем <font color="red">{name}'
