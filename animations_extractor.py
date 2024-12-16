import json


with open("movie_data_series_new.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load(request_getAllTitles_json_final_load)
with open("post-db_cartoon_flix.json", "r", encoding="utf-8") as names_db:
    names_db_s = json.load(names_db)

ls = []
for i in request_getAllTitles_json_file :
    if "Animation" in i['genre'] :
        for j in str(i['genre']).split(",") :
            if j not in ls :
                ls.append(j)


with open('naes_animations.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(ls, ensure_ascii=False))