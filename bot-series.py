import requests
import json
import os
from libs.func import  get_year , get_years_as_list , media_gen , get_genre , get_genres_as_list , get_series_data
from io import BytesIO
from tqdm import tqdm
from colorama import Fore, Style
ers = {}
err_total = []
count = 0
apikeys = ['6273c114'  , '42a575eb' , "7dd47dfa" , "57ebdc94"]
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2NhcnRvb25mbGl4LmlyIiwiaWF0IjoxNzM0Mzc5NjE1LCJuYmYiOjE3MzQzNzk2MTUsImV4cCI6MTczNjk3MTYxNSwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMTk1In19fQ.Ntq6LW-DQBgO_3NGFx-8IMkOiA8rWkX369IUUZt6Le0"
cdn : dict = {
    "poster": "https://s35.upera.net/thumb?w=675&h=1000&q=90&src=https://s35.upera.net/s3/posters/",
    "backdrop": "https://s35.upera.net/thumb?w=764&h=400&q=100&src=https://s35.upera.net/s3/backdrops/",
    "lg_poster": "https://s35.upera.net/thumb?w=675&h=1000&q=90&src=https://s35.upera.net/s3/posters/",
    "lg_backdrop": "https://s35.upera.net/thumb?w=764&h=400&q=100&src=https://s35.upera.net/s3/backdrops/",
    "md_poster": "https://s35.upera.net/thumb?w=337&h=500&q=90&src=https://s35.upera.net/s3/posters/",
    "md_backdrop": "https://s35.upera.net/thumb?w=382&h=200&q=90&src=https://s35.upera.net/s3/backdrops/",
    "sm_poster": "https://s35.upera.net/thumb?w=225&h=333&q=90&a=t&src=https://s35.upera.net/s3/posters/",
    "sm_backdrop": "https://s35.upera.net/thumb?w=191&h=100&q=90&src=https://s35.upera.net/s3/backdrops/"
}
ref: int = 5198534
categories =  { "animation": 2572 , "anime": 2710 , "seriali": 8 }

score =  { "۰ تا ۲": 145 , "۲ تا ۵": 146 , "۵ تا ۷": 147 , "بالای ۷": 148 }
rate = { "G": 2577 , "PG": 138 , "PG-13": 137 , "R": 136 }

genre_a = [
  { "name": "action", "id": 53 },
  { "name": "animation", "id": 1703 },
  { "name": "horror", "id": 2253 },
  { "name": "crime", "id": 315 },
  { "name": "family", "id": 57 },
  { "name": "drama", "id": 244 },
  { "name": "sci-fi", "id": 535 },
  { "name": "fantasy", "id": 2252 },
  { "name": "comedy", "id": 55 },
  { "name": "short", "id": 68 },
  { "name": "adventure", "id": 56 },
  { "name": "mystery", "id": 2395 },
  { "name": "musical", "id": 67 },
  { "name": "thriller", "id": 54 }
]


