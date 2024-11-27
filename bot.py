import requests
import json
import os
from data import cdn , bearer_token
from func import getAllTitles_movie ,get_movie_data
from io import BytesIO
from tqdm import tqdm
from colorama import Fore, Style
if not os.path.isfile('movie_data_movie.json'):
    getAllTitles_movie()

with open("movie_data_movie.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load(request_getAllTitles_json_final_load)

y = {"erros_name_movie" : []}
total_items = len(request_getAllTitles_json_file)
categories = {'irani' : 7558 , 'dubble' : 6 , 'zernevis' : 2572 , 'animations': 8775}

with tqdm(total=total_items, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%]", colour="green") as progress_bar:

    for movie in request_getAllTitles_json_file :
        for attempt in range(3):
            try :
                movie_data = get_movie_data(movie)
                break
            except :
                continue

        for attempt in range(3):
            try :
                response_Image_poster = requests.get(movie_data['cdn_poster'] , timeout=20)
                break
            except :
                continue    
        

        if response_Image_poster.status_code == 200:

            poster_content = BytesIO(response_Image_poster.content)  
            poster_name = movie_data['poster']  

            files = {
                "file": (poster_name, poster_content)
            }

            headers = {
                "Authorization": f"Bearer {bearer_token}"
            }

            for attempt in range(3):
                try :
                    upload_response = requests.post("https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/media", headers=headers, files=files, timeout=20)
                    break
                except :
                    y['erros_name_movie'].append(movie_data['name_fa'])
                    continue
                
            if upload_response.status_code == 201:
                poster_id = upload_response.json()["id"]
                for attempt in range(3):
                    try :
                        response_Image_backdrop = requests.get(movie_data['cdn_backdrop'] , timeout=20)
                        break
                    except :
                        continue
                
                if response_Image_backdrop.status_code == 200:

                    backdrop_content = BytesIO(response_Image_backdrop.content)  
                    backdrop_name = movie_data['backdrop']  

                    files = {
                        "file": (backdrop_name, backdrop_content)
                    }

                    headers = {
                        "Authorization": f"Bearer {bearer_token}"
                    }
                    for attempt in range(3):
                        try :
                            upload_response = requests.post("https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/media", headers=headers, files=files , timeout=20)
                            backdrop_id = upload_response.json()["id"]
                            break
                        except :
                            y['erros_name_movie'].append(movie_data['name_fa'])
                            continue
                    
                    categorie = 1
                    if movie_data['isirani'] == 1 :
                        categorie = categories['irani']

                    else :
                        if movie_data['ispersian_or_doubble'] == 1 :

                            if "Animation" in movie_data['genre']:
                                categorie = categories['animations']
                            else :
                                categorie = categories['dubble']
                        else :

                            if movie_data['ispersian_or_doubble'] == 0 and movie_data['dl_datials']['sub']['dl_480']['size'] != "" :
                                if "Animation" in movie_data['genre']:
                                    categorie = categories['animations']
                                else :
                                    categorie = categories['zernevis']



                    send_data = {
                        "title": movie_data['name_fa'],
                        "content": "",
                        "status": "publish",
                        "acf" : {
                            "slider_image2": {
                                "ID": backdrop_id,
                                "id": backdrop_id,
                                "title": "hello",
                                "filename": backdrop_name,
                                "filesize": 397067,
                                "url": f"https://vod.tarinet.ir/wp-content/uploads/2024/11/{backdrop_name}",
                                "link": f"https://vod.tarinet.ir/tt1535108/{backdrop_name}",
                                "alt": "",
                                "author": "2",
                                "description": "",
                                "caption": "",
                                "name": backdrop_name,
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
                        "post-type" : "film",
                        "released" : movie_data['year'],
                        "imdbRating" : movie_data['rate'],
                        "time" : f"{movie_data['runtime']} دقیقه",
                        "imdb": movie_data['imdb'],
                        "story" : movie_data['overview_fa'],
                        "imdb-id" : movie_data['imdb'],
                        "en_title" : movie_data['name'],
                        "persian-doble" : True if movie_data['ispersian_or_doubble'] == 1 and movie_data['isirani'] == 0 else False,
                        "mobile_online":movie_data['dl_datials']['dub']['dl_HLS']['dl_lnk'],
                        "categories" : [int(categorie)],
                        "censored": True if movie_data['isirani'] == 0 else False,
                        "def-version": True if movie_data['dl_datials']['sub']['dl_480']['size'] != "" else False,
                        "playonline": True,
                        "film-dl": [
                            {
                                "farsi-doble": "yes",
                                "farsi-doble-link": "",
                                "film_info": "",
                                "is_free": False,
                                "subtitle-film": "",
                                "online_link": movie_data['dl_datials']['dub']['dl_HLS']['dl_lnk'],
                                "online_link_480": "",
                                "online_link_720": "",
                                "online_link_1080": "",
                                "subtitle_online_film": "",
                                "film-dl-link": [
                                {
                                    "quality-film-select": "480p",
                                    "quality-film": "480p",
                                    "size-film": movie_data['dl_datials']['dub']['dl_480']['size'],
                                    "dl-film-link": movie_data['dl_datials']['dub']['dl_480']['dl_lnk'],
                                    "version": "",
                                    "film-price": "",
                                    "dl_row_info": ""
                                },
                                {
                                    "quality-film-select": "720p",
                                    "quality-film": "720p",
                                    "size-film": movie_data['dl_datials']['dub']['dl_720']['size'],
                                    "dl-film-link": movie_data['dl_datials']['dub']['dl_720']['dl_lnk'],
                                    "version": "",
                                    "film-price": "",
                                    "dl_row_info": ""
                                },
                                {
                                    "quality-film-select": "1080p",
                                    "quality-film": "1080p",
                                    "size-film": movie_data['dl_datials']['dub']['dl_1080']['size'],
                                    "dl-film-link": movie_data['dl_datials']['dub']['dl_1080']['dl_lnk'],
                                    "version": "",
                                    "film-price": "",
                                    "dl_row_info": ""
                                },
                                {
                                    "quality-film-select": "1080p_HQ",
                                    "quality-film": "1080p_HQ",
                                    "size-film": movie_data['dl_datials']['dub']['dl_HQ_1080']['size'],
                                    "dl-film-link": movie_data['dl_datials']['dub']['dl_HQ_1080']['dl_lnk'],
                                    "version": "",
                                    "film-price": "",
                                    "dl_row_info": ""
                                },
                                {
                                    "quality-film-select": "BluRay",
                                    "quality-film": "BluRay",
                                    "size-film": movie_data['dl_datials']['dub']['dl_BLURAY']['size'],
                                    "dl-film-link": movie_data['dl_datials']['dub']['dl_BLURAY']['dl_lnk'],
                                    "version": "",
                                    "film-price": "",
                                    "dl_row_info": ""
                                }
                                ]
                            }
                            ]
                        
                    },
                    "featured_media": poster_id 

                    }

                    headers = {
                        "Authorization": f"Bearer {bearer_token}",
                        "Content-Type": "application/json"
                    }
                    for attempt in range(3):
                        try :
                            response = requests.post("https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/posts", json=send_data, headers=headers, timeout=20)
                            break
                        except :
                            y['erros_name_movie'].append(movie_data['name_fa'])
                            continue


                    if response.status_code == 200 or response.status_code == 201:
                        post_id = response.json()["id"]
                        for attempt in range(3):
                            try :
                                response = requests.post(f"https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/posts/{post_id}", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }, json={ "categories" : [int(categorie)] }, timeout=15)
                                break
                            except :
                                y['erros_name_movie'].append(movie_data['name_fa'])
                                continue

                        if response.status_code == 200:
                            progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")
                            progress_bar.update(1)
                        else:
                            print("Failed to update post:", response.text)
                    else:
                        print("Error:", response.status_code, response.text)

    

            

with open('errors.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(y, ensure_ascii=False))