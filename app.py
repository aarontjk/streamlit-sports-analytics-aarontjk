import streamlit as st


c1, c2 = st.columns(2)


with c1:
    with st.form('Home Team Lineup:'):
        home_player1 = st.selectbox("Enter Home Team Player 1:", options = ['test1','test2','test3'])
        home_player2 = st.selectbox("Enter Home Team Player 2:", options = ['test1','test2','test3'])
        home_player3 = st.selectbox("Enter Home Team Player 3:", options = ['test1','test2','test3'])
        home_player4 = st.selectbox("Enter Home Team Player 4:", options = ['test1','test2','test3'])
        home_player5 = st.selectbox("Enter Home Team Player 5:", options = ['test1','test2','test3'])
        home_player6 = st.selectbox("Enter Home Team Player 6:", options = ['test1','test2','test3'])
        home_player7 = st.selectbox("Enter Home Team Player 7:", options = ['test1','test2','test3'])
        home_player8 = st.selectbox("Enter Home Team Player 8:", options = ['test1','test2','test3'])
        home_player9 = st.selectbox("Enter Home Team Player 9:", options = ['test1','test2','test3'])
        home_player10 = st.selectbox("Enter Home Team Player 10:", options = ['test1','test2','test3'])
        home_player11 = st.selectbox("Enter Home Team Player 11:", options = ['test1','test2','test3'])



with c2:
    with st.form('Away Team Lineup:'):
        away_player1 = st.selectbox("Enter Away Team Player 1:", options = ['test1','test2','test3'])
        away_player2 = st.selectbox("Enter Away Team Player 2:", options = ['test1','test2','test3'])
        away_player3 = st.selectbox("Enter Away Team Player 3:", options = ['test1','test2','test3'])
        away_player4 = st.selectbox("Enter Away Team Player 4:", options = ['test1','test2','test3'])
        away_player5 = st.selectbox("Enter Away Team Player 5:", options = ['test1','test2','test3'])
        away_player6 = st.selectbox("Enter Away Team Player 6:", options = ['test1','test2','test3'])
        away_player7 = st.selectbox("Enter Away Team Player 7:", options = ['test1','test2','test3'])
        away_player8 = st.selectbox("Enter Away Team Player 8:", options = ['test1','test2','test3'])
        away_player9 = st.selectbox("Enter Away Team Player 9:", options = ['test1','test2','test3'])
        away_player10 = st.selectbox("Enter Away Team Player 10:", options = ['test1','test2','test3'])
        away_player11 = st.selectbox("Enter Away Team Player 11:", options = ['test1','test2','test3'])
