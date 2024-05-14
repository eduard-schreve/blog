# python -m streamlit run app.py
import requests
import streamlit as st
# from streamlit_lottie import st_lottie

def load_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

home_animation = load_animation("https://lottie.host/9d81cf4f-ef02-4e30-801e-7d1539ab0eec/dFPlYOdROc.json")

st.set_page_config("The coffee coder", "CoffeeCoder.png", "wide")
st.title("The Coffee Coder")
st.subheader("Bolgpost #3 The last one")
st.write("Hello everyone, today we will discuss something other than my game. We will be discussing the "
" Arduino.")
st.write("---")
st.write("I’m the coffee coder and let’s dive in.")
st.write("---")
st.write("So let’s start with the blatantly obvious question of:”What is Arduino?” Well Arduino is a "
 "microcontroller there are many variatons but the most common is the Arduino Uno (figure 1) and "
 "for good reason, the Arduino is a cheap yet powerful microcontroller that can be used for many "
 "electronics projects including building your own robot.")
st.write("---")
st.write("The second question would be:“How do I aquire an Arduino and how do I start building stuff with "
 "it?” Well first you must go to an electronics shop near you that sells Arduino’s along with an "
 "Arduino buy some stuff for your project you want to build. Second: go to the [official Arduino website](https://www.arduino.cc/en/software) "
 "and get the latest version of the Arduino IDE. Last but not least build your circuit and "
 "connect it to your Arduino via a USB type B or whatever port your Arduino has.")
st.write("---")
st.write("Now be sure to check out my friend [Nicolaas’ blogpost](https://coding-discussions.blogspot.com/2024/04/my-experience-with-coding.html) it is more about coding overall but it still is "
 "a realy nice blog.")
st.write("---")
st.write("I’m the Coffee Coder and have a good one!")
st.image("arduino uno.png", "fig.1 Arduino Uno")
# st_lottie(home_animation, height=300)