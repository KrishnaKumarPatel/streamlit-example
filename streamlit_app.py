import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_Training = st.container()


data_file = 'student.csv'
# This is a cache. It runs only once when the page is loaded. If the user selects any value
# from interactive options, the entire code is loaded Except cache. This should save some time by
# not loading the same data again and again
@st.cache
def get_data(data_file):
    student_data = pd.read_csv(data_file)
    return student_data


with header:
    st.title('This is a title.')
    st.text("This is a lil bit about the project I'm working on.")

with dataset:
    st.header('This is a header.')
    st.text("This dataset describes a pdb file which we'll be learning about.")
    student_data = get_data(data_file)
    st.write(student_data.head(10))
    st.header('Bar Chart')
    chart_type = st.radio('Which coloumn do you want to plot?', options=['class', 'mark', 'gender'])
    data_distribution = pd.DataFrame(student_data[chart_type])
    st.bar_chart(data_distribution)
    st.header('Altair Chart')



with features:
    st.header('This is another header.')
    st.text('Here is a list.')
    st.markdown('* **list 1**: Description.')
    st.markdown('* *This is italicized*')
    st.markdown('* **This is bold**')
    st.markdown('* ***This is italicized and bold***')
    st.markdown('* ****This is italicized****')




with model_Training:
    st.header('Time to train data.')
    st.text('We\'ll train the machine based on correct pdb files so that when we upload an incorrect pdb file it can correct that.')
    sel_col, dis_col, useless_col = st.columns([2,1,1])
    user_sel = sel_col.slider('You get to select: ',min_value=10, max_value=100, value=20, step=5)     #value=20 ; default. step=5; users can only increase values by 5
    number_of_trees = dis_col.selectbox('How many trees should there be?', options=[100, 200, 'no limit'])
