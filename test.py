
import requests
for i in range(10000000) :
    request = requests.post("https://seeko.film/api/v1/ghost/get/getaffiliatelinks?id=ff8dcc10-17ff-11ed-b206-d3db3132bd8b&type=movie&ref=2", headers={ 'Accept': 'application/json'})
    print(request.status_code)
    print(i)