import streamlit as st

image_path = "TPhead.png"
st.image(image_path, use_column_width=True)



recorded_file = 'output_sample.mp4'
sample_vid = st.empty()
sample_vid.video(recorded_file)

    
    

    


