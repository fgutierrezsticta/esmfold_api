import streamlit as st
from stmol import showmol
import py3Dmol
import requests
import biotite.structure.io as bsio

API_KEY = "Bearer API_KEY" # replace with your api nvidia key...

#st.set_page_config(layout = 'wide')
st.sidebar.title('🎈 ESMFold')
st.sidebar.write('[*ESMFold*](https://esmatlas.com/about) is an end-to-end single sequence protein structure predictor based on the ESM-2 language model. For more information, read the [research article](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2) and the [news article](https://www.nature.com/articles/d41586-022-03539-1) published in *Nature*.')

# stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    pdbview.spin(False)
    showmol(pdbview, height = 500,width=800)

# Protein sequence input
DEFAULT_SEQ = "MAAGSITTLPALPEDGGSGAFPPGHFKDPKRLYCKNGGFFLRIHPDGRVDGVREKSDPHIKLQLQAEERGVVSIKGVCANRYLAMKEDGRLLASKCVTDECFFFERLESNNYNTYRSRKYSSWYVALKRTGQYKLGPKTGPGQKAILFLPMSAKS"
txt = st.sidebar.text_area('Input sequence', DEFAULT_SEQ, height=275)

# ESMfold API
def update(sequence=txt):

   invoke_url = "https://health.api.nvidia.com/v1/biology/nvidia/esmfold"
   headers = {"Authorization": API_KEY, "Accept": "application/json",}
   payload = {"sequence": sequence}
   
   # re-use connections
   session = requests.Session()
   response = session.post(invoke_url, headers=headers, json=payload)

   response.raise_for_status()
   response_body = response.json()
   
   pdb_string = response_body['pdbs'][0]
   with open('predicted.pdb', 'w') as f:
        f.write(pdb_string)
   
   struct = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])
   b_value = round(struct.b_factor.mean(), 4)
   
   # Display protein structure
   st.subheader('Visualization of predicted protein structure')
   render_mol(pdb_string)
   
   # plDDT value is stored in the B-factor field
   st.subheader('plDDT')
   st.write('plDDT is a per-residue estimate of the confidence in prediction on a scale from 0-100.')
   st.info(f'plDDT: {b_value}')
   
   st.download_button(
        label="Download PDB",
        data=pdb_string,
        file_name='predicted.pdb',
        mime='text/plain',
   )

predict = st.sidebar.button('Predict', on_click=update)

if not predict:
    st.warning('👈 Enter protein sequence data!')
