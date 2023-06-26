
from flask import Flask, request

from typing import Callable, Mapping, Protocol, Sequence

import re

app = Flask(__name__)



DATA_DIR = "R:\Python\lesson23_project_source\data/apache_logs.txt"
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")

class Handler(Protocol):
    def __call__(self, *args) -> list[str]: # type: ignore
        ...


@app.route("/perform_query")
def perform_query() -> tuple[str, int] | list[str]: # type: ignore
    try:
        cmd1 = request.args.get('cmd1')
        cmd2 = request.args.get('cmd2')
        if cmd1 == None and cmd2 == None:
           return 'Что-то пошло не так', 400      
        if cmd1 and cmd2 == None:            
            return data_response_cmd1()
        if cmd1 and cmd2:
            return data_response_cmd2()
    except FileNotFoundError:
        return 'Файл не найден', 400
    except KeyError:
        return 'Такой команды не существует', 400
    except:
        return 'Что-то пошло не так', 400
    
    

def open_file() -> list[str]:
    file_name = request.args['file_name']
    with open(file_name, 'r') as file:
        return list(file)
    

def data_response_cmd1() -> list[str]:
    value1 = request.args['value1']
    cmd1 = request.args['cmd1']
    CMD_1_MAPPER: Mapping[str, Handler] = {
        'filter': data_filter_cmd1,
        'map': data_map_cmd1,
        'unique': data_unique_cmd1,
        'limit': data_limit_cmd1,
        'regex': data_regex_cmd1
}
    value = CMD_1_MAPPER[cmd1](value1,cmd1)
    return value
    

def data_response_cmd2() -> list[str]:
    value2 = request.args['value2']
    cmd2 = request.args['cmd2']
    MD_2_MAPPER: Mapping[str, Handler] = {
        'filter': data_filter_cmd1,
        'map': data_map_cmd1,
        'unique': data_unique_cmd1,
        'limit': data_limit_cmd1,
        'regex': data_regex_cmd1
}
    value = MD_2_MAPPER[cmd2](value2,cmd2)
    return value

def data_filter_cmd1(*args: str) -> list[str]:
    data_filter = list(filter(lambda file: args[0] in file, open_file()))
    return data_filter


def data_map_cmd1(*args: int) -> list[str]:
    data_map = list(map(lambda i: i.split(' ')[int(args[0])], open_file()))
    return data_map
        

def data_unique_cmd1(*args: str) -> list[str]:
    data_unique = list(set([i for i in open_file()]))
    return data_unique


def data_limit_cmd1(*args: str) -> list[str]:
    data_limit = sorted(open_file())
    data_limit = list(data_limit[0:int(args[0])])
    return data_limit


def data_regex_cmd1(*args: str) -> list[str]:
    new_str = args[0].replace(' ', '+')
    data_regex = re.compile(rf'{new_str}')
    results = list(filter(data_regex.search, open_file()))
    return results


def data_filter_cmd2(*args: str) -> list:
    data_filter = list(filter(lambda file: args[0] in file, data_response_cmd1()))
    return data_filter


def data_map_cmd2(*args: int) -> list[str]:
    data_map = list(map(lambda i: i.split(' ')[int(args[0])], data_response_cmd1()))
    return data_map


def data_limit_cmd2(*args: str) -> list[str]:
    data_limit = sorted(data_response_cmd1())
    data_limit = list(data_limit[0:int(args[0])])
    return data_limit


def data_unique_cmd2(*args: str) -> list[str]:
        data_unique = list(set(data_response_cmd1()))
        return data_unique


def data_regex_cmd2(*args: str) -> list[str]:
    new_str = args[0].replace(' ', '+')
    data_regex = re.compile(rf'{new_str}')
    results = list(filter(data_regex.search, data_response_cmd1()))
    return results
# # # #     # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
# # # #     # проверить, что файл file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
# # # #     # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
# # # #     # вернуть пользователю сформированный результат
# # # #     # return app.response_class('', content_type="text/plain")
    

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

