import streamlit as st
from views import home, video_record, records
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image
from pathlib import Path
import base64

