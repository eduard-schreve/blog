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
st.subheader("Bolgpost #1")
st.write("Hello so this blog will be about the game that I’m creating, more spesifically the code and the "
"evolution of the code. ")
st.write("---")
st.write("I’m the Coffee Coder and let’s dive in. ")
st.write("---")
st.write("I begun my quest rather slowly in the middle of the summer vacation I was writing a chess program "
"but found it rather boring so I created my own game I set in the bacics you know a player, a "
"backround and movement controlls but things got difficult when it came to the enemy. The thing is "
"creating an enemy is not so difficult it is making the enemy follow the player that is hard, but I had "
"a solution, the enemy was going to follow a line.  More spesifically every point in that line and it "
"will decide what point to go to depending on the speed of enemy movement. I know this is "
"something every game developer struggles with so you can get my code on my [github repository](https://github.com/eduard-schreve/Astronomical) "
"also my friend [Nicolaas has an amasing blog](https://coding-discussions.blogspot.com/2024/04/my-experience-with-coding.html) about coding and you should really check it out, who "
"knows maybe you will get into coding like me. ")
st.write("---")
st.write("I’m the Coffee Coder goodbye!")
st.image("CoffeeCoder.png", "fig.1 Coffee Coder logo")
st.image("Jack E. Bresenham.png", "fig.2 Jack E Bresenham")
# st_lottie(home_animation, height=300)