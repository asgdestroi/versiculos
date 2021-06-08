import streamlit as st
import random

versiculos_lista = open("versiculos.txt","r")
versiculos = dict(versiculos_lista)

st.beta_set_page_config(page_title='VERSICULOS', page_icon='fir.png', layout='centered', initial_sidebar_state='collapsed')
vers = random.choice(list(versiculos.values()))
st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione a página', ['Página 1','Página 2'])
if paginaSelecionada == 'Página 1':
    #st.image('fir.png', width=100, )
    st.markdown("<h1 style='text-align: center; color: grey;'>PROMESSAS</h1>", unsafe_allow_html=True)
    st.text_area('', vers)
    if st.button('Versículo'):
        vers = random.choice(list(versiculos.values()))
    else:
        st.write(' ')
elif paginaSelecionada == 'Página 2':
    st.title('Você selecionou a página 2')


