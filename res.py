import pickle
with open('model.pkl', 'rb') as file:
    d = pickle.load(file)
def get_key(d, value):
    for k, v in d.items():
        if v == value:

            return k
print("Введите фразу")
s = tuple(input().lower().split())
print("Сколько слов вывести?")
count = int(input())
ls = list()
for i in range(len(s)):
    if d.get(s, False) != False:
        x = d.get(s)
        break
    else:
        list1 = list(s)
        s = tuple(list1[i+1:])
sorted_x = dict(sorted(x.items(), key=lambda item: item[1]))
for i in sorted_x:
    ls.append(sorted_x.get(i))
lss = list(reversed(ls))
for i in range(len(lss)):
    if count == i:
        break
    print(get_key(sorted_x,lss[i]))
    sorted_x.pop(get_key(sorted_x,lss[i]))


