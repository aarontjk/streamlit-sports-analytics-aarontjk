import streamlit as st


home = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10', 'test11']
away = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10', 'test11']



### UI Design Below ###

st.markdown("<h1 style='text-align: center; color: red;'>SportsAnalytics \n Football Outcome Predictor</h1>", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)

with c1:
    with st.form('Home Team Lineup:'):
        home_player1 = st.selectbox("Enter Home Team Player 1:", options = home)
        home_player2 = st.selectbox("Enter Home Team Player 2:", options = home)
        home_player3 = st.selectbox("Enter Home Team Player 3:", options = home)
        home_player4 = st.selectbox("Enter Home Team Player 4:", options = home)
        home_player5 = st.selectbox("Enter Home Team Player 5:", options = home)
        home_player6 = st.selectbox("Enter Home Team Player 6:", options = home)
        home_player7 = st.selectbox("Enter Home Team Player 7:", options = home)
        home_player8 = st.selectbox("Enter Home Team Player 8:", options = home)
        home_player9 = st.selectbox("Enter Home Team Player 9:", options = home)
        home_player10 = st.selectbox("Enter Home Team Player 10:", options = home)
        home_player11 = st.selectbox("Enter Home Team Player 11:", options = home)
        st.form_submit_button('Submit')



with c3:
    with st.form('Away Team Lineup:'):
        away_player1 = st.selectbox("Enter Away Team Player 1:", options = away)
        away_player2 = st.selectbox("Enter Away Team Player 2:", options = away)
        away_player3 = st.selectbox("Enter Away Team Player 3:", options = away)
        away_player4 = st.selectbox("Enter Away Team Player 4:", options = away)
        away_player5 = st.selectbox("Enter Away Team Player 5:", options = away)
        away_player6 = st.selectbox("Enter Away Team Player 6:", options = away)
        away_player7 = st.selectbox("Enter Away Team Player 7:", options = away)
        away_player8 = st.selectbox("Enter Away Team Player 8:", options = away)
        away_player9 = st.selectbox("Enter Away Team Player 9:", options = away)
        away_player10 = st.selectbox("Enter Away Team Player 10:", options = away)
        away_player11 = st.selectbox("Enter Away Team Player 11:", options = away)
        st.form_submit_button('Submit')
