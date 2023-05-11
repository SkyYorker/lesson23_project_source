import os
import requests
from flask import Flask, request

app = Flask(__name__)



# DATA_DIR = "R:\Python\lesson23_project_source\data/apache_logs.txt"
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    response = requests.get('http://127.0.0.1:9997')
    file_name = request.args.get('file_name')
    value = request.args.get('value')
    value1 = request.args.get('value1')
    cmd1 = request.args.get('cmd1')
    cmd2 = request.args.get('cmd2')           
    try:
        data_file = open(file_name, 'r')
        if response.status_code != 500:
            if cmd1 == 'filter' and cmd2 == None or cmd1 == 'filter':
                response_data_filter = list(filter(lambda file: value1 in file, data_file))
                if cmd2 == 'map':
                    response_data_filter = list(map(lambda i: i.split(' ')[int(value)], response_data_filter))
                    return response_data_filter                 
                elif cmd2 == 'unique':
                    response_data_filter = list(set(response_data_filter))
                    return response_data_filter
                elif cmd2 == 'limit':
                    response_data_filter = sorted(response_data_filter)
                    return list(response_data_filter[0:int(value)])
                return response_data_filter

            if cmd1 == 'map' and cmd2 == None or cmd1 == 'map':
                response_data_map = list(map(lambda i: i.split(' ')[int(value1)], data_file))  
                if cmd2 == 'filter':
                    response_data_map = list(filter(lambda file: value in file, response_data_map))
                    return response_data_map
                elif cmd2 == 'unique':
                    response_data_map = list(set(response_data_map))
                    return response_data_map
                elif cmd2 == 'limit':
                    response_data_map = sorted(response_data_map)
                    return list(response_data_map[0:int(value)])
                return response_data_map

            if cmd1 == 'unique' and cmd2 == None or cmd1 == 'unique':
                response_data_unique = list(set([i for i in data_file]))  
                if cmd2 == 'filter':
                    response_data_unique = list(filter(lambda file: value in file, response_data_unique))
                    return response_data_unique
                elif cmd2 == 'map':
                        response_data_unique = list(map(lambda i: i.split(' ')[int(value)], response_data_unique))
                        return response_data_unique
                elif cmd2 == 'limit':
                    response_data_unique = sorted(response_data_unique)
                    return list(response_data_unique[0:int(value)])
                return response_data_unique
            
            if cmd1 == 'limit' and cmd2 == None or cmd1 == 'limit':
                response_data_sort = sorted(data_file)
                response_data_sort = list(response_data_sort[0:int(value1)])  
                if cmd2 == 'filter':
                    response_data_sort = list(filter(lambda file: value in file, response_data_sort))
                    return response_data_sort
                elif cmd2 == 'unique':
                    response_data_sort = list(set(response_data_sort))
                    return response_data_sort
                elif cmd2 == 'map':
                        response_data_sort = list(map(lambda i: i.split(' ')[int(value)], response_data_sort))
                        return response_data_sort
                return response_data_sort
        data_file.close()
        return f'Что-то пошло не так', 400
    except FileNotFoundError:
        return f'Файл не найден', 400
    except TypeError:
        return f'Вы не выбрали файл', 400

            
    
# # # #     # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
# # # #     # проверить, что файл file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
# # # #     # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
# # # #     # вернуть пользователю сформированный результат
# # # #     # return app.response_class('', content_type="text/plain")
    


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9997, debug=True)

