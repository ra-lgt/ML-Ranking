import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
path="test.xlsx"
file=pd.read_excel("./data.xlsx")
data=file.drop(columns=["Sno"])
plt.xlabel("codelab")

plt.ylabel("position")
plt.scatter(data["skillrack"],data["position"],color="blue")
plt.scatter(data["hackerrank"],data["position"],color="green")
plt.scatter(data["leetcode"],data["position"],color="black")
plt.show()

x=data[["skillrack","hackerrank","leetcode"]]
y=data["position"]
#	print(len(x),len(y))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=LogisticRegression(max_iter=10000)
model.fit(x_train,y_train)
position=[]
try:
	f=pd.read_excel(path)

	for s,h,l in zip(f["skillrack"],f["hackerrank"],f["leetcode"]):
		lst=[]
		lst.append(s)
		lst.append(h)
		lst.append(l)
		var=np.reshape(lst,(1,-1))
		warnings.filterwarnings('ignore')
		flag=model.predict(var)
		position.append(flag)
		lst.clear()
except Exception as e:
	print(e)

output={

	}
dataframe=pd.DataFrame(output)
name=list(f["name"])
dataframe.insert(0,'name',name)
dataframe.insert(1,'position',position)

print(dataframe)
	

