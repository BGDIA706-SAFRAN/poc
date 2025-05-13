import streamlit as st
from streamlit_option_menu import option_menu
from pages.menu_page import  display_home_page
from pages.technical_information import *
from pages.detection_page import display_detection_page
from pages.examples_page import display_examples_page



selected = option_menu(
    menu_title=None,
    options=["home", "Anomalie Detection", "About", "Examples"],
    icons=["house", "robot", "info-circle", "folder"],
    orientation="horizontal",
)


if selected == "home":
    display_home_page()
elif selected == "Anomalie Detection":
    display_detection_page()
elif selected == "About":
    display_about_page()
elif selected == "Examples":
    display_examples_page()