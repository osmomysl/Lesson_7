import io
import json
import time
from datetime import datetime

start_time = time.time()

car_parameters = []
with io.open('car_data', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 0:
            keys = line.replace("\n", "").split(', ')
        else:
            values = line.replace("\n", "").split(', ')
            dict_cars = dict(zip(keys, values))
            car_parameters.append(dict_cars)
print(car_parameters)
# parameters_json = json.dumps(car_parameters, ensure_ascii=False)
# print(type(parameters_json), parameters_json)

file_date = datetime.now().strftime("%Y-%m-%d_%H%M%S")
with open('car_parameters_{}.txt'.format(file_date), 'w') as json_file:
    json.dump(car_parameters, json_file, ensure_ascii=False)
# ensure_ascii=False - чтобы кириллица читалась, иначе в json будут записаны коды Unicode (это тоже норм)

print('done')
print('it took {} seconds'.format(time.time() - start_time))   # время, затраченное на генерацию отчета
