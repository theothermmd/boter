import requests
import json
import os
from libs.func import getAllTitles_movie, get_movie_data , get_yearr , get_year_as_list , media_gen , get_ganres , get_country ,   get_genres_as_list , get_country_as_list
from io import BytesIO
from tqdm import tqdm
from colorama import Fore, Style
count = 0
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3ZvZC50YXJpbmV0LmlyIiwiaWF0IjoxNzMzMTY0ODg2LCJuYmYiOjE3MzMxNjQ4ODYsImV4cCI6MTczMzc2OTY4NiwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.c1NIRwSq2rmFeIZ-OBS7hu32TuD1GwSqwUVPPCVB3To"
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
categories =  { "animation": 8775 , "irani_berooz": 8898 , "irani": 7558 , "dubble": 6 , "zirnevis": 2572 }

score =  { "۰ تا ۲": 145 , "۲ تا ۵": 146 , "۵ تا ۷": 147 , "بالای ۷": 148 }
rate = { "G": 4082 , "PG": 8900 , "PG-13": 8901 , "R": 136 }


if not os.path.isfile('movie_data_movie.json'): getAllTitles_movie()

with open("movie_data_movie.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load( request_getAllTitles_json_final_load)


y = {"erros_name_movie": []}

years = get_year_as_list()
countrys_list = get_country_as_list()
genres_list = get_genres_as_list()

db_post_backdrop = {"data": []}

rev = request_getAllTitles_json_file[::-1]

total_items = len(request_getAllTitles_json_file)

with tqdm(total=total_items, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%] Remaining: {remaining}", colour="blue", dynamic_ncols=True, miniters=1) as progress_bar:
    progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")
    
    for movie in rev:
        try :
            movie_data = get_movie_data(movie)
        except :
            print("error")
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

                country = []
                apikeys = ['8812c608' , '6273c114' , '8812c608' , '42a575eb' , '54a50e39']
                apikey = apikeys[count]
                if movie_data['isirani'] != 1 and movie_data['imdb'] != None and movie_data['imdb'] != "" :
                    for attempt in range(3):
                        try:
                            imdb_data = requests.get( f"http://www.omdbapi.com/?i={movie_data['imdb']}&apikey={apikey}", headers=headers, timeout=30).json()
                            if "Error" in imdb_data:
                                count += 1
                                continue
                            break
                        except:
                            continue
                    try :
                            if imdb_data['Country'] != "N/A" :
                                if "," in imdb_data['Country'] :
                                    
                                    for i in str(imdb_data['Country']).split(",") :
                                        ls = get_country(i.strip() , countrys_list)

                                        if ls['flag'] == True :
                                            countrys_list.append({'name' : ls['name'] , 'id' : ls['id']})

                                        country.append(ls['id'])

                                else :
                                    country.append(get_country(str(imdb_data['Country']) , countrys_list)['id'])
                    except :
                            country = []
                            
                    
                else :
                    country.append(117)

                film_dl = []

                if movie_data['sub'] == False and movie_data['isdoubble'] == 1 :
                    film_dl = [
                                {
                                    "farsi-doble": "yes",
                                    "farsi-doble-link": "",
                                    "film_info": "",
                                    "is_free": False,
                                    "subtitle-film": "",
                                    "online_link": movie_data['dl_datials']['dub_links']['dl_HLS']['dl_lnk'],
                                    "online_link_480": "",
                                    "online_link_720": "",
                                    "online_link_1080": "",
                                    "subtitle_online_film": "",

                                    "film-dl-link": [
                                        {
                                            "quality-film-select": "480p",
                                            "quality-film": "480p",
                                            "size-film": movie_data['dl_datials']['dub_links']['dl_480']['size'],
                                            "dl-film-link": movie_data['dl_datials']['dub_links']['dl_480']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "720p",
                                            "quality-film": "720p",
                                            "size-film": movie_data['dl_datials']['dub_links']['dl_720']['size'],
                                            "dl-film-link": movie_data['dl_datials']['dub_links']['dl_720']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "1080p",
                                            "quality-film": "1080p",
                                            "size-film": movie_data['dl_datials']['dub_links']['dl_1080']['size'],
                                            "dl-film-link": movie_data['dl_datials']['dub_links']['dl_1080']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "1080p_HQ",
                                            "quality-film": "1080p_HQ",
                                            "size-film": movie_data['dl_datials']['dub_links']['dl_HQ_1080']['size'],
                                            "dl-film-link": movie_data['dl_datials']['dub_links']['dl_HQ_1080']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "BluRay",
                                            "quality-film": "BluRay",
                                            "size-film": movie_data['dl_datials']['dub_links']['dl_BLURAY']['size'],
                                            "dl-film-link": movie_data['dl_datials']['dub_links']['dl_BLURAY']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        }
                                    ]
                                }
                            ]  
                elif  movie_data['sub'] == True and movie_data['isdoubble'] == 1 :
                    film_dl = [
                                        {
                                            "farsi-doble": "yes",
                                            "farsi-doble-link": "",
                                            "film_info": "نسخه دوبله فارسی",
                                            "is_free": False,
                                            "subtitle-film": "",
                                            "online_link": movie_data['dl_datials']['dub_links']['dl_HLS']['dl_lnk'],
                                            "online_link_480": "",
                                            "online_link_720": "",
                                            "online_link_1080": "",
                                            "subtitle_online_film": "",
                                            "film-dl-link": [
                                            {
                                                "quality-film-select": "480p",
                                                "quality-film": "480p",
                                                "size-film": movie_data['dl_datials']['dub_links']['dl_480']['size'],
                                                "dl-film-link": movie_data['dl_datials']['dub_links']['dl_480']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "720p",
                                                "quality-film": "720p",
                                                "size-film": movie_data['dl_datials']['dub_links']['dl_720']['size'],
                                                "dl-film-link": movie_data['dl_datials']['dub_links']['dl_720']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "1080p",
                                                "quality-film": "1080p",
                                                "size-film": movie_data['dl_datials']['dub_links']['dl_1080']['size'],
                                                "dl-film-link": movie_data['dl_datials']['dub_links']['dl_1080']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "1080p_HQ",
                                                "quality-film": "1080p_HQ",
                                                "size-film": movie_data['dl_datials']['dub_links']['dl_HQ_1080']['size'],
                                                "dl-film-link": movie_data['dl_datials']['dub_links']['dl_HQ_1080']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "BluRay",
                                                "quality-film": "BluRay",
                                                "size-film": movie_data['dl_datials']['dub_links']['dl_BLURAY']['size'],
                                                "dl-film-link": movie_data['dl_datials']['dub_links']['dl_BLURAY']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            }
                                            ]
                                        },
                                        {
                                            "farsi-doble": "no",
                                            "farsi-doble-link": "",
                                            "film_info": "نسخه زیرنویس فارسی",
                                            "is_free": False,
                                            "subtitle-film": "",
                                            "online_link": movie_data['dl_datials']['sub_links']['dl_480']['dl_lnk'],
                                            "online_link_480": "",
                                            "online_link_720": "",
                                            "online_link_1080": "",
                                            "subtitle_online_film": "",
                                            "film-dl-link": [
                                            {
                                                "quality-film-select": "480p",
                                                "quality-film": "480p",
                                                "size-film": movie_data['dl_datials']['sub_links']['dl_480']['size'],
                                                "dl-film-link": movie_data['dl_datials']['sub_links']['dl_480']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "720p",
                                                "quality-film": "720p",
                                                "size-film": movie_data['dl_datials']['sub_links']['dl_720']['size'],
                                                "dl-film-link": movie_data['dl_datials']['sub_links']['dl_720']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "1080p",
                                                "quality-film": "1080p",
                                                "size-film": movie_data['dl_datials']['sub_links']['dl_1080']['size'],
                                                "dl-film-link": movie_data['dl_datials']['sub_links']['dl_1080']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "1080p_HQ",
                                                "quality-film": "1080p_HQ",
                                                "size-film": movie_data['dl_datials']['sub_links']['dl_HQ_1080']['size'],
                                                "dl-film-link": movie_data['dl_datials']['sub_links']['dl_HQ_1080']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            },
                                            {
                                                "quality-film-select": "BluRay",
                                                "quality-film": "BluRay",
                                                "size-film": movie_data['dl_datials']['sub_links']['dl_BLURAY']['size'],
                                                "dl-film-link": movie_data['dl_datials']['sub_links']['dl_BLURAY']['dl_lnk'],
                                                "version": "",
                                                "film-price": "",
                                                "dl_row_info": ""
                                            }
                                            ]
                                        }
                                        ]
                elif movie_data['sub'] == True and movie_data['isdoubble'] == 0 :  

                    film_dl = [
                                {
                                    "farsi-doble": "no",
                                    "farsi-doble-link": "",
                                    "film_info": "",
                                    "is_free": False,
                                    "subtitle-film": "",
                                    "online_link": movie_data['dl_datials']['sub_links']['dl_HLS']['dl_lnk'],
                                    "online_link_480": "",
                                    "online_link_720": "",
                                    "online_link_1080": "",
                                    "subtitle_online_film": "",

                                    "film-dl-link": [
                                        {
                                            "quality-film-select": "480p",
                                            "quality-film": "480p",
                                            "size-film": movie_data['dl_datials']['sub_links']['dl_480']['size'],
                                            "dl-film-link": movie_data['dl_datials']['sub_links']['dl_480']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "720p",
                                            "quality-film": "720p",
                                            "size-film": movie_data['dl_datials']['sub_links']['dl_720']['size'],
                                            "dl-film-link": movie_data['dl_datials']['sub_links']['dl_720']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "1080p",
                                            "quality-film": "1080p",
                                            "size-film": movie_data['dl_datials']['sub_links']['dl_1080']['size'],
                                            "dl-film-link": movie_data['dl_datials']['sub_links']['dl_1080']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "1080p_HQ",
                                            "quality-film": "1080p_HQ",
                                            "size-film": movie_data['dl_datials']['sub_links']['dl_HQ_1080']['size'],
                                            "dl-film-link": movie_data['dl_datials']['sub_links']['dl_HQ_1080']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        },
                                        {
                                            "quality-film-select": "BluRay",
                                            "quality-film": "BluRay",
                                            "size-film": movie_data['dl_datials']['sub_links']['dl_BLURAY']['size'],
                                            "dl-film-link": movie_data['dl_datials']['sub_links']['dl_BLURAY']['dl_lnk'],
                                            "version": "",
                                            "film-price": "",
                                            "dl_row_info": ""
                                        }
                                    ]
                                }
                            ]  
                    

                type_file = ""
                if categories['animation'] in categorie :
                    type_file = "انیمیشن"
                else :
                    type_file = "فیلم"
                countryyy = ''
                if movie_data['isirani'] != 1 and movie_data['imdb'] != None and movie_data['imdb'] != "": 
                    try :
                        if imdb_data['Country'] != "N/A" :
                            countryyy = imdb_data['Country'] 
                    except :
                        countryyy = "نامشخص" 
                else :
                    countryyy = "ایران"
                if lang == "فارسی" :
                    lang = "زبان فارسی"
                genres_ls = movie_data['genre']
                about = f"{type_file} {movie_data['name_fa']} محصول کشور {countryyy} در ژانر {genres_ls} که در سال {str(movie_data['year'])} ساخته شده است. شما میتوانید به انتخاب خودتان این {type_file} را با {lang} با بهترین کیفیت دانلود و یا به صورت آنلاین از مووی پیکس تماشا کنید."
                if lang == "زبان فارسی" :
                    lang = "فارسی"
                send_data = {
                        "yearr": [get_yearr(str(movie_data['year']) , years)['id']],
                        "type_of_post": [ 995 ],
                        "title": movie_data['name_fa'],
                        "content": "",
                        "country": country,
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
                                "url": f"https://vod.tarinet.ir/wp-content/uploads/2024/11/{backdrop['media_name']}",
                                "link": f"https://vod.tarinet.ir/tt1535108/{backdrop['media_name']}",
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
                                "icon": "https://vod.tarinet.ir/wp-includes/images/media/default.png",
                                "width": 1920,
                                "height": 1080,

                            },
                            "post-type": "film",
                            "released": movie_data['year'],
                            "imdbRating": movie_data['rate'],
                            "time": f"{movie_data['runtime']} دقیقه",
                            "imdb": movie_data['imdb'],
                            "story": movie_data['overview_fa'],
                            "imdb-id": movie_data['imdb'],
                            "en_title": movie_data['name'],
                            "persian-doble": True if movie_data['isdoubble'] == 1 and movie_data['isirani'] == 0 else False,
                            "mobile_online": movie_data['dl_datials']['dub_links']['dl_HLS']['dl_lnk'] if movie_data['dl_datials']['dub_links']['dl_HLS']['dl_lnk'] != "" else movie_data['dl_datials']['sub_links']['dl_480']['dl_lnk'],
                            "categories": categorie,
                            "censored": True if movie_data['isirani'] == 0 else False,
                            "playonline": True,
                            "def-version": True if movie_data['sub'] == True else False,
                            "film-dl": film_dl,
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

                        },
                        "featured_media": poster['media_id']

                    }

            for attempt in range(3):
                try:
                    response = requests.post( "https://vod.tarinet.ir/wp-json/wp/v2/posts", json=send_data, headers=headers, timeout=20)
                    break
                except:
                    y['erros_name_movie'].append(movie_data['name_fa'])
                    continue
            if response.status_code == 200 or response.status_code == 201:
                post_id = response.json()["id"]
                for attempt in range(3):
                    try:
                        response = requests.post(f"https://vod.tarinet.ir/wp-json/wp/v2/posts/{post_id}", headers={
                                                 "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, json={"categories": categorie}, timeout=15)
                        break
                    except:
                        y['erros_name_movie'].append(
                            movie_data['name_fa'])
                        continue
                if response.status_code == 200:
                    db_post_backdrop['data'].append( {movie_data['id']:  {"post_id": post_id, "poster_id": poster['media_id']}})
                    progress_bar.update(1)
                else:
                    print("Failed to update post:", response.text)
            else:
                 print("Error:", response.status_code, response.text)


with open('errors.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(y, ensure_ascii=False))


with open('poster.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(db_post_backdrop, ensure_ascii=False))
