from collections import defaultdict
import re
import pickle
print("Введите асолютный путь файла для обучения")
s=input()

try:
    with open('model.pkl', 'rb') as file:
        f=pickle.load(file)
        sl=defaultdict(dict,f)
except:
    sl=defaultdict(dict)
with open(s, encoding='utf-8') as a:
    stroka=''
    for c in a:
        stroka+=c.strip().lower()
    result = re.split(r'\s*[?,!–().;]\s*', stroka)
    for c in result:
        g=re.split(r'\s*[,: -]\s*', c)
        g=list(map(lambda x: x.lower(), g))
        for j in range(len(g)-1):
            for i in range(j+1,len(g)):
                tup=tuple(g[j:i])
                if g[i] in sl[tup].keys():
                    sl[tup][g[i]]+=1
                else:
                    sl[tup][g[i]]=1
with open('model.pkl', 'wb') as basa:
    sl=dict(sl)
    pickle.dump(sl, basa)
