
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


def information_gain(feature,label):
    index=feature.index
    feature_elements=set(feature)
    label_elements=set(label)
    results={}
    for feature_element in feature_elements:
        result={}
        for label_element in label_elements:
            count=0
            for i in index:
                if(feature[i]==feature_element) and (label[i]==label_element):
                    count+=1
            result[label_element]=count
        results[feature_element]=result
    return results

def show_distribution(info_gain,feature_name='',label_name='',dicts_f={},dicts_l={}):
    keys=[i for i in info_gain]
    sum_all=0
    for key in keys:
        child_keys=[i for i in info_gain[key]]
        for child_key in child_keys:
            sum_all+=info_gain[key][child_key]
    print('\t\t  {}-{} Distribution\n'.format(feature_name,label_name))
    print("Number of Data : {}".format(sum_all))
    print("Feature        : {}".format(feature_name))
    print("Label          : {}\n".format(label_name))
    for key in keys:
        if(len(dicts_f)==0):
            print("Feature Element : {}".format(key))
        else:
            print("Feature Element : {}".format(dicts_f[key]))
        print("Label Element\t  N     Local Percentage   Global Percentage".format())
        child_keys=[i for i in info_gain[key]]
        sum_child=0
        for child_key in child_keys:
            sum_child+=info_gain[key][child_key]
        for child_key in child_keys:
            if(len(dicts_l)==0):
                print("     {}\t  {}\t     {}%\t\t{}%".format(child_key,info_gain[key][child_key],round(info_gain[key][child_key]*100/sum_child,2),round(info_gain[key][child_key]*100/sum_all,2)))
            else:
                print("     {}\t  {}\t     {}%\t\t{}%".format(dicts_l[child_key],info_gain[key][child_key],round(info_gain[key][child_key]*100/sum_child,2),round(info_gain[key][child_key]*100/sum_all,2)))
        print("    ------------------------------------------------")
        print("     Sum\t  {}\t     {}%\t\t{}%\n".format(sum_child,100,round(sum_child*100/sum_all,2)))


# In[3]:


df=pd.read_csv('data_cleaned.csv',index_col = 0)


# In[4]:


dic_Gender={}
dic_Umur={}
dic_Profesi={}
dic_Penghasilan={}
dic_Frekuensi={}
dic_Fashion={}
dic_Groceries={}
dic_HP={}
dic_PC={}
dic_Elektronik={}
dic_Kosmetik={}
dic_Makanan={}
dic_Pulsa={}
dic_Pesawat={}
dic_Kereta={}
dic_Hotel={}
dic_Konser={}
dic_Wisata={}
dic_Bioskop={}
dic_Kendaraan={}

dic_Gender[0]='No Data'
dic_Umur[0]='No Data'
dic_Profesi[0]='No Data'
dic_Penghasilan[0]='No Data'
dic_Frekuensi[0]='No Data'
dic_Fashion[0]='No Data'
dic_Groceries[0]='No Data'
dic_HP[0]='No Data'
dic_PC[0]='No Data'
dic_Elektronik[0]='No Data'
dic_Kosmetik[0]='No Data'
dic_Makanan[0]='No Data'
dic_Pulsa[0]='No Data'
dic_Pesawat[0]='No Data'
dic_Kereta[0]='No Data'
dic_Hotel[0]='No Data'
dic_Konser[0]='No Data'
dic_Wisata[0]='No Data'
dic_Bioskop[0]='No Data'
dic_Kendaraan[0]='No Data'

dic_Fashion[1]='Online'
dic_Groceries[1]='Online'
dic_HP[1]='Online'
dic_PC[1]='Online'
dic_Elektronik[1]='Online'
dic_Kosmetik[1]='Online'
dic_Makanan[1]='Online'
dic_Pulsa[1]='Online'
dic_Pesawat[1]='Online'
dic_Kereta[1]='Online'
dic_Hotel[1]='Online'
dic_Konser[1]='Online'
dic_Wisata[1]='Online'
dic_Bioskop[1]='Online'
dic_Kendaraan[1]='Online'

dic_Fashion[2]='Offline'
dic_Groceries[2]='Offline'
dic_HP[2]='Offline'
dic_PC[2]='Offline'
dic_Elektronik[2]='Offline'
dic_Kosmetik[2]='Offline'
dic_Makanan[2]='Offline'
dic_Pulsa[2]='Offline'
dic_Pesawat[2]='Offline'
dic_Kereta[2]='Offline'
dic_Hotel[2]='Offline'
dic_Konser[2]='Offline'
dic_Wisata[2]='Offline'
dic_Bioskop[2]='Offline'
dic_Kendaraan[2]='Offline'

dic_Gender[1]='Laki-Laki'
dic_Umur[1]='<15 Tahun'
dic_Profesi[1]='Pelajar'
dic_Penghasilan[1]='<2 jt'
dic_Frekuensi[1]='Menurun'

dic_Gender[2]='Perempuan'
dic_Umur[2]='16-20 Tahun'
dic_Profesi[2]='Ibu Rumah Tangga'
dic_Penghasilan[2]='2-5jt'
dic_Frekuensi[2]='Tetap'

dic_Umur[3]='21-30 Tahun'
dic_Profesi[3]='Pekerja'
dic_Penghasilan[3]='5-10jt'
dic_Frekuensi[3]='Bertambah'

dic_Umur[4]='31-40 Tahun'
dic_Penghasilan[4]='>10jt'

dic_Umur[5]='41-50 Tahun'
dic_Umur[6]='>50 Tahun'

dics={}

dics['Gender']=dic_Gender
dics['Umur']=dic_Umur
dics['Profesi']=dic_Profesi
dics['Penghasilan']=dic_Penghasilan
dics['Frekuensi Belanja Online']=dic_Frekuensi
dics['Fashion']=dic_Fashion
dics['Groceries']=dic_Groceries
dics['HP']=dic_HP
dics['PC']=dic_PC
dics['Elektronik']=dic_Elektronik
dics['Kosmetik']=dic_Kosmetik
dics['Makanan']=dic_Makanan
dics['Pulsa']=dic_Pulsa
dics['Pesawat']=dic_Pesawat
dics['Kereta']=dic_Kereta
dics['Hotel']=dic_Hotel
dics['Konser']=dic_Konser
dics['Wisata']=dic_Wisata
dics['Bioskop']=dic_Bioskop
dics['Kendaraan Umum']=dic_Kendaraan


# In[5]:


df.head(5)


# In[6]:


feature='Penghasilan'
label='Fashion'
temp=information_gain(df[feature],df[label])
show_distribution(temp,feature_name=feature,label_name=label,dicts_f=dics[feature],dicts_l=dics[label])


# In[7]:


df

