import requests

key = '93485ccf46504e6fb5ed6e11e678bddc'
api_address= "http://newsapi.org/v2/everything?q=tesla&from=2021-01-15&sortBy=publishedAt&apiKey="+key
json_dat = requests.get(api_address).json()

ar = []

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1)+"," + json_dat["articles"][i]["title"]+".")
    return ar

#ass = news()
#print(ass)
