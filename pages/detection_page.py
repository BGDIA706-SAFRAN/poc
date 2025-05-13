import streamlit as st
from PIL import Image
# from .models import iad_model


def display_detection_page():
    """ Anomalie detection interface """

    st.title('Visual Anomalie Detection')

    image_2_upload = st.file_uploader('Drop the image to analyse', type = ['jpg', 'png', 'jpeg'])

    if image_2_upload is not None :
        image = Image.open(image_2_upload)
        st.image(image, caption = 'Loaded image', use_container_width=True)

        st.write('🗨️ **Chatbot :** Quelles anomalies vous attendez-vous à détecter ?')

        anomalies = st.text_input("Describe anomalies you expect to track...")

        if anomalies:
            st.write(f"🗨️ **Chatbot**: You want to track the following anomalies : {anomalies}")
            st.write("🔍 Processing \U0001F6E0 ...")


if __name__ == '__main__':
    display_detection_page()