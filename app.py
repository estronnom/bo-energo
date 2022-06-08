from flask import Flask
from math import sqrt

app = Flask(__name__)


@app.route('/')
def index():
    return 'Тестовое задание для компании БО-ЭНЕРГО<br>' \
           'Выполнил Чибисов Михаил'


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
        if not a:
            response['message'] = 'Коэффициент a НЕ должен быть равен нулю'
            return response

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

    return response


if __name__ == '__main__':
    app.run()
