a=dict('un':{1,2,3}, 'deux': {4,5,6}, 'trois': {7,8,9})
b=a
seuil = 5
for k, v in a:
    print(k, 'vaut', v)
    if v > seuil: del v

print('a = ', a, 'b = ', b)