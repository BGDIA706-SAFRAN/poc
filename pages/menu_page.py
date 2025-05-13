import streamlit as st
from PIL import Image


def display_home_page():
    """
    Display the home page content
    """

    # Display main image

    # Display the representation text
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Anomalies Detection</h1>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>Welcome to the Anomaly Detection Web App!</h3>",
                unsafe_allow_html=True)
    st.markdown("---")

    # Description concise avec sections et icônes
    st.subheader("\U0001F4CC	 Main purpose")
    st.write("""
            This app helps detect **anomalies in images** from industrial contexts. 
            Simply go to the [detection page](detection_page), upload your image, and specify the anomalies you want to detect.
        """)

    st.subheader('\U0001F50D Informations')
    st.write(
            '\U0001F4A1 To **detect anomalies** on your media go to the [detection page](detection_page). \n'
            'Then upload the image you want to analyse as well as the informations about the anomalies you expect to catch.\n'
             '\U0001F916 You will be guided trough this by our chatbot anomachat. \n')

    st.write('\U0001F680 You might also want to check **tutorials** on the [examples page](examples_page). \n')
    st.write('\U0001F4D6 **Technical details** are available on the [Informations page](technical_infprmation).')

if __name__ == '__main__':
    display_home_page()
