import streamlit as st
import pickle

# Charger le modèle de prédiction

pickle_in = open('DT.pkl', 'rb') 
model = pickle.load(pickle_in) 

# Créer une barre latérale pour la recherche
user_input = st.sidebar.text_input("Entrez votre recherche ici")

# Afficher le résultat de la prédiction
if st.button('Prédire'):
    prediction = model.predict([user_input])
    st.write(f"La prédiction du modèle pour '{user_input}' est: {prediction}")
