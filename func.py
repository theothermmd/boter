import requests
import json
from data import cdn , ref



def get_movie_data(movie_json_file : dict) -> dict:


    id: str = movie_json_file['id']
    name: str = movie_json_file['name']
    name_fa: str = movie_json_file['name_fa']
    poster: str = movie_json_file['poster']
    cdn_poster: str = cdn["poster"] + poster
    backdrop: str = movie_json_file['backdrop']
    cdn_backdrop: str = cdn["backdrop"] + backdrop
    isirani: int = movie_json_file['ir']
    overview_fa: str = movie_json_file['overview_fa']
    year: str = movie_json_file['year']
    genre: str = movie_json_file['genre']
    rate: str = movie_json_file['rate']
    age: str = movie_json_file['age']
    imdb: str = movie_json_file['imdb']
    runtime: str = movie_json_file['runtime']
    ispersian_or_doubble: int = movie_json_file['persian']


    get_movie_links_with_id = f"https://seeko.film/api/v1/ghost/get/getaffiliatelinks?id={id}&type=movie&ref={ref}"

    request = requests.post(get_movie_links_with_id, headers={ 'Accept': 'application/json'})


    dl_datails = {
       "dub" : {
          
        "dl_480" : {
            "dl_lnk" : "" ,
            "size" : ""
        },
        "dl_720" : {
            "dl_lnk" : "" ,
            "size" : ""
        },
        "dl_1080" : {
            "dl_lnk" : "" ,
            "size" : ""
        },
        "dl_HQ_1080" : {
            "dl_lnk" : "" ,
            "size" : ""
        },
        "dl_BLURAY" : {
            "dl_lnk" : "" ,
            "size" : ""
        },
        "dl_HLS" : {
            "dl_lnk" : "" ,
            "size" : ""
        },

       },
        "sub" : {
           
            "dl_480" : {
                "dl_lnk" : "" ,
                "size" : ""
            },
            "dl_720" : {
                "dl_lnk" : "" ,
                "size" : ""
            },
            "dl_1080" : {
                "dl_lnk" : "" ,
                "size" : ""
            },
            "dl_HQ_1080" : {
                "dl_lnk" : "" ,
                "size" : ""
            },
            "dl_BLURAY" : {
                "dl_lnk" : "" ,
                "size" : ""
            },
            "dl_HLS" : {
                "dl_lnk" : "" ,
                "size" : ""
            },
        }

        }
    request_data_json = request.json()

    for i in request_data_json['data']['links']:
      if i['type'] == "traffic" and "IFRAME" not in i['title']:
          
          if "480" in i['title']:
            dl_datails['dub']["dl_480"]["dl_lnk"] = i['link']
            dl_datails['dub']["dl_480"]["size"] = i['size']

          elif "720" in i['title']:
            dl_datails['dub']["dl_720"]["dl_lnk"] = i['link']
            dl_datails['dub']["dl_720"]["size"] = i['size']

          elif "کیفیت 1080" in i['title']:
            dl_datails['dub']["dl_1080"]["dl_lnk"] = i['link']
            dl_datails['dub']["dl_1080"]["size"] = i['size']

          elif "کیفیت HQ_1080" in i['title']:
            dl_datails['dub']["dl_HQ_1080"]["dl_lnk"] = i['link']
            dl_datails['dub']["dl_HQ_1080"]["size"] = i['size']

          elif "BLURAY" in i['title']:
            dl_datails['dub']["dl_BLURAY"]["dl_lnk"] = i['link']
            dl_datails['dub']["dl_BLURAY"]["size"] = i['size']

          elif "HLS" in i['title']:
            dl_datails['dub']["dl_HLS"]["dl_lnk"] = i['link']
            dl_datails['dub']["dl_HLS"]["size"] = i['size']
    
    for i in request_data_json['data']['links']:
        if i['type'] == "traffic" and "IFRAME" not in i['title'] and "زیرنویس" in i['title']:
            
            if "480" in i['title']:
                dl_datails['sub']["dl_480"]["dl_lnk"] = i['link']
                dl_datails['sub']["dl_480"]["size"] = i['size']

            elif "720" in i['title']:
                dl_datails['sub']["dl_720"]["dl_lnk"] = i['link']
                dl_datails['sub']["dl_720"]["size"] = i['size']

            elif "کیفیت 1080" in i['title']:
                dl_datails['sub']["dl_1080"]["dl_lnk"] = i['link']
                dl_datails['sub']["dl_1080"]["size"] = i['size']

            elif "کیفیت HQ_1080" in i['title']:
                dl_datails['sub']["dl_HQ_1080"]["dl_lnk"] = i['link']
                dl_datails['sub']["dl_HQ_1080"]["size"] = i['size']

            elif "BLURAY" in i['title']:
                dl_datails['sub']["dl_BLURAY"]["dl_lnk"] = i['link']
                dl_datails['sub']["dl_BLURAY"]["size"] = i['size']
                
            elif "HLS" in i['title']:
                dl_datails['sub']["dl_HLS"]["dl_lnk"] = i['link']
                dl_datails['sub']["dl_HLS"]["size"] = i['size']
                
    return {
        "name": name,
        "name_fa": name_fa,
        "poster": poster,
        "cdn_poster": cdn_poster,
        "backdrop": backdrop,
        "cdn_backdrop": cdn_backdrop,
        "isirani": isirani,
        "overview_fa": overview_fa,
        "year": year,
        "genre": genre,
        "rate": rate,
        "age": age,
        "imdb": imdb,
        "runtime": runtime,
        "dl_datials": dl_datails,
        "ispersian_or_doubble": ispersian_or_doubble
    }



def getAllTitles_movie() -> None :
    
    request_getAllTitles = requests.get( "https://seeko.film/api/v1/get/getAllTitles?f_type=movie", headers={'Accept': 'application/json'})

    request_getAllTitles_json = request_getAllTitles.json()

    request_getAllTitles_json_final : list = request_getAllTitles_json['data']['all_titles']['data']

    with open('movie_data_movie.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json_final, ensure_ascii=False))
    print("movie getted.")

def getAllTitles_series() -> None :
    
    request_getAllTitles = requests.get( "https://seeko.film/api/v1/get/getAllTitles?f_type=series", headers={'Accept': 'application/json'})

    request_getAllTitles_json = request_getAllTitles.json()

    request_getAllTitles_json_final : list = request_getAllTitles_json['data']['all_titles']['data']

    with open('movie_data_series.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps( request_getAllTitles_json_final, ensure_ascii=False))
    print("series getted.")



