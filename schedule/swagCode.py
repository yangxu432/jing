import urllib2, urllib
import time
from BeautifulSoup import BeautifulSoup
import re
import json
def openPage():
    #68.180.195.138:80
    #proxy = urllib2.ProxyHandler({'http': '68.180.195.138:80'})
    #opener = urllib2.build_opener(proxy)
    opener = urllib2.build_opener()
    http_header = {
                    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.46 Safari/535.11",
                    "Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
                    "Accept-Language" : "en-us,en;q=0.5",
                    "Accept-Charset" : "ISO-8859-1",
                    "Content-type": "application/x-www-form-urlencoded",
                    "Host" : "www.mitfahrgelegenheit.de",
                    "Referer" : "http://www.mitfahrgelegenheit.de/mitfahrzentrale/Dresden/Potsdam.html/"
                    }
    opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) ')]

    urllib2.install_opener(opener)
    
    content = urllib2.urlopen('http://sc-s.com/').read()
    result = re.compile('<div class="p_code_data"(.*?)>', re.DOTALL).findall(content)

    return getElement(result)
def checkIsActive(p_expires_date):
    import datetime
    now = datetime.datetime.now()
    if  p_expires_date > now:
        return True
    else:
        return False

def getElement(result):
    #result = [' id="p_7507fa0649" \r\n  data-code-type="swagbucks" data-code="3Pennies" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Facebook" \r\n  data-location-link="https://www.facebook.com/swagbucks" \r\n  data-expires="1374764400" data-expires-f="08:00 AM PDT"\r\n  data-worth="3" data-timezone="PDT" data-thanks="sleepy"\r\n  data-countries="us,ca" data-is-update="true"', ' id="p_ee57eb9093" \r\n  data-code-type="swagbucks" data-code="LightsOut" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Twitter" \r\n  data-location-link="http://twitter.com/swagbucks/status/360278386079301633" \r\n  data-expires="1374735600" data-expires-f="12:00 AM PDT"\r\n  data-worth="3" data-timezone="PDT" data-thanks="scs-bot"\r\n  data-countries="*"', ' id="p_43c132013a" \r\n  data-code-type="swagbucks" data-code="GhostStory " data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Facebook" \r\n  data-location-link="https://www.facebook.com/swagbucks" \r\n  data-expires="1374728400" data-expires-f="10:00 PM PDT"\r\n  data-worth="4" data-timezone="PDT" data-thanks="erik"\r\n  data-countries="*"', ' id="p_98d02ef4a0" \r\n  data-code-type="swagbucks" data-code="BingoHall" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Facebook" \r\n  data-location-link="https://www.facebook.com/swagbucks" \r\n  data-expires="1374717600" data-expires-f="07:00 PM PDT"\r\n  data-worth="6" data-timezone="PDT" data-thanks="KawhiLeonardMVP"\r\n  data-countries="*"', ' id="p_89291eda0d" \r\n  data-code-type="swagbucks" data-code="SnackTime" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Blog (CA)" \r\n  data-location-link="http://blog.ca.swagbucks.com/" \r\n  data-expires="1374710400" data-expires-f="05:00 PM PDT"\r\n  data-worth="5" data-timezone="PDT" data-thanks="erik"\r\n  data-countries="*"', ' id="p_8396b7bbaa" \r\n  data-code-type="swagbucks" data-code="SnackTime" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Blog (UK)" \r\n  data-location-link="http://blog.uk.swagbucks.com/2013/07/camp-fun-and-snack-break.html" \r\n  data-expires="1374710400" data-expires-f="05:00 PM PDT"\r\n  data-worth="5" data-timezone="PDT" data-thanks="sleepy"\r\n  data-countries="uk"', ' id="p_69ebb057ac" \r\n  data-code-type="swagbucks" data-code="Canteen" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Facebook" \r\n  data-location-link="https://www.facebook.com/swagbucks" \r\n  data-expires="1374699600" data-expires-f="02:00 PM PDT"\r\n  data-worth="12" data-timezone="PDT" data-thanks="tired82812"\r\n  data-countries="*"', ' id="p_af8c784df9" \r\n  data-code-type="swagbucks" data-code="Smores" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Blog" \r\n  data-location-link="http://blog.swagbucks.com/2013/07/time-for-science-camp.html" \r\n  data-expires="1374692400" data-expires-f="12:00 PM PDT"\r\n  data-worth="7" data-timezone="PDT" data-thanks="sleepy"\r\n  data-countries="*"', ' id="p_775b055945" \r\n  data-code-type="swagbucks" data-code="tugOwar" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="games " \r\n  data-location-link="http://www.swagbucks.com/games" \r\n  data-expires="1374687000" data-expires-f="10:30 AM PDT"\r\n  data-worth="4" data-timezone="PDT" data-thanks="erik"\r\n  data-countries="*"', ' id="p_41f741f3bc" \r\n  data-code-type="swagbucks" data-code="MessHall" data-valid-at-name="Swagbucks" \r\n  data-valid-at-link="http://swagbucks.com" data-location-name="Facebook" \r\n  data-location-link="https://www.facebook.com/swagbucks" \r\n  data-expires="1374674400" data-expires-f="07:00 AM PDT"\r\n  data-worth="6" data-timezone="PDT" data-thanks="erik"\r\n  data-countries="*" data-is-update="true"']
    from collections import OrderedDict
    dic = OrderedDict();

    import datetime
    for i in result:
        p_code = re.compile('data-code="(.*?)"', re.DOTALL).findall(i)
        p_worth = re.compile('data-worth="(.*?)"', re.DOTALL).findall(i)
        time = re.compile('data-expires="(.*?)"', re.DOTALL).findall(i)[0]
        p_expires_date = datetime.datetime.fromtimestamp(int(time))

            
        dic.update({p_code[0]:{"code":p_code[0],
                               "worth":p_worth[0],
                               "expires":p_expires_date,
                               "isActive":checkIsActive(p_expires_date)
                               }
                    })
    now = datetime.datetime.now()
    active = {}
    expired = {}
    counter = 0
    '''
    for key, value in dic.iteritems() :

        if value["expires"] > now:
            print "Active", key, 
            print " "*5, 'Code:', value['code'],'Worth:', value['worth'], 'Expires:',str(value['expires'])
            active.update({counter:{'Code': value['code'],
                'Worth': value['worth'], 
                'Expires':str(value['expires'])}})
        else:
            print "Expired", key
            print " "*5, 'Code:', value['code'],'Worth:', value['worth'], 'Expires:',str(value['expires'])
            expired.update({counter:{'Code': value['code'],'Worth': value['worth'], 'Expires':str(value['expires'])}})
        print ""
        counter = counter + 1
    '''
    #for key, value in dic.iteritems() :
    #    value["expires"] = str(value["expires"])

    return dic


if __name__ == "__main__":
    print json.dumps(openPage())
