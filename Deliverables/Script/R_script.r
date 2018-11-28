
library(mosaic)

Gender<-list("0"="Missing Data","1"="Laki-Laki","2"="Perempuan")
Umur<-list("0"="Missing Data","1"="<15 Tahun","2"="16-20 Tahun","3"="21-30 Tahun","4"="31-40 Tahun","5"="41-50 Tahun","6"=">50 Tahun")
Profesi<-list("0"="Missing Data","1"="Pelajar","2"="Ibu Rumah Tangga","3"="Bekerja")
Penghasilan<-list("0"="Missing Data","1"="<Rp 2 Jt","2"="Rp 2-5 Jt","3"="Rp 5 - 10 Jt","4"=">Rp 10 Jt")

Frekuensi_Belanja_Online<-list("0"="Missing Data","1"="Menurun","2"="Tetap","3"="Meningkat")
Preferensi_Belanja_Online<-list("0"="Missing Data","1"="Online","2"="Offline")
Preferensi_Toko_Online<-list("0"="Missing","1"="Tokopedia","2"="Bukalapak","3"="Shopee","4"="Blibli","5"="Lazada","6"="Elevenia","7"="Matahari","8"="OLX","9"="Zalora","10"="Blanja","11"="Gojek")
Preferensi_Booking_Online<-list("0"="Missing","1"="Agoda","2"="Traveloka","3"="Tiket","4"="Booking","5"="Rajakamar","6"="Gojek","7"="uTicket","8"="Tokopedia","9"="Bukalapak","10"="Blibli","11"="Pegi-pegi","12"="Hotels","13"="Airbnb","14"="Airyrooms","15"="Zenrooms","16"="Reddoorz")
Kendaraan_Online<-list("0"="Missing Data","1"="Pernah","2"="Tidak Pernah")

Dictionary_Mapping<-list(
    'Gender' = "Gender",
    'Umur' = "Umur",
    'Profesi' =  "Profesi",
    'Penghasilan' = "Penghasilan",
    'Frekuensi.Belanja.Online' =  "Frekuensi_Belanja_Online",
    'Fashion' = "Preferensi_Belanja_Online",
    'Groceries' = "Preferensi_Belanja_Online",
    'HP' = "Preferensi_Belanja_Online",
    'PC' = "Preferensi_Belanja_Online",
    'Elektronik' = "Preferensi_Belanja_Online",
    'Kosmetik' ="Preferensi_Belanja_Online",
    'Makanan' ="Preferensi_Belanja_Online",
    'Pulsa' ="Preferensi_Belanja_Online",
    'Pesawat'= "Preferensi_Belanja_Online",
    'Kereta' ="Preferensi_Belanja_Online",
    'Hobi' ="Preferensi_Belanja_Online",
    'Hotel' ="Preferensi_Belanja_Online",
    'Konser' ="Preferensi_Belanja_Online",
    'Wisata' ="Preferensi_Belanja_Online",
    'Bioskop' ="Preferensi_Belanja_Online",
    'Kendaraan.Umum' ="Preferensi_Belanja_Online",
    'Preferensi.Toko.Online.1' ="Preferensi_Toko_Online",
    'Preferensi.Toko.Online.2' ="Preferensi_Toko_Online",
    'Preferensi.Toko.Online.3' ="Preferensi_Toko_Online",
    'Preferensi.Booking.Online.1' ="Preferensi_Booking_Online",
    'Preferensi.Booking.Online.2' ="Preferensi_Booking_Online",
    'Preferensi.Booking.Online.3'= "Preferensi_Booking_Online",
    'Gojek.Motor'="Kendaraan_Online" ,
    'Grab.Motor' ="Kendaraan_Online",
    'Uber.Motor' ="Kendaraan_Online",
    'Gojek.Car' ="Kendaraan_Online",
    'Uber.Car' ="Kendaraan_Online",
    'Grab.Car' ="Kendaraan_Online",
    'Grab.Taxi'="Kendaraan_Online"
)

data <- read.csv(file="data_cleaned.csv", header=TRUE)
rownames(data) <- data$X
data<-data[-1]

head(data,5)

for(i in colnames(data))
{
    if(length(unique(data[[i]]))==3)
    {
            print(i)
    }
}

colnames(data)[1+0:(length(colnames(data))-14)]

data_numeric=data

options(warn=-1)
for(element in 0:2)
{
    data$Gender[data$Gender==element]<-Gender[toString(element)]
    data$Fashion[data$Fashion==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Groceries[data$Groceries==element]<-Preferensi_Belanja_Online[toString(element)]
    data$HP[data$HP==element]<-Preferensi_Belanja_Online[toString(element)]
    data$PC[data$PC==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Elektronik[data$Elektronik==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Kosmetik[data$Kosmetik==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Makanan[data$Makanan==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Pulsa[data$Pulsa==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Pesawat[data$Pesawat==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Kereta[data$Kereta==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Hobi[data$Hobi==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Hotel[data$Hotel==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Konser[data$Konser==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Wisata[data$Wisata==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Bioskop[data$Bioskop==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Kendaraan.Umum[data$Kendaraan.Umum==element]<-Preferensi_Belanja_Online[toString(element)]
    data$Gojek.Motor[data$Gojek.Motor==element]<-Kendaraan_Online[toString(element)]
    data$Gojek.Car[data$Gojek.Car==element]<-Kendaraan_Online[toString(element)]
    data$Grab.Motor[data$Grab.Motor==element]<-Kendaraan_Online[toString(element)]
    data$Grab.Car[data$Grab.Car==element]<-Kendaraan_Online[toString(element)]
    data$Grab.Taxi[data$Grab.Taxi==element]<-Kendaraan_Online[toString(element)]
    data$Uber.Motor[data$Uber.Motor==element]<-Kendaraan_Online[toString(element)]
    data$Uber.Car[data$Uber.Car==element]<-Kendaraan_Online[toString(element)]
}
for(element in 0:3)
{
    data$Profesi[data$Profesi==element]<-Profesi[toString(element)]
    data$Frekuensi.Belanja.Online[data$Frekuensi.Belanja.Online==element]<-Frekuensi_Belanja_Online[toString(element)]
}
for(element in 0:4)
{
    data$Penghasilan[data$Penghasilan==element]<-Penghasilan[toString(element)]
}
for(element in 0:6)
{
    data$Umur[data$Umur==element]<-Umur[toString(element)]
}
for(element in 0:11)
{
    data$Preferensi.Toko.Online.1[data$Preferensi.Toko.Online.1==element]<-Preferensi_Toko_Online[toString(element)]
    data$Preferensi.Toko.Online.2[data$Preferensi.Toko.Online.2==element]<-Preferensi_Toko_Online[toString(element)]
    data$Preferensi.Toko.Online.3[data$Preferensi.Toko.Online.3==element]<-Preferensi_Toko_Online[toString(element)]
}
for(element in 0:16)
{
    data$Preferensi.Booking.Online.1[data$Preferensi.Booking.Online.1==element]<-Preferensi_Booking_Online[toString(element)]
    data$Preferensi.Booking.Online.2[data$Preferensi.Booking.Online.2==element]<-Preferensi_Booking_Online[toString(element)]
    data$Preferensi.Booking.Online.3[data$Preferensi.Booking.Online.3==element]<-Preferensi_Booking_Online[toString(element)]
}
options(warn=0)

data_string=data

color<-c('#794044','#0E2F44','#008080','#800080','#008000')
targets<-colnames(data)[1+0:(length(colnames(data))-14)]
for (target in colnames(data))
{
        if(length(unique(data[[target]]))<=9)
        {
        save_file=paste("histogram/",target,".png",sep="")
        dev.copy(png,save_file,res=100,width=1280,height=720)
        Data<-data_numeric[[target]]
        if(length(unique(data[[target]]))==3)
        {
            cx=1
            ls=1
            hz=FALSE
        }
        if(length(unique(data[[target]]))==4)
        {
            cx=1
            ls=1
            hz=FALSE
        }
        if(length(unique(data[[target]]))==5)
        {
            cx=1
            ls=1
            hz=FALSE
        }
        if(length(unique(data[[target]]))==7)
        {
            cx=1
            ls=1
            hz=FALSE
        }
        if(length(unique(data[[target]]))==12)
        {
            cx=1
            ls=1
            hz=FALSE
        }
        if(length(unique(data[[target]]))==17)
        {
            cx=1
            ls=1
            hz=FALSE
        }
        exp<-paste('barplot(table(data_numeric[[target]]),col="#794044",names.arg=',Dictionary_Mapping[target],',horiz=',hz,',space=0.05,las=',ls,',cex.names=',cx,')')
        eval(parse(text=exp))
        dev.off()
        }
}


for (element in colnames(data)) 
{
    if(length(unique(data_numeric[[element]]))<=3)
    {
        temp<-data_numeric[[element]]
        N=length(temp[temp==1])+length(temp[temp==2])
        p=length(temp[temp==1])/N
        standard_error=sqrt(p*(1-p)/N)
        critical_value=1.96
        margin_of_error=standard_error*critical_value
        print(element)
        text<-paste('P (Sample): ',round(p,2),sep='')
        print(text)
        text<-paste('95% Confidence Interval : ',round((p-margin_of_error),2),' < P < ',round((p+margin_of_error),2),sep='')
        print(text)
        critical_value=2.58
        margin_of_error=standard_error*critical_value
        text<-paste('99% Confidence Interval : ',round((p-margin_of_error),2),' < P < ',round((p+margin_of_error),2),sep='')
        print(text)
        print('')
    }
}

for (element in colnames(data))
{
    if(length(unique(data_numeric[[element]]))<=3)
    {
        temp<-data_numeric[[element]]
        N=length(temp[temp==1])+length(temp[temp==2])
        p=length(temp[temp==1])/N
        standard_error=sqrt(p*(1-p)/N)
        critical_value=1.96
        margin_of_error=standard_error*critical_value
        print(element)
        text<-paste('Mean : ',p*100,sep='')
        print(text)
        text<-paste('99% Confidence Interval : ',(p-margin_of_error)*100,'<x<',(p+margin_of_error)*100,sep='')
        print(text)
        print('')
    }
}

table(data_numeric[["Preferensi.Toko.Online.1"]])
table(data_numeric[["Preferensi.Toko.Online.2"]])
table(data_numeric[["Preferensi.Toko.Online.3"]])

table(data_numeric[["Preferensi.Booking.Online.1"]])
table(data_numeric[["Preferensi.Booking.Online.2"]])
table(data_numeric[["Preferensi.Booking.Online.3"]])

toko<-c(0,510,327,198,46,308,32,32,106,67,2,445)
booking<-c(0,228,641,263,76,14,240,18,175,81,42,82,14,73,56,3,5)

save_file=paste("histogram/toko.png",sep="")
dev.copy(png,save_file,res=100,width=800,height=600)
barplot(toko,names.arg=Preferensi_Toko_Online,space=0.05,col="#794044",horiz=TRUE,las=1,cex.names=0.7)
dev.off()

save_file=paste("histogram/booking.png",sep="")
dev.copy(png,save_file,res=100,width=800,height=600)
barplot(booking,names.arg=Preferensi_Booking_Online,space=0.05,col="#794044",horiz=TRUE,las=1,cex.names=0.675)
dev.off()


sum(toko)
sum(booking)

N=768
p=240/N
standard_error=sqrt(p*(1-p)/N)
critical_value=2.57
margin_of_error=standard_error*critical_value
text<-paste('Mean : ',p*100,sep='')
print(text)
text<-paste('99% Confidence Interval : ',(p-margin_of_error)*100,'<x<',(p+margin_of_error)*100,sep='')
print(text)
print('')
