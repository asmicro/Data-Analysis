import pandas as pd
import matplotlib.pyplot as plt

EXCEL_FILE = "cars_engage_2022.csv"
df = pd.read_csv(EXCEL_FILE)

x = []
y = []
z = []
ind = []

torque = df['Torque']

for i in range(0, len(df)):
    s = ""
    t = ""
    # Splitting Torque(Nm) and Engine speed(rpm) from Torque column
    if type(torque[i]) != float and 'Nm' in torque[i] and 'rpm' in torque[i]:
        a = torque[i].split('@')[0]
        b = torque[i].split('@')[1]
        for p in b:
            if 48 <= ord(p) <= 57:
                s = s + p
            if len(s) == 4:
                break
        z.append(int(s))
        for q in a:
            if 48 <= ord(q) <= 57:
                t = t + q
            else:
                break
        if int(t) in y:
            ind.append(len(z)-1)
        else:
            y.append(int(t))

for i in range(0, len(z)):
    if i in ind:
        continue
    else:
        x.append(z[i])

# Graph with Engine Speed on X-axis and Torque on Y-axis
plt.plot(x, y)
plt.xlabel('Engine Speed(rpm)')
plt.ylabel('Torque(Nm)')
plt.title('Engine Speed - Torque')
plt.show()
