import requests , json
from tqdm import tqdm
from colorama import Fore, Style
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL21vdmllcGl4LmlyIiwiaWF0IjoxNzM0Mjc1NjUwLCJuYmYiOjE3MzQyNzU2NTAsImV4cCI6MTczNjg2NzY1MCwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.S_37MUOjG7yNdS3LK66Us4-b2m4XvUSB914PQlCJ9LY"

ls = []

with tqdm(total=122, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%] Remaining: {remaining}", colour="blue", dynamic_ncols=True, miniters=1) as progress_bar:
    progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")

    for page_number in range(1 , 200) :
        for attempt in range(3):
            try:
                response = requests.get(f"https://moviepix.ir/wp-json/wp/v2/posts?per_page=50&page={page_number}&status=trash", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, timeout=30)
                break 

            except:
                continue
        if response.status_code == 200 :
            for i in response.json() :
                try :
                    ls.append({'id' : i['id'] , 'name_fa': i['title']['rendered']})
                except :
                    with open('ers.json', 'w', encoding='UTF-8') as file:
                        file.write(json.dumps(i, ensure_ascii=False))
                    input("error")
            progress_bar.update(1)
        else :
            break
print("finish!")
with open('trash_db.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(ls, ensure_ascii=False))
