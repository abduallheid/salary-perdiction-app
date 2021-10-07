import os
import streamlit as st

def shorten_vid_option(opt):
    return opt.split("/")[-1]



def call_vedieo():
    st.title("vedios that explain some algorithmis which are uesd in model")

    st.write("""### on youtube""")


    vidurl = st.selectbox(
    "Pick a video to play",
    (

        "https://www.youtube.com/watch?v=ydvnVw80I_8",
        "https://www.youtube.com/watch?v=HoqXask9cN8",
        "https://www.youtube.com/watch?v=sI6mZqO91P4"
    ),
    0,
    shorten_vid_option,
    )

    x=st.video(vidurl)

    return x