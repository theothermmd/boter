import json


with open("movie_data_series.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load(request_getAllTitles_json_final_load)[::-1]



ls = {'data' : []}

for i in request_getAllTitles_json_file :
    if i['series_name_fa'] not in ls and i['series_name'] not in ls:
        ls['data'].append({"name" : i['series_name'] , "id": i['series_id']})



seen_series = set()
filtered_data = []

for item in ls["data"]:
    if item["name"] not in seen_series:
        filtered_data.append({
            "name": item["name"], 
            "id": item["id"]
        })
        seen_series.add(item["name"])

# ساخت دیکشنری نهایی
result = {"data": filtered_data}

with open('series.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))