import re
import pickle
from collections import defaultdict
print("Введите абсолютный путь файла для обучения")
s = input()
try:
    with open('model.pkl', 'rb') as file:
        f = pickle.load(file)
        sl = defaultdict(dict,f)
except:
    sl = defaultdict(dict)
with open(s, encoding='utf-8') as a:
    stroka = ''
    for c in a:
        stroka += c.strip().lower()
    result = re.split(r'\s*[?,!–().;]\s*', stroka)
    for i in result:
        vesss = re.split(r'\s*[,: -]\s*', i)
        vesss = list(map(lambda x: x.lower(), vesss))
        for j in range(len(vesss)-1):
            for i in range(j+1,len(vesss)):
                tup=tuple(vesss[j:i])
                if vesss[i] in sl[tup].keys():
                    sl[tup][vesss[i]] += 1
                else:
                    sl[tup][vesss[i]] = 1
with open('model.pkl', 'wb') as basa:
    sl = dict(sl)
    pickle.dump(sl, basa)
print(sl)
