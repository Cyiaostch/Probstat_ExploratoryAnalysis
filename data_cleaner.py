
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


data=pd.read_excel('data.xlsx')


# In[3]:


newcolumns=[]
for i in list(data):
    newcolumns.append(data[i][0])


# In[4]:


newcolumns[0]='No'
newcolumns[1]='Nama'
newcolumns[29]='Meningkat'
newcolumns[30]='Menurun'
newcolumns[31]='Tetap'
newcolumns[88]='Fashion Y'
newcolumns[89]='Fashion N'
newcolumns[113]='Groceries Y'
newcolumns[114]='Groceries N'
newcolumns[138]='HP Y'
newcolumns[139]='HP N'
newcolumns[164]='PC Y'
newcolumns[165]='PC N'
newcolumns[188]='Elektronik Y'
newcolumns[189]='Elektronik N'
newcolumns[212]='Kosmetik Y'
newcolumns[213]='Kosmetik N'
newcolumns[237]='Hobi Y'
newcolumns[238]='Hobi N'
newcolumns[260]='Makanan Y'
newcolumns[261]='Makanan N'
newcolumns[284]='Pulsa Y'
newcolumns[285]='Pulsa N'
newcolumns[316]='Pesawat Y1'
newcolumns[317]='Pesawat Y2'
newcolumns[318]='Pesawat Y3'
newcolumns[319]='Pesawat N'
newcolumns[341]='Kereta Y1'
newcolumns[342]='Kereta Y2'
newcolumns[343]='Kereta Y3'
newcolumns[344]='Kereta N1'
newcolumns[345]='Kereta N2'
newcolumns[367]='Hotel Y1'
newcolumns[368]='Hotel Y2'
newcolumns[369]='Hotel Y3'
newcolumns[370]='Hotel N1'
newcolumns[371]='Hotel N2'
newcolumns[372]='Konser Y1'
newcolumns[373]='Konser Y2'
newcolumns[374]='Konser Y3'
newcolumns[375]='Konser N1'
newcolumns[376]='Konser N2'
newcolumns[377]='Wisata Y1'
newcolumns[378]='Wisata Y2'
newcolumns[379]='Wisata Y3'
newcolumns[380]='Wisata N1'
newcolumns[381]='Wisata N2'
newcolumns[382]='Bioskop Y1'
newcolumns[383]='Bioskop Y2'
newcolumns[384]='Bioskop Y3'
newcolumns[385]='Bioskop N1'
newcolumns[386]='Bioskop N2'
newcolumns[390]='Kendaraan Umum Y1'
newcolumns[391]='Kendaraan Umum Y2'
newcolumns[392]='Kendaraan Umum N1'
newcolumns[393]='Kendaraan Umum N2'
newcolumns[394]='Kendaraan Umum N3'
newcolumns[395]='Kendaraan Umum N4'
newcolumns[396]='Kendaraan Umum N5'
newcolumns[397]='Kendaraan Umum N6'
newcolumns[398]='Kendaraan Umum N7'


# In[5]:


data.columns=newcolumns


# In[6]:


data.drop(data.index[0],inplace=True)


# In[7]:


