import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib
import datetime
import random
# import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) -> DAVID 
# print(voices[1].id) -> ZIRA
engine.setProperty('voice', voices[1].id)
emaildict = {   
                "soham" : "bppcs.11500119115@gmail.com", 
                "subhrakanti" : "bppcs.11500119116@gmail.com", 
                "tathagata" : "bppcs11500119117@gmail.com", 
                "sourasish" : "bppcs.11500119119@gmail.com", 
                "swarnava" : "swarnavadas2014@gmail.com"
            }
def speak(audio):       #speak function
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Welcome Soham Das, I am back on duty. Waiting for your command")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sohamdas8697@gmail.com', 'PASSWORD')
    server.sendmail('sohamdas8697@gmail.com', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        speak("I am Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"Soham said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again....")
        speak("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
# searches
        if 'wikipedia' in query:
            speak("Searching")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
     
        # elif 'how is the weather' and 'weather' in query:

        #     url = 'https://api.openweathermap.org/'#Open api link here

        #     res = requests.get(url)

        #     data = res.json()

        #     weather = data['weather'] [0] ['main'] 
        #     temp = data['main']['temp']
        #     wind_speed = data['wind']['speed']

        #     latitude = data['coord']['lat']
        #     longitude = data['coord']['lon']

        #     description = data['weather'][0]['description']
        #     speak('Temperature : {} degree celcius'.format(temp))
        #     print('Wind Speed : {} m/s'.format(wind_speed))
        #     print('Latitude : {}'.format(latitude))
        #     print('Longitude : {}'.format(longitude))
        #     print('Description : {}'.format(description))
        #     print('weather is: {} '.format(weather))
        #     speak('weather is : {} '.format(weather))
        elif 'weather' in query:
            area = webbrowser.open("https://www.google.com/search?q=weather")
            speak("Weather forcast of area is")

        elif 'search' in query:
            query=query.replace("search","")
            speak("opening Google baaba")
            webbrowser.open("https://www.google.com/search?q="+query)
        elif 'play' in query:
            query=query.replace("play", "")
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
        elif 'open geeks for geeks' in query:
            speak("opening geeksforgeeks")
            webbrowser.open("geeksforgeeks.org")
#time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")   
            # strDate = datetime.datetime.now().strftime("%d-%m-20%y")
            print(f"Sir, the time is {strTime}")
            # print(f"Sir, the date is {strDate}")
            speak(f"Sir, the time is {strTime}")
            # speak(f"Sir, the date is {strDate}")
#introduction and chats
        elif 'hello' in query:
            speak("I am Jenny 1.0")
            speak("I am designed by Soham Das in his room, and i am happy with it")#, as he was very depressed, so he built me, to share his feelings, 
            speak("i am always ready to help anyone")#, in return of love
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
      
        elif "your feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 


# openings

        elif 'open vs code' in query:
            speak("Opening visual,studio,code")
            codePath="D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open dev c' in query:
            speak("opening c++, and try to complete atleast 10 problems")
            codePath="D:\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
        # elif 'how are you' in query:
        #     speak("I am fine!!")
        #     speak("What about you?")
        #     # print("What about you?")

# email 
        elif 'send an email to' in query:
            try:
                query = query.replace("send an email to ", "")
                to = emaildict[query]
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()    
                sendEmail(to, content)
                speak("Your email has been sent succesfully!")
                print("Your email has been sent succesfully!")
            except Exception:
                speak("Sorry! I am not able to send this email")
                print("Sorry! I am not able to send this email")
        
        elif 'tell some jokes' in query:
            print("Why did the cowboy buy a dachshund? Someone told him to get a long little doggy.")
            speak("Why did the cowboy buy a dachshund? Someone told him to get a long little doggy.")
        elif 'tell me something interesting' in query:
            print("It's estimated that there are 75 quintillion grains of sand on Earth. That's 75 with 17 zeros after it!")
            speak("It's estimated that there are 75 quintillion grains of sand on Earth. That's 75 with 17 zeros after it!")

# game
        elif 'game' in query:
            speak("Choose among, rock, scissor and stone")
            print("Choose among, rock, scissor and stone")
            pmove = str(input())
            moves = ["rock", "stone", "scissor"]
            cmove = random.choice(moves)
            if pmove==cmove:
                speak("the match is draw")
            elif pmove== "rock" and cmove== "scissor":
                speak("you wins")
            elif pmove== "rock" and cmove== "paper":
                speak("hurray!!!, i wins")
            elif pmove== "paper" and cmove== "rock":
                speak("you wins")
            elif pmove== "paper" and cmove== "scissor":
                speak("hurray!!, wins")
            elif pmove== "scissor" and cmove== "paper":
                speak("you wins")
            elif pmove== "scissor" and cmove== "rock":
                speak("huraay!!, i wins")

# toss
        elif 'toss' in query:
            moves = ['head', 'tail']
            tmove = random.choice(moves)
            speak("I choose " + tmove)

        elif 'location' in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You must be somewhere near here, as per Google maps") 
        
        elif 'ipl' in query:
            webbrowser.get().open("https://www.iplt20.com/")
            speak("Enjoy the live matches")

# shut down
        elif 'sleep' in query:
            speak("ok sir shutting down the system")
            quit()
