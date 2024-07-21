from flask import Flask, jsonify, make_response
import json

app = Flask(__name__)

country_data = {}

# Función para cargar datos desde el archivo
def load_country_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 3:
                country, capital, continent = parts
                country_data[country] = {'capital': capital, 'continent': continent}

# Cargar los datos al iniciar la aplicación
load_country_data('country_data.txt')

@app.route('/get_capital/<country>', methods=['GET'])
def get_capital(country):
    data = country_data.get(country)
    
    if data:
        response_data = {'Country': country, 'Capital': data['capital'], 'Continent': data['continent']}
    else:
        response_data = {'error': 'Country not found'}
        response = make_response(json.dumps(response_data, ensure_ascii=False), 404)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

    response = make_response(json.dumps(response_data, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True)
