# from config.wsgi import *
# from core.erp.models import *
# import random
#
# data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
#         'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
#         'Grasas, aceite y mantequilla']
#
# # delete from public.erp_category;
# # ALTER SEQUENCE erp_category_id_seq RESTART WITH 1;
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#            'u', 'v', 'w', 'x', 'y', 'z']
#
# for i in range(1, 6000):
#     name = ''.join(random.choices(letters, k=5))
#     while Category.objects.filter(name=name).exists():
#         name = ''.join(random.choices(letters, k=5))
#     Category(name=name).save()
#     print('Guardado registro {}'.format(i))

word = 'hola como estas que tal te va'
word_array = word.split(' ')
num_words = []

for i in word_array:
    num_words.append(len(i))

for pos in range(1, len(num_words)):
    long = num_words[pos]
    print('La longitud de palabra {} es {} caracteres'.format(pos, long))
