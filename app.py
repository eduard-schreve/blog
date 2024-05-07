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
st.subheader("Bolgpost #2")
st.write("Hello again today we’ll be talking about noise, more specifically Perlin and white noise")
st.write("---")
st.write("I’m the Coffee Coder and let’s dive in. ")
st.write("---")
st.write("So perlin noise (figure 1) is a natural looking random generator which can be used to create game"
 "maps and make it look realistic a noise which is also used is fractal brownian motion."
 "Perllin noise was first created by Ken Perlin (figure 2) in 1983 for the movie: Tron to"
 "create natural looking patterns as previously mentioned.")
st.write("---")
st.write("Next: white noise (figure 3) is used, in my game for example, to put trees and other objects at"
 "random places in the game map to make it more natural looking."
 "White noise can be seen in the everyday world when you turn on the TV and it just gives you static"
 "well that static is a visual example of white noise.")
st.write("---")
st.write("And hey be sure to check out my friend Nicolaas’ blog it is also about coding and I think it is a very"
 "intuative post and this one and I find it highly interesting as I’m sure you will too.")
st.write("---")
st.write("I’m the coffee coder and have a good one!")
st.image("pelin noise.png", "fig.1 perlin noise")
st.image("ken perlin.png", "fig.2 Ken Perlin")
st.image("white noise.png", "fig.3 White noise")
# st_lottie(home_animation, height=300)