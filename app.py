import streamlit as st
import pandas as pd


active = False

### Load player dataset ###
data = "raw_data/FM 2023.csv"
players = pd.read_csv(data)

### Retrieve list of clubs ###
clubs_path = "raw_data/final.csv"
clubs_df = pd.read_csv(clubs_path)
clubs = list(clubs_df['home_team_name'].unique())
clubs.sort()


### UI Design Below ###

st.markdown("<h1 style='text-align: center; color: red;'>SportsAnalytics</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'>Football Outcome Predictor</h1>", unsafe_allow_html=True)


### Enter home and away teams ###

a1, a2, a3 = st.columns(3)

with a1:
    home_team = st.selectbox("Home Team:", options = clubs)


with a3:
    away_team = st.selectbox("Away Team:", options = clubs)


### Get players from each team ###
home_players = players.query(f"Club == '{home_team}'")
home_players = list(home_players['Name'])
home_players.sort()
away_players = players.query(f"Club == '{away_team}'")
away_players = list(away_players['Name'])
away_players.sort()


### Enter players ###


with st.form('Matchup:'):

    c1, c2, c3 = st.columns(3)

    with c1:
        home_lineup = st.multiselect(
        f'Select the starting lineup:',
        home_players, key='home_lineup')
        st.write(len(home_lineup))

        home_form = st.text_input('Please enter the last 5 results of the home team (e.g. WWDDL):')



    with c3:
        away_lineup = st.multiselect(
        f'Select the starting lineup:',
        away_players, key='away_lineup')
        st.write(len(away_lineup))

        away_form = st.text_input('Please enter the last 5 results of the away team (e.g. WWDDL):')


    with c2:
        st.form_submit_button("Submit")
