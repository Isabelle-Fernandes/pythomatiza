import streamlit as st
import random  
 
st.title('Jogo de Adivinhação')
st.markdown("---")
st.write('Tente adivinhar o número entre 1 e 100!')
st.write('Ganha quem acertar em um menor número de tentativas!')

def adivinha():
    if 'numero' not in st.session_state:
        st.session_state.numero = random.randint(1, 100)
        st.session_state.tentativas = 0
        st.session_state.jogador = st.text_input('Digite seu nome: ')

    palpite = st.number_input('Digite seu palpite:', min_value=1, max_value=100, step=1)
    
    if st.button('Enviar'):
        st.session_state.tentativas += 1
        
        if palpite < st.session_state.numero:
            st.write(f'O palpite {palpite} é MENOR que o número.')
        elif palpite > st.session_state.numero:
            st.write(f'O palpite {palpite} é MAIOR que o número.')
        else:
            st.write(f'Parabéns, você acertou na tentativa {st.session_state.tentativas}!')
            st.write(f'{st.session_state.jogador}: {st.session_state.tentativas}!')
            del st.session_state.numero
            del st.session_state.tentativas
            del st.session_state.jogador
            st.write('O jogo foi reiniciado. Tente novamente!')
            adivinha()

adivinha()
