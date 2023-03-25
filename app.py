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
home_players = list(home_players['Name'])
home_players.sort()
away_players = players.query(f"Club == '{away_team}'")
away_players = list(away_players['Name'])
away_players.sort()


### Enter players ###

c1, c2, c3 = st.columns(3)

with c1:
    with st.form('Home Team Lineup:'):
        home_player1 = st.selectbox("Enter Home Team Player 1:", options = home_players)
        home_players.pop(home_player1)
        home_player2 = st.selectbox("Enter Home Team Player 2:", options = home_players)
        home_players.pop(home_player2)
        home_player3 = st.selectbox("Enter Home Team Player 3:", options = home_players)
        home_players.pop(home_player3)
        home_player4 = st.selectbox("Enter Home Team Player 4:", options = home_players)
        home_players.pop(home_player4)
        home_player5 = st.selectbox("Enter Home Team Player 5:", options = home_players)
        home_players.pop(home_player5)
        home_player6 = st.selectbox("Enter Home Team Player 6:", options = home_players)
        home_players.pop(home_player6)
        home_player7 = st.selectbox("Enter Home Team Player 7:", options = home_players)
        home_players.pop(home_player7)
        home_player8 = st.selectbox("Enter Home Team Player 8:", options = home_players)
        home_players.pop(home_player8)
        home_player9 = st.selectbox("Enter Home Team Player 9:", options = home_players)
        home_players.pop(home_player9)
        home_player10 = st.selectbox("Enter Home Team Player 10:", options = home_players)
        home_players.pop(home_player10)
        home_player11 = st.selectbox("Enter Home Team Player 11:", options = home_players)
        home_players.pop(home_player11)
        st.form_submit_button('Submit')



with c3:
    with st.form('Away Team Lineup:'):
        away_player1 = st.selectbox("Enter Away Team Player 1:", options = away_players)
        away_players.pop(away_player1)
        away_player2 = st.selectbox("Enter Away Team Player 2:", options = away_players)
        away_players.pop(away_player2)
        away_player3 = st.selectbox("Enter Away Team Player 3:", options = away_players)
        away_players.pop(away_player3)
        away_player4 = st.selectbox("Enter Away Team Player 4:", options = away_players)
        away_players.pop(away_player4)
        away_player5 = st.selectbox("Enter Away Team Player 5:", options = away_players)
        away_players.pop(away_player5)
        away_player6 = st.selectbox("Enter Away Team Player 6:", options = away_players)
        away_players.pop(away_player6)
        away_player7 = st.selectbox("Enter Away Team Player 7:", options = away_players)
        away_players.pop(away_player7)
        away_player8 = st.selectbox("Enter Away Team Player 8:", options = away_players)
        away_players.pop(away_player8)
        away_player9 = st.selectbox("Enter Away Team Player 9:", options = away_players)
        away_players.pop(away_player9)
        away_player10 = st.selectbox("Enter Away Team Player 10:", options = away_players)
        away_players.pop(away_player10)
        away_player11 = st.selectbox("Enter Away Team Player 11:", options = away_players)
        away_players.pop(away_player11)
        st.form_submit_button('Submit')
