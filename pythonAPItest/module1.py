from tkinter import W
from unicodedata import decimal
import requests
import json

from decimal import Decimal


def toFaren(num):
    celcius = num*(9/5) + 32
    format_celcius = "{:.2f}".format(celcius)
    return format_celcius


def weatherStr(weather):#implement clear day function
    weatherString=""
    if(weather=="pcloudyday" or weather=="pcloudynight" or weather=="pcloudy"):
        weatherString = "partly cloudy: 20%-60% coverage"
    elif(weather=="mcloudyday" or weather=="mcloudynight" or weather=="mcloudy"):
        weatherString = "moderatly cloudy: 60%-80% coverage"
    elif(weather=="cloudyday" or weather=="cloudynight"):
        weatherString = "very cloudy: >80% coverage"
    elif(weather=="humidday" or weather=="humidnight"):
        weatherString = "humidity >90% with cloud coverage <60%"
    elif(weather=="lightrainday" or weather=="lightrainnight" or weather=="lightrain"):
        weatherString = "precipitation less than 4mm/hr with cloud coverage >80%"
    elif(weather=="oshowerday" or weather=="oshowernight" or weather=="ishowerday" or weather=="ishowernight" or weather=="ishower" or weather=="oshower"):
        weatherString = "lgiht rain day"
    elif(weather=="lightsnowday" or weather=="lightsnownight" or weather=="lightsnow"):
        weatherString = "light rain"
    elif(weather=="rainday" or weather=="rainnight" or weather=="snowday" or weather=="snownight"):
        weatherString = "moderate precipitation"
    return weatherString

def getDogFacts():
    dog_facts = requests.get('http://dog-api.kinduff.com/api/facts')
    print(dog_facts.status_code)
    orgJson=dog_facts.json()

    orgText = json.dumps(orgJson, indent=2)
    factString= orgText['facts']
    return factString
    
def getCatFact():
    cat_facts = requests.get('https://catfact.ninja/fact')
    print(cat_facts.status_code)
    orgJson=cat_facts.json()
    factString = orgJson['fact']
    return factString


def getWeather():#implement custom latitude and longtitude 
    url = requests.get('http://www.7timer.info/bin/api.pl?lon=-71.412&lat=41.824&product=civillight&output=json')
    #print(url.status_code)
    JSONtxt = url.json()
    orgTXT = json.dumps(JSONtxt, indent=2)
    pyObj = json.loads(orgTXT)
    print(orgTXT)
    for obj in pyObj['dataseries']:
       dateStr = str(obj['date'])
       print("date:"+dateStr[4:6]+ "/"+dateStr[6:8]+"/"+dateStr[0:4] + "   " + "     max  temp in farenheit: " + str(toFaren(obj['temp2m']['max'])) + "     min temp in farenheit: " + str(toFaren(obj['temp2m']['min'])) + "     weather for today: " + weatherStr(obj['weather']))
       print("\n")

def dictionary():
    url = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/truck')
    JSONtxt=url.json()
    JSONstring = json.dumps(JSONtxt, indent=2)
    print(JSONstring)
    pyObj = json.loads(JSONstring)


    partofSpeech = "partOfSpeech: "
    phoneticPron = "Phonetic Pronunciation: "
    definition = "Definition: "
    sysnon = "sysnonyms: "
    antonyms = "antonyms: "


    print(phoneticPron +  pyObj[0]['phonetics'][1]['text'])
    
    j=0
    int(j)
    

    for defs in pyObj[0]['meanings']:
        print(defs['partOfSpeech'])
        print(defs['definitions'])
        print("\n")
            
            
        
        
        

    #print(partofSpeech + pyObj[0]['meanings'][0]['partOfSpeech'])
    #print(definition + pyObj[0]['meanings'][0]['definitions'][0]['definition'])
    #print(sysnon + str(pyObj[0]['meanings'][0]['synonyms']))




    



    
                               
    
   

