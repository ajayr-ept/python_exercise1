#Write a Python program to filter the height and width of students, which are stored in a
# dictionary. Height >= 6ft and Weight>= 70kg:
#Original Dictionary: {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),
# 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
#Output : {'Cierra Vega': (6.2, 70)}


dic = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),
            'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print('original',dic)
dic = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), dic.items()))
print(dic)
