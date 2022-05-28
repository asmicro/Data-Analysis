import pandas as pd
from collections import OrderedDict
from flask import Flask, render_template, request

app = Flask(__name__)


# function to convert String to Integer
def strToInt(s):
    st = ""
    for i in s:
        if ord(i) >= 48 and ord(i) <= 57:
            st = st + i
    return int(st)


EXCEL_FILE = "cars_engage_2022.csv"
df = pd.read_csv(EXCEL_FILE)


# Route to render Homepage
@app.route('/')
def index():
    return render_template('index.html')


# Function to generate results according to the given filters
@app.route('/', methods=['POST'])
def filter():
    ind = []
    values = []
    price = request.form["price"]
    fuel = request.form['fuel']
    type = request.form['type']
    cap = request.form['cap']
    p_a = strToInt(price.split('_')[0])
    p_b = strToInt(price.split('_')[1])
    c_a = strToInt(cap.split('_')[0])
    c_b = strToInt(cap.split('_')[1])
    prices = df['Ex-Showroom_Price']
    fuels = df['Fuel_Type']
    types = df['Type']
    caps = df['Displacement']
    make = df['Make']
    model = df['Model']
    variant = df['Variant']
    height = df['Height']
    length = df['Length']
    width = df['Width']
    gears = df['Gears']
    seating_Capacity = df['Seating_Capacity']
    torque = df['Torque']

    # Condition which extracts row according to the  given filter
    for i in range(0, len(df)):
        if strToInt(prices[i]) >= p_a and strToInt(prices[i]) <= p_b and fuels[i] == fuel and types[i] == type and caps[i] != '' and strToInt(caps[i]) >= c_a and strToInt(caps[i]) <= c_b:
            ind.append(i)

    for i in range(0, len(ind)):
        value = {}
        value['make'] = make[ind[i]]
        value['model'] = model[ind[i]]
        value['variant'] = variant[ind[i]]
        value['height'] = height[ind[i]]
        value['length'] = length[ind[i]]
        value['width'] = width[ind[i]]
        value['gears'] = gears[ind[i]]
        value['seating_Capacity'] = seating_Capacity[ind[i]]
        value['torque'] = torque[ind[i]]
        values.append(value)
    length = len(ind)
    return render_template('index.html', values=values, length=length)


# Method to print cars which can be launched on consideration to some important criteria
@app.route('/launch')
def launch():
    launches = []
    make = df['Make']
    model = df['Model']
    power = df['Power']
    variant = df['Variant']
    avgfuel = df['Average_Fuel_Consumption']
    childsafety = df['Child_Safety_Locks']
    abs = df['ABS_(Anti-lock_Braking_System)']
    airbags = df['Airbags']
    speedalert = df['High_Speed_Alert_System']
    ebd = df['EBD_(Electronic_Brake-force_Distribution)']
    for i in range(0, len(df)):
        if avgfuel[i] == 'Yes' and childsafety[i] == 'Yes' and abs[i] == 'Yes' and airbags[i] != '' and speedalert[i] == 'Yes' and ebd[i] == 'Yes':
            value = {}
            value['make'] = make[i]
            value['model'] = model[i]
            value['variant'] = variant[i]
            launches.append(value)

    dict = {}
    for i in range(0, len(df)):
        s = ""
        for x in power[i]:
            if ord(x) >= 48 and ord(x) <= 57:
                s = s + x
            else:
                break
        if type(make[i]) == float:
            if 'Mercedes-Benz' in model[i]:
                dict[strToInt(s)] = 'Mercedes-Benz'
            elif 'Rolls-Royce' in model[i]:
                dict[strToInt(s)] = 'Rolls-Royce'
        else:
            dict[strToInt(s)] = make[i]
    # dict1 stores reverse sorted list containing power
    dict1 = OrderedDict(reversed(sorted(dict.items())))
    a = []
    for key in dict1:
        if not dict1[key] in a:
            a.append(dict1[key])
    length = len(a)
    return render_template('launch.html', launches=launches, a=a, length=length)


# Route to render Profiling Report of .csv sheet
@app.route('/cars')
def cars():
    return render_template('cars_engage_2022.html')


if __name__ == '__main__':
    app.run(debug=True)
