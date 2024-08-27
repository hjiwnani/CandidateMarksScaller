import streamlit as st
import numpy as np

# Function to scale the score
def scale_score(score, old_min=0, old_max=211, new_min=0, new_max=10):
    scaled_score = (score - old_min) * (new_max - new_min) / (old_max - old_min) + new_min
    return scaled_score

# Streamlit app
st.title("Score Scaler")

# Input from the user
score = st.number_input("Enter a score (0-211):", min_value=0, max_value=211, value=0)

# Scale the score
scaled_score = scale_score(score)

# Display the result
st.write(f"Original score: {score}")
st.write(f"Scaled score (0-10 range): {scaled_score:.2f}")
