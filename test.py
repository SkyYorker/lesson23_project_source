import re


def open_file():
    with open('R:\Python\lesson24_project_source\data\\apache_logs.txt', 'r') as file:
        return list(file)


def data_regex_cmd1(*args):
    data_regex = re.compile(rf'{args[0]}')
    results = list(filter(data_regex.search, open_file()))
    return results

print(data_regex_cmd1('images\/\w+\.png', 'regex'))