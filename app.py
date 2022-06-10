from flask import Flask
from math import sqrt, ceil, floor
from random import randint, shuffle

app = Flask(__name__)


@app.route('/')
def index():
    return {'message': 'Тестовое задание для компании БО-ЭНЕРГО',
            'author': 'Чибисов Михаил'}


@app.route('/quad_equation/')
def quad_eq_overview():
    return {'message': 'Этот эндпоинт решает квадратное уравнение: '
                       'введите коэффициенты a, b и c в URL сайта'
                       ' ..../quad_equation/a/b/c'}


@app.route('/quad_equation/<a>/<b>/<c>')
def quad_eq_solver(a, b, c):
    response = dict()
    response['solutions_num'] = 0

    try:
        a, b, c = float(a.replace(',', '.')), \
                  float(b.replace(',', '.')), \
                  float(c.replace(',', '.'))
        assert a != 0

        d = b ** 2 - 4 * a * c
        if d < 0:
            response['message'] = 'Дискриминант уравнения меньше нуля, ' \
                                  'решений нет'

        else:
            solution_1 = (-b + sqrt(d)) / (2 * a)
            solution_2 = (-b - sqrt(d)) / (2 * a)
            if solution_1 == solution_2:
                response['solutions_num'] = 1
                response['solution_1'] = solution_1
            else:
                response['solutions_num'] = 2
                response['solution_1'] = solution_1
                response['solution_2'] = solution_2

    except ValueError:
        response['message'] = 'Введенные коэффициенты некорректны'
    except AssertionError:
        response['message'] = 'Коэффициент a НЕ должен быть равен нулю'

    return response


@app.route('/rand_object/')
def rand_object():
    return {
        "message": "Этот эндпоинт решает вторую тестовую задачку. Чтобы "
                   "приложение попыталось угадать цвет предмета "
                   "введите его в URL сайта в следующем формате "
                   "'..../rand_object/номер предмета'"
    }


@app.route('/rand_object/<num>')
def rand_object_result(num):
    try:
        num = int(num)
        assert 1 <= num <= 100
    except ValueError:
        return {
            "error": "Введенное число некорректно"
        }
    except AssertionError:
        return {
            'error': 'Число должно быть в диапозоне от 1 до 100 включительно'
        }

    '''
    blue + green + red = 100
    "сильно больше" > "немного больше"
    blue - green > green - red
    blue can be from 35 to 97
    '''

    blue_min = 35
    blue_max = 97
    blue = randint(blue_min, blue_max)
    red_max = (100 - blue) / 2
    if red_max % 1:
        red_max = int(red_max)
    else:
        red_max = int(red_max) - 1
    red_min = (98 - blue) // 2
    if int(red_min) % 2:
        red_min = ceil(red_min)
    else:
        red_min = floor(red_min)
    if blue == 35:  # catching exception
        red_min = red_max = 32
    red = randint(red_min, red_max)
    green = 100 - blue - red
    if not blue - green > green - red:
        print('wrong difference')

    stack = ['Синий'] * blue + ['Зеленый'] * green + ['Красный'] * red
    shuffle(stack)

    return {
        "blue_items": blue,
        "green_items": green,
        "red_items": red,
        "guess_color": f"{stack[num - 1]}"
    }


if __name__ == '__main__':
    app.run()
