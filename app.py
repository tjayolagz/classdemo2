import pandas as pd
import numpy as np
import streamlit as st
import json
import matplotlib.pyplot as plt
import altair as alt

st.title('Streamlit Class Demo')

st.write('Another day with python')

penguins =pd.read_csv('https://raw.githubusercontent.com/tjayolagz/instructionaldatasets/refs/heads/main/data/penguins.csv')

st.scatter_chart(data=penguins, x= 'flipper_length_mm', y = 'body_mass_g', x_label = 'Flipper Length (mm)', y_label = 'Body mass (g)', color = 'species')

st.area_chart(data=penguins,x='species',y='culmen_length_mm', x_label='Species', y_label = 'Culmen Depth (mm)', use_container_width=True)

st.bar_chart(data = penguins, y='flipper_length_mm', x='species', color='species', use_container_width=True, horizontal=True, x_label ='Species', y_label='Flipper Length (mm)')

st.sidebar.header("Select Options")
selected_category = st.sidebar.selectbox("Select Category",  options=[ 'All','Adele','Chinstrap','Gentoo'])

if selected_category != 'All':
    filtered_data = penguins[penguins['species']== selected_category]
else:
    filtered_data = penguins

st.write("### Matplotlib Histogram")
fig, ax=plt.subplots()
ax.hist(filtered_data['culmen_length_mm'], bins=30, color="skyblue", edgecolor="black")
ax.set_title("Matplotlib Histogram for Culmen Lengths")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

#st.pyplot(fig)

#st.write("### Seaborn Density Plot")
#fig, ax=plt.subplots()
#fig=sns.displot(filtered_data['culmen_depth_mm'], color="black", #kind='kde', ax=ax, fill=True)
#ax.set_title("Seaborn Density Plots for Culmen Lengths")
#ax.set_xlabel("Value")
#ax.set_ylabel("Density")
#st.pyplot(fig)

#st.write("### Altair Scatter Plot")

#scatter_plot=alt.Chart(filtered_data).mark_circle().encode(x=alt.X('flipper_length_mm',title='Flipper Length'),
#y=alt.Y('body_mass_g', title='Body Mass'), color=alt.Color('island', scale=alt.Scale(scheme="tableau10")),tooltip=['island','flipper_length_mm','body_mass_g']
#)


###make checkboxes and slider filter types and usethem
# pip install pipreqs
# streamlit run app.py
#pip install streamlit



#st.write("#### Matplotlib0")


st.sidebar.header("Select Options")
selected_category = st.sidebar.selectbox("Select Category", options=['All', 'Adelie', 'Chinstrap', 'Gentoo'])

# Filter data based on selection
if selected_category != 'All':
    filtered_data = penguins[penguins['species'] == selected_category]
else:
    filtered_data = penguins

# Matplotlib Histogram
st.write("### Matplotlib Histogram")
fig, ax = plt.subplots()
ax.hist(filtered_data['culmen_length_mm'], bins=30, color="skyblue", edgecolor="black")
ax.set_title("Matplotlib Histogram for Culmen Lengths")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Seaborn Density Plot
st.write("### Seaborn Density Plot")
fig, ax = plt.subplots()
sns.kdeplot(filtered_data['culmen_depth_mm'], color="black", fill=True, ax=ax)
ax.set_title("Seaborn Density Plot for Culmen Depths")
ax.set_xlabel("Value")
ax.set_ylabel("Density")
st.pyplot(fig)

# Altair Scatter Plot
st.write("### Altair Scatter Plot")
scatter_plot = alt.Chart(filtered_data).mark_circle().encode(
    x=alt.X('flipper_length_mm', title='Flipper Length'),
    y=alt.Y('body_mass_g', title='Body Mass'),
    color=alt.Color('island', scale=alt.Scale(scheme="tableau10")),
    tooltip=['island', 'flipper_length_mm', 'body_mass_g']
)
st.altair_chart(scatter_plot, use_container_width=True)