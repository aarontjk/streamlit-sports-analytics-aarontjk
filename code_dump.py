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
    st.write(away_df)


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

    home_form = st.text_input('Please enter the last 5 results of the home team (e.g. WWDDL):')

    away_form = st.text_input('Please enter the last 5 results of the away team (e.g. WWDDL):')



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

    """
