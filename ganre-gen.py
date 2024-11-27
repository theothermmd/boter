import json





with open("movie_data_movie.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load_m:
    request_getAllTitles_json_file_m = json.load(request_getAllTitles_json_final_load_m)

ganres = []
for i in request_getAllTitles_json_file_m :
    for j in i['genre'].split(",") :
        if j not in ganres :
            ganres.append(j)
            

with open("movie_data_series.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load_s:
    request_getAllTitles_json_file_s = json.load(request_getAllTitles_json_final_load_s)


for i in request_getAllTitles_json_file_s :
    for j in i['genre'].split(",") :
        if j not in ganres :
            ganres.append(j)



x = {'ganres' : ganres}
with open('ganres.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( x, ensure_ascii=False))