import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = 'R:\Python\lesson23_project_source/file.txt'
        
# print(os.path.exists('R:\Python\lesson23_project_source\data/apache_logs.txt'))
value1 = 2
cmd1 = 'unique'
cmd2 = 'map'
value = 0
def _():
    with open(DATA_DIR, 'r') as file:                   
        if cmd1 == 'unique':
            response_data_sort = sorted(file)
            response_data_sort = list(response_data_sort[0:int(value1)])
            return list(set(response_data_sort))
            
            # if cmd2 == 'map':
            #     return list(map(lambda i: i.split(' ')[int(value)], response_data_filter)) 
        
            
        # elif cmd2 == 'map':
        #     return list(map(lambda i: i.split(' ')[int(value)], response_data_filter))
        # elif cmd2 == 'unique':
        #     return set(response_data_filter)
        
print(_())