import os

from flask import Flask, request

app = Flask(__name__)


DATA_DIR = "R:\Python\lesson23_project_source\data/apache_logs.txt"




@app.route("/perform_query")
def perform_query(file_name, value, ):
    file_name = request.args.get('file_name')
    value = request.args.get('value')
    if not DATA_DIR:
        return f"", 400
    if value and request.args != '':       
        with open(DATA_DIR) as file:                   
                response_data = list(filter(lambda file: value in file, file))
                return f"{response_data}\n"       
    else:
        return f"", 400
    
# # #     # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
# # #     # проверить, что файл file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
# # #     # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
# # #     # вернуть пользователю сформированный результат
# # #     # return app.response_class('', content_type="text/plain")
    


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9999, debug=True)

# print(perform_query())
# def open_file(value):
#     with open(DATA_DIR, 'r') as file:
#         response_data_1 = map(lambda i: i.split(' ')[value], file)
#         return list(response_data_1)
    
# print(open_file(0))

# def open_file(value):
#     with open(DATA_DIR, 'r') as file:
#         response_data_1 = map(lambda i: i.split(' ')[value], file)
#         return set(response_data_1)
    
# print(open_file(0))

def open_file(value):
    with open(DATA_DIR, 'r') as file:
        response_data_1 = sorted(file)
        return list(response_data_1[0:value])
print(open_file(4))


# a = [1,2,3,5,6]
# print(a[0:3])