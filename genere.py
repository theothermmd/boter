import json

with open("ganres.json", "r", encoding="utf-8") as ganres:
    ganres_S = json.load(ganres)


ls : list = []
for i in ganres_S :
    ls.append({'name' : i['slug'] , 'id' : i['id']})





with open('ngr.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(ls, ensure_ascii=False))