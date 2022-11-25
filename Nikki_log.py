import module.lib as lib
import os
# import module.lib2 as lib2
try:
    import speech_recognition as sr
    from selenium import webdriver
    import pyttsx3,random,os,datetime

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

error      = 1
netError   = 0
meeringMk  = 0
meetingEng = 0
main_path = '/home/prem/Desktop/my_code/Nikki_verse/NikkiVersion4_5/' #/home/prem/Desktop/my_code/Nikki_verse/NikkiVersion4_5/chromedriver-sel/chromedriver

eng      = pyttsx3.init()
voices   = eng.getProperty('voices')
flag     = 'unmute'
joke_nik = [['I invented a new word!Plagiarism!],[Did you hear about the mathematician who’s afraid of negative numbers?He’ll stop at nothing to avoid them.'],['Why do we tell actors to “break a leg?”Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.'],['Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”],[Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.'],['Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?”' ],['Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'],['A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”“Don’t worry,” said the doc. “Those are just contractions.”'],['A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”'],['Did you hear about the actor who fell through the floorboards?He was just going through a stage.'],['Did you hear about the claustrophobic astronaut? He just needed a little space.'],['Why don’t scientists trust atoms? Because they make up everything.'],['Why did the chicken go to the séance?To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.'],['Where are average things manufactured?The satisfactory.'],['How do you drown a hipster? Throw him in the mainstream.'],['What sits at the bottom of the sea and twitches?A nervous wreck.'],['What does a nosy pepper do? Gets jalapeño business!'],['How does Moses make tea? He brews.'],['Why can’t you explain puns to kleptomaniacs?They always take things literally.'],['How do you keep a bagel from getting away?Put lox on it.'],['A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”The doctor replies, “Sorry, I don’t follow you …”']]
try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/snap/bin/brave'
    chrome_options.add_argument('--remote-debugging-port=9224')
    driver = webdriver.Chrome(main_path+'chromedriver-sel/chromedriver',chrome_options= chrome_options)
except:
    print('error')
call     = lib.Nikki_functions_class(driver) # object create 
# call2    =  lib2.accounts(driver)                                 # object create lib2 class

driver.get(f'file://{main_path}/views/front_nikki.html')

eng.setProperty('voice', 'english_rp+f3')
eng.setProperty('rate',130)
eng.setProperty('volume', 2.0)

while True:
    try:
        user_audio_text = call.NikkiVoiceSource()
        if 'Nikki' in user_audio_text or 'Ni' in user_audio_text or 'ok' in user_audio_text:
            call.NikkiWritingHistory(user_audio_text,meetingEng,meeringMk)
            if 'open class' in user_audio_text or 'dsc class' in user_audio_text or 'class time' in user_audio_text:
                call.NikkiYoutube('https://youtu.be/Oe421EPjeBE')

            elif ('play' in user_audio_text and 'YouTube music' in user_audio_text ) or ('play 'in user_audio_text and ('music' in user_audio_text) or 'song' in user_audio_text) :
                if 'play songs in YouTube music' in user_audio_text:
                    f = user_audio_text.find('music')+5
                    song = user_audio_text[f:]
                else:
                    l = user_audio_text.split()
                    song = ' '.join(l[3:])
                call.NikkiPlaySong(song)

            elif 'blog' in user_audio_text or 'blog app' in user_audio_text:
                call.NIkkiblog()

            elif 'open YouTube' in user_audio_text or 'YouTube' in  user_audio_text :
                value_ = user_audio_text.find('YouTube')
                search_ = user_audio_text[value_+8:]
                call.NikkiYoutube(search_)
                
            elif 'translate' in user_audio_text or 'what is in Telugu' in user_audio_text:
                if 'Telugu' in user_audio_text:
                    call.NikkiTranslation(''.join(user_audio_text[23:]))
                else:
                    call.NikkiTranslation(''.join(user_audio_text[16:]))
            elif 'search' in user_audio_text or 'Google' in user_audio_text:
                if 'ok' in user_audio_text:res = user_audio_text[2:]
                else:res = user_audio_text[13:]
                call.NikkiSearch(res)

            elif 'hi' in user_audio_text or 'hello' in user_audio_text:
                call.timeFun()
                call.NikkiWork()

            elif 'what about you' in user_audio_text or 'what about you' in user_audio_text:
                call.NikkiSay("i'm Nikki i born in june 13 2022 developed by Prem kumar he is very creative person because he created me i respect him ")

            elif 'p***' in user_audio_text or 'sex videos' in user_audio_text :
                call.NikkiSay('what the hell you want man fuck your self')

            elif 'translation' in user_audio_text:
                call.NikkiTranslation(user_audio_text[17:])

            elif 'weather in' in user_audio_text:
                call.NikkiSay('ok boss')
                mn = user_audio_text.find('in')
                cloud = user_audio_text[mn+3:].lower()
                call.NikkiWeather(cloud) 

            elif 'what are you doing' in user_audio_text :
                call.NikkiSay("i'm still learning new things ")
                call.NikkiFeelTalk() 

            elif 'reading time' in user_audio_text or ('read' in user_audio_text and ('book' in user_audio_text or 'books' in user_audio_text)):
                call.NikkiSay('which book you want boss')
                res = call.NikkiVoiceSource()
                call.Nikkibook(res)

            elif 'feeling boring' in user_audio_text:
                call.NikkiBoring()

            elif 'how are you' in user_audio_text or 'how Nikki' in user_audio_text:
                call.NikkiSay("i'm doing great what about you")

            elif 'time in' in user_audio_text  :
                mn = user_audio_text.find('in')
                timeL = user_audio_text[mn+3:].lower()
                call.NikkiTime(timeL)

            elif 'who is' in user_audio_text:
                call.NikkiSay('ok Boss')
                call.NikkiWhoIs(user_audio_text[6:])
            
            elif 'any joke' in user_audio_text or 'tell' in user_audio_text and 'joke' in user_audio_text:
                r = random.randrange(0,len(joke_nik)-1)
                call.NikkiSay(f'ok boss {joke_nik[r],joke_nik[r]}')

            elif 'new movie' in user_audio_text or 'movie time' in user_audio_text:
                if 'elugu' in user_audio_text:
                    driver.get('https://ww16.ibomma.bar/telugu-movies/')
                else:
                    driver.switch_to.new_window()
                    driver.get('https://www.osee.in/movie')

            elif "news today" in user_audio_text or 'today news' in user_audio_text:
                call.NikkiSay('ok boss wait for a second')
                call.NikkiNewstoday()

            elif 'I love you' in user_audio_text or 'I love you' in user_audio_text :
                call.NikkiSay('hoo thank you i love you too Boss')

            elif 'bhai' in user_audio_text or 'exit' in user_audio_text or 'bye' in user_audio_text:
                call.NikkiSay(' bye boss i miss you ')
                break 

            elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
                call.NikkiMute(user_audio_text)

            elif 'set account' in user_audio_text or 'set google' in user_audio_text:
                call.NikkiSetGoogle('prem')

            elif ('set up' in user_audio_text or 'set' in user_audio_text and ('Browser' in user_audio_text or 'browser' in user_audio_text ))or 'new browser' in user_audio_text:
                call.NikkiFrontEnd()

            elif (('Close' in user_audio_text or 'close' in user_audio_text) and ('tab' in user_audio_text or 'Tab' in user_audio_text))or ('close the tab' in user_audio_text or 'stop music' in user_audio_text):
                tabName = user_audio_text[user_audio_text.find('ab')+3:]
                call.NikkiCloseTab(tabName,user_audio_text)

            elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
                flag =  call.NikkiMute(user_audio_text,flag)

            else:
                call.NikkiSay('i am still learning ')

        elif user_audio_text == 'what is your name' or user_audio_text in 'your name':
            call.NikkiSay('hello my name is NIKKI by prem')

        elif (('Close' in user_audio_text or 'close' in user_audio_text) and ('tab' in user_audio_text or 'Tab' in user_audio_text))or ('close the tab' in user_audio_text or 'stop music' in user_audio_text):
            tabName = user_audio_text[user_audio_text.find('tab')+4:]
            call.NikkiCloseTab(tabName,user_audio_text)

        elif 'how to use' in  user_audio_text or 'help' in user_audio_text:
            call.NikkiSay("you can ask first you need to say 'NIKKI' After 'Nikki play song' , news today, any joke, who is, time in ,open YouTube,open insta,weather ")
        
        elif 'mute' in user_audio_text or 'Unmute' in user_audio_text or 'sleep' in user_audio_text:
           flag =  call.NikkiMute(user_audio_text,flag)

        elif ('set up' in user_audio_text or 'set' in user_audio_text and ('Browser' in user_audio_text or 'browser' in user_audio_text ))or 'new browser' in user_audio_text:
            call.NikkiFrontEnd()

        elif 'set account' in user_audio_text or 'set google' in user_audio_text:
            call.NikkiSetGoogle('prem')
            
        else:
            call.NikkiSay('call my name and ask anything')
    except sr.UnknownValueError:                              # call back code 
            eng.say('Could not understand audio')
            eng.runAndWait()
            if error > 2:
                s = 0
                voices = eng.getProperty('voices')
                eng.setProperty('voice', 'english_rp+f3')
                eng.setProperty('volume',0)
                TrueFalse = True

                while TrueFalse :
                    try:   
                        error,TrueFalse = call.NikkiCallBack(error,TrueFalse)
                    except sr.UnknownValueError:
                        s+=1 
                        if s == 300:
                            call.NikkiSay('Hello boss i here to help you')
                            r = random.randrange(0,len(joke_nik)-1)
                            call.NikkiSay(joke_nik[r])   
                    except :
                        call.NikkiSay('oopes error boss')
                        pass
            else:
                error+=1
    except sr.RequestError:
        call.NikkiSay('network error check you wifi ')
        netError+=1
        if netError > 6:
            s = 0
            voices = eng.getProperty('voices')
            eng.setProperty('voice', 'english_rp+f3')
            eng.setProperty('volume',0)
            TrueFalse = True
    except Exception as e:
        call.NikkiSay('oopes MAIN ERROR boss')
        print(e)
