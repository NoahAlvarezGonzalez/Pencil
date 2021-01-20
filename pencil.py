import streamlit as st
import cv2
import PIL
from PIL import Image
import numpy as np
import base64
import io


# Convert the image uploaded by the user into a pencil sketch
def pencil(image):
    img = np.array(image)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)
    return pencil_sketch_img


def main():
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("")
        st.write("Drawing...")
        result = pencil(image)
        st.image(result, caption="Result", use_column_width=True)
        download = st.button('Download JPG File')
        if download:
            dl = PIL.Image.fromarray(result)
            buffered = io.BytesIO()
            dl.save(buffered, format="JPEG")
            dl_str = base64.b64encode(buffered.getvalue()).decode()
            href = f'<a href="data:file/jpg;base64,{dl_str}" download="pencil.jpg">Download JPG File</a>'
            st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
