import streamlit as st

st.title("Halaman Dashboard")
st.image("rumah.jpg", caption= "Mau kaya? Nabung")

#Fungsi menghitung dan Menyimpan total
def total():
    total_nabung = sum(t['Jumlah'] 
                       for t in st.session_state
                       ['total_semua'] 
                       if t ['tipe'] == 'Menabung')
    
    return total_nabung

total_semua=st.session_state['total_semua']
total_nabung=total()

st.metric('total Menabung', f"Rp {total_nabung}")

