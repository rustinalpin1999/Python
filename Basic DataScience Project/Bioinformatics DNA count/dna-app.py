import pandas as pd
import streamlit as st
import altair as alt


st.write("""
# DNA Nucleotide Web App
""")

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('INPUT(DNA Query)')
sequence

st.header('OUTPUT(DNA Nucleotide Count)')

st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict( 
        [
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

st.subheader('2. Print text')
st.write('There are ' + str(X['A'])+'Adenine(A)')
st.write('There are ' + str(X['T'])+'Thymine(T)')
st.write('There are ' + str(X['G'])+'Adenine(guanine)')
st.write('There are ' + str(X['C'])+'thymine(cytosine)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

st.subheader('4.Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)