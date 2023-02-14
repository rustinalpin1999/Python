import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL football stats(Rushing Data)')

st.markdown("""
Perform Basic Web Scraping of NFL Football players
* **Python Libraries Used: ** base64, pandas, streamlit, numpy, matplotlit, seaborn 
* ** Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/)
""")

st.sidebar.header('Input Features')
selected_year = st.sidebar.selectbox('Year',list(reversed(range(1990,2022))))

@st.cache
def load_data(year):
    url = "https://www.pro-football-reference.com/years/"+ str(year)+ "/rushing.htm"
    html = pd.read_html(url, header=1)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

#Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

#select Position
unique_position = ['RB','QB','WR','FB','TE']
selected_position = st.sidebar.multiselect('Position',unique_position, unique_position)

#Filter
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Position.isin(selected_position))]

st.header("Display Player stats of Team's")
st.write('Data Dimension:' + str(df_selected_team.shape[0])+ 'Row Dimension:'+ str(df_selected_team.shape[1]))
st.dataframe(df_selected_team)

def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href= "data:file/csv;base64,{b64}" download="playerstats.csv"> Download CSV Filed</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

#heatmap
if st.button('Intercorrelation Heatmap'):
     st.header('Intercorrelation Matrix Heatmap')
     df_selected_team.to_csv('footb output.csv',index= False)
     df = pd.read_csv('footb output.csv')

     corr = df.corr()
     mask = np.zeros_like(corr)
     mask[np.triu_indices_from(mask)] = True
     with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7,5))
        ax = sns.heatmap(corr,mask=mask,vmax=1,square=True)
st.pyplot()