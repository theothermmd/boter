import json
ls = []
with open("movie_data_series_new.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load(request_getAllTitles_json_final_load)

with open("file.txt", "r", encoding="utf-8") as file:

    for line in file:

        for i in request_getAllTitles_json_file :
            if i['series_name_fa'] == line.strip() :
                if not any(item['id'] == i['series_id'] for item in ls) :
                    ls.append({'id': i['series_id'] , 'name': i['series_name_fa'] })


with open('iddddddddddd.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(ls, ensure_ascii=False))