# import module.lib as lib
import service.alg as alg
import os

try:
    import speech_recognition as sr
    from selenium import webdriver
    import pyttsx3,os,json

except ImportError:
    os.system('sudo apt-get install python3-tk python3-dev')
    os.system('sudo apt install espeak')
    os.system('sudo apt install espeak')
    os.system('sudo apt-get install libxml2 libxml2-dev libxslt1-dev')
    os.system('sudo apt-get install lxml') 
    os.system('sudo apt-get install portaudio19-dev')
    os.system('pip install selenium')
    os.system('pip install speechRecognition')
    os.system('pip install pyaudio')
    os.system('pip install pyttsx3')
    os.system('pip install pyautogui')


error      = 1
netError   = 0
meeringMk  = 0
meetingEng = 0
main_path  = '/home/prem/Desktop/my_code/Nikki_verse/work_space/NikkiVersion5_5/' #/home/prem/Desktop/my_code/Nikki_verse/NikkiVersion4_5/chromedriver-sel/chromedriver
  
eng      = pyttsx3.init()
voices   = eng.getProperty('voices')
flag     = 'unmute'
joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]

windows_title = []
last_call     = None
c             = 0

with open(f'{main_path}Manage_file/main_save.json','r') as f:
    voice_save_file =  json.loads(f.read())

eng.setProperty('voice',voice_save_file[0]['voice'])
eng.setProperty('rate',voice_save_file[0]['rate'] )
eng.setProperty('volume', voice_save_file[0]['volume'])

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/snap/bin/brave'
    chrome_options.add_argument('--remote-debugging-port=9000')
    eng.say('wait boss setting the browser it will take few seconds')
    eng.runAndWait()
    driver = webdriver.Chrome(main_path+'chromedriver-sel/chromedriver',chrome_options= chrome_options)
    call     = alg.Service(driver,main_path,eng,windows_title,voice_save_file) # object create 
    li = driver.window_handles
    for i in range(len(li)):
        c = driver.window_handles[i]
        driver.switch_to.window(c)
        
        windows_title.append(driver.title)
    if 'Sign in - Google Accounts' not in windows_title:
        windows_title.append('Sign in - Google Accounts')
        call.NikkiSetGoogle()
        driver.get(f'file://{main_path}views/front_nikki.html')
    
except Exception as e:
    eng.say(f'oopes something wrong in first set up function. boss')
    eng.runAndWait()
    pass



while True:
    try:
        user_audio_text = call.NikkiQuickVoice()
        print(user_audio_text)
        if user_audio_text == None:
            TrueFalse = True
            while TrueFalse :
                    try:   
                        error,TrueFalse = call.NikkiCallBack(4,TrueFalse)
                    except:pass

        # user_audio_text = 'Nikki play music telugu song'
        call.NikkiCondition(user_audio_text)
        
    except sr.UnknownValueError:                              # call back code  
            call.NikkiSay('Could not understand audio')
            if error > 2:
                TrueFalse = True
                while TrueFalse :
                    try:   
                        error,TrueFalse = call.NikkiCallBack(error,TrueFalse)
                    except:pass
            else:
                error+=1

    except sr.RequestError:
        call.NikkiSay('network error check you wifi ')
        netError+=1
        if netError > 6:
            s = 0
            TrueFalse = True

    except Exception as e:
        try:
            e = str(e)
            if 'Message: unexpected alert open' in e:
                call.NikkiSay('Boss. Please close the browser')
                call.driver.quit()
            if 'unknown' in e or 'call' in e :
                eng.say('Unexpected somthing wrong dont worry Boss. i  am set it. wait boss setting the browser it will take few seconds')
                eng.runAndWait()

                chrome_options                  = webdriver.ChromeOptions()
                chrome_options.binary_location  = '/snap/bin/brave'
                chrome_options.add_argument('--remote-debugging-port=9000')
                driver    = webdriver.Chrome(main_path+'chromedriver-sel/chromedriver',chrome_options= chrome_options)
                call      = alg.Service(driver,main_path,eng,windows_title,voice_save_file) # object create 
                
                windowli    = driver.window_handles
                
                for i in range(len(windowli)):
                    c = driver.window_handles[i]
                    driver.switch_to.window(c)
                    windows_title.append(driver.title)
                    
                if ('Sign in - Google Accounts' not in windows_title):
                    windows_title.append('Sign in - Google Accounts')   
                    call.NikkiSetGoogle('prem')
                    driver.get(f'file://{main_path}/views/front_nikki.html')
                try:
                    call.NikkiCondition(user_audio_text)
                except:pass
                
        except Exception as e:
            # print(e,'<<<<<<<<<<<<','except')
            eng.say("don't do anything, Boss")
            eng.runAndWait()
