import joblib
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# from joblib import load
app = Flask(__name__)


# Load the model
model = joblib.load('nuruel_random_forest_clasfier_model.pkl')


# Define the preprocessing function
def preprocess_input(data):
    # Convert the following numerical labels from integer to float
    float_array = data[["night_mainland", "night_zanzibar"]].values.astype(float)

    binary_features = ['package_transport_int', 'package_accomodation', 'package_food',
                       'package_transport_tz', 'package_sightseeing', 'package_guided_tour',
                       'package_insurance', 'first_trip_tz']

    numerical_features = ['total_female', 'total_male', 'night_mainland', 'night_zanzibar']

    # Label encode binary features
    le = LabelEncoder()
    # Label Encoder conversion
    data["package_transport_int"] = le.fit_transform(data["package_transport_int"])
    data["package_accomodation"] = le.fit_transform(data["package_accomodation"])
    data["package_food"] = le.fit_transform(data["package_food"])
    data["package_transport_tz"] = le.fit_transform(data["package_transport_tz"])
    data["package_sightseeing"] = le.fit_transform(data["package_sightseeing"])
    data["package_guided_tour"] = le.fit_transform(data["package_guided_tour"])
    data["package_insurance"] = le.fit_transform(data["package_insurance"])
    data["main_activity"] = le.fit_transform(data["main_activity"])
    data["purpose"] = le.fit_transform(data["purpose"])
    data["age_group"] = le.fit_transform(data["age_group"])
    data["country"] = le.fit_transform(data["country"])
    data["travel_with"] = le.fit_transform(data["travel_with"])

    # scale our data into range of 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)

    return data


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_cost():
    if request.method == 'POST':
        # Extract form data
        input_data = {
            'country': request.form['country'],
            'age_group': request.form['age_group'],
            'travel_with': request.form['travel_with'],
            'total_female': float(request.form['total_female']),
            'total_male': float(request.form['total_male']),
            'purpose': request.form['purpose'],
            'main_activity': request.form['main_activity'],
            'package_transport_int': request.form['package_transport_int'],
            'package_accomodation': request.form['package_accomodation'],
            'package_food': request.form['package_food'],
            'package_transport_tz': request.form['package_transport_tz'],
            'package_sightseeing': request.form['package_sightseeing'],
            'package_guided_tour': request.form['package_guided_tour'],
            'package_insurance': request.form['package_insurance'],
            'night_mainland': float(request.form['night_mainland']),
            'night_zanzibar': float(request.form['night_zanzibar']),
        }

        # Convert the data into a DataFrame and preprocess it
        input_df = pd.DataFrame([input_data])
        processed_input = preprocess_input(input_df)

        # Predict the cost range
        prediction = model.predict(processed_input)

        # Display the prediction
        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)