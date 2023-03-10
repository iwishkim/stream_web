import streamlit as st
import pandas as pd 

view = [100,150,30]
st.write('# 유튜브조회수')
st.write('## 유튜브조회수')
view
st.write('### 유튜브조회수')
st.bar_chart(view)

sview = pd.Series(view)
sview