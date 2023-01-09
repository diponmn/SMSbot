import  requests

#headers required and bearer is authorization token

head={
    "Host": "search5-noneu.truecaller.com",
    "authorization": "Bearer a1i01--TU-jKXkAkHSBQTsbxUUlonfO_fm8M9WFnCbImysMQp5oLbHFxF6-4_P2N",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.59.7 (Android;9)"
 } 
  
def main(num):

    url='https://search5-noneu.truecaller.com/v2/search?countryCode=IN&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&adId=1af646b1-8cdf-4e8a-b9d4-349f546890c5&encoding=json&q='+str(num)
    req=requests.get(url,headers=head)
    try:
        data=req.json()
        if data:
            name=data['data'][0]['name'] if data['data'][0]['name'] else None                
            carrier=data['data'][0]['phones'][0]['carrier']  if data['data'][0]['phones'] else None
            email=data['data'][0]['internetAddresses'][0]['id']  if data['data'][0]['internetAddresses'] else None
            address=data['data'][0]['addresses'][0]['city']  if data['data'][0]['addresses'] else None
            info = [name,carrier,email,address]
            info = list(filter(None,info))
    except:
        return False

    
         
    return info

