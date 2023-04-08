import streamlit as st
import pandas as pd
import requests



def check_submit(home_lineup, home_form, away_lineup, away_form):
    go = True
    if (len(home_lineup) != 11 or len(away_lineup) != 11):
        st.error("Please verify number of players selected.",icon="🚨")
        go = False

    if (len(home_form) != 5 or len(away_form) != 5):
        st.error("Please verify Form input.",icon="🚨")
        go = False

    if not home_team_id:
        st.error("Please select Home Team.",icon="🚨")
        go = False


    if not away_team_id:
        st.error("Please select Away Team.",icon="🚨")
        go = False

    if go == False:
        st.error("Something is wrong!",icon="🚨")

    return go


### Load player dataset ###
data = "raw_data/player_attribute_2023.csv"
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
    home_team_id = clubs_df.query("home_team_name == '{home_team}'")['home_team_id']

with a3:
    away_team = st.selectbox("Away Team:", options = clubs)
    away_team_id = clubs_df.query("away_team_name == '{away_team}'")['away_team_id']


### Get players from each team ###
home_players = players.query(f"player_team_name == '{home_team}'")
home_players = list(home_players['Name'])
home_players.sort()
away_players = players.query(f"player_team_name == '{away_team}'")
away_players = list(away_players['Name'])
away_players.sort()


### Enter players ###

c1, c2, c3 = st.columns(3)

with st.form('Matchup:'):

    with c1:
        home_lineup = st.multiselect(
        f'Select the starting lineup:',
        home_players, key='home_lineup')
        st.write(len(home_lineup))


    with c3:
        away_lineup = st.multiselect(
        f'Select the starting lineup:',
        away_players, key='away_lineup')
        st.write(len(away_lineup))


    submitted = st.form_submit_button("Submit", use_container_width=True)


homeplayers_param = ''
for player in home_lineup:
    homeplayers_param += f'{player},'
homeplayers_param = homeplayers_param[:-1]


awayplayers_param = ''
for player in away_lineup:
    awayplayers_param += f'{player},'
awayplayers_param = awayplayers_param[:-1]


url = f'https://ourapi.url/predict?home_lineup={homeplayers_param}&away_lineup={awayplayers_param}&home_team_id={home_team_id}&away_team_id={away_team_id}'

st.write(url)


if submitted:
    if check_submit(home_lineup, home_form, away_lineup, away_form) == True:
        session = requests.Session()
        outcome = session.get(url).json()

        st.markdown(f"""#Outcome: {outcome}""")
