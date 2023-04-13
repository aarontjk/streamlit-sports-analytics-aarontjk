import streamlit as st
import pandas as pd
import requests
from PIL import Image


st.markdown(
    """
    <style>
    span[data-baseweb="tag"] {
    background-color: grey !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )


def check_submit(home_lineup, home_team_id, away_lineup, away_team_id):
    go = True
    if (len(home_lineup) != 11 or len(away_lineup) != 11):
        st.error("Please verify number of players selected.",icon="🚨")
        go = False

    if not home_team_id:
        st.error("Please select Home Team.",icon="🚨")
        go = False

    if not away_team_id:
        st.error("Please select Away Team.",icon="🚨")
        go = False

    if go == False:
        st.error("Something is wrong!",icon="🚨")

    if not date_played:
        st.error("Please enter match date.",icon="🚨")

    return go


### Load player dataset ###
data = "raw_data/player_attribute_2023.csv"
players = pd.read_csv(data)

### Retrieve list of clubs ###
clubs_path = "raw_data/final.csv"
clubs_df = pd.read_csv(clubs_path)
clubs = list(clubs_df['home_team_name'].unique())
clubs.sort()
clubs.remove('Burnley')
clubs.remove('Norwich City')
clubs.remove('Watford')



### UI Design Below ###

st.markdown("<h1 style='text-align: center;'>SportsAnalytics</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Football Outcome Predictor</h1>", unsafe_allow_html=True)


### Enter home and away teams ###

a1, a2, a3 = st.columns(3)

with a2:
    date_played = st.date_input("Match Date:", value=None)

with a1:
    home_team = st.selectbox("Home Team:", options = clubs)
    home_team_id = clubs_df.query(f"home_team_name == '{home_team}'")['home_team_id'].iloc[0]
    url = f"https://images.fotmob.com/image_resources/logo/teamlogo/{home_team_id}_large.png"
    st.image(url, caption='Home Logo', use_column_width=True)


with a3:
    away_team = st.selectbox("Away Team:", options = clubs)
    away_team_id = clubs_df.query(f"away_team_name == '{away_team}'")['away_team_id'].iloc[0]
    url = f"https://images.fotmob.com/image_resources/logo/teamlogo/{away_team_id}_large.png"
    st.image(url, caption='Away Logo', use_column_width=True)


### Get players from each team ###
home_players = players.query(f"player_team_name == '{home_team}'")
home_players = list(home_players['player_name'])
home_players.sort()
away_players = players.query(f"player_team_name == '{away_team}'")
away_players = list(away_players['player_name'])
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


url = f'https://sportsanalytics-maaojgn3sq-ew.a.run.app/predict2?date_played={date_played}&home_lineup={homeplayers_param}&away_lineup={awayplayers_param}&home_team_id={home_team_id}&away_team_id={away_team_id}'


if submitted:
    if check_submit(home_lineup, home_team_id, away_lineup, away_team_id) == True:
        session = requests.Session()
        outcome = session.get(url).json()['home_predicted']
        if outcome == 0:
            outcome = 'LOSE'
            color = 'red'
        elif outcome == 1:
            outcome = 'DRAW'
            color = 'orange'
        elif outcome == 2:
            outcome = 'WIN'
            color = 'green'


        st.markdown(f"""
        <style>
        .big-font {{
            font-size:30px !important;
            width: 1000px;
            color: {color};
        }}
        </style>
        """, unsafe_allow_html=True)

        st.markdown(f'<p class="big-font">{home_team} will <b><u>{outcome}</b></u> against {away_team}</p>', unsafe_allow_html=True)
