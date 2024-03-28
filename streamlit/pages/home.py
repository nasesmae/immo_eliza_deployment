import streamlit as st
from PIL import Image

image_path = r"d:\1-BeCode\p12\streamlit\images\header.webp"
new_width = 1600
new_height = 300

img = Image.open(image_path)
# Use Image.Resampling.LANCZOS for high-quality downsampling
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
img.save(image_path)  # Overwrite the original image or save as a new file

# Display a logo and a title using raw strings for paths
st.image(image_path)

with st.sidebar:
    # Use a raw string for the path
    st.image(r"d:\1-BeCode\p12\streamlit\images\logo.webp", width=100)

st.title("Price Prediction API")
st.subheader("Our project")
st.markdown(
    """
    Property prices are more than just numbers; they're essential for everyone involved in real estate, from professionals to private individuals. Our tool focuses on empowering private sellers and buyers, helping them understand and decide on property prices easily and independently.

    Here's what our app offers:

    - Direct evaluations without intermediaries.
    - Quick, accurate, and trustworthy assessments.
    - A simple and friendly user experience.

    We aim to provide dependable price estimations by analyzing critical property features with advanced data analysis and machine learning.

    We plan to enhance our app with more market insights for everyone's benefit.

    Stay tuned for updates: [GitHub](https://github.com/nasesmae/immo.eliza.deployment)

    Enjoy exploring!
    """
)
