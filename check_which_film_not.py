import json , requests
from tqdm import tqdm
from colorama import Fore, Style
"""
names = []
headers = { "Authorization": f"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3ZvZC50YXJpbmV0LmlyIiwiaWF0IjoxNzMzMTY0ODg2LCJuYmYiOjE3MzMxNjQ4ODYsImV4cCI6MTczMzc2OTY4NiwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.c1NIRwSq2rmFeIZ-OBS7hu32TuD1GwSqwUVPPCVB3To", "Content-Type": "application/json" }
with tqdm(total=93, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%] Remaining: {remaining}", colour="blue", dynamic_ncols=True, miniters=1) as progress_bar:
    progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")
    for i in range(1 , 93) :
        request = requests.get(f"https://vod.tarinet.ir/wp-json/wp/v2/posts?per_page=50&status=publish&page={i}" , timeout=30, headers=headers).json()
        for j in request :
            names.append(j['acf']['en_title'])
            
            
        progress_bar.update(1)


with open('series.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps({'names' : names}, ensure_ascii=False))

"""


with open("series.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load2:
    request_getAllTitles_json_file2 = json.load( request_getAllTitles_json_final_load2)


with open("movie_data_movie.json", "r", encoding="utf-8") as request_getAllTitles_json_final_load:
    request_getAllTitles_json_file = json.load( request_getAllTitles_json_final_load)

max = request_getAllTitles_json_file2['names']

ls = []


for j in request_getAllTitles_json_file :
        if j['name'] not in max :
            ls.append(j)

with open('series_2.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps({'names' : ls}, ensure_ascii=False))
