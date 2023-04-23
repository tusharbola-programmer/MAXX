from mainbrain_p_and_s import get_response_txt
from other.getpaths import getpaths
from schedule.alarm import check_alarm
d=getpaths()
screenre=d[0]
screenshot=d[1]
taskps=d[2]
api=d[3]
webdriver='webdriverpth/chromedriver.exe'



while True:
    check_alarm()
    q=input("Query: ")
    get_response_txt(apipath=api,query=q,screenshotloc=screenshot,screenreloc=screenre,web=webdriver)
