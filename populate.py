from players.models import Player, Player_lite
from pathlib2 import Path 
import pandas as pd 
import glob

path_fbs = 'DIV1FCS_2017/*/*.csv'
path_fcs = 'DIV1FBS_2017/*/*.csv'
fbs = glob.glob(path_fbs)
fcs = glob.glob(path_fcs)

frame = pd.DataFrame()
list_ = []

for fname in fbs:
    df = pd.read_csv(fname,index_col=None,header=0)
    list_.append(df)
    
for fname in fcs:
    df = pd.read_csv(fname,index_col=None,header=0)
    list_.append(df)

frame = pd.concat(list_)
frame = frame.drop('High School/JUCO',axis=1)
frame[['Number','Height','Weight']] = frame[['Number','Height','Weight']].apply(pd.to_numeric,errors='coerce')
frame.fillna(0,inplace=True)

for index,row in frame.iterrows():
	player = Player(year=row['Class'],height=row['Height'],hometown=row['Hometown'],name=row['Name'],position=row['Position'],weight=row['Weight'])
	player.save()


