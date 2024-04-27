



# importing libraries
import streamlit as st #web app and camera
import numpy as np # for image processing 
from PIL import Image #Image processing 
import cv2 #computer vision 
import os
import time


# image conversion functions
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)


# Use wide option to view full page
st.set_page_config(layout="wide")


# setting up app title 
st.markdown(""" 
# P2S
""")


# setting up menu  buttons
rad =st.sidebar.radio(" Menu",["Home","Help","About us","Contact us"])


# if else staements for switching from one option to another
if rad=="Home":

    # displaying an image and tagline
    st.markdown("""
    #  Image  to Pencil Sketch 



    Before you convert  you have to upload or capture an image
    for the conversion of image to a pencil sketch image......😊🙂🙂😊😊
    """)


# adding ballons animation
    # st.balloons()


    # connecting download features to sidebar functions
    with st.sidebar:
            st.title("Image conversion")
            textOutput = st.selectbox(
                "How do you want your output data?",
                ('Select an option','Capture Image', 'Upload Image'))
                
                            



# code for image conversion





    if textOutput=='Select an option':
        displaying an image and tagline
        st.markdown("""
        ##  PencilSketch Editor....
    

        Before you convert  you have to upload or capture an image
        for the conversion of image to a pensil sketch image......😊🙂🙂😊😊
        """)


    elif textOutput=='Capture Image':
        file_image = st.camera_input(label = "Take a pic of you to be sketched out")

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

                            time.sleep(60)
                            os.remove(file_path)
                            file_path ="/PSEditor/final_image.png"

   



    elif textOutput=='Upload Image':

    
            uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    

            if uploaded_file  is not None:

            


                    input_img = Image.open(uploaded_file)
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

                                    time.sleep(60)
                                    os.remove(file_path)
                                    file_path ="/PSEditor/final_image.png"       


# help section stats here
if rad=="Help":
        #  how to use section
    st.markdown("""
    ## How to use...
        """)


    st.markdown("""    
        1.Select an option from the sidebar.
        """)


    st.markdown(""" 
        2.For capture image,take a picture and for remmoving option use clear photo.
        """)
    

    st.markdown("""    
        3.For upload image option you have to select and upload the image.
    """)


    st.markdown("""    
        4.After generating the image you will see a Generate download option.Select it and then you 
        will be able to download the image.""")


# note section
    st.markdown("""    
    ## Note:
    """)


    st.markdown(""" 
            1.Do not upload file size greater than 200mb.
            """)


    st.markdown(""" 
            2.Use appropriate file format like png,jpg & jpeg.
            """)
        

    st.markdown(""" 
            3.App supports only English language.
            """)


    # st.write("Hiii")
    st.write("This part is still in beta condition.......................👷‍♂️👷‍♂️👷")


# About section
if rad=="About us":
        
    st.markdown("""
    #  Developed by..... me.....
    """)
    



# Contact us section
if rad=="Contact us":
    st.write("Courtesy: itsyou  - [Sketch Code](https://github.com/Yash19-Yash19/)")
    st.markdown("![](https://avatars.githubusercontent.com/u/73273674?s=400&u=2eedf54ee0e7d1bfd8eafc4a78f574074ace7130&v=4)")




