from datetime import datetime
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
import io
import time

start_time = time.time()


with io.open('car_data', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 1:      # мы будем делать отчёт только по второй строке файла с русифицированными данными
            line_1 = line.replace("\n", "")

content = line_1.split(sep=', ')


def get_context(brand, model, nickname, engine_volume, price_rub):
    return{
        'brand': brand,
        'model': model,
        'nickname': nickname,
        'engine_volume': engine_volume,
        'price_rub': price_rub
    }


def from_template(brand, model, nickname, engine_volume, price_rub, template, picture):
    template = DocxTemplate(template)
    context = get_context(brand, model, nickname, engine_volume, price_rub)

    img_size = Cm(3)        # sets the size of the image
    pic = InlineImage(template, picture, img_size)
    context['pic'] = pic    # adds the InlineImage object to the context

    template.render(context)
    file_date = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    template.save('{}_data_{}.docx'.format(brand, file_date))


def generate_report(brand, model, nickname, engine_volume, price_rub):
    template = 'cars_template.docx'
    picture = 'GAZ_24-10.jpg'
    from_template(brand, model, nickname, engine_volume, price_rub, template, picture)

"""
def toFixed(numObj, digits=0):   # не понял, зачем эта функция. Работает и без неё
    return f"{numObj:.{digits}f}"
"""

generate_report(*content)

print('done')
print("it took %s seconds" % (time.time() - start_time))   # время, затраченное на генерацию отчета
