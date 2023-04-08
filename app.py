# library
import streamlit as st

# write
st.title('Software Perkalian')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan bulat')

#Input bilangan pertama
number1 = st.number_input('Masukkan bilangan pertama')
st.write('bilangan pertama adalah ', {number1})

#Input bilangan kedua
number2 = st.number_input('Masukkan bilangan kedua')
st.write('bilangan kedua adalah ', {number2})

#Hasil kali
hasil = number1*number2

if st.button('Hitung'):
             st.write(f'hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
             st.write('silahkan klik tombol hitung')
  