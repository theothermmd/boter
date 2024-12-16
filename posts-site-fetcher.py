import requests , json
from tqdm import tqdm
from colorama import Fore, Style
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2NhcnRvb25mbGl4LmlyIiwiaWF0IjoxNzM0Mzc1NzU4LCJuYmYiOjE3MzQzNzU3NTgsImV4cCI6MTczNjk2Nzc1OCwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMTk1In19fQ.U2Zzt_7xcTTbcdsZuwNcV75LpU2zlQWErEM9o7eucj0"
ls = []

with tqdm(total=31, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%] Remaining: {remaining}", colour="blue", dynamic_ncols=True, miniters=1) as progress_bar:
    progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")

    for page_number in range(1 , 200) :
        for attempt in range(3):
            try:
                response = requests.get(f"https://cartoonflix.ir/wp-json/wp/v2/posts?per_page=50&page={page_number}", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"}, timeout=30)
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
with open('post-db_cartoon_flix.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(ls, ensure_ascii=False))
