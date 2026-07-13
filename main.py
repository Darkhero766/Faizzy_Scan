import streamlit as st 
import cv2
from PIL import Image
import os

files = st.file_uploader("Upload Image" , type=["jpg", "jpeg", "png"])

stage = "main"

if "stage" not in st.session_state:
    st.session_state.stage = "main"

st.title("Faizzy Scan")

def main():
    if files is not None:

     #   pil = Image.open(files)
        
        files.save("cat.jpg")
        
        image = cv2.imread(mine)
        st.write(" ")
        st.write(" ")

        st.image(image, caption="Original", width=500)

    st.write(" ")

    st.write(" ")

    if st.button("Cut Edges"):
        st.session_state.stage = "edge"

    

def edge ():
    st.write(" ")

    image = cv2.imread(img)

    edges = cv2.Canny(img, 100,200)
    
    st.write(" ")
    st.write(" ")

    st.image(edges)


if st.session_state.stage == "main":
    main()

elif st.button.stage == "edge":
    edge()

