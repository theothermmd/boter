import requests
import json
bearer_token : str ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2NhcnRvb25mbGl4LmlyIiwiaWF0IjoxNzM0Mzc5NjE1LCJuYmYiOjE3MzQzNzk2MTUsImV4cCI6MTczNjk3MTYxNSwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMTk1In19fQ.Ntq6LW-DQBgO_3NGFx-8IMkOiA8rWkX369IUUZt6Le0"
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
from io import BytesIO

def try_execute(function, max_retries: int = 3):
    for retry in range(max_retries):
        try:
            result = function()
            return {'status': True, 'result': result}
        except Exception as e:
            if retry == max_retries - 1:
                return {'status': False, 'result': str(e)}

def get_movie_data(movie_json_file):


    id: str = movie_json_file['id']

    name: str = movie_json_file['name']
    name_fa: str = movie_json_file['name_fa']

    overview: str = movie_json_file['overview']
    overview_fa: str = movie_json_file['overview_fa']

    poster: str = movie_json_file['poster']
    cdn_poster: str = cdn["poster"] + poster

    backdrop: str = movie_json_file['backdrop']
    cdn_backdrop: str = cdn["backdrop"] + backdrop

    year: str = movie_json_file['year']

    genre: str = movie_json_file['genre']

    rate: str = movie_json_file['rate']

    age: str = movie_json_file['age']

    runtime: str = movie_json_file['runtime']

    isirani: int = movie_json_file['ir']

    imdb: str = movie_json_file['imdb']

    isdoubble: int = movie_json_file['persian']
    
    request = requests.post(f"https://seeko.film/api/v1/ghost/get/getaffiliatelinks?id={id}&type=movie&ref={ref}", headers={ 'Accept': 'application/json'})


    dl_datails = {
        "dub_links" : {
            "dl_480" : { "dl_lnk" : "" , "size" : "" },
            "dl_720" : { "dl_lnk" : "" , "size" : "" },
            "dl_1080" : { "dl_lnk" : "" , "size" : "" },
            "dl_HQ_1080" : { "dl_lnk" : "" , "size" : "" },
            "dl_BLURAY" : { "dl_lnk" : "" , "size" : "" },
            "dl_HLS" : { "dl_lnk" : "" , "size" : "" },

       },
        "sub_links" : {
            "dl_480" : { "dl_lnk" : "" , "size" : "" },
            "dl_720" : { "dl_lnk" : "" , "size" : "" },
            "dl_1080" : { "dl_lnk" : "" , "size" : "" },
            "dl_HQ_1080" : { "dl_lnk" : "" , "size" : "" },
            "dl_BLURAY" : { "dl_lnk" : "" , "size" : "" },
            "dl_HLS" : { "dl_lnk" : "" , "size" : "" },
        }

        }
    
    request_data_json = request.json()
    

    for i in request_data_json['data']['links']:
                
                if i['type'] == "traffic" and "IFRAME" not in i['title'] and "زیرنویس" not in i['title'] :
                    
                    if "480" in i['title']:
                        dl_datails['dub_links']["dl_480"]["dl_lnk"] = i['link']
                        dl_datails['dub_links']["dl_480"]["size"] = i['size']

                    elif "720" in i['title']:
                        dl_datails['dub_links']["dl_720"]["dl_lnk"] = i['link']
                        dl_datails['dub_links']["dl_720"]["size"] = i['size']

                    elif "کیفیت 1080" in i['title']:
                        dl_datails['dub_links']["dl_1080"]["dl_lnk"] = i['link']
                        dl_datails['dub_links']["dl_1080"]["size"] = i['size']

                    elif "کیفیت HQ_1080" in i['title']:
                        dl_datails['dub_links']["dl_HQ_1080"]["dl_lnk"] = i['link']
                        dl_datails['dub_links']["dl_HQ_1080"]["size"] = i['size']

                    elif "BLURAY" in i['title']:
                        dl_datails['dub_links']["dl_BLURAY"]["dl_lnk"] = i['link']
                        dl_datails['dub_links']["dl_BLURAY"]["size"] = i['size']

                    elif "HLS" in i['title'] :
                        dl_datails['dub_links']["dl_HLS"]["dl_lnk"] = i['link']
                        dl_datails['dub_links']["dl_HLS"]["size"] = i['size']
            
    for i in request_data_json['data']['links']:

                if i['type'] == "traffic" and "IFRAME" not in i['title'] :
                    
                    if "480" in i['title'] and "زیرنویس" in i['title']:
                        dl_datails['sub_links']["dl_480"]["dl_lnk"] = i['link']
                        dl_datails['sub_links']["dl_480"]["size"] = i['size']

                    elif "720" in i['title'] and "زیرنویس" in i['title']:
                        dl_datails['sub_links']["dl_720"]["dl_lnk"] = i['link']
                        dl_datails['sub_links']["dl_720"]["size"] = i['size']

                    elif "کیفیت 1080" in i['title'] and "زیرنویس" in i['title']:
                        dl_datails['sub_links']["dl_1080"]["dl_lnk"] = i['link']
                        dl_datails['sub_links']["dl_1080"]["size"] = i['size']

                    elif "کیفیت HQ_1080" in i['title'] and "زیرنویس" in i['title']:
                        dl_datails['sub_links']["dl_HQ_1080"]["dl_lnk"] = i['link']
                        dl_datails['sub_links']["dl_HQ_1080"]["size"] = i['size']

                    elif "BLURAY" in i['title'] and "زیرنویس" in i['title']:
                        dl_datails['sub_links']["dl_BLURAY"]["dl_lnk"] = i['link']
                        dl_datails['sub_links']["dl_BLURAY"]["size"] = i['size']
                        
                    elif "HLS" in i['title']:
                        dl_datails['sub_links']["dl_HLS"]["dl_lnk"] = i['link']
                        dl_datails['sub_links']["dl_HLS"]["size"] = i['size']




    return {
        "id": id,
        "name": name,
        "name_fa": name_fa,
        "poster": poster,
        "cdn_poster": cdn_poster,
        "backdrop": backdrop,
        "cdn_backdrop": cdn_backdrop,
        "isirani": isirani,
        "overview_fa": overview_fa,
        "overview" : overview,
        "year": year,
        "genre": genre,
        "rate": rate,
        "age": age,
        "imdb": imdb,
        "runtime": runtime,
        "dl_datials": dl_datails,
        "isdoubble": isdoubble,
        "sub": True if dl_datails['sub_links']['dl_480']['dl_lnk'] != "" else False
    }

def getAllTitles_movie() -> None :
    
    request_getAllTitles = requests.get( "https://seeko.film/api/v1/get/getAllTitles?f_type=movie", headers={'Accept': 'application/json'})

    request_getAllTitles_json = request_getAllTitles.json()

    request_getAllTitles_json_final : list = request_getAllTitles_json['data']['all_titles']['data']

    with open('movie_data_movie.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json_final, ensure_ascii=False))
    print("movie getted.")

def getAllTitles_movie_new() :
    request_getAllTitles = requests.get( "https://seeko.film/api/v1/get/getAllTitles?f_type=movie", headers={'Accept': 'application/json'})

    request_getAllTitles_json = request_getAllTitles.json()

    request_getAllTitles_json_final : list = request_getAllTitles_json['data']['all_titles']['data']

    with open('movie_data_movie_new.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json_final, ensure_ascii=False))

    with open("movie_data_movie.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
        request_getAllTitles_json_file = json.load(request_getAllTitles_json_final_load)

    with open("movie_data_movie_new.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
        request_getAllTitles_json_file_new = json.load(request_getAllTitles_json_final_load)
    ls = []
    for i in request_getAllTitles_json_file_new :
            if i not in request_getAllTitles_json_file :
                ls.append(i)
    with open('movie_data_movie_ekhtelaf.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( ls, ensure_ascii=False))

    print("movie getted.")


def getAllTitles_series() -> None :
    
    request_getAllTitles = requests.get( "https://seeko.film/api/v1/get/getAllTitles?f_type=series", headers={'Accept': 'application/json'})

    request_getAllTitles_json = request_getAllTitles.json()

    request_getAllTitles_json_final : list = request_getAllTitles_json['data']['all_titles']['data']

    with open('movie_data_series_new.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json_final, ensure_ascii=False))

    with open("movie_data_series.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
        request_getAllTitles_json_file = json.load(request_getAllTitles_json_final_load)

    with open("movie_data_series_new.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
        request_getAllTitles_json_file_new = json.load(request_getAllTitles_json_final_load)
    ls = []
    for i in request_getAllTitles_json_file_new :
            if i not in request_getAllTitles_json_file :
                ls.append(i)
    with open('movie_data_series_ekhtelaf.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( ls, ensure_ascii=False))

    print("series getted.")

def media_gen(poster_url: str, poster_name: str):
    
    response_Image_poster = requests.get(poster_url, timeout=30)

    if response_Image_poster.status_code == 200:

        poster_content = BytesIO(response_Image_poster.content)
        files = {"file": (poster_name, poster_content)}
        headers = {"Authorization": f"Bearer {bearer_token}"}
        for attempt in range(3):
            try:
                upload_response = requests.post( "https://cartoonflix.ir/wp-json/wp/v2/media", headers=headers, files=files, timeout=40)
                break
            except:
                if attempt == 2:
                    return {"status": None, "message": "Error in upload_response"}
                continue
        if upload_response.status_code == 201:
            poster_id = upload_response.json()["id"]
            return {"status": True, "media_id": poster_id, "media_name": poster_name}
        else:
            return {"status": None, "message": upload_response.text}
    else:
        return {"status": None, "message": "Error in get poster from url"}

def get_years_as_list():
    yearr = {'yearr' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://cartoonflix.ir/wp-json/wp/v2/yearr?per_page=100&page={i}' , timeout=30)
                break
            except :
                if attempt == 2:
                    return {"status": None, "message": "Error in upload_response"}
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                return {"status": None, "message": "Error in 2"}
            for j in response.json() :
                yearr['yearr'].append({'name' : j['name'] , 'id' : j['id']})

            return yearr['yearr']
        
        
def get_year(name: str, year_list):

            flg = False
            for i in year_list :
                if i['name'] == name :
                    flg = True
                    break
            if flg :
                for i in year_list :
                    if i['name'] == name :
                        return {'flag' : False , 'name':  i['name'],  'id' : i['id']}
            else :
                data = {"name" : f"{str(name)}" }
                headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
                new_yearr = requests.post( f"https://cartoonflix.ir/wp-json/wp/v2/yearr", headers=headers,  json=data, timeout=30)
                if new_yearr.status_code != 400 :
                    year_list.append({'name' : name , 'id' : new_yearr.json()['id']})
                    return  {'flag' : True , 'name' : new_yearr.json()['name'] , 'id' : new_yearr.json()['id']}
                else :
                    return  {'flag' : False , 'name' : name , 'id' : new_yearr.json()['data']['term_id']}
        
def get_directors_as_list() :
    """Retrieve a list of director objects from the WordPress API.

    Returns:
        A list of dictionaries, where each dictionary contains the name and ID of a director.
    """
    directors = []

    for page in range(1, 200):
        response = requests.get(
            f"https://cartoonflix.ir/wp-json/wp/v2/director?per_page=100&page={page}",
            timeout=30,
        )

        if response.status_code == 200:
            director_data = response.json()

            if not director_data:
                break

            directors.extend(
                [{"name": director["name"], "id": director["id"]} for director in director_data]
            )

    return directors
        
def get_director(name: str, directors) :
    """Retrieve a director object from the WordPress API, or create a new one if it does not exist.

    Args:
        name (str): The name of the director to retrieve or create.
        directors (List[Dict[str, Union[str, int]]]): A list of director objects.

    Returns:
        A dictionary containing the name, ID, and a flag indicating whether the director was created or retrieved.
    """

    for director in directors:
        if director["name"] == name:
            return {"flag": False, "name": director["name"], "id": director["id"]}

    data = {"name": name}
    headers = {"Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}

    response = requests.post("https://cartoonflix.ir/wp-json/wp/v2/director", headers=headers, json=data, timeout=30)

    if response.status_code == 201:
        directors.append({"name": response.json()["name"], "id": response.json()["id"]})
        return {"flag": True, "name": response.json()["name"], "id": response.json()["id"]}
    else:
        return {"flag": False, "name": name, "id": response.json()["data"]["term_id"]}
    
def get_genres_as_list():
    ganres = {'ganres' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://cartoonflix.ir/wp-json/wp/v2/genre?per_page=100&page={i}' , timeout=30)
                break
            except :
                if attempt == 2:
                    return {"status": None, "message": "Error in upload_response"}
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                return {"status": None, "message": "Error in 2"}
            for j in response.json() :
                ganres['ganres'].append({'name' : j['name'] , 'id' : j['id']})

            return ganres['ganres']
        
def get_genre(name: str, genres) :

            flg = False
            for i in genres :
                if i['name'] == name :
                    flg = True
            if flg :
                for i in genres :
                    if i['name'] == name :
                        return {'flag' : False , 'id' : i['id']}
            else :
                data = {"name" : f"{str(name)}" }
                headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
                new_ganre = requests.post( f"https://cartoonflix.ir/wp-json/wp/v2/genre", headers=headers,  json=data, timeout=30)
                if new_ganre.status_code != 400 :
                    genres.append({'name' : name , 'id' : new_ganre.json()['id']})
                    return  {'flag' : True , "name" : new_ganre.json()['name'] , 'id' : new_ganre.json()['id']}
                else :
                    return  {'flag' : False , 'id' : new_ganre.json()['data']['term_id']}
        
def get_countries():
    countrys = {'countrys' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://cartoonflix.ir/wp-json/wp/v2/country?per_page=100&page={i}' , timeout=30)
                break
            except :
                if attempt == 2:
                    return {"status": None, "message": "Error in upload_response"}
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                return {"status": None, "message": "Error in 2"}
            for j in response.json() :
                countrys['countrys'].append({'name' : j['name'] , 'id' : j['id']})

            return countrys['countrys']
        
def get_country(name: str, countrys) :
            flg = False
            for i in countrys :
                if i['name'] == name :
                    flg = True
            if flg :
                for i in countrys :
                    if i['name'] == name :
                        return {'flag' : False , 'id' : i['id']}
            else :
                data = {"name" : f"{str(name)}" }
                headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
                new_country = requests.post( f"https://cartoonflix.ir/wp-json/wp/v2/country", headers=headers,  json=data, timeout=30)
                if new_country.status_code != 400 :
                    countrys.append({'name' : name , 'id' : new_country.json()['id']})
                    return  {'flag' : True , "name" : new_country.json()['name'] , 'id' : new_country.json()['id']}
                else :
                    return  {'flag' : False , 'id' : new_country.json()['data']['term_id']}
         
def get_series_data(id : dict) -> dict:


    request= requests.get(f"https://seeko.film/api/v1/ghost/get/series/{id}?affiliate=1", headers={ 'Accept': 'application/json'} , timeout=30).json()

    try :
        request_series_data = request['data']['series']
    except :
        return None
    
    name: str = request_series_data['name']
    name_fa: str = request_series_data['name_fa']

    overview: str = request_series_data['overview']
    overview_fa: str = request_series_data['overview_fa']

    poster: str = request_series_data['poster']
    cdn_poster: str = cdn["poster"] + poster

    backdrop: str = request_series_data['backdrop']
    cdn_backdrop: str = cdn["backdrop"] + backdrop

    year: str = request_series_data['year']

    genre: str = request_series_data['genre']

    rate: str = request_series_data['rate']

    age: str = request_series_data['age']
    sub : bool = False
    with open('movie_data_series_new.json', "r", encoding="utf-8") as request_getAllTitles_json_final_load:
        request_getAllTitles_json_file = json.load( request_getAllTitles_json_final_load)
    runtime = 0
    ctn = 0
    for time in request_getAllTitles_json_file :
        if time['series_id'] == id :
            runtime += time['runtime']
            ctn += 1
    runtime = runtime // ctn
    isirani: int = request_series_data['ir']

    isdoubble: int = request_series_data['persian']
    erros = []
    seasons_names : dict = {'1' : 'فصل اول','2' : 'فصل دوم','3' : 'فصل سوم','4' : 'فصل چهارم','5' : 'فصل پنجم','6' : 'فصل ششم','7' : 'فصل هفتم','8' : 'فصل هشتم','9' : 'فصل نهم','10' : 'فصل دهم','11' : 'فصل یازدهم','12' : 'فصل دوازدهم','13' : 'فصل سیزدهم','14' : 'فصل چهاردهم','15' : 'فصل پانزدهم','16' : 'فصل شانزدهم', }
    seasons : dict = {}
    serialdl : list = []
    if isirani != 1 :

        for x in request['data']['season'].keys() :
            seasons[x] = []
            serialdl.append({"season-name": seasons_names[x] + " - دوبله فارسی", "episode-count": "",  "dl-links" : [] })
            serialdl.append({"season-name": seasons_names[x] + " - زیرنویس فارسی", "episode-count": "",  "dl-links" : [] })
    else :
        for x in request['data']['season'].keys() :
            seasons[x] = []
            serialdl.append({"season-name": seasons_names[x], "episode-count": "",  "dl-links" : [] })
            serialdl.append({"season-name": seasons_names[x], "episode-count": "",  "dl-links" : [] })
    
    for j, (serial, next_item) in zip(seasons.keys(), zip(serialdl[::2], serialdl[1::2])):
        serial['episode-count'] = f"{len(request['data']['season'][j])} قسمت"
        next_item['episode-count'] = f"{len(request['data']['season'][j])} قسمت"
        for w , counter in zip(request['data']['season'][j] , range(1 , len(request['data']['season'][j]) + 1)) :
                
                requestz = requests.post(f"https://seeko.film/api/v1/ghost/get/getaffiliatelinks?id={w['id']}&type=episode&ref={ref}", headers={ 'Accept': 'application/json'} , timeout=30)
                dl_datails = {
                    "dub_links" : { "dl_480" : { "dl_lnk" : "" , "size" : "" }, "dl_720" : { "dl_lnk" : "" , "size" : "" }, "dl_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_HQ_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_BLURAY" : { "dl_lnk" : "" , "size" : "" }, "dl_HLS" : { "dl_lnk" : "" , "size" : "" }, },
                    "sub_links" : { "dl_480" : { "dl_lnk" : "" , "size" : "" }, "dl_720" : { "dl_lnk" : "" , "size" : "" }, "dl_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_HQ_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_BLURAY" : { "dl_lnk" : "" , "size" : "" }, "dl_HLS" : { "dl_lnk" : "" , "size" : "" }, }
                    }
                request_data_json = requestz.json()
                for atn in range(3) :
                    try :
                        if 'data' not in request_data_json :
                            requestz = requests.post(f"https://seeko.film/api/v1/ghost/get/getaffiliatelinks?id={w['id']}&type=episode&ref={ref}", headers={ 'Accept': 'application/json'})
                            request_data_json = requestz.json()
                            continue
                        else :
                            break
                    except :
                        continue
                try :
                    for i in request_data_json['data']['links']:
                                    if i['type'] == "traffic" and "IFRAME" not in i['title'] and "زیرنویس" not in i['title'] :
                                        if "480" in i['title']:
                                            dl_datails['dub_links']["dl_480"]["dl_lnk"] = i['link']
                                            dl_datails['dub_links']["dl_480"]["size"] = i['size']
                                        elif "720" in i['title']:
                                            dl_datails['dub_links']["dl_720"]["dl_lnk"] = i['link']
                                            dl_datails['dub_links']["dl_720"]["size"] = i['size']
                                        elif "کیفیت 1080" in i['title']:
                                            dl_datails['dub_links']["dl_1080"]["dl_lnk"] = i['link']
                                            dl_datails['dub_links']["dl_1080"]["size"] = i['size']
                                        elif "کیفیت HQ_1080" in i['title']:
                                            dl_datails['dub_links']["dl_HQ_1080"]["dl_lnk"] = i['link']
                                            dl_datails['dub_links']["dl_HQ_1080"]["size"] = i['size']
                                        elif "BLURAY" in i['title']:
                                            dl_datails['dub_links']["dl_BLURAY"]["dl_lnk"] = i['link']
                                            dl_datails['dub_links']["dl_BLURAY"]["size"] = i['size']
                                        elif "HLS" in i['title'] :
                                            dl_datails['dub_links']["dl_HLS"]["dl_lnk"] = i['link']
                                            dl_datails['dub_links']["dl_HLS"]["size"] = i['size']
                except :
                    erros.append(w['id'])
                    continue    
                for i in request_data_json['data']['links']:
                            if i['type'] == "traffic" and "IFRAME" not in i['title'] :
                                if "480" in i['title'] and "زیرنویس" in i['title']:
                                    dl_datails['sub_links']["dl_480"]["dl_lnk"] = i['link']
                                    dl_datails['sub_links']["dl_480"]["size"] = i['size']
                                elif "720" in i['title'] and "زیرنویس" in i['title']:
                                    dl_datails['sub_links']["dl_720"]["dl_lnk"] = i['link']
                                    dl_datails['sub_links']["dl_720"]["size"] = i['size']
                                elif "کیفیت 1080" in i['title'] and "زیرنویس" in i['title']:
                                    dl_datails['sub_links']["dl_1080"]["dl_lnk"] = i['link']
                                    dl_datails['sub_links']["dl_1080"]["size"] = i['size']
                                elif "کیفیت HQ_1080" in i['title'] and "زیرنویس" in i['title']:
                                    dl_datails['sub_links']["dl_HQ_1080"]["dl_lnk"] = i['link']
                                    dl_datails['sub_links']["dl_HQ_1080"]["size"] = i['size']
                                elif "BLURAY" in i['title'] and "زیرنویس" in i['title']:
                                    dl_datails['sub_links']["dl_BLURAY"]["dl_lnk"] = i['link']
                                    dl_datails['sub_links']["dl_BLURAY"]["size"] = i['size']
                                elif "HLS" in i['title']:
                                    dl_datails['sub_links']["dl_HLS"]["dl_lnk"] = i['link']
                                    dl_datails['sub_links']["dl_HLS"]["size"] = i['size']
  
                        
                seasons[j].append({"number" : w['episode_number'] , "id" : w['id'] , "dl_datails" : dl_datails })
                if dl_datails['sub_links']["dl_480"]["dl_lnk"] != "" :
                    sub = True
                if dl_datails['dub_links']["dl_480"]["dl_lnk"] != "" :  

                    serial['dl-links'].append(
                        {"episode": f"قسمت {counter}",
                        "farsi": "yes",
                        "farsi-sound": "",
                        "subtitle": "",
                        "serial-price": "",
                        "serial_info": "",
                        "is_free": False,
                        "subtitle_online_serial": "",
                        "online_link_serial": dl_datails['dub_links']["dl_HLS"]["dl_lnk"],
                        "online_link_480": "",
                        "online_link_720": "",
                        "online_link_1080": "",
                        "serial_480": dl_datails['dub_links']["dl_HLS"]["dl_lnk"],
                        "serial_720": dl_datails['dub_links']["dl_HLS"]["dl_lnk"],
                        "serial_1080": dl_datails['dub_links']["dl_HLS"]["dl_lnk"],
                        "quality" : [
                            { "quality-name-select": "480p", "quality-name": "480p", "quality-dl-link": dl_datails['dub_links']["dl_480"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_480"]["size"], "sale": False } if dl_datails['dub_links']["dl_480"]["dl_lnk"] != "" else None,
                            { "quality-name-select": "720p", "quality-name": "720p", "quality-dl-link": dl_datails['dub_links']["dl_720"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_720"]["size"], "sale": False } if dl_datails['dub_links']["dl_720"]["dl_lnk"] != "" else None,
                            { "quality-name-select": "1080p", "quality-name": "1080p", "quality-dl-link": dl_datails['dub_links']["dl_1080"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_1080"]["size"], "sale": False } if dl_datails['dub_links']["dl_1080"]["dl_lnk"] != "" else None,
                            { "quality-name-select": "1080p_HQ", "quality-name": "1080p_HQ", "quality-dl-link": dl_datails['dub_links']["dl_HQ_1080"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_HQ_1080"]["size"], "sale": False } if dl_datails['dub_links']["dl_HQ_1080"]["dl_lnk"] != "" else None,
                            { "quality-name-select": "BluRay", "quality-name": "BluRay", "quality-dl-link": dl_datails['dub_links']["dl_BLURAY"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_BLURAY"]["size"], "sale": False } if dl_datails['dub_links']["dl_BLURAY"]["dl_lnk"] != "" else None
                        ]
                })

                if dl_datails['sub_links']["dl_480"]["dl_lnk"] != "" :

                    if dl_datails['dub_links']["dl_480"]["dl_lnk"] != "" :

                        next_item['dl-links'].append(
                            {"episode": f"قسمت {counter}",
                            "farsi": "yes",
                            "farsi-sound": "",
                            "subtitle": "",
                            "serial-price": "",
                            "serial_info": "",
                            "is_free": False,
                            "subtitle_online_serial": "",
                            "online_link_serial": dl_datails['sub_links']["dl_480"]["dl_lnk"],
                            "online_link_480": "",
                            "online_link_720": "",
                            "online_link_1080": "",
                            "serial_480": dl_datails['sub_links']["dl_480"]["dl_lnk"] if dl_datails['sub_links']["dl_480"]["dl_lnk"] != "" else None,
                            "serial_720": dl_datails['sub_links']["dl_720"]["dl_lnk"] if dl_datails['sub_links']["dl_720"]["dl_lnk"] != "" else None,
                            "serial_1080": dl_datails['sub_links']["dl_1080"]["dl_lnk"] if dl_datails['sub_links']["dl_1080"]["dl_lnk"] != "" else None,
                            "quality" : [
                                { "quality-name-select": "480p", "quality-name": "480p", "quality-dl-link": dl_datails['sub_links']["dl_480"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_480"]["size"], "sale": False } if dl_datails['sub_links']["dl_480"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "720p", "quality-name": "720p", "quality-dl-link": dl_datails['sub_links']["dl_720"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_720"]["size"], "sale": False } if dl_datails['sub_links']["dl_720"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "1080p", "quality-name": "1080p", "quality-dl-link": dl_datails['sub_links']["dl_1080"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_1080"]["size"], "sale": False } if dl_datails['sub_links']["dl_1080"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "1080p_HQ", "quality-name": "1080p_HQ", "quality-dl-link": dl_datails['sub_links']["dl_HQ_1080"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_HQ_1080"]["size"], "sale": False } if dl_datails['sub_links']["dl_HQ_1080"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "BluRay", "quality-name": "BluRay", "quality-dl-link": dl_datails['sub_links']["dl_BLURAY"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_BLURAY"]["size"], "sale": False } if dl_datails['sub_links']["dl_BLURAY"]["dl_lnk"] != "" else None
                            ]
                            })
                    else :
                        next_item['dl-links'].append(
                            {"episode": f"قسمت {counter}",
                            "farsi": "yes",
                            "farsi-sound": "",
                            "subtitle": "",
                            "serial-price": "",
                            "serial_info": "",
                            "is_free": False,
                            "subtitle_online_serial": "",
                            "online_link_serial": dl_datails['sub_links']["dl_HLS"]["dl_lnk"],
                            "online_link_480": "",
                            "online_link_720": "",
                            "online_link_1080": "",
                            "serial_480": dl_datails['sub_links']["dl_HLS"]["dl_lnk"],
                            "serial_720": "",
                            "serial_1080": "",
                            "quality" : [
                                { "quality-name-select": "480p", "quality-name": "480p", "quality-dl-link": dl_datails['sub_links']["dl_480"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_480"]["size"], "sale": False } if dl_datails['sub_links']["dl_480"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "720p", "quality-name": "720p", "quality-dl-link": dl_datails['sub_links']["dl_720"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_720"]["size"], "sale": False } if dl_datails['sub_links']["dl_720"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "1080p", "quality-name": "1080p", "quality-dl-link": dl_datails['sub_links']["dl_1080"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_1080"]["size"], "sale": False } if dl_datails['sub_links']["dl_1080"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "1080p_HQ", "quality-name": "1080p_HQ", "quality-dl-link": dl_datails['sub_links']["dl_HQ_1080"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_HQ_1080"]["size"], "sale": False } if dl_datails['sub_links']["dl_HQ_1080"]["dl_lnk"] != "" else None,
                                { "quality-name-select": "BluRay", "quality-name": "BluRay", "quality-dl-link": dl_datails['sub_links']["dl_BLURAY"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_BLURAY"]["size"], "sale": False } if dl_datails['sub_links']["dl_BLURAY"]["dl_lnk"] != "" else None
                            ]
                            })

    for i in serialdl :
        if i['dl-links'] == [] :
            serialdl.remove(i)
    for i in serialdl :
        if i['dl-links'] == [] :
            serialdl.remove(i)        
    return {
        "id": id,
        "name": name,
        "name_fa": name_fa,
        "poster": poster,
        "cdn_poster": cdn_poster,
        "backdrop": backdrop,
        "cdn_backdrop": cdn_backdrop,
        "isirani": isirani,
        "overview_fa": overview_fa,
        "overview" : overview,
        "year": year,
        "genre": genre,
        "rate": rate,
        "age": age,
        "runtime": runtime,
        "dl_datials": dl_datails,
        "isdoubble": isdoubble,
        "sub": sub,
        "serialdl": serialdl,
        "seasons" : seasons,
        "erros"  : erros
    }




