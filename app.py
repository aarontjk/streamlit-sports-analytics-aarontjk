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

    for char in home_form:
        if (char not in "WDL"):
            st.error("Invalid Home Form input.",icon="🚨")
            go = False
            break

    for char in away_form:
        if (char not in "WDL"):
            st.error("Invalid Away Form input.",icon="🚨")
            go = False
            break

    if go == False:
        st.error("Something is wrong!",icon="🚨")



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


with a3:
    away_team = st.selectbox("Away Team:", options = clubs)


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

        home_form = st.text_input('Please enter the last 5 results of the home team (e.g. WWDDL):')




    with c3:
        away_lineup = st.multiselect(
        f'Select the starting lineup:',
        away_players, key='away_lineup')
        st.write(len(away_lineup))

        away_form = st.text_input('Please enter the last 5 results of the away team (e.g. WWDDL):')


    submitted = st.form_submit_button("Submit", use_container_width=True, on_click=check_submit, args=(home_lineup,home_form,away_lineup,away_form))


homeplayers_param = ''
for player in home_lineup:
    homeplayers_param += f'{player},'
homeplayers_param = homeplayers_param[:-1]
st.write(homeplayers_param)

awayplayers_param = ''
for player in away_lineup:
    awayplayers_param += f'{player},'
awayplayers_param = awayplayers_param[:-1]
st.write(awayplayers_param)

home_form_num = 0
for char in  home_form:
    if char == "W":
        home_form_num += 2
    elif char == "D":
        home_form_num += 1

away_form_num = 0
for char in  away_form:
    if char == "W":
        away_form_num += 2
    elif char == "D":
        away_form_num += 1


url = f'https://ourapi.url/predict?home_lineup={homeplayers_param}&away_lineup={awayplayers_param}&home_form={home_form_num}&away_form={away_form_num}'

st.write(url)


if submitted:
    session = requests.Session()
    outcome = session.get(url).json()

    st.markdown(f"""#Outcome: {outcome}""")
