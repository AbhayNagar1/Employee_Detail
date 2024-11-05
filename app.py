from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # API URL
    url = "https://erp.myapex.in/ords/rest_api/hr/employees/?empno=7499"

    # Making the GET request
    response = requests.get(url)
    employee_data = {}

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extracting employee data from the response
        if 'items' in data and len(data['items']) > 0:
            employee_data = data['items'][0]

    return render_template('index.html', employee=employee_data)

if __name__ == '__main__':
    app.run(debug=True)
