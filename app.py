
from flask import Flask, request
# from _typeshed import SupportsRichComparisonT
from typing import Any, Callable, Generic, List, Iterable, Optional, Union, Tuple
import re

app = Flask(__name__)



DATA_DIR = "R:\Python\lesson23_project_source\data/apache_logs.txt"
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query() -> Tuple[str, int]:
    cmd1 = request.args.get('cmd1')
    cmd2 = request.args.get('cmd2')
    try:
            # return 'Что-то пошло не так', 400
        if cmd1 and cmd2 == None:
            return data_response_cmd1()
        elif cmd1 and cmd2:
            return data_response_cmd2()
    except FileNotFoundError:
        return 'Файл не найден', 400
    except:
        return 'Что-то пошло не так', 400
    
    

def open_file() -> List[str]:
    file_name = request.args.get('file_name')
    with open(file_name, 'r') as file:
        return list(file)
    

def data_response_cmd1() -> Tuple[str, int]:
    value1: Union[str, int, None] = request.args.get('value1')  
    cmd1: Union[str, None] = request.args.get('cmd1')
    value_dict = {
        'filter': data_filter_cmd1,
        'map': data_map_cmd1,
        'unique': data_unique_cmd1,
        'limit': data_limit_cmd1
    }
    value = value_dict.get(cmd1)(value1,cmd1)
    
    return value


def data_response_cmd2() -> Tuple[str, int]:
    value2: Optional[str] = request.args.get('value2')
    cmd2: Optional[str] = request.args.get('cmd2')
    value_dict = {
        'filter': data_filter_cmd2,
        'map': data_map_cmd2,
        'unique': data_unique_cmd2,
        'limit': data_limit_cmd2

    }
    value: Any = value_dict.get(cmd2)(value2,cmd2)
    return value

def data_filter_cmd1(*args: Union[Tuple[str], None]) -> List[str]:
    data_filter: List[str] = list(filter(lambda file: args[0] in file, open_file()))
    return data_filter


def data_map_cmd1(*args: Union[Tuple[int], None]) -> List[str]:
    data_map: List[str] = list(map(lambda i: i.split(' ')[int(args[0])], open_file()))
    return data_map
        

def data_unique_cmd1() -> List[str]:
    data_unique = list(set([i for i in open_file()]))
    return data_unique


def data_limit_cmd1(*args: Union[Tuple[int], None]) -> List[str]:
    data_limit = sorted(open_file())
    data_limit = list(data_limit[0:int(args[0])])
    return data_limit


def data_filter_cmd2(*args: str) -> List[bool]:
    data_filter = list(filter(lambda file: args[0] in file, data_response_cmd1()))
    return data_filter

def data_map_cmd2(*args: int) -> List[str]:
    data_map: List[str] = list(map(lambda i: i.split(' ')[int(args[0])], data_response_cmd1()))
    return data_map

def data_limit_cmd2(*args):
    data_limit = sorted(data_response_cmd1())
    data_limit = list(data_limit[0:int(args[0])])
    return data_limit

def data_unique_cmd2(*args: str) -> List[object]:
        data_unique = list(set(data_response_cmd1()))
        return data_unique


def data_regex_cmd1(*args: str) -> List[str]:
    rsponse = re.compile(rf'{args[0]}')
    results: List[str] = list(filter(rsponse.search, open_file()))
    return results
# # # #     # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
# # # #     # проверить, что файл file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
# # # #     # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
# # # #     # вернуть пользователю сформированный результат
# # # #     # return app.response_class('', content_type="text/plain")
    

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

