import streamlit as st
import plotly.express as px
from backend import get_data

try:
    st.title(f"Weather Forecast for the Next Days.")
    place = st.text_input("Place")
    days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select no. of days")
    option = st.selectbox("Select Data to view", ("Temperature", "Sky"))
    st.subheader(f"{option} for the next {days} days in {place}")


    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            Temperature = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=Temperature, labels={"x": "Date", "y": "Temperature(c)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_condition =[dict['weather'][0]['main'] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=115)
except:
    st.info("You entered wrong information!")