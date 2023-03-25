import streamlit as st
import pandas as pd


### Load player dataset ###
data = "raw_data/FM 2023.csv"
players = pd.read_csv(data)

### Retrieve list of clubs ###
clubs_df = players[['Club']].dropna(axis=0)
clubs = list(clubs_df['Club'].unique())
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
away_players = players.query(f"Club == '{away_team}'")



### Enter players ###

c1, c2, c3 = st.columns(3)

with c1:
    with st.form('Home Team Lineup:'):
        home_player1 = st.selectbox("Enter Home Team Player 1:", options = home_players)
        home_player2 = st.selectbox("Enter Home Team Player 2:", options = home_players)
        home_player3 = st.selectbox("Enter Home Team Player 3:", options = home_players)
        home_player4 = st.selectbox("Enter Home Team Player 4:", options = home_players)
        home_player5 = st.selectbox("Enter Home Team Player 5:", options = home_players)
        home_player6 = st.selectbox("Enter Home Team Player 6:", options = home_players)
        home_player7 = st.selectbox("Enter Home Team Player 7:", options = home_players)
        home_player8 = st.selectbox("Enter Home Team Player 8:", options = home_players)
        home_player9 = st.selectbox("Enter Home Team Player 9:", options = home_players)
        home_player10 = st.selectbox("Enter Home Team Player 10:", options = home_players)
        home_player11 = st.selectbox("Enter Home Team Player 11:", options = home_players)
        st.form_submit_button('Submit')



with c3:
    with st.form('Away Team Lineup:'):
        away_player1 = st.selectbox("Enter Away Team Player 1:", options = away_players)
        away_player2 = st.selectbox("Enter Away Team Player 2:", options = away_players)
        away_player3 = st.selectbox("Enter Away Team Player 3:", options = away_players)
        away_player4 = st.selectbox("Enter Away Team Player 4:", options = away_players)
        away_player5 = st.selectbox("Enter Away Team Player 5:", options = away_players)
        away_player6 = st.selectbox("Enter Away Team Player 6:", options = away_players)
        away_player7 = st.selectbox("Enter Away Team Player 7:", options = away_players)
        away_player8 = st.selectbox("Enter Away Team Player 8:", options = away_players)
        away_player9 = st.selectbox("Enter Away Team Player 9:", options = away_players)
        away_player10 = st.selectbox("Enter Away Team Player 10:", options = away_players)
        away_player11 = st.selectbox("Enter Away Team Player 11:", options = away_players)
        st.form_submit_button('Submit')
