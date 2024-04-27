import streamlit as st #web app and camera
import numpy as np # for image processing 
from PIL import Image #Image processing 
import cv2 #computer vision 
import os
import time

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


st.title("PencilSketcher App - updated streamlit camera 📷 module")
st.write("This Web App is to help convert your photos to realistic Pencil Sketches")

# collect the user input 

# file_image = st.sidebar.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])

# collecting the input image from user camera 

file_image = st.camera_input(label = "Take a pic of you to be sketched out")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the contents of the file
    # image = uploaded_file.read()

    # convert the uploaded image into the pensil sketch

    uploaded_file= Image.open(uploaded_file)
    final_sketch = pencilsketch(np.array(uploaded_file))

    one, two = st.columns(2)
    with one:
        st.write("**Uploaded Photo**")
        st.image(uploaded_file, use_column_width=True)
    with two:
        st.write("**Output Pencil Sketch**")
        st.image(final_sketch, use_column_width=True)

    # Display the uploaded image
    # st.image(image, caption='Uploaded Image', use_column_width=True)


if file_image:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    one, two = st.columns(2)
    with one:
        st.write("**Input Photo**")
        st.image(input_img, use_column_width=True)
    with two:
        st.write("**Output Pencil Sketch**")
        st.image(final_sketch, use_column_width=True)
    if st.button("Generate image to download...........",):
        im_pil = Image.fromarray(final_sketch)
        im_pil.save('final_image.png')
        with open("final_image.png", "rb") as file:
            btn = st.download_button(
            label="Download image",
            data=file,
            file_name="final.png",
            mime="image/png"
            )
        # st.button("Download Sketch Images")
        # st.write('Download completed')



    
            file_path ="/PSEditor/final_image.png"




        time.sleep(10)
        os.remove(file_path)


else:
    st.write("You haven't uploaded any image file")


st.write("Courtesy: itsyou  - [Sketch Code](https://github.com/Yash19-Yash19/PSEditor)")

st.markdown("![](https://avatars.githubusercontent.com/u/73273674?s=400&u=2eedf54ee0e7d1bfd8eafc4a78f574074ace7130&v=4)")