with open("iddddddddddd.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load( request_getAllTitles_json_final_load)


y = {"erros_name_movie": []}

years = get_years_as_list()


db_post_backdrop = {"data": []}

rev = request_getAllTitles_json_file

total_items = len(request_getAllTitles_json_file)

with tqdm(total=total_items, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%] Remaining: {remaining}", colour="blue", dynamic_ncols=True, miniters=1) as progress_bar:
    progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")
    
    for movie in rev:
        count += 1
        if count == 4 :
            count = 0
        try :
            movie_data = get_series_data(movie['id'])

            if movie_data == None :

                with open('errors_total_none.json', "r", encoding="utf-8") as request_getAllTitles_json_final_load3:
                    errors_total_none = json.load( request_getAllTitles_json_final_load3)

                errors_total_none.append(movie['id'])

                with open('errors_total_none.json', 'w', encoding='UTF-8') as file:
                    file.write(json.dumps(errors_total_none, ensure_ascii=False))
                progress_bar.update(1)
                continue

            if movie_data['erros'] != [] :
                with open('errors_eisodes_nazashte.json', "r", encoding="utf-8") as request_getAllTitles_json_final_load4:
                        errors_nazade = json.load( request_getAllTitles_json_final_load4)

                errors_nazade.append(movie_data['erros'])
                
                with open('errors_eisodes_nazashte.json', 'w', encoding='UTF-8') as file:
                    file.write(json.dumps(errors_nazade, ensure_ascii=False))

        except:
            err_total.append(movie['id'])
            with open('errors_total.json', "r", encoding="utf-8") as request_getAllTitles_json_final_load3:
                errors_total = json.load( request_getAllTitles_json_final_load3)

            errors_total.append(movie['id'])

            with open('errors_total.json', 'w', encoding='UTF-8') as file:
                file.write(json.dumps(errors_total, ensure_ascii=False))


            progress_bar.update(1)
            continue

        if movie_data['dl_datials']['sub_links']['dl_480']['size'] == "" and movie_data['dl_datials']['dub_links']['dl_480']['size'] == "" or movie_data['isdoubble'] == 0:
            progress_bar.update(1)
            continue
        poster = media_gen( poster_url=movie_data['cdn_poster'] , poster_name=movie_data['poster'] )
        headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }

        if poster['status'] == True:

            backdrop = media_gen( poster_url=movie_data['cdn_backdrop'] , poster_name=movie_data['backdrop'] )
            if backdrop['status'] == True:

            



                rate = []
                if movie_data['age'] == "G" :
                    rate.append(2577)
                elif movie_data['age'] == "PG" : 
                    rate.append(138)
                elif movie_data['age'] == "PG-13" :  
                    rate.append(137)
                elif movie_data['age'] == "R" : 
                    rate.append(136)

                scorex = []
                if 0 <= movie_data['rate'] < 2 :
                    scorex.append(145)
                elif 2 <= movie_data['rate'] < 5 :
                    scorex.append(146)
                elif 5 <= movie_data['rate'] < 7 :
                    scorex.append(147) 
                elif movie_data['rate'] > 7 :
                    scorex.append(148)
    
                quality_meta = ""
                if movie_data['dl_datials']['sub_links']['dl_BLURAY']['size'] != "" or movie_data['dl_datials']['dub_links']['dl_BLURAY']['size'] != "":  
                    quality_meta = 'Bluray'
                else :
                    if movie_data['dl_datials']['sub_links']['dl_1080']['size'] != "" or movie_data['dl_datials']['dub_links']['dl_1080']['size'] != "":
                        quality_meta = "Full HD"
                    else :
                        if movie_data['dl_datials']['sub_links']['dl_720']['size'] != "" or movie_data['dl_datials']['dub_links']['dl_720']['size'] != "":
                            quality_meta = "HD"
                        else :
                            if movie_data['dl_datials']['sub_links']['dl_480']['size'] != "" or movie_data['dl_datials']['dub_links']['dl_480']['size'] != "":
                                quality_meta = "SD"


                lang = "دوبله فارسی"

                genres = [] 
                for i in str(movie_data['genre']).split(",") :
                        if any(item['name'] == str(i).lower() for item in genre_a) :
                            for j in genre_a :
                                if j['name'] == str(i).lower() :
                                    genres.append(j['id'])
  
   
                countryyy = ''
                if movie_data['isirani'] != 1 : 
                     countryyy = "" 
                else :
                    countryyy = "محصول کشور ایران"

                genres_ls = movie_data['genre']

                about = f"{"سریال"} {movie_data['name_fa']} {countryyy} در ژانر {genres_ls} که در سال {str(movie_data['year'])} ساخته شده است. شما میتوانید به انتخاب خودتان این {"سریال"} را با {lang} با بهترین کیفیت دانلود و یا به صورت آنلاین از مووی پیکس تماشا کنید."
                send_data = {
                        "yearr": [get_year(str(movie_data['year']) , years)['id']],
                        "type_of_post": [ 48 ],
                        "title": movie_data['name_fa'],
                        "content": "",
                        "country": [117] if movie_data['isirani'] == 1 else [] ,
                        "status": "publish",
                        "score": scorex,
                        "rate" :  rate,
                        "genre" : genres,
                        "categories" : [8],
                        "acf": {
                            "Language" : lang,
                            "about" : about,
                            "quality-meta" : quality_meta,
                            "en_title" : movie_data['name'],
                            "slider_image2": {
                                "ID": backdrop['media_id'],
                                "id": backdrop['media_id'],
                                "title": "hello",
                                "filename": backdrop['media_name'],
                                "filesize": 397067,
                                "url": f"https://cartoonflix.ir/wp-content/uploads/2024/11/{backdrop['media_name']}",
                                "link": f"https://cartoonflix.ir/tt1535108/{backdrop['media_name']}",
                                "alt": "",
                                "author": "2",
                                "description": "",
                                "caption": "",
                                "name": backdrop['media_name'],
                                "status": "inherit",
                                "uploaded_to": 4320,
                                "date": "2024-11-08 15:44:48",
                                "modified": "2024-11-08 15:44:48",
                                "menu_order": 0,
                                "mime_type": "image/jpeg",
                                "type": "image",
                                "subtype": "jpeg",
                                "icon": "https://cartoonflix.ir/wp-includes/images/media/default.png",
                                "width": 1920,
                                "height": 1080,

                            },
                            "post-type": "series",
                            "released": movie_data['year'],
                            "imdbRating": movie_data['rate'],
                            "time": f"{movie_data['runtime']} دقیقه",
                            "story": movie_data['overview_fa'],
                            "en_title": movie_data['name'],
                            "persian-doble": True if movie_data['isdoubble'] == 1 and movie_data['isirani'] == 0 else False,
                            "censored": True if movie_data['isirani'] == 0 else False,
                            "playonline": True,
                            "def-version": True if movie_data['sub'] == True else False,
                            "slider": False,
                            "legal": False,
                            "custom-badge": "",
                            "top-250-imdb": False,
                            "top-250-series": False,
                            "rel_date": "",
                            "imdbVotes": "",
                            "malRating": "",
                            "malVotes": "",
                            "Awards": "",
                            "Writer": "",
                            "update_info": "",
                            "air_status": "",
                            "mal_id": "",
                            "save_images": True,
                            "dontSave_actors": False,
                            "slider-badge": "",
                            "slider-badge-color": "red",
                            "film_logo": False,
                            "slider_button": "تماشای فیلم",
                            "serial-jadval": False,
                            "cover-trailer": False,
                            "trailer": "",
                            "gallery": False,
                            "internet": "",
                            "mobile_1080": "",
                            "mobile_720": "",
                            "mobile_480": "",
                            "mobile_subtitle": "",
                            "slider_image": False,
                            "related_blog_post": False,
                            "collection_id": False,
                            "mobile_slider_tiwix": False,
                            "rotten": "",
                            "metacritic": "",
                            "imdb": "",
                            "imdb-id": "",
                            "actors": False,
                            "director": False

                        },
                        "featured_media": poster['media_id']

                    }

                




                for attempt in range(3):
                        try:
                            response = requests.post( "https://cartoonflix.ir/wp-json/wp/v2/posts", json=send_data, headers=headers, timeout=40)
                            break
                        except:
                            continue
                if response.status_code == 400 :
                        with open('errorssssssssssssssssssssssssssssss.json', 'w', encoding='UTF-8') as file:
                            file.write(json.dumps(response.json(), ensure_ascii=False))
                if response.status_code == 200 or response.status_code == 201:
                        post_id = response.json()["id"]
                        for attempt in range(3):
                            try:
                                response = requests.put(f"https://cartoonflix.ir/wp-json/wp/v2/posts/{post_id}", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, json={"genre" : genres}, timeout=40)
                                break
                            except:
                                continue
      
                        if response.status_code == 200:

                            db_post_backdrop['data'].append( {movie_data['id']:  {"post_id": post_id, "poster_id": poster['media_id']}})
    
                            for attempt in range(5):
                                try:
                                    response = requests.put(f"https://cartoonflix.ir/wp-json/wp/v2/posts/{post_id}", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, json= { "acf": {"serial-dl": movie_data['serialdl'] }}, timeout=240)
                                    if response.status_code == 200 :
                                        break
                                    else :
                                        continue
                                except :
                                    continue
                                
                            ers[movie_data['name']] = movie_data['erros']
                            progress_bar.update(1)
                else:
                        print("Failed to update post:", response.text)



with open('errors.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(y, ensure_ascii=False))

with open('poster.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(db_post_backdrop, ensure_ascii=False))
