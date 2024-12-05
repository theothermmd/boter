import requests , json
headers = {"Content-Type": "application/json" }
apikeys = ['8812c608' , '6273c114' , '8812c608' , '42a575eb' , '54a50e39']
data = "tt0218817"
count = 0
for i in range(3) :
    imdb_data = requests.get( f"http://www.omdbapi.com/?i={data}&apikey={apikeys[count]}", headers=headers, timeout=30).json()

    if "Error" in imdb_data :
        print("Error")
        count += 1
        continue
    else :  
        print(imdb_data)