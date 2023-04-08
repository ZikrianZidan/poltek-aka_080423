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

import numpy as np
array1 = np.random.randint(10,40, size=(10,))
array2 = np.random.randint(10,40, size=(10,))

import pandas as pd
st.dataframe(pd.DataFrame({'kelas A' : array1,
                           'kelas B' : array2
                          }))