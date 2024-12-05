import requests
import json


from functools import wraps



ref: int = 5198534

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
def try_execute(func, *args, retries=3, **kwargs):
    """
    Tries to execute a function up to a specified number of retries.
    
    Parameters:
        func (callable): The function to execute.
        *args: Positional arguments to pass to the function.
        retries (int): Number of retry attempts (default: 3).
        **kwargs: Keyword arguments to pass to the function.
    
    Returns:
        The result of the function if successful.
    
    Raises:
        Exception: If all attempts fail.
    """
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt < retries - 1:
                continue
            else:
                raise e


def get_Directors() :
    directors = {'directors' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://vod.tarinet.ir/wp-json/wp/v2/director?per_page=100&page={i}' , timeout=30)
                break
            except :
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                break
            for j in response.json() :
                directors['directors'].append({'name' : j['name'] , 'id' : j['id']})
            return directors
        
        else :
            return None
            


def get_Actors() :
    actors = {'actors' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://vod.tarinet.ir/wp-json/wp/v2/actor?per_page=100&page={i}' , timeout=30)
                break
            except :
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                break
            for j in response.json() :
                actors['actors'].append({'name' : j['name'] , 'id' : j['id']})

            return actors
        
        else :
            return None





def get_movie_data(movie_json_file : dict) -> dict:


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

def getAllTitles_series() -> None :
    
    request_getAllTitles = try_execute(requests.get( "https://seeko.film/api/v1/get/getAllTitles?f_type=series", headers={'Accept': 'application/json'}))

    request_getAllTitles_json = request_getAllTitles.json()

    request_getAllTitles_json_final : list = request_getAllTitles_json['data']['all_titles']['data']

    with open('movie_data_series.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json_final, ensure_ascii=False))
    print("series getted.")

def get_series_data(movie_json_file : dict) -> dict:

    
    id: str = movie_json_file['data']['series']['id']
    name: str = movie_json_file['data']['series']['name']
    name_fa: str = movie_json_file['data']['series']['name_fa']
    poster: str = movie_json_file['data']['series']['poster']
    cdn_poster: str = cdn["poster"] + poster
    backdrop: str = movie_json_file['data']['series']['backdrop']
    cdn_backdrop: str = cdn["backdrop"] + backdrop
    isirani: int = movie_json_file['data']['series']['ir']
    overview_fa: str = movie_json_file['data']['series']['overview_fa']
    year: str = movie_json_file['data']['series']['year']
    genre: str = movie_json_file['data']['series']['genre']
    rate: str = movie_json_file['data']['series']['rate']
    age: str = movie_json_file['data']['series']['age']
    runtime: str = movie_json_file['data']['series']['hour']
    ispersian_or_doubble: int = movie_json_file['data']['series']['persian']
    season_count : int = len(movie_json_file['data']['series']['season'])

    for i in range(0 , season_count) :
        for j in movie_json_file['data']['series']['season'][i] :
            request = requests.post(f"https://seeko.film/api/v1/ghost/get/getaffiliatelinks?id={j['id']}&type=episode&ref=5198534", headers={ 'Accept': 'application/json'})


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

    get_movie_links_with_id = f"https://seeko.film/api/v1/ghost/get/series/{id}?affiliate=1"

    request = requests.post(get_movie_links_with_id, headers={ 'Accept': 'application/json'})



data =   {
    "type": "movie",
    "id": "a01a0ca0-9073-11ef-ac89-29491062b877",
    "name": "Kiayi Academy",
    "name_fa": "آکادمی کیمیایی",
    "created_at": "2024-10-22 12:46:15",
    "updated_at": "2024-10-29 05:43:03",
    "poster": "terfomywfJtwaVZLpRvs.jpg",
    "overview": "\"Kimiaei Academy\" follows the journey of young men and women aspiring to enter the professional world of cinema. In this talent discovery and training program, renowned faces and cinema veterans accompany them to help overcome the challenges they face along the way.",
    "overview_fa": "\"آکادمی کیمیایی\" ماجرای دختران و پسرانی است که قصد ورود به دنیای حرفه‌ای سینما را دارند و در این استعدادیابی و آموزش، چهره‌های مطرح و بزرگان سینما با آنها همراه می‌شوند تا این چالش را پشت سر بگذارند.",
    "year": 2024,
    "genre": "Documentary",
    "rate": 6,
    "backdrop": "CHnB9bkDT7WjMzQHUVez.jpg",
    "age": "PG-13",
    "runtime": 90,
    "free": 0,
    "traffic": 0,
    "traffic_oo": 0,
    "current_time": 0,
    "duration_time": 0,
    "player": "aws",
    "upera": "3001899",
    "cloud": "aws",
    "ir": 1,
    "owner": 5611868,
    "imdb": None,
    "persian": 1,
    "series_id": "0",
    "series_name": "0",
    "series_name_fa": "0",
    "season_number": "0",
    "episode_number": "0",
    "tvod_price": "12000.00"
  }





from io import BytesIO


def media_gen(poster_url: str, poster_name: str) -> dict:
    response_Image_poster = requests.get(poster_url, timeout=30)
    if response_Image_poster.status_code == 200:
        poster_content = BytesIO(response_Image_poster.content)
        files = {"file": (poster_name, poster_content)}
        headers = {"Authorization": f"Bearer {bearer_token}"}
        for attempt in range(3):
            try:
                upload_response = requests.post(
                    "https://vod.tarinet.ir/wp-json/wp/v2/media", headers=headers, files=files, timeout=30)
                break
            except:
                if attempt == 2:
                    return {"status": None, "message": "Error in upload_response"}
                continue
        if upload_response.status_code == 201:
            poster_id = upload_response.json()["id"]
            return {"status": True, "media_id": poster_id, "media_name": poster_name}
        else:
            return {"status": None, "message": "Error in generate poster id in wordpress"}
    else:
        return {"status": None, "message": "Error in get poster from url"}


def get_Actors_as_list(): 
    actors = {'actors' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://vod.tarinet.ir/wp-json/wp/v2/actor?per_page=100&page={i}' , timeout=30)
                break
            except :
                if attempt == 2:
                    return {"status": None, "message": "Error in upload_response"}
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                return {"status": None, "message": "Error in 2"}
            for j in response.json() :
                actors['actors'].append({'name' : j['name'] , 'id' : j['id']})

            return actors['actors']
        


def get_Actors(name: str , actors : list): 

            flg = False
            for i in actors :
                if i['name'] == name :
                    flg = True
                    break
            if flg :
                for i in actors :
                    if i['name'] == name :
                        return {'flag' : False , 'name':  i['name'],  'id' : i['id']}
            else :
                data = {"name" : f"{str(name)}" }
                headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
                new_actor = requests.post( f"https://vod.tarinet.ir/wp-json/wp/v2/actor", headers=headers,  json=data, timeout=30)
                if new_actor.status_code != 400 :
                    actors.append({'name' : name , 'id' : new_actor.json()['id']})
                    return  {'flag' : True , 'name' : new_actor.json()['name'] , 'id' : new_actor.json()['id']}
                else :
                    return  {'flag' : False , 'name' : name , 'id' : new_actor.json()['data']['term_id']}
        


def get_Directors_as_list() :
    directors = {'directors' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://vod.tarinet.ir/wp-json/wp/v2/director?per_page=100&page={i}' , timeout=30)
                break
            except :
                if attempt == 2:
                    return {"status": None, "message": "Error in upload_response"}
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                return {"status": None, "message": "Error in 2"}
            for j in response.json() :
                directors['directors'].append({'name' : j['name'] , 'id' : j['id']})

            return directors['directors']
        

def get_Directors(name: str , directors : list): 

            flg = False
            for i in directors :
                if i['name'] == name :
                    flg = True
            if flg :
                for i in directors :
                    if i['name'] == name :
                        return {'flag' : False , 'id' : i['id']}
            else :
                data = {"name" : f"{str(name)}" }
                headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
                new_director = requests.post( f"https://vod.tarinet.ir/wp-json/wp/v2/director", headers=headers,  json=data, timeout=30)
                if new_director.status_code != 400 :
                    directors.append({'name' : name , 'id' : new_director.json()['id']})
                    return  {'flag' : True , "name" : new_director.json()['name'] , 'id' : new_director.json()['id']}
                else :
                    return {'flag' : False , 'id' : new_director.json()['data']['term_id']}
        

def get_genres_as_list() :
    ganres = {'ganres' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://vod.tarinet.ir/wp-json/wp/v2/genre?per_page=100&page={i}' , timeout=30)
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
        


def get_ganres(name: str , ganres : list): 

            flg = False
            for i in ganres :
                if i['name'] == name :
                    flg = True
            if flg :
                for i in ganres :
                    if i['name'] == name :
                        return {'flag' : False , 'id' : i['id']}
            else :
                data = {"name" : f"{str(name)}" }
                headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
                new_ganre = requests.post( f"https://vod.tarinet.ir/wp-json/wp/v2/genre", headers=headers,  json=data, timeout=30)
                if new_ganre.status_code != 400 :
                    ganres.append({'name' : name , 'id' : new_ganre.json()['id']})
                    return  {'flag' : True , "name" : new_ganre.json()['name'] , 'id' : new_ganre.json()['id']}
                else :
                    return  {'flag' : False , 'id' : new_ganre.json()['data']['term_id']}
        


def get_country_as_list() : 
    countrys = {'countrys' : []}

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://vod.tarinet.ir/wp-json/wp/v2/country?per_page=100&page={i}' , timeout=30)
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
        

def get_country(name: str , countrys : list): 

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
                new_country = requests.post( f"https://vod.tarinet.ir/wp-json/wp/v2/country", headers=headers,  json=data, timeout=30)
                if new_country.status_code != 400 :
                    countrys.append({'name' : name , 'id' : new_country.json()['id']})
                    return  {'flag' : True , "name" : new_country.json()['name'] , 'id' : new_country.json()['id']}
                else :
                    return  {'flag' : False , 'id' : new_country.json()['data']['term_id']}
        


