import streamlit as st
import pickle
import pandas as pd

teams=['Kolkata Knight Riders',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Mumbai Indians',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Punjab Kings',
 'Gujarat Titans',
 'Lucknow Super Giants']
venues=['Brabourne Stadium', 'MA Chidambaram Stadium, Chepauk',
       'Eden Gardens, Kolkata', 'M.Chinnaswamy Stadium',
       'Arun Jaitley Stadium', 'Sawai Mansingh Stadium',
       'M Chinnaswamy Stadium', 'Sharjah Cricket Stadium',
       'Dr DY Patil Sports Academy, Mumbai',
       'Dubai International Cricket Stadium', 'Feroz Shah Kotla',
       'Dr DY Patil Sports Academy',
       'Himachal Pradesh Cricket Association Stadium',
       'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
       'Wankhede Stadium, Mumbai', 'Sardar Patel Stadium, Motera',
       'Sheikh Zayed Stadium', 'MA Chidambaram Stadium, Chepauk, Chennai',
       'Buffalo Park', 'Wankhede Stadium', 'Barabati Stadium',
       'Narendra Modi Stadium, Ahmedabad',
       'Rajiv Gandhi International Stadium',
       'Zayed Cricket Stadium, Abu Dhabi', 'Brabourne Stadium, Mumbai',
       'Eden Gardens', 'MA Chidambaram Stadium',
       'Maharashtra Cricket Association Stadium, Pune',
       'De Beers Diamond Oval',
       'Rajiv Gandhi International Stadium, Uppal',
       'Punjab Cricket Association Stadium, Mohali', 'SuperSport Park',
       'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur',
       'M Chinnaswamy Stadium, Bengaluru',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Holkar Cricket Stadium', 'Kingsmead',
       'Sawai Mansingh Stadium, Jaipur', 'Subrata Roy Sahara Stadium',
       'New Wanderers Stadium', 'Arun Jaitley Stadium, Delhi',
       'Himachal Pradesh Cricket Association Stadium, Dharamsala',
       'Maharashtra Cricket Association Stadium', 'Newlands',
       'Punjab Cricket Association IS Bindra Stadium',
       'JSCA International Stadium Complex', "St George's Park",
       'OUTsurance Oval',
       'Shaheed Veer Narayan Singh International Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam',
       'Barsapara Cricket Stadium, Guwahati',
       'Vidarbha Cricket Association Stadium, Jamtha']
pipe=pickle.load(open('pipe.pkl','rb'))
st.title('Ipl Win Predictor')

col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('select batting team',teams)
with col2:
    bowling_team=st.selectbox('select bowling team',teams)

selected_venue=st.selectbox('select venue',venues)
target=st.number_input('Target')
col1,col2,col3,col4=st.columns(4)
with col1:
    score=st.number_input('score')

with col2:
    overs=st.number_input('overs completed')

with col3:
    balls=st.number_input('balls bowled in this over')

with col4:
    wickets=st.number_input('wickets out')
if st.button('predict'):
    runs_left=target-score
    balls_left=120-(6*overs+balls)
    wickets_left=10-wickets
    if balls_left==0:
        st.header('match-ended')
    elif balls_left==120:
        st.header('let the 2nd inning start')
    else:
        crr=score/(6*overs+balls)
        rrr=runs_left/balls_left
        df=pd.DataFrame({
            'batting_team':[batting_team],'bowling_team':[bowling_team],'venue':[selected_venue],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'target_runs':[target],'crr':[crr],'rrr':[rrr]
        })
        result=pipe.predict_proba(df)
        win=result[0][0]
        loss=result[0][1]
        st.header(batting_team+" -"+str(round(loss*100))+"%")
        st.header(bowling_team+" -"+str(round(win*100))+"%")