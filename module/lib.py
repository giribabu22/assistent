import os

try:
    import speech_recognition as sr
    import pyttsx3,time,random,json,requests,datetime
    from bs4 import BeautifulSoup as useMe
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium import webdriver

except ImportError:
    os.system('pip install bs4')
    os.system('pip install selenium')
    os.system('pip install ib2to3')
    os.system('pip install speechRecognition')
    os.system('pip install pyaudio')
    os.system('pip install pyttsx3')

error    = 1
netError = 0
eng      = pyttsx3.init()
voices   = eng.getProperty('voices')
flag     = 'unmute'
joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]

eng.setProperty('voice', 'english_rp+f3')
eng.setProperty('rate',130)
eng.setProperty('volume', 2.0)

class Nikki_functions_class():
    def __init__(self,driver):
        self.driver = driver
        self.main_path = '/home/prem/Desktop/my_code/Nikki_verse/NikkiVersion4_5/'
        self.meetingEng = 0
        self.meeringMk = 0  
        self.last_time = datetime.datetime.now()
        self.new_day = 1
        
    def NikkiSay(self,data):
        eng.say(data)
        eng.runAndWait()

    def display_frontend(self):
        self.driver.get(f'file:///{self.main_path}views/front_nikki.html')
    
    def NikkiVoiceSource(self):
        self.NikkiTimetableOfMeeting()
        r = sr.Recognizer()                                                       
        with sr.Microphone() as source: 
            eng.setProperty('rate',200)
            self.NikkiSay('Listening…')
            eng.setProperty('rate',130)
            audio = r.listen(source,None,7) 
        return r.recognize_google(audio)

    def NIkkiblog(self):
      self.driver.get('https://exploring-blog-app.herokuapp.com')
      not_now2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forEmail']")))
      not_now3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forPassword']")))
      not_now2.send_keys('mynikki007@gmail.com')
      not_now3.send_keys('nikki@123')
      WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'submit']"))).click()  
      time.sleep(2)
      WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type = 'button']"))).click()  
      WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forText']"))).send_keys("Hello i'm NIkki by prem")
      WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='forTextarea']"))).send_keys("this is my first meet with the dlog bro nice to meet you bro")


    def NikkiPlaySong(self,song):
        self.NikkiSay('ok boss ! wait i am opening youtube music ')
        self.driver.switch_to.new_window()
        self.driver.get(f'https://music.youtube.com/search?q={song}')
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"yt-icon[class ='icon style-scope ytmusic-play-button-renderer']"))).click() 
        time.sleep(7)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='ytp-ad-skip-button ytp-button']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tp-yt-paper-icon-button[class='player-minimize-button style-scope ytmusic-player']"))).click()

    def NikkiYoutube(self,src_youtube):
        self.NikkiSay('ok boss ! wait i am opening youtube')
        res = src_youtube.replace(' ','+')     
        self.driver.switch_to.new_window()
        if len(src_youtube) >0:
            self.driver.get(f'https://www.youtube.com/results?search_query={res}')
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"yt-formatted-string[class ='style-scope ytd-video-renderer']"))).click()
        else:
            self.driver.get(f'https://www.youtube.com/')

    def NikkiBoring(self,r=True):
        list_play = ['telugu songs','ellie goulding','chaganti koteswara rao speeches mahabharatham etv','SriGarikipatiNarasimhaRaoOfficial','summer ball 2022']
        while r :
            self.NikkiSay('if you want i will play something on youtube, News and book for read ?')
            ply = self.NikkiVoiceSource()
            if 'YouTube' in ply:
                cho = random.choice(list_play)
                self.NikkiYoutube(cho)
                r = False
            elif 'News' in ply :
                self.NikkiNewstoday()
                r = False
            elif 'you play' in ply:
                res = ply.find('you play')+8
                self.NikkiYoutube(ply[res:])      
                r = False  
            elif 'book' in ply:
                res = ply.find('book')+9
                self.Nikkibook(ply[res:])
                r = False 
            else:
                r = True
        return r


    def NikkiFeelTalk(self):
        r = True
        while r:
            try:
                self.NikkiSay("what about you Boss ")
                myans = self.NikkiVoiceSource()
                if 'boring' in myans:
                    r = self.NikkiBoring(r)
                elif 'fine' in myans or 'great' in myans:
                    self.NikkiSay('great to hear from you')
                    r = False
                else:
                    self.NikkiSay('what you mean Boss!!')
            except sr.UnknownValueError:
                self.NikkiSay('Could not understand audio')
                pass
            except:
                pass


    def NikkiGreatings(self):
        t = datetime.datetime.now().hour
        res = 'good '

        if t >= 1 and t <= 11:
            res = 'good morning'
        elif t >= 12 and t <= 15:
            res = 'good afternoon'
        elif t >= 16 and t <= 21:
            res = 'good evening'

        self.NikkiSay(f'{res}')

    def NikkiWhoIs(self,user_audio_text):                              # this function help, to find the who is questions
        last_url = str(user_audio_text).replace(' ','+')
        url = 'https://www.google.com/search?q='+last_url
        page = requests.get(url).text
        soup = useMe(page,'lxml')
        data =soup.prettify()
        r = soup.find('div' ,class_="kCrYT").getText()
        self.NikkiSay(r)

    def NikkiMute(self,user_audio_text,flag = "Unmute"):
        if 'mute' in user_audio_text and len(user_audio_text) == 4 or user_audio_text[:5] == 'sleep':
            flag = 'mute'
            self.NikkiSay("i am mute But i am waiting for you boss")
            eng.setProperty('volume', 0)
        elif 'Unmute' in user_audio_text:
            voices = eng.getProperty('voices')
            eng.setProperty('voice', 'english_rp+f3')
            eng.setProperty('volume', 5.0)
            flag = 'Unmute'
            self.NikkiSay("i am unmute know")
        return flag

    def NikkiReminder(self,do='w',data=None):
        if do == 'r':
            f = open('/home/navgurukul/Desktop/workOftheday.txt')
            res = f.read()
            self.NikkiSay(res)
        if do == 'w':
            self.NikkiSay(data)
            f = open('/home/navgurukul/Desktop/workOftheday.txt','a')
            f.write(data)


    def NikkiTranslation(self,word):
        self.NikkiSay('ok boss opening  translate')
        self.driver.switch_to.new_window()
        self.driver.get('https://translate.google.co.in/?sl=en&tl=te&op=translate')
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"textarea[class ='er8xn']"))).send_keys(word)

    def NikkiTime(self,timeL):                                          # this function tell time 
        url = f'https://www.google.com/search?q=time+{timeL}'
        page = requests.get(url).content
        soup = useMe(page,'lxml')
        data = soup.find('div',class_="BNeawe iBp4i AP7Wnd")
        self.NikkiSay(f'time in {timeL,data.text}')
        return data.text,int(data.text[:-6])

    def NikkiNewstoday(self):
        latestNews = []
        url = 'https://www.ndtv.com/latest'
        page = requests.get(url).text
        soup = useMe(page,'lxml')
        d = soup.findAll('div',class_="news_Itm")
        r = random.randrange(0,len(d)-1)
        for i in d:
            latestNews.append(i.text)
        if latestNews[r] in 'window._taboola ':
            del latestNews[r]
        self.NikkiSay(f'this is today news-paper {latestNews[r]}')

    def NikkiSearch(self,search_in):                                    # this function search anything in the browser
        self.NikkiSay('ok boss i am opening google for you Boss')                                      
        self.driver.switch_to.new_window()
        self.driver.get('https://www.google.com/')
        src = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='q']")))
        src.clear()
        src.send_keys(search_in) 
        src.send_keys(Keys.ENTER)

    def NikkiWeather(self,cloud):                                       # this function tell weather  
        url = f'https://www.google.com/search?q=weather+{cloud}'
        page = requests.get(url).content
        soup = useMe(page,'lxml')
        r = open('x.html','w') 
        r.write(soup.prettify())
        data = soup.find('div',class_="kvKEAb")
        self.NikkiSay(f'weather in{cloud,data.text}')


    def NikkiCallBack(self,error,TrueFalse=True):
        user_audio_text = self.NikkiVoiceSource()
        if 'hello Nikki' in user_audio_text or 'are you there' in user_audio_text or 'hai Nikki' in user_audio_text or 'are there' in user_audio_text:
            eng.setProperty('voice', 'english_rp+f3')
            eng.setProperty('volume', 2.0)
            self.NikkiSay('Hello boss i here for you ___')
            error = 1
            TrueFalse = False
        elif 'mute' in user_audio_text or 'Unmute' in user_audio_text:
            self.NikkiMute(user_audio_text)
            if 'Unmute' in user_audio_text:
                self.NikkiSay('your in sleep mood')
        else:
            self.NikkiSay('this is try block')
            error=0
            s+=1
        return error,TrueFalse


    def NikkiCloseTab(self,tabName,user_audio_text):
        self.NikkiSay('ok Boss closing the tab')
        c = self.driver.window_handles[0]
        li = self.driver.window_handles
        if 'stop music' in user_audio_text :
            tabName = 'YouTube music'
        if len(li) > 1:
            for i in range(len(li)):
                if tabName == self.driver.title:
                    c = self.driver.window_handles[i+1]
                    self.driver.switch_to.window(c)
                    self.driver.close()
                    break
            else:
                if user_audio_text[-1] in ['1','2','3','4','5','6','7','8','9','0']:
                    num = int(user_audio_text[-1])
                    c = self.driver.window_handles[num]
                    self.driver.switch_to.window(c)
                c = self.driver.window_handles[len(li)-1]
                self.driver.close()
        else:
            self.NikkiSay('all tabs are closed boss')

    def Nikkibook(self,book):
        self.NikkiSay('wait boss i am finding your asking book')
        self.driver.switch_to.new_window()
        self.driver.get(f'https://www.google.com/search?tbm=bks&q={book}')
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='VvrH3b']"))).click()
    
    def NikkiFrontEnd(self):
        self.NikkiSay('wait boss setting the broser it will take few seconds')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = '/snap/bin/brave'
        chrome_options.add_argument('--remote-debugging-port=9224')
        self.driver = webdriver.Chrome(self.main_path+'chromedriver-sel/chromedriver',chrome_options= chrome_options)                
        self.driver.get(f'file://{self.main_path}views/front_nikki.html')

    def NikkiWritingHistory(self,user_audio_text):
        dic = {}
        with open(f'/{self.main_path}historyDataOfNikki/History_nikki.txt','r') as f:
            f2 =  f.read()
        with open(f'/{self.main_path}historyDataOfNikki/History_nikki.txt','a') as f:
            f.write(' '+user_audio_text+' \n')
        with open(f'/{self.main_path}historyDataOfNikki/History_nikki.txt','r') as f:
            f2 =  f.read()

        li = f2.split(' ')
        for word in li:
            if word in dic:
                dic[word] += 1  
            else: 
                dic[word] = 1
        del dic['\n']

        li = list(dic.values())
        li.sort(reverse = True)
        newDict = {}

        for ele in li:
            for k,v in dic.items():
                if ele == v:
                    newDict[k] = v
        with open(f'/{self.main_path}historyDataOfNikki/mostlyUseWords.json','w') as f1:
            f1.write(json.dumps(newDict,indent = 3))

    def NikkiMeeting(self,link):
        self.driver.switch_to.new_window()
        self.driver.get(link)
        try:
            time.sleep(4)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dismiss']"))).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Join now']"))).click()
        except:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Ask to join']"))).click()

    def NikkiSetGoogle(self,name):
        if 'prem' in  name:
            user = 'giribabu22@navgurukul.org'
            pin = 'prem@630'
        else:
            user = 'mynikki007@gmail.com'
            pin = 'Nikki@630'
        try:
            self.driver.implicitly_wait(15)
            self.NikkiSay('ok boss sighin your google account')
            self.driver.switch_to.new_window()
            self.driver.get('https://accounts.google.com/signin')
            self.driver.find_element(By.CSS_SELECTOR, "input#identifierId").send_keys(user)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
            self.driver.find_element(By.NAME,'Passwd').send_keys(pin)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))).click()
            time.sleep(5)
        except:
            self.NikkiSay('you already sign-in the google!')

    def NikkiTimetableOfMeeting(self):
        current_time = datetime.datetime.now()
        eng.setProperty('volume', 2.0)
        if self.new_day != current_time.day:
            self.NikkiSay('Hello boss, welcome back')
            self.NikkiGreatings()
            self.meeringMk = 0
            self.meetingEng = 0
            self.new_day = current_time.day
            
        li12 = f'{current_time - self.last_time }'
        li12 = li12.split(':')

        if int(li12[0]) > 1 or int(li12[1]) > 3:
            self.NikkiSay('you unlocked you laptop boss. what you want')

        if (current_time.strftime('%A') != 'Sunday'):
            if (current_time.hour == 10 and (current_time.minute >= 14 and current_time.minute <= 25 )) and self.meeringMk == 0 :
                self.NikkiSay('Boss, You have meeting with Meraki team you want to Join')
                self.meeringMk = 1
                self.NikkiSetGoogle('prem')
                self.NikkiMeeting('https://meet.google.com/vhr-ubsi-jcq')
                self.NikkiMute('sleep')

            elif (current_time.hour == 10 and (current_time.minute >= 39 and current_time.minute <= 44 )) and self.meetingEng == 0:
                self.NikkiSay('Boss, You have english meeting you want to Join')
                self.NikkiSetGoogle('prem')
                self.meetingEng = 1
                self.NikkiMeeting('https://meet.google.com/kkj-djxf-usn')
                self.NikkiMute('sleep')
        eng.setProperty('volume',0)
        self.last_time = current_time