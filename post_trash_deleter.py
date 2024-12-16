import requests , json
from tqdm import tqdm
from colorama import Fore, Style
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL21vdmllcGl4LmlyIiwiaWF0IjoxNzM0Mjc1NjUwLCJuYmYiOjE3MzQyNzU2NTAsImV4cCI6MTczNjg2NzY1MCwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.S_37MUOjG7yNdS3LK66Us4-b2m4XvUSB914PQlCJ9LY"


with open('trash_db.json', "r", encoding="utf-8") as trash_db:
                    trashes = json.load(trash_db)

with tqdm(total=len(trashes), bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%] Remaining: {remaining}", colour="blue", dynamic_ncols=True, miniters=1) as progress_bar:
    progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")

    for i in trashes :
        for attempt in range(3):
            try:
                response = requests.delete(f"https://moviepix.ir/wp-json/wp/v2/posts/{i['id']}?force=true", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, timeout=15)
                break 
            except:
                continue
        if response.status_code == 200 :
            progress_bar.update(1)
        else :
            continue