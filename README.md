# esmfold_api

[*ESMFold*](https://esmatlas.com/about) is an end-to-end single sequence protein structure predictor based on the ESM-2 language model.

## Demo App

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://esmfold.streamlit.app/)

## Instalation
- git clone https://github.com/fgutierrezsticta/esmfold_api.git
- cd esmfold_api
- conda create -n esmfold pip
- pip install -r requirements.txt
- Edit the api_key variable in the app.py file by obtaining the key from [Try NVIDIA NIM APIs](https://build.nvidia.com/explore/biology#esmfold)
- streamlit run app.py

## Credit

This app was inspired by [Data Professor video](https://www.youtube.com/watch?v=GHoE4VkDehY&t=623s).

## Further Reading
For more information, read the following articles:
- [ESM Metagenomic Atlas: The first view of the ‘dark matter’ of the protein universe](https://ai.facebook.com/blog/protein-folding-esmfold-metagenomics/)
- [Evolutionary-scale prediction of atomic level protein structure with a language model](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2)
- [AlphaFold’s new rival? Meta AI predicts shape of 600 million proteins](https://www.nature.com/articles/d41586-022-03539-1)