data=data[[
            '<15 tahun','16 - 20 tahun','21 - 30 tahun','31 - 40 tahun','41 - 50 tahun','> 50 tahun',
            'Pelajar / Mahasiswa','Ibu Rumah Tangga',
            'Laki-Laki','Perempuan',
            '< Rp 2 juta','Rp 2 juta - Rp 5 juta','Rp 5 juta - RP 10 juta','> Rp 10 juta',
            'Meningkat','Menurun','Tetap',
            'Fashion Y','Fashion N',
            'Groceries Y','Groceries N',
            'HP Y','HP N',
            'PC Y','PC N',
            'Elektronik Y','Elektronik N',
            'Kosmetik Y','Kosmetik N',
            'Hobi Y','Hobi N',
            'Makanan Y','Makanan N',
            'Pulsa Y','Pulsa N',
            'Pesawat Y1','Pesawat Y2','Pesawat Y3','Pesawat N',
            'Kereta Y1','Kereta Y2','Kereta Y3','Kereta N1','Kereta N2',
            'Hotel Y1','Hotel Y2','Hotel Y3','Hotel N1','Hotel N2',
            'Konser Y1','Konser Y2','Konser Y3','Konser N1','Konser N2',
            'Wisata Y1','Wisata Y2','Wisata Y3','Wisata N1','Wisata N2',
            'Bioskop Y1','Bioskop Y2','Bioskop Y3','Bioskop N1','Bioskop N2',
            'Kendaraan Umum Y1','Kendaraan Umum Y2',
            'Kendaraan Umum N1','Kendaraan Umum N2','Kendaraan Umum N3','Kendaraan Umum N4','Kendaraan Umum N5','Kendaraan Umum N6','Kendaraan Umum N7', 
            'Tokopedia','Bukalapak','Shopee','Blibli','Lazada','Elevenia','Matahari Mall','OLX','Zalora','Blanja','GoJek (GoFood, GoMart, GoShop, dll)',
            'Agoda.com','Traveloka.com','Tiket.com','Booking.com','Rajakamar.com','GoJek (Go-Tix)','uTicket.com','Tokopedia.com','Bukalapak.com','Blibli.com','Pegi-pegi.com','Hotels.com','Airbnb','Airyrooms','Zenrooms','Reddoorz'
         ]]


# In[8]:


##Features
data['Gender']=np.nan
data['Umur']=np.nan
data['Profesi']=np.nan
data['Penghasilan']=np.nan


for i in data.index:
    if(data['<15 tahun'][i] not in [np.nan]):
        data['Umur'][i]=1
    elif(data['16 - 20 tahun'][i] not in [np.nan]):
        data['Umur'][i]=2
    elif(data['21 - 30 tahun'][i] not in [np.nan]):
        data['Umur'][i]=3
    elif(data['31 - 40 tahun'][i] not in [np.nan]):
        data['Umur'][i]=4
    elif(data['41 - 50 tahun'][i] not in [np.nan]):
        data['Umur'][i]=5
    elif(data['> 50 tahun'][i]not in [np.nan]):
        data['Umur'][i]=6
    else:
        data['Umur'][i]=0
        
    if(data['Pelajar / Mahasiswa'][i] not in [np.nan]):
        data['Profesi'][i]=1
    elif(data['Ibu Rumah Tangga'][i] not in [np.nan]):
        data['Profesi'][i]=2
    else:
        data['Profesi'][i]=3
        
    if(data['Laki-Laki'][i] not in [np.nan]):
        data['Gender'][i]=1
    elif(data['Perempuan'][i] not in [np.nan]):
        data['Gender'][i]=2
    else:
        data['Gender'][i]=0    
    
    if(data['< Rp 2 juta'][i] not in [np.nan]):
        data['Penghasilan']=1
    elif(data['Rp 2 juta - Rp 5 juta'][i] not in [np.nan]):
        data['Penghasilan']=2
    elif(data['Rp 5 juta - RP 10 juta'][i] not in [np.nan]):
        data['Penghasilan']=3
    elif(data['> Rp 10 juta'][i] not in [np.nan]):
        data['Penghasilan']=4
    else:
        data['Penghasilan']=0


# In[11]:


##Labels
data['Frekuensi Belanja Online']=np.nan
data['Fashion']=np.nan
data['Groceries']=np.nan
data['HP']=np.nan
data['PC']=np.nan
data['Elektronik']=np.nan
data['Kosmetik']=np.nan
data['Makanan']=np.nan
data['Pulsa']=np.nan
data['Pesawat']=np.nan
data['Kereta']=np.nan
data['Hobi']=np.nan
data['Hotel']=np.nan
data['Konser']=np.nan
data['Wisata']=np.nan
data['Bioskop']=np.nan
data['Kendaraan Umum']=np.nan
data['Preferensi Toko Online']=np.nan
data['Preferensi Booking Online']=np.nan
data['Preferensi Toko Online 1']=np.nan
data['Preferensi Booking Online 1']=np.nan
data['Preferensi Toko Online 2']=np.nan
data['Preferensi Booking Online 2']=np.nan
data['Preferensi Toko Online 3']=np.nan
data['Preferensi Booking Online 3']=np.nan

