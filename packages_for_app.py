import pandas as pd

#Download fingerprints_xml.zip

import requests

url_1 = "https://github.com/dataprofessor/padel/raw/main/fingerprints_xml.zip"
file_name = "fingerprints_xml.zip"

response = requests.get(url_1)

if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print('File downloaded and saved successfully')
else:
    print('Failed to download file')

#unzipping fingerprints_xml.zip
import zipfile

zip_file_path = r"C:\Users\jhamb\OneDrive\Desktop\Bioactivity_prediction_app\fingerprints_xml.zip"
destination_folder = r"C:\Users\jhamb\OneDrive\Desktop\Bioactivity_prediction_app"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(destination_folder)

#sorting fingerprints_xml
import glob
xml_files = glob.glob("*.xml")
xml_files.sort()
print(xml_files)

FP_list = ['AtomPairs2DCount',
 'AtomPairs2D',
 'EState',
 'CDKextended',
 'CDK',
 'CDKgraphonly',
 'KlekotaRothCount',
 'KlekotaRoth',
 'MACCS',
 'PubChem',
 'SubstructureCount',
 'Substructure']

fp = dict(zip(FP_list, xml_files))
print(fp)

#downloading raw data
import requests

url_1 = "https://raw.githubusercontent.com/dataprofessor/data/master/acetylcholinesterase_04_bioactivity_data_3class_pIC50.csv"
file_name = "acetylcholinesterase_04_bioactivity_data_3class_pIC50.csv"

response = requests.get(url_1)

if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print('File downloaded and saved successfully')
else:
    print('Failed to download file')


#loading the raw data as a data frame
df = pd.read_csv('acetylcholinesterase_04_bioactivity_data_3class_pIC50.csv')

#save new dataframe into molecule.smi
df2 = pd.concat( [df['canonical_smiles'],df['molecule_chembl_id']], axis=1 )
df2.to_csv('molecule.smi', sep='\t', index=False, header=False)
print(df2)