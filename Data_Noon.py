import requests
import time
import psycopg2

def connn():
  conn = psycopg2.connect(database='database', user='postgres', password='1999', host='localhost', port='5432')
  cur = conn.cursor()
  return(conn,cur)

def category(w):
  conn,cur=connn()     
  cur.execute("INSERT INTO category(sweetName) VALUES (%s)",(w))
  conn.commit()  

def data(*v):
  conn,cur=connn() 
  for l in v:
    if 'product_rating' in l:
      if l['sale_price']== None :
        v=l['offer_code'],l['sku'],l['name'],l['is_buyable'],l['price'],l['product_rating']['value'],l['brand'],l['image_key']
      else:
        v=l['offer_code'],l['sku'],l['name'],l['is_buyable'],l['sale_price'],l['product_rating']['value'],l['brand'],l['image_key']

      cur.execute("INSERT INTO noon(noonID,sku,title,active,lastprice,rate,manufacture,mainimg) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(v))

    else:
      if l['sale_price']== None :
        v=l['offer_code'],l['sku'],l['name'],l['is_buyable'],l['price'],l['brand'],l['image_key']
      else:
        v=l['offer_code'],l['sku'],l['name'],l['is_buyable'],l['sale_price'],l['brand'],l['image_key']
      cur.execute("INSERT INTO noon(noonID,sku,title,active,lastprice,manufacture,mainimg) VALUES (%s,%s,%s,%s,%s,%s,%s)",(v))
  conn.commit() 
def Datapayload():
  payload={"brand":[],"category":l,"filterKey":[],"f":{},"sort":{"by":"popularity","dir":"desc"},"limit":50,"page":page_number}
  response = requests.request("POST", url, headers=headers, json=payload)
  if(response.status_code==429):
    print(response.status_code)
    time.sleep(5)
    w=Datapayload()
  else:
    response=response.json()
    w=response.get('hits')
    for m in w:
      m=[m]
      category(l) 
      data(*m)
      print(l)
      print(m)
  # print(w)
  return w
lists=[['electronics-and-mobiles/mobiles-and-accessories'],['electronics-and-mobiles/computers-and-accessories'],['electronics-and-mobiles/video-games-10181'],['electronics-and-mobiles/television-and-video'],['electronics-and-mobiles/camera-and-photo-16165'],['electronics-and-mobiles/portable-audio-and-video'],['electronics-and-mobiles/wearable-technology'],['electronics-and-mobiles/home-audio'],['electronics-and-mobiles/accessories-and-supplies']]
for l in lists:
  l=l
  page_number=1
  a=True
  while a :
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
    Datapayload()
    print(page_number)  
    page_number+=1
    
  