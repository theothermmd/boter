import requests
from data import bearer_token
# اطلاعات
api_url_genre = "https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/genre"


headers = {
    "Authorization": f"Bearer {bearer_token}"
}


genre_name = "اکشن"


response = requests.get(api_url_genre, headers=headers, params={"search": genre_name})

if response.status_code == 200:
    genres = response.json()
    if genres:
        genre_id = genres[0]["id"]  
        print(f"Genre ID for '{genre_name}': {genre_id}")
    else:
        print(f"No genre found for name: {genre_name}")
else:
    print("Error fetching genres:", response.status_code, response.text)
