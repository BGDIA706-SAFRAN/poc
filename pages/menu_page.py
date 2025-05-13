import streamlit as st
from PIL import Image


def display_menu():
    """
    Display the menu page content
    """

    # Display main image

    # Display the representation text
    st.title("Anomalies detection")

    st.header('Informations')
    st.write(' Welcome to Anomalie detection web app ! This application aims to help anomalie detection on industrial context. \n'
            ':bulb: To use this functionality go to the detection page accessible trought the navigation bar on your left. \n'
             'Then upload the image you want to analyse as well as the informations about the anomalies you expect to catch.\n'
             ':robot: You will be guided trough this by our chatbot anomachat. \n')


