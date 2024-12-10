import requests
ref: int = 5198534
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL21vdmllcGl4LmlyIiwiaWF0IjoxNzMzNzQzMDQ2LCJuYmYiOjE3MzM3NDMwNDYsImV4cCI6MTczNjMzNTA0NiwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.3nhDfqRZ7BbdCg7cCcO1j_uBvR4LcO3j5LqEswO5gX0"
cdn : dict = { "poster": "https://s35.upera.net/thumb?w=675&h=1000&q=90&src=https://s35.upera.net/s3/posters/", "backdrop": "https://s35.upera.net/thumb?w=764&h=400&q=100&src=https://s35.upera.net/s3/backdrops/", "lg_poster": "https://s35.upera.net/thumb?w=675&h=1000&q=90&src=https://s35.upera.net/s3/posters/", "lg_backdrop": "https://s35.upera.net/thumb?w=764&h=400&q=100&src=https://s35.upera.net/s3/backdrops/", "md_poster": "https://s35.upera.net/thumb?w=337&h=500&q=90&src=https://s35.upera.net/s3/posters/", "md_backdrop": "https://s35.upera.net/thumb?w=382&h=200&q=90&src=https://s35.upera.net/s3/backdrops/", "sm_poster": "https://s35.upera.net/thumb?w=225&h=333&q=90&a=t&src=https://s35.upera.net/s3/posters/", "sm_backdrop": "https://s35.upera.net/thumb?w=191&h=100&q=90&src=https://s35.upera.net/s3/backdrops/" }






def get_series_data(id : dict) -> dict:
    request : dict = requests.get(f"https://seeko.film/api/v1/ghost/get/series/{id}?affiliate=1", headers={ 'Accept': 'application/json'}).json()

    request_series_data : dict = request['data']['series']
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

    runtime: str = request_series_data['hour']

    isirani: int = request_series_data['ir']

    isdoubble: int = request_series_data['persian']

    seasons_names : dict = {'1' : 'فصل اول','2' : 'فصل دوم','3' : 'فصل سوم','4' : 'فصل چهارم','5' : 'فصل پنجم','6' : 'فصل ششم','7' : 'فصل هفتم','8' : 'فصل هشتم','9' : 'فصل نهم','10' : 'فصل دهم','11' : 'فصل یازدهم','12' : 'فصل دوازدهم','13' : 'فصل سیزدهم','14' : 'فصل چهاردهم','15' : 'فصل پانزدهم','16' : 'فصل شانزدهم', }
    seasons : dict = {}
    serialdl : list = []
    for x in request['data']['season'].keys() :
        seasons[x] = []
        serialdl.append({"season-name": seasons_names[x] + " - دوبله فارسی", "episode-count": "",  "dl-links" : [] })
        serialdl.append({"season-name": seasons_names[x] + " - زیرنویس فارسی", "episode-count": "",  "dl-links" : [] })
    
    for j , serial in zip(seasons.keys(), serialdl) :

        for w , counter in zip(request['data']['season'][j] , range(1 , len(request['data']['season'][j]) + 1)) :
                
                requestz = requests.post(f"https://seeko.film/api/v1/ghost/get/getaffiliatelinks?id={w['id']}&type=episode&ref={ref}", headers={ 'Accept': 'application/json'})
                dl_datails = {
                    "dub_links" : { "dl_480" : { "dl_lnk" : "" , "size" : "" }, "dl_720" : { "dl_lnk" : "" , "size" : "" }, "dl_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_HQ_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_BLURAY" : { "dl_lnk" : "" , "size" : "" }, "dl_HLS" : { "dl_lnk" : "" , "size" : "" }, },
                    "sub_links" : { "dl_480" : { "dl_lnk" : "" , "size" : "" }, "dl_720" : { "dl_lnk" : "" , "size" : "" }, "dl_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_HQ_1080" : { "dl_lnk" : "" , "size" : "" }, "dl_BLURAY" : { "dl_lnk" : "" , "size" : "" }, "dl_HLS" : { "dl_lnk" : "" , "size" : "" }, }
                    }
                request_data_json = requestz.json()
                if " - دوبله فارسی" in serial['season-name'] :
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
                                        
                elif " - زیرنویس فارسی" in serial['season-name'] :
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

                if " - دوبله فارسی" in serial['season-name'] :
                     
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
                        "serial_720": "",
                        "serial_1080": "",
                        "quality" : [
                            { "quality-name-select": "480p", "quality-name": "480p", "quality-dl-link": dl_datails['dub_links']["dl_480"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_480"]["size"], "sale": False },
                            { "quality-name-select": "720p", "quality-name": "720p", "quality-dl-link": dl_datails['dub_links']["dl_720"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_720"]["size"], "sale": False },
                            { "quality-name-select": "1080p", "quality-name": "1080p", "quality-dl-link": dl_datails['dub_links']["dl_1080"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_1080"]["size"], "sale": False },
                            { "quality-name-select": "1080p_HQ", "quality-name": "1080p_HQ", "quality-dl-link": dl_datails['dub_links']["dl_HQ_1080"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_HQ_1080"]["size"], "sale": False },
                            { "quality-name-select": "BluRay", "quality-name": "BluRay", "quality-dl-link": dl_datails['dub_links']["dl_BLURAY"]["dl_lnk"], "serial_size": dl_datails['dub_links']["dl_BLURAY"]["size"], "sale": False }
                        ]
                })
                elif " - زیرنویس فارسی" in serial['season-name'] :

                    serial['dl-links'].append(
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
                            { "quality-name-select": "480p", "quality-name": "480p", "quality-dl-link": dl_datails['sub_links']["dl_480"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_480"]["size"], "sale": False },
                            { "quality-name-select": "720p", "quality-name": "720p", "quality-dl-link": dl_datails['sub_links']["dl_720"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_720"]["size"], "sale": False },
                            { "quality-name-select": "1080p", "quality-name": "1080p", "quality-dl-link": dl_datails['sub_links']["dl_1080"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_1080"]["size"], "sale": False },
                            { "quality-name-select": "1080p_HQ", "quality-name": "1080p_HQ", "quality-dl-link": dl_datails['sub_links']["dl_HQ_1080"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_HQ_1080"]["size"], "sale": False },
                            { "quality-name-select": "BluRay", "quality-name": "BluRay", "quality-dl-link": dl_datails['sub_links']["dl_BLURAY"]["dl_lnk"], "serial_size": dl_datails['sub_links']["dl_BLURAY"]["size"], "sale": False }
                        ]
                })


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
        "sub": True if dl_datails['sub_links']['dl_480']['dl_lnk'] != "" else False,
        "serialdl": serialdl
    }
