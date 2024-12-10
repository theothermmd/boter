import json , requests


def getAllTitles_series() -> None :
    print("Downloading...")
    request_getAllTitles = requests.get( "https://seeko.film/api/v1/get/getAllTitles?f_type=series", headers={'Accept': 'application/json'})

    request_getAllTitles_json = request_getAllTitles.json()

    request_getAllTitles_json_final : list = request_getAllTitles_json['data']['all_titles']['data']

    with open('movie_data_series.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json_final, ensure_ascii=False))
    print("Download completed.")

    
getAllTitles_series()