import COVID19Py
import matplotlib.pyplot as plt
covid19=COVID19Py.COVID19()
data=covid19.getAll(timelines=True)
virusdetails=dict(data["latest"])
names=list(virusdetails.keys())
Values=list(virusdetails.values())
plt.bar(range(len(virusdetails)),Values,tick_label=names)
plt.show()
print(virusdetails)