import streamlit as st
from multiapp import MultiApp
from apps import home, predictor # import your app modules here

app = MultiApp()

st.markdown("""
# m1A-Pred
""")

st.subheader("m1A-Pred predicts 1-mehtyladenosine (m1A) sites in RNA sequences")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Predictor", predictor.app)
# The main app
app.run()
