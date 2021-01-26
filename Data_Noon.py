import requests
import time
import psycopg2





urlrate = "https://www.noon.com/_svc/reviews/fetch/v1/product-reviews/list"
headersrate = {
  'content-type': 'application/json',
  'accept': 'application/json, text/plain, */*',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'accept-language': 'en-US,en;q=0.9',
}
def connn():
  conn = psycopg2.connect(database='Notify', user='postgres', password='1999', host='localhost', port='5432')
  cur = conn.cursor()
  return(conn,cur)


def category(w):
  conn,cur=connn()     
  cur.execute("INSERT INTO category(Name) VALUES (%s)",(w))
  conn.commit()  

def data(*v):
  conn,cur=connn()  
  for l in v:
    v=l['offer_code'],l['sku'],l['name'],l['is_buyable'],l['price']
    cur.execute("INSERT INTO Data_Noon(NoonID,sku,title,active,lastprice) VALUES (%s,%s,%s,%s,%s)",(v))
  conn.commit() 




lists=[['electronics-and-mobiles/mobiles-and-accessories'],['electronics-and-mobiles/computers-and-accessories'],['electronics-and-mobiles/video-games-10181'],['electronics-and-mobiles/television-and-video'],['electronics-and-mobiles/camera-and-photo-16165'],['electronics-and-mobiles/portable-audio-and-video'],['electronics-and-mobiles/wearable-technology'],['electronics-and-mobiles/home-audio'],['electronics-and-mobiles/accessories-and-supplies']]
for l in lists:
  url = "https://www.noon.com/_svc/catalog/api/search"
  payload="{\"brand\":[\"apple\"],\"category\":[\"electronics-and-mobiles/mobiles-and-accessories/mobiles-20905\"],\"filterKey\":[],\"f\":{},\"sort\":{\"by\":\"popularity\",\"dir\":\"desc\"},\"limit\":50,\"page\":2}"
  headers = {
  'authority': 'www.noon.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
  'x-locale': 'en-eg',
  'x-content': 'mobile',
  'x-mp': 'noon',
  'x-platform': 'web',
  'x-cms': 'v2',
  'content-type': 'application/json',
  'accept': 'application/json, text/plain, */*',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'origin': 'https://www.noon.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.noon.com/egypt-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/apple',
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8'}
  a=True
  page_number=1
  while a :
    payload={"brand":[],"category":l,"filterKey":[],"f":{},"sort":{"by":"popularity","dir":"desc"},"limit":50,"page":page_number}
    response = requests.request("POST", url, headers=headers, json=payload)
    if(response.status_code==429):
      time.sleep(7)
    else:
      response=response.json()
      v=response.get('hits')
      print(v)
      for q in response.get('navPills'):
        d=[q['code']]
    data(*v)
    category(d)
    page_number+=1
    
  



# category(*q)

# if(response.status_code==429):
#     time.sleep(5)
# else:
#     response=response.json()
#     a=response.get('hits')



# def category(*w):
#   conn,cur=connn()     
#   cur.execute("INSERT INTO category(Name) VALUES (%s)",(w))
#   conn.commit()  

  # m=0
  # for z in n:
  #   print(z)
  #   m+=1
  # q=response['search']['category']
  # k=0
  # for item in v:
  #   rating=rate(v[k]['sku'])
  #   k+=1