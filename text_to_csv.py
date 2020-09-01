import csv
import io
import time
from datetime import datetime

start_time = time.time()

with io.open('car_data', encoding='utf-8') as f:
    lines = f.read().split("\n")

table_content = [x.split(', ') for x in lines]

file_date = datetime.now().strftime("%Y-%m-%d_%H%M%S")
with open('car_data_{}.csv'.format(file_date), 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')       # delimiter=';' - чтобы содержимое распределилось по ячейкам
    writer.writerows(table_content)

print('done')
print("it took %s seconds" % (time.time() - start_time))   # время, затраченное на генерацию отчета
