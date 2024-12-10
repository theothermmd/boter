import requests
import json
import os
from libs.func import  get_yearr , get_year_as_list , media_gen , get_ganres , get_genres_as_list , get_country_as_list, get_series_data
from io import BytesIO
from tqdm import tqdm
from colorama import Fore, Style
ers = {}
err_total = []
count = 0
apikeys = ['6273c114'  , '42a575eb' , "7dd47dfa" , "57ebdc94"]
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL21vdmllcGl4LmlyIiwiaWF0IjoxNzMzNzQzMDQ2LCJuYmYiOjE3MzM3NDMwNDYsImV4cCI6MTczNjMzNTA0NiwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.3nhDfqRZ7BbdCg7cCcO1j_uBvR4LcO3j5LqEswO5gX0"
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
categories =  { "animation": 8852 , "irani_berooz": 8899 , "irani": 8851 , "dubble": 8 , "zirnevis": 8791 }

score =  { "۰ تا ۲": 145 , "۲ تا ۵": 146 , "۵ تا ۷": 147 , "بالای ۷": 148 }
rate = { "G": 4082 , "PG": 8900 , "PG-13": 8901 , "R": 136 }



with open("series.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load( request_getAllTitles_json_final_load)['data']


y = {"erros_name_movie": []}

years = get_year_as_list()
genres_list = get_genres_as_list()

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

        except :
            err_total.append(movie['id'])
            with open('errors_total.json', "r", encoding="utf-8") as request_getAllTitles_json_final_load3:
                errors_total = json.load( request_getAllTitles_json_final_load3)

            errors_total.append(movie['id'])

            with open('errors_total.json', 'w', encoding='UTF-8') as file:
                file.write(json.dumps(errors_total, ensure_ascii=False))


            progress_bar.update(1)
            continue

        if movie_data['dl_datials']['sub_links']['dl_480']['size'] == "" and movie_data['dl_datials']['dub_links']['dl_480']['size'] == "":
            continue
        poster = media_gen( poster_url=movie_data['cdn_poster'] , poster_name=movie_data['poster'] )
        headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
        if poster['status'] == True:

            backdrop = media_gen( poster_url=movie_data['cdn_backdrop'] , poster_name=movie_data['backdrop'] )
            if backdrop['status'] == True:

                
                categorie = [] 
                if movie_data['isirani'] == 1:
                    categorie.append(categories['irani'])
                else:
                    if movie_data['isdoubble'] == 1:
                        if "Animation" in movie_data['genre']:
                            categorie.append(categories['animation'])
                        else:
                            if movie_data['isdoubble'] == 1 and movie_data['sub'] : 
                                categorie.append(categories['dubble'])
                                categorie.append(categories['zirnevis'])
                            else :
                                if movie_data['isdoubble'] == 1 :
                                    categorie.append(categories['dubble'])
                    else:
                        if movie_data['isdoubble'] == 0 and movie_data['dl_datials']['sub_links']['dl_480']['size'] != "":
                            if "Animation" in movie_data['genre']:
                                categorie.append(categories['animation'])
                            else:
                                categorie.append(categories['zirnevis'])



                rate = []
                if movie_data['age'] == "G" :
                    rate.append(4082)
                elif movie_data['age'] == "PG" : 
                    rate.append(8900)
                elif movie_data['age'] == "PG-13" :  
                    rate.append(8901)
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

                lang = ''
                if movie_data['isirani'] == 1 and movie_data['dl_datials']['sub_links']['dl_480']['size'] == "":
                    lang = "فارسی"
                elif movie_data['isdoubble'] == 1 and movie_data['dl_datials']['sub_links']['dl_480']['size'] == "" and movie_data['isirani'] == 0 :
                     lang = "دوبله فارسی"
                elif movie_data['isirani'] == 0 and movie_data['isdoubble'] == 0 and movie_data['dl_datials']['dub_links']['dl_480']['size'] == "":
                    lang = "زبان اصلی با زیرنویس فارسی"
                elif movie_data['dl_datials']['sub_links']['dl_480']['size'] != "" and movie_data['dl_datials']['dub_links']['dl_480']['size'] != "":
                    lang = "دوبله فارسی + زبان اصلی"

                genres = [] 
                for i in str(movie_data['genre']).split(",") :
                        
                        if i != "" :
                            ls = get_ganres(i.strip() , genres_list)

                            if ls['flag'] == True :
                                    genres_list.append({'name' : ls['name'] , 'id' : ls['id']})

                            genres.append(ls['id'])
  
   
                countryyy = ''
                if movie_data['isirani'] != 1 : 
                     countryyy = "" 
                else :
                    countryyy = "محصول کشور ایران"
                if lang == "فارسی" :
                    lang = "زبان فارسی"
                genres_ls = movie_data['genre']
                about = f"{"سریال"} {movie_data['name_fa']} {countryyy} در ژانر {genres_ls} که در سال {str(movie_data['year'])} ساخته شده است. شما میتوانید به انتخاب خودتان این {"سریال"} را با {lang} با بهترین کیفیت دانلود و یا به صورت آنلاین از مووی پیکس تماشا کنید."
                if lang == "زبان فارسی" :
                    lang = "فارسی"
  
                send_data = {
                        "yearr": [get_yearr(str(movie_data['year']) , years)['id']],
                        "type_of_post": [ 48 ],
                        "title": movie_data['name_fa'],
                        "content": "",
                        "country": [117] if movie_data['isirani'] == 1 else [] ,
                        "status": "publish",
                        "score": scorex,
                        "rate" :  rate,
                        "genre" : genres,
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
                                "url": f"https://moviepix.ir/wp-content/uploads/2024/11/{backdrop['media_name']}",
                                "link": f"https://moviepix.ir/tt1535108/{backdrop['media_name']}",
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
                                "icon": "https://moviepix.ir/wp-includes/images/media/default.png",
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
                            "categories": categorie,
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
                        response = requests.post( "https://moviepix.ir/wp-json/wp/v2/posts", json=send_data, headers=headers, timeout=120)
                        break
                    except:
                        y['erros_name_movie'].append(movie_data['name_fa'])
                        continue
                
                if response.status_code == 200 or response.status_code == 201:
                    post_id = response.json()["id"]
                    for attempt in range(3):
                        try:
                            response = requests.put(f"https://moviepix.ir/wp-json/wp/v2/posts/{post_id}", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, json={"categories": categorie}, timeout=30)
                            break
                        except:
                            y['erros_name_movie'].append( movie_data['name_fa'])
                            continue
                    if response.status_code == 200:

                        db_post_backdrop['data'].append( {movie_data['id']:  {"post_id": post_id, "poster_id": poster['media_id']}})
 
                        for attempt in range(3):
                            try:
                                response = requests.put(f"https://moviepix.ir/wp-json/wp/v2/posts/{post_id}", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, json= { "acf": {"serial-dl": movie_data['serialdl'] }}, timeout=120)
                                break
                            except :
                                continue
                        ers[movie_data['name']] = movie_data['erros']
                        progress_bar.update(1)
                else:
                    print("Failed to update post:", response.text)
            else:
                 print("Error:", response.status_code, response.text)


with open('errors.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(y, ensure_ascii=False))

with open('poster.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(db_post_backdrop, ensure_ascii=False))
