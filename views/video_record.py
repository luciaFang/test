import glob
import io
import time
from pathlib import Path

from revChatGPT.V1 import Chatbot
import cv2  # rgb. bgr
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import speech_recognition as sr
import streamlit as st
from moviepy.editor import *
from datetime import datetime

from deepface import DeepFace
from deepface.commons import functions

