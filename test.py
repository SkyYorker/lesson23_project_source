import re


def open_file():
    with open('R:\Python\lesson24_project_source\data\\apache_logs.txt', 'r') as file:
        return list(file)


def data_regex_cmd1(*args):
    new_str = args[0].replace(' ', '+')
    data_regex = re.compile(rf'{new_str}')
    results = list(filter(data_regex.search, open_file()))
    return results

print(data_regex_cmd1('images\\/\\w \\.png'))