import streamlit as st
from datetime import datetime
st.sidebar.title("Locadora de Veículos")
st.sidebar.title("Vendese e Aluga-se carros")
st.sidebar.image("novo touro da carful.png")
st.sidebar.title("Pratrocinador Leopardo Locadora")
st.sidebar.title("Carros a venda")

carro = st.sidebar.selectbox("Selecione o carro dos seus sonhos",
                     ["Mustang GT", "BMW M3", "Porsche 911 GT3", "Lamborghini Aventador", "bugatti bolide", "Red Bull RB17", "Pagani Utopia"])
valores_diarias = {"Mustang GT":1199, "BMW M3":1279, "Porsche 911 GT3":2899, "Lamborghini Aventador":11099, "bugatti bolide":99600, "Red Bull RB17":100500, "Pagani Utopia":320000}
valor_do_carro = {"Mustang GT":550000, "BMW M3":894950, "Porsche 911 GT3": 1620000, "Lamborghini Aventador":2000000, "bugatti bolide":25000000, "Red Bull RB17":35000000, "Pagani Utopia":60000000}

st.image(f"{carro}.png", width=750)
st.subheader(f"Tacha diaria: R$ {valores_diarias[carro]}")
st.subheader(f"Valor de compra: R$ {valor_do_carro[carro]}")

st.title("Aluga-se:")
data_retirada = st.date_input("Selecione a data de retirada: ", datetime.now())
data_devolucao = st.date_input("Selecione a data da devolução: ", data_retirada)
if st.button("Alugar"):
    dias = (data_devolucao - data_retirada).days
    total = dias * valores_diarias[carro]
    st.success(f"Alugando o carro por {dias} dias o custo total é: R$ {total,}")

if st.button("comprar"):
    total = valor_do_carro
    st.succece(f"Parabems pelo o carro do sonhos {carro} em nossa consensonaria, a sua compra total ficou {valor_do_carro} ")