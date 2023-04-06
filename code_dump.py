""" def prep_data(home_lineup, home_form, away_lineup, away_form):

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


    home_df = players[players['player_name'].isin(home_lineup)]

    away_df = players[players['player_name'].isin(away_lineup)]

    st.write(home_df)
    st.write(away_df) """
