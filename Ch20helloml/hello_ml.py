import pandas as pd
import matplotlib.pyplot as plt
data={
    "metrekare":[100,80,120,150,200],
    "oda_sayisi":[2,1,3,4,5],
    "fiyat":[135000,120000,150000,190000,240000],
}

df=pd.DataFrame(data)
print(df)
#df.plot(x="metrekare", y="fiyat", kind="line")  # veya kind="bar", "scatter"
#plt.show()

df.plot(x="oda_sayisi", y="fiyat", kind="scatter")  # Oda sayısına göre fiyat
plt.title("Oda Sayısına Göre Fiyat")
plt.xlabel("Oda Sayısı")
plt.ylabel("Fiyat (TL)")
plt.grid()
plt.show()