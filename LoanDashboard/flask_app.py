# from flask import Flask, jsonify, render_template
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/results')
# def get_results():
#     # Load or generate results
#     data = pd.DataFrame({
#         'ID': [1, 2, 3],
#         'Prediction': [1, 0.5, 1]  # Example predictions
#     })
#     return jsonify(data.to_dict(orient='records'))

# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=5000)
# 8888888888888888888888888888888888888888888888888888888888888888888888888888888888
# from flask import Flask, render_template, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/data')
# def get_data():
#     # Sample data to mimic your dashboard
#     return jsonify({
#         "status_data": [4, 60, 14, 33],
#         "priority_data": [5, 45, 30, 20],
#         "workload_data": [61, 39],
#         "team_labels": ["Aniket Goyal", "Srijan Kafle"]
#     })

# if __name__ == '__main__':
#     app.run(debug=True)
# 88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Link to the dashboard page

if __name__ == "__main__":
    app.run(debug=True)

