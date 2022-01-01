from sys import flags
import pyttsx3
import speech_recognition as sr
import bs4
import requests
from speech_recognition import UnknownValueError
import datetime as dt
import playsound
import time

global audio_file


class voiceboxx:
    def __init__(self):
        self.weather_api = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=serampore&appid=e95ca05942ec1468ead893f6222ee51e")
        self.high_pressure = "expeting a  hot climate"
        self.normal_pressure = "expecting a normal day"
        self.low_pressure = "expecting a  overcast or rainy day "
        self.audio_clock_data = []

    def speak(self, inpuut):
        voice = pyttsx3.init()
        voice.say(inpuut)
        voice.runAndWait()

    def ask_time(self):
        noww = dt.datetime.now()

        a = noww.strftime("%I:%M %p")
        return a.replace(":", " ")

    def what_Date(self):
        dater = dt.datetime.now()
        a = dater.strftime("%D")
        return a.replace("/", " ")

    def tempe(self):
        a = self.weather_api.json()
        temp = a["main"]["temp"]
        humidity = a["main"]["humidity"]
        final_temp = temp - 273.15 + 1
        return (
            str(int(final_temp))
            + "degree celcius"
            + "  and the humidity is around"
            + str(int(humidity))
        )

    def weather(self):
        b = self.weather_api.json()
        tempe = b["main"]["temp"]
        humid = b["main"]["humidity"]  # to later work on
        min_tempe = b["main"]["temp_min"]
        pressure = b["main"]["pressure"]
        place = b['name']
        final_tempe = tempe - 273.15 + 1
        # print(final_tempe)##for P.D.B
        pressure_quality = ""
        if int(pressure) > 1100:
            a = self.high_pressure
        elif int(pressure) < 980:
            a = self.low_pressure
        elif int(pressure) >= 1000:
            a = self.normal_pressure
        return f"todays weather in {place} is with temperature of {int(final_tempe)}degree celcius  and the skies are  {a}"
        # geolocation                         #float to str                                  #pressure

    def alarm_set(self):
        print("please try again?!#")
        speaker_alarm = sr.Recognizer()

# clock time input
        with sr.Microphone() as source2:
            audio_clocker = speaker_alarm.listen(source2)

        try:
            audio_clock = speaker_alarm.recognize_google(audio_clocker)
            self.audio_clock_data.append(audio_clock)

        except UnknownValueError or LookupError or UnboundLocalError:
            print("Please try again")
# clock
        ii = self.audio_clock_data[0][-5:]
        xy = (str(ii))
        if len(ii) < 4:

            xy = (str(ii))
            hours = (xy[0])

            minutess = (xy[1:])
            print(minutess)
        else:
            # xy=str(ii)
            hours = (xy[0:2])
            minutess = (xy[2:])

        # current_time_am_pm = dt.datetime.now().strftime('%p') #for later
        whileloop = True
        while whileloop:
            if dt.datetime.now().hour == int(hours) and dt.datetime.now().minute == int(minutess):
                playsound.playsound(
                    "C:\\Users\\syncm\Desktop\\everyThinG__Python\\vs_code_files\\nuclear-alarm.mp3")
                time.sleep(3)
                break
            else:
                continue


# initiating
man2 = voiceboxx()


def intiator():
    # microphone
    speaker = sr.Recognizer()
    with sr.Microphone() as source:
        aud = speaker.listen(source)
    try:
        print("BOOTING......")
        print("LISTENING.....")
        audio_file = speaker.recognize_google(aud)

        # audiofile is the file as input
    except UnknownValueError or LookupError or UnboundLocalError:
        man2.speak("pardon!")

    # initiation of object
    man1 = voiceboxx()
    # conditions
    if audio_file == "time":
        man1.speak("its now" + man1.ask_time())
        exit()
    if audio_file == "date":
        man1.speak("Today is" + man1.what_Date())
        exit()
    if audio_file == "what is the temperature":
        man1.speak(f"Now the temperature is {man1.tempe()} ")
        exit()
    if audio_file == "what is the weather today":
        man1.speak(man1.weather())
        exit()
    if audio_file == "alarm":
        man1.speak(man1.alarm_set())
    else:
        man1.speak("pardon ? ? ")


intiator()