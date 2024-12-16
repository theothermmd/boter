
import requests , json

request_getAllTitles = requests.get( "https://seeko.film/api/v1/ghost/get/series/f1aeb720-4758-11ed-8a9b-55c1b877ca6e?affiliate=1", headers={'Accept': 'application/json'})

request_getAllTitles_json = request_getAllTitles.json()







with open('test555555555555.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json, ensure_ascii=False))