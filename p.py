# import requests,json
# data = requests.get('https://doeslist.herokuapp.com/api/data').text
# page =  json.loads(data)
# print(page,type(page))
# print(page['do_data'])
# with open(f'time_for_meeting.json', "w") as file1:
#     file1.write(json.dump(page['do_data']))
# import module.lib as lib
import os
# import module.lib2 as lib2
try:
    import speech_recognition as sr
    from selenium import webdriver
    import pyttsx3,random,os,datetime,json,requests
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from bs4 import BeautifulSoup as useMe

except ImportError:
    os.system('sudo apt install espeak')
    os.system('sudo apt install espeak')
    os.system('sudo apt-get install libxml2 libxml2-dev libxslt1-dev')
    os.system('sudo apt-get install lxml') 
    os.system('sudo apt-get install portaudio19-dev')
    os.system('pip install selenium')
    os.system('pip install speechRecognition')
    os.system('pip install pyaudio')
    os.system('pip install pyttsx3')
    # os.system('pip install webdriver-manager')

main_path = '/home/prem/Desktop/my_code/Nikki_verse/NikkiVersion5/' #/home/prem/Desktop/my_code/Nikki_verse/NikkiVersion4_5/chromedriver-sel/chromedriver
  
eng      = pyttsx3.init()
voices   = eng.getProperty('voices')
flag     = 'unmute'
joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = '/snap/bin/brave'
# chrome_options.add_argument('--remote-debugging-port=9222')
# # chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(main_path+'chromedriver-sel/chromedriver',chrome_options= chrome_options)

while 'p':
    try:
        def start():
            print('start!!!')
        start()
    except :
        print('error')
    finally:
        start()

   
# word = 'prem'
# if ('Nikki' in word):
#     user = 'nikkiai048@gmail.com'
#     pin = 'nikki@630'
# else:
#     user = 'giribabu22@navgurukul.org'
#     pin = 'prem@630'

# driver.switch_to.new_window()


# driver.implicitly_wait(15)
# # NikkiSay('ok boss sighin your google account')
# driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-1626596033%3A1670046303495198&continue=https%3A%2F%2Fsupport.google.com%2Faccounts%2Fthread%2F22873505%2Fthis-browser-or-app-may-not-be-secure-error-when-trying-to-sign-in-with-google-on-desktop-apps%3Fhl%3Den%23redirected%3Dtrue%26action%3DmeToo&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAvnBYNSkMPGdrDMBadDqhndi5j6GFVeVNHkuIfzpl5eBCIe2HlDZTZVl61RT60LATcwkmQwOw')
# driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys(user)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
# driver.find_element(By.NAME,'Passwd').send_keys(pin)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()



# url = 'https://meet.google.com/'
# driver.get(url)
# Data = driver.find_elements(By.CLASS_NAME,'VdLOD')
# li = Data[0].text.split('/n')
# for 

# page = requests.get(url).content
# soup = useMe(page,'html5lib')
# data =soup.prettify()
# r = soup.find('div' ,class_="VdLOD")
# print(r)
# cur = str(datetime.datetime.now()).split(' ')
# res = cur[1].split(':')

# per_cpu = psutil.cpu_percent(percpu=True)
# for idx, usage in enumerate(per_cpu):
#     print(f"CORE_{idx+1}: {usage}%")
# if end_time[0] ==  res[0] and end_time[1] == res[1]:


# time.sleep(6) wKIIs  /VdLOD yUoCvf JxfZTd