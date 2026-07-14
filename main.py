import streamlit as st 
import cv2
from PIL import Image
import os
import qrcode


#files = st.file_uploader("Upload Image" , type=["jpg", "jpeg", "png"])

stage = "main"

if "stage" not in st.session_state:
    st.session_state.stage = "main"

st.title("Faizzy QR Scan")

def main():
           
    st.write(" ")
    st.write(" ")

    options = st.radio("select the Choice", options=["None","text","website" ])



    st.write(" ")

    st.write(" ")

    if options == "text":
        st.session_state.stage = "text"

    elif options == "website":
        st.session_state.stage = "website"

    
    else:
        st.write("Error")

    

def card ():
    st.write(" ")

   # image = Image.open(files)

    #edges = cv2.Canny(img, 100,200)

    card = Image.new('RGB', (400,700), 'white')
    
    st.write(" ")
    st.write(" ")

def text():

    st.header("Make Your Text Qr")
    st.write(" ")

    st.write(" ")

    text = st.text_input("Enter Your Text Here ....")

    st.write(" ")

    code = qrcode.make(text)

    code = code.get_image()

    st.image(code)

    st.write(" ")
    st.write(" ")

    if st.button("Return To Home"):
        st.session_state.stage = "home"

def website():
    st.header("Make Yoi Website Url into Qr")

    st.write(" ")
    st.write(" ")

    link = st.text_input("Website Url")

    st.write(" ")

    web = qrcode.make(link)

    web = web.get_image()

    st.write(" ")

    st.image(web)

    st.write(" ")
    if st.button("Return to Home"):
        st.session_state.stage = "home"






if st.session_state.stage == "main":
    main()

elif st.session_state.stage == "card":
    card()



elif st.session_state.stage == "text":
    text()

elif st.session_state.stage == "website":
    website()

