import requests , json
from tqdm import tqdm
from colorama import Fore, Style

directors = {'directors' : []}
with tqdm( 
          bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:.1f}%] Remaining: {remaining}", 
          colour="green", 
          dynamic_ncols=True,  
          miniters=1) as progress_bar:  
    progress_bar.set_description(f"{Fore.CYAN}Processing{Style.RESET_ALL}")

    for i in range(1 , 200) :
        for attempt in range(3):
            try :
                response = requests.get(f'https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/director?per_page=100&page={i}' , timeout=30)
                break
            except :
                continue
        
        if response.status_code == 200 :
            if len(response.json()) == 0 :
                break
            for j in response.json() :
                directors['directors'].append({'name' : j['name'] , 'id' : j['id']})
        
        else :
            print("error")
            exit()
        progress_bar.update(1)

with open('directors.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(directors, ensure_ascii=False))