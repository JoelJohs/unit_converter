from flask import Flask, render_template, request

def convert_length(value, from_unit, to_unit):
    # Factores de conversión a metros
    conversions = {
        'milímetro': 0.001,
        'centímetro': 0.01,
        'metro': 1.0,
        'kilómetro': 1000.0,
        'pulgada': 0.0254,
        'pie': 0.3048,
        'yarda': 0.9144,
        'milla': 1609.34
    }
    
    try:
        meters = float(value) * conversions[from_unit]
        result = meters / conversions[to_unit]
        return round(result, 6)
    except:
        return None

def convert_weight(value, from_unit, to_unit):
    # Factores de conversión a kilogramos
    conversions = {
        'miligramo': 0.000001,
        'gramo': 0.001,
        'kilogramo': 1.0,
        'onza': 0.0283495,
        'libra': 0.453592
    }
    
    try:
        kg = float(value) * conversions[from_unit]
        result = kg / conversions[to_unit]
        return round(result, 6)
    except:
        return None
    

def convert_temperature(value, from_unit, to_unit):
    try:
        temp = float(value)
        if from_unit == 'celsius':
            if to_unit == 'fahrenheit':
                return round((temp * 9/5) + 32, 2)
            elif to_unit == 'kelvin':
                return round(temp + 273.15, 2)
            else:
                return temp
        elif from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return round((temp - 32) * 5/9, 2)
            elif to_unit == 'kelvin':
                return round((temp - 32) * 5/9 + 273.15, 2)
            else:
                return temp
        elif from_unit == 'kelvin':
            if to_unit == 'celsius':
                return round(temp - 273.15, 2)
            elif to_unit == 'fahrenheit':
                return round((temp - 273.15) * 9/5 + 32, 2)
            else:
                return temp
    except:
        return None

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    result = None
    if request.method == 'POST':
        value = request.form['value']
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_length(value, from_unit, to_unit)
    
    units = ['milímetro', 'centímetro', 'metro', 'kilómetro', 'pulgada', 'pie', 'yarda', 'milla']
    return render_template('length.html', units=units, result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight_converter():
    result = None
    if request.method == 'POST':
        value = request.form['value']
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_weight(value, from_unit, to_unit)

    units = ['miligramo', 'gramo', 'kilogramo', 'onza', 'libra']    
    return render_template('weight.html', units=units, result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature_converter():
    result = None
    if request.method == 'POST':
        value = request.form['value']
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_temperature(value, from_unit, to_unit)
    
    units = ['celsius', 'fahrenheit', 'kelvin']
    return render_template('temperature.html', units=units, result=result)

if __name__ == '__main__':
    app.run(debug=True)


