import requests
import time
import psycopg2

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
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
  'cookie': '_gcl_au=1.1.1937204933.1605203504; _scid=16312ce0-2d84-47d9-bf8a-c4d21c9520e2; _ga=GA1.2.801958656.1605203504; visitor_id=5cf46760-d7fc-4dbc-bc8b-34e5d7303f72; _fbp=fb.1.1605203507022.962250653; __zlcmid=118ja39IgWz3NR5; nloc=en-egypt; _sctr=1|1609279200000; AKA_A2=A; _gcl_aw=GCL.1609482304.CjwKCAiAirb_BRBNEiwALHlnD4NQqBVU0H8m58xKai2yEbzuwhUCiNJRenmuh-RdntcORyUDXOD0nhoCLBgQAvD_BwE; _gid=GA1.2.1468877620.1609482305; _gac_UA-84507530-14=1.1609482307.CjwKCAiAirb_BRBNEiwALHlnD4NQqBVU0H8m58xKai2yEbzuwhUCiNJRenmuh-RdntcORyUDXOD0nhoCLBgQAvD_BwE; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM09HSTRNalUyWldNek9URTBaV1kyT0ROaVpHSXpPVEppWVRjMU1qazJOeUlzSW1saGRDSTZNVFl3TlRJd016VXdObjAuY0N2Y2htZjBCa1I2aXBJZW5BN3lMQ0xaRElVbmFLNzJ2SkpNcUdpV0JsMCIsImlhdCI6MTYwOTQ4NDYyNn0.Nma9eKoFscdgyYkIYdQLmW8cM9CiHyA0kU4mBMUaiQA; _nsc=nsv1.public.eyJzdGlkIjoiOTFkNDhkMjMtNWFmYS00ZTk0LTkyZWEtZDFhZTljY2Q5ZjY1Iiwic2lkIjoiNzhiODI1NmVjMzkxNGVmNjgzYmRiMzkyYmE3NTI5NjciLCJpYXQiOjE2MDk0ODQ2MjYsInZpZCI6IjVjZjQ2NzYwLWQ3ZmMtNGRiYy1iYzhiLTM0ZTVkNzMwM2Y3MiIsImhvbWVwYWdlIjp7fX1randhWkVJWS9TQVU3WEJnVmZIY1JsWmd0TUJBT2NWMjhrTnpudzR2Lys4PQ.MQ; _gat_UA-84507530-14=1; next-i18next=ar-EG; RT="z=1&dm=noon.com&si=92ec3ddd-c381-4934-981d-892dc6b5915b&ss=kjdw7fmk&sl=i&tt=fca&bcn=%2F%2F685b3918.akstat.io%2F&obo=e&rl=1&nu=d41d8cd98f00b204e9800998ecf8427e&cl=1gicd"; next-i18next=en-AE; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM09HSTRNalUyWldNek9URTBaV1kyT0ROaVpHSXpPVEppWVRjMU1qazJOeUlzSW1saGRDSTZNVFl3TlRJd016VXdObjAuY0N2Y2htZjBCa1I2aXBJZW5BN3lMQ0xaRElVbmFLNzJ2SkpNcUdpV0JsMCIsImlhdCI6MTYwNjM5MjA5NH0.ngGfIlYXHjA8-0zzSt_L_39TaCoXrWALbPba3uv42XM; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJM09HSTRNalUyWldNek9URTBaV1kyT0ROaVpHSXpPVEppWVRjMU1qazJOeUlzSW1saGRDSTZNVFl3TlRJd016VXdObjAuY0N2Y2htZjBCa1I2aXBJZW5BN3lMQ0xaRElVbmFLNzJ2SkpNcUdpV0JsMCIsImlhdCI6MTYwOTQ4MzIxMn0.2-fp0-NYoe7nTGVrTEjnC1mGwT2NStqR8dwxrRcBsxw; _nsc=nsv1.public.eyJzdGlkIjoiNTRkNTRiZTMtNjNmMC00OTcyLWEyNzktNDU1NDY2YWY3MjQ0Iiwic2lkIjoiNzhiODI1NmVjMzkxNGVmNjgzYmRiMzkyYmE3NTI5NjciLCJpYXQiOjE2MDk0ODMyMTIsInZpZCI6IjVjZjQ2NzYwLWQ3ZmMtNGRiYy1iYzhiLTM0ZTVkNzMwM2Y3MiIsImhvbWVwYWdlIjp7fX1qdHhDMGNDb0wveCtwdHBIaXZYV3Y2SE40TUZlY1UwWS9ESjZ6aUMydi84PQ.MQ'
}

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

def rate(b):
  payloadrate={"catalogCode":"noon","sku":b,"lang":None,"ratings":[1,2,3,4,5],"provideBreakdown":True,"page":1}
  responserate = requests.request("POST", urlrate, headers=headersrate, json=payloadrate)
  if(responserate.status_code==429):
    time.sleep(5)
    a=rate(b)
  else:
    responserate=responserate.json()
    a=[responserate['summary']['rating']]
    conn,cur=connn()
    cur.execute("INSERT INTO noon(rate) VALUES(%s)",(a))
    conn.commit()
  return(a)

lists=[['electronics-and-mobiles/mobiles-and-accessories'],['electronics-and-mobiles/computers-and-accessories'],['electronics-and-mobiles/video-games-10181'],['electronics-and-mobiles/television-and-video'],['electronics-and-mobiles/camera-and-photo-16165'],['electronics-and-mobiles/portable-audio-and-video'],['electronics-and-mobiles/wearable-technology'],['electronics-and-mobiles/home-audio'],['electronics-and-mobiles/accessories-and-supplies']]
for l in lists:
  l=l
  page_number=1
  a=True
  while a :
    payload={"brand":[],"category":l,"filterKey":[],"f":{},"sort":{"by":"popularity","dir":"desc"},"limit":50,"page":page_number}
    response = requests.request("POST", url, headers=headers, json=payload)
    if(response.status_code==429):
      time.sleep(5)
    else:
      response=response.json()
      v=response.get('hits')
      k=0
      for item in v:
        rating=rate(v[k]['sku'])
        print(rating,v[k]['url'])
        k+=1
    page_number+=1