from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS for frontend communication

app = Flask(__name__)
CORS(app)  # Allow frontend (HTML) to access the backend

# BMI Category Function
def categorize_bmi(bmi):
    if bmi < 16: return "Severe Thinness"
    elif bmi < 17: return "Moderate Thinness"
    elif bmi < 18.5: return "Mild Thinness"
    elif bmi < 25: return "Normal"
    elif bmi < 30: return "Overweight"
    elif bmi < 35: return "Obese Class I"
    elif bmi < 40: return "Obese Class II"
    else: return "Obese Class III"

# Route to Calculate BMI
@app.route('/calculate-bmi', methods=['GET'])
def calculate_bmi():
    weight = request.args.get('weight')
    height = request.args.get('height')

    if not weight or not height:
        return jsonify({"error": "Weight and height are required!"}), 400

    try:
        weight = float(weight)
        height = float(height)

        if height <= 0:
            return jsonify({"error": "Height must be greater than zero"}), 400

        bmi = round(weight / (height ** 2), 2)
        category = categorize_bmi(bmi)

        return jsonify({"bmi": bmi, "category": category})
    
    except ValueError:
        return jsonify({"error": "Invalid numeric values"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Runs on port 5000
