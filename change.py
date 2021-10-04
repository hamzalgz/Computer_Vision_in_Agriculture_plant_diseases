import os
import pathlib
from os.path import join
import re
from typing import Dict
import pandas as pd

path_mf4 =pathlib.Path('D:/image_classification/maladie fongique')/'chancre fusicocum'
path_mf3 =pathlib.Path('D:/image_classification/maladie fongique')/'coryneum'
path_mf5 =pathlib.Path('D:/image_classification/maladie fongique')/'moniliose'
path_mf6 =pathlib.Path('D:/image_classification/maladie fongique')/'phytophtora'
path_mf2 =pathlib.Path('D:/image_classification/maladie fongique')/'polystigma'
path_mf1=pathlib.Path('D:/image_classification/maladie fongique')/'rouille'


path_r3 =pathlib.Path('D:/image_classification/les insectes/ravageur')/'acariens'
path_r1 =pathlib.Path('D:/image_classification/les insectes/ravageur')/'faux tigre'
path_r6 =pathlib.Path('D:/image_classification/les insectes/ravageur')/'othyorinques'
path_r5 =pathlib.Path('D:/image_classification/les insectes/ravageur')/'puceron noir'
path_r2 =pathlib.Path('D:/image_classification/les insectes/ravageur')/'puceron vert'
path_r4 =pathlib.Path('D:/image_classification/les insectes/ravageur')/'scolytes'

diict={}

lebels=['rouille','polystigma','coryneum','chancre fusicocum','moniliose','phytophtora', 'faux tigre', 'puceron vert', 'acariens', 'scolytes','puceron noir', 'othyorinques']

i=0
j=0
for path in [path_mf1,path_mf2,path_mf3,path_mf4,path_mf5,path_mf6, path_r1,path_r2,path_r3,path_r4,path_r5, path_r6]:
   
    for file in os.listdir(path):
        print(file)
        newfile_name='new_data{}.jpeg'.format(i)
        print(newfile_name)
        diict[newfile_name]=lebels[j]
        os.rename(join(path, file), join(path, newfile_name))
        i+=1
        
    
    j+=1

df=pd.DataFrame.from_dict(diict , orient='index')

df.to_csv('data_llhajbbb.csv')

