from flask import Flask
from math import sqrt, ceil
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
                       ' ..../quad_eqiation/a/b/c'}


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
    return 'pass'


@app.route('/rand_object/<num>')
def rand_object_result(num):
    try:
        num = int(num)
        assert 1 <= num <= 100
    except ValueError:
        return {'error': 'Введенное число некорректно'}
    except AssertionError:
        return {'error': 'Число должно быть в диапозоне от 1 до 100 '
                         'включительно'}

    while True:
        blue = randint(33, 98)
        green = randint(ceil((100 - blue) / 2), 99 - blue)
        red = 100 - green - blue
        if blue - green > green - red:
            stack = ['Синий'] * blue + ['Зеленый'] * green + ['Красный'] * red
            shuffle(stack)
            return f'{stack[num - 1]}'


if __name__ == '__main__':
    app.run()
