import datetime as dt
import time


from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


start_time = dt.datetime.now()
file = 'weapon.txt'


def get_context(file):  # возвращает словарь аргументов
    data = []
    with open(file, encoding='utf-8') as f:
        for line in f:
            data.append(line.strip())

    list_temp = []
    for i in data:
        list_temp.append(i.split(' - '))

    dict_temp = {}
    for i in list_temp:
        dict_temp[i[0]] = i[1]
    return dict_temp


def from_template(file, template, signature):
    template = DocxTemplate(template)
    context = get_context(file)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    context['img'] = acc  # adds the InlineImage object to the context
    template.render(context)

    template.save('Газета_' + str(dt.datetime.now().date()) + '_gazete.docx')


def generate_report(file):
    template = 'gazete.docx'
    signature = 'nuc_msk.png'
    document = from_template(file, template, signature)



generate_report(file)


doc_time = dt.datetime.now() - start_time

print('Файл создан, время затраченное на выполнение: ', doc_time)
