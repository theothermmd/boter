import requests , json
from data import bearer_token
# اطلاعات
api_url_genre = "https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/genre"  


with open("ganres.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load_m:
    request_getAllTitles_json_file_m = json.load(request_getAllTitles_json_final_load_m)

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

for i in request_getAllTitles_json_file_m['ganres'] :
    genre_data = {
        "name": i 
    }

    response = requests.post(api_url_genre, headers=headers, json=genre_data)

    if response.status_code == 201:
        print("Genre created successfully")
    else:
        print("Error creating genre:", response.status_code, response.text)