for i in data.index:
    if(data['Meningkat'][i] not in [np.nan]):
        data['Frekuensi Belanja Online'][i]=3
    elif(data['Menurun'][i] not in [np.nan]):
        data['Frekuensi Belanja Online'][i]=1
    elif(data['Tetap'][i] not in [np.nan]):
        data['Frekuensi Belanja Online'][i]=2
    else:
        data['Frekuensi Belanja Online'][i]=0
        
    if(data['Fashion Y'][i] not in [np.nan]):
        data['Fashion'][i]=1
    elif(data['Fashion N'][i] not in [np.nan]):
        data['Fashion'][i]=2
    else:
        data['Fashion'][i]=0
    
    if(data['Groceries Y'][i] not in [np.nan]):
        data['Groceries'][i]=1
    elif(data['Groceries N'][i] not in [np.nan]):
        data['Groceries'][i]=2
    else:
        data['Groceries'][i]=0
        
    if(data['HP Y'][i] not in [np.nan]):
        data['HP'][i]=1
    elif(data['HP N'][i] not in [np.nan]):
        data['HP'][i]=2
    else:
        data['HP'][i]=0
        
    if(data['PC Y'][i] not in [np.nan]):
        data['PC'][i]=1
    elif(data['PC N'][i] not in [np.nan]):
        data['PC'][i]=2
    else:
        data['PC'][i]=0
    
    if(data['Hobi Y'][i] not in [np.nan]):
        data['Hobi'][i]=1
    elif(data['Hobi N'][i] not in [np.nan]):
        data['Hobi'][i]=0
        
    if(data['Elektronik Y'][i] not in [np.nan]):
        data['Elektronik'][i]=1
    elif(data['Elektronik N'][i] not in [np.nan]):
        data['Elektronik'][i]=2
    else:
        data['Elektronik'][i]=0

    if(data['Kosmetik Y'][i] not in [np.nan]):
        data['Kosmetik'][i]=1
    elif(data['Kosmetik N'][i] not in [np.nan]):
        data['Kosmetik'][i]=2
    else:
        data['Kosmetik'][i]=0
        
    if(data['Makanan Y'][i] not in [np.nan]):
        data['Makanan'][i]=1
    elif(data['Makanan N'][i] not in [np.nan]):
        data['Makanan'][i]=2
    else:
        data['Makanan'][i]=0
        
    if(data['Pulsa Y'][i] not in [np.nan]):
        data['Pulsa'][i]=1
    elif(data['Pulsa N'][i] not in [np.nan]):
        data['Pulsa'][i]=2
    else:
        data['Pulsa'][i]=0
        
    if(data['Pesawat Y1'][i] not in [np.nan]):
        data['Pesawat'][i]=1
    elif(data['Pesawat Y2'][i] not in [np.nan]):
        data['Pesawat'][i]=1
    elif(data['Pesawat Y3'][i] not in [np.nan]):
        data['Pesawat'][i]=1
    elif(data['Pesawat N'][i] not in [np.nan]):
        data['Pesawat'][i]=2
    else:
        data['Pesawat'][i]=0
    
    if(data['Kereta Y1'][i] not in [np.nan]):
        data['Kereta'][i]=1
    elif(data['Kereta Y2'][i] not in [np.nan]):
        data['Kereta'][i]=1
    elif(data['Kereta Y3'][i] not in [np.nan]):
        data['Kereta'][i]=1
    elif(data['Kereta N1'][i] not in [np.nan]):
        data['Kereta'][i]=2
    elif(data['Kereta N2'][i] not in [np.nan]):
        data['Kereta'][i]=2
    else:
        data['Kereta'][i]=0
        
    if(data['Hotel Y1'][i] not in [np.nan]):
        data['Hotel'][i]=1
    elif(data['Hotel Y2'][i] not in [np.nan]):
        data['Hotel'][i]=1
    elif(data['Hotel Y3'][i] not in [np.nan]):
        data['Hotel'][i]=1
    elif(data['Hotel N1'][i] not in [np.nan]):
        data['Hotel'][i]=2
    elif(data['Hotel N2'][i] not in [np.nan]):
        data['Hotel'][i]=2
    else:
        data['Hotel'][i]=0

    if(data['Konser Y1'][i] not in [np.nan]):
        data['Konser'][i]=1
    elif(data['Konser Y2'][i] not in [np.nan]):
        data['Konser'][i]=1
    elif(data['Konser Y3'][i] not in [np.nan]):
        data['Konser'][i]=1
    elif(data['Konser N1'][i] not in [np.nan]):
        data['Konser'][i]=2
    elif(data['Konser N2'][i] not in [np.nan]):
        data['Konser'][i]=2
    else:
        data['Konser'][i]=0

    if(data['Wisata Y1'][i] not in [np.nan]):
        data['Wisata'][i]=1
    elif(data['Wisata Y2'][i] not in [np.nan]):
        data['Wisata'][i]=1
    elif(data['Wisata Y3'][i] not in [np.nan]):
        data['Wisata'][i]=1
    elif(data['Wisata N1'][i] not in [np.nan]):
        data['Wisata'][i]=2
    elif(data['Wisata N2'][i] not in [np.nan]):
        data['Wisata'][i]=2
    else:
        data['Wisata'][i]=0
        
    if(data['Bioskop Y1'][i] not in [np.nan]):
        data['Bioskop'][i]=1
    elif(data['Bioskop Y2'][i] not in [np.nan]):
        data['Bioskop'][i]=1
    elif(data['Bioskop Y3'][i] not in [np.nan]):
        data['Bioskop'][i]=1
    elif(data['Bioskop N1'][i] not in [np.nan]):
        data['Bioskop'][i]=2
    elif(data['Bioskop N2'][i] not in [np.nan]):
        data['Bioskop'][i]=2
    else:
        data['Bioskop'][i]=0
        
    if(data['Kendaraan Umum Y1'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=1
    elif(data['Kendaraan Umum Y2'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=1
    elif(data['Kendaraan Umum N1'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=2
    elif(data['Kendaraan Umum N2'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=2
    elif(data['Kendaraan Umum N3'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=2
    elif(data['Kendaraan Umum N4'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=2
    elif(data['Kendaraan Umum N5'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=2
    elif(data['Kendaraan Umum N6'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=2
    elif(data['Kendaraan Umum N7'][i] not in [np.nan]):
        data['Kendaraan Umum'][i]=2
    else:
        data['Kendaraan Umum'][i]=0
     
    data['Preferensi Toko Online'][i]=''
    if(data['Tokopedia'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 1'
    if(data['Bukalapak'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 2'
    if(data['Shopee'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 3'
    if(data['Blibli'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 4'
    if(data['Lazada'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 5'
    if(data['Elevenia'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 6'
    if(data['Matahari Mall'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 7'
    if(data['OLX'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 8'
    if(data['Zalora'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 9'
    if(data['Blanja'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 10'
    if(data['GoJek (GoFood, GoMart, GoShop, dll)'][i] not in [np.nan]):
        data['Preferensi Toko Online'][i]+=' 11'
    if(data['Preferensi Toko Online'][i]==''):
        data['Preferensi Toko Online'][i]+=' 0'
    
    data['Preferensi Booking Online'][i]=''
    if(data['Agoda.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 1'
    if(data['Traveloka.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 2'
    if(data['Tiket.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 3'
    if(data['Booking.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 4'
    if(data['Rajakamar.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 5'
    if(data['GoJek (Go-Tix)'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 6'
    if(data['uTicket.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 7'
    if(data['Tokopedia.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 8'
    if(data['Bukalapak.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 9'
    if(data['Blibli.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 10'
    if(data['Pegi-pegi.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 11'
    if(data['Hotels.com'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 12'
    if(data['Airbnb'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 13'
    if(data['Airyrooms'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 14'
    if(data['Zenrooms'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 15'
    if(data['Reddoorz'][i] not in [np.nan]):
        data['Preferensi Booking Online'][i]+=' 16'
    if(data['Preferensi Booking Online'][i]==''):
        data['Preferensi Booking Online'][i]+=' 0'


# In[18]:


for i in data.index:
    toko_splitted=data['Preferensi Toko Online'][i].split(' ')
    booking_splitted=data['Preferensi Booking Online'][i].split(' ')
    
    if(len(toko_splitted)==2):
        if(toko_splitted[1]=='0'):
            data['Preferensi Toko Online 1'][i]=0
            data['Preferensi Toko Online 2'][i]=0
            data['Preferensi Toko Online 3'][i]=0
        else:
            data['Preferensi Toko Online 1'][i]=int(toko_splitted[1])
            data['Preferensi Toko Online 2'][i]=0
            data['Preferensi Toko Online 3'][i]=0
        
    elif(len(toko_splitted)==3):
        data['Preferensi Toko Online 1'][i]=int(toko_splitted[1])
        data['Preferensi Toko Online 2'][i]=int(toko_splitted[2])
        data['Preferensi Toko Online 3'][i]=0
        
    elif(len(toko_splitted)==4):
        data['Preferensi Toko Online 1'][i]=int(toko_splitted[1])
        data['Preferensi Toko Online 2'][i]=int(toko_splitted[2])
        data['Preferensi Toko Online 3'][i]=int(toko_splitted[3])

    if(len(booking_splitted)==2):
        if(booking_splitted[0]=='0'):
            data['Preferensi Booking Online 1'][i]=0
            data['Preferensi Booking Online 2'][i]=0
            data['Preferensi Booking Online 3'][i]=0
        else:
            data['Preferensi Booking Online 1'][i]=int(booking_splitted[1])
            data['Preferensi Booking Online 2'][i]=0
            data['Preferensi Booking Online 3'][i]=0
        
    elif(len(booking_splitted)==3):
        data['Preferensi Booking Online 1'][i]=int(booking_splitted[1])
        data['Preferensi Booking Online 2'][i]=int(booking_splitted[2])
        data['Preferensi Booking Online 3'][i]=0
        
    elif(len(booking_splitted)==4):
        data['Preferensi Booking Online 1'][i]=int(booking_splitted[1])
        data['Preferensi Booking Online 2'][i]=int(booking_splitted[2])
        data['Preferensi Booking Online 3'][i]=int(booking_splitted[3])


# In[20]:


data_fixed=data[[
            'Gender','Umur','Profesi','Penghasilan',
    
            'Frekuensi Belanja Online','Fashion','Groceries','HP','PC','Elektronik','Kosmetik',
            'Makanan','Pulsa','Pesawat','Kereta','Hobi','Hotel','Konser','Wisata','Bioskop','Kendaraan Umum',
            'Preferensi Toko Online 1','Preferensi Toko Online 2','Preferensi Toko Online 3',
            'Preferensi Booking Online 1','Preferensi Booking Online 2','Preferensi Booking Online 3'
        ]]


# In[23]:


print(data_fixed['Preferensi Booking Online 1'].head(1))
print(data_fixed['Preferensi Booking Online 2'].head(1))
print(data_fixed['Preferensi Booking Online 3'].head(1))


# In[25]:


data_fixed.to_csv('data_cleaned.csv')

