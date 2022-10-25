# базовая функция сверяющая элемент строки с шаблоном
# используется в check_template и сама по себе
def subcheck(t, s):
    if len(t) != len(s):
        return False
    for i in range(len(t)):
        if (t[i] != s[i]) and t[i] != '?':
            return False
    return True


# функция, ищущая в строке вхождение шаблона
# возвращает индекс начала вхождения или False,
# если шаблон не найден
def check_template(t, s):
    if len(t) > len(s):
        return False
    i = 0
    while len(t) <= len(s[i:]):
        #         print(t,s[i:i+len(t)])
        if subcheck(t, s[i:i + len(t)]):
            return i
        i += 1
    return False


# краевые случаи. Единичная длина.
# нет звездочки в начале
# нет звездочки в конце

def validation(template, string, t_index, s_index, s_star, e_star):
    total = len(template)
    #     поскольку исходный шаблон не может быть нулевым, то такой случай возможен лишь
    # при условии, что он состоял из одной или нескольких звездочек
    if template == '':
        return True

    #     отдельно вынесу случай с единичным элементом
    if total == 1:
        if s_star and e_star:
            #
            return type(check_template(template[0], string)) == int
        elif s_star:
            #
            return subcheck(template[0], string[-len(template[0]):])
        elif e_star:
            #             print('e_star')
            return subcheck(template[0], string[:len(template[0])])
        else:
            #             print('no_stars')
            return subcheck(template[0], string)

    #   обработчик первого элемента
    if t_index == 0:
        if s_star:
            ind = check_template(template[0], string)
            if type(ind) == int:
                #
                return validation(template, string, t_index + 1, s_index + ind + len(template[0]), s_star, e_star)
            else:
                #
                return False
        else:
            if subcheck(template[0], string[:len(template[0])]):
                ind = len(template[0])
                return validation(template, string, t_index + 1, s_index + ind, s_star, e_star)
            else:
                return False

    #  обработчик последнего элемента
    elif t_index == total - 1:

        if e_star:
            return type(check_template(template[t_index], string[s_index:])) == int
        else:
            if len(string[s_index:]) < len(template[t_index]):
                return False
            return subcheck(template[t_index], string[-len(template[t_index]):])

    # обработчик всех остальных элементов
    else:
        ind = check_template(template[t_index], string[s_index:])
        if type(ind) == int:
            return validation(template, string, t_index + 1, s_index + ind, s_star, e_star)
        else:
            return False


template = str(input())
string = str(input())


def validator(base_template, s):
    start_star = int(base_template[0] == '*')
    end_star = int(base_template[-1] == '*')
    t = base_template.strip('*').split('*')
    #     print(t)
    return (validation(t, s, 0, 0, start_star, end_star))


ans = validator(template, string)
print('YES' * ans + 'NO' * (not ans))