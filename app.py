from flask import Flask, render_template, request
from markupsafe import Markup
from model import predict_image
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)

            plant_info = utils.plant_geo[prediction]
            result_html = Markup(plant_info['desc'])
            locations = plant_info['locations']
            census = plant_info.get('census', {})

            return render_template(
                'display.html',
                result=result_html,
                plant_name=prediction,
                locations=locations,
                census=census,
                scientific_name=plant_info.get('scientific_name'),
                uses=plant_info.get('uses'),
                flowering_season=plant_info.get('flowering_season'),
                biodiversity_zone=plant_info.get('biodiversity_zone')
            )
        except Exception as e:
            print("Error:", e)

    return render_template('index.html', status=500, res="Internal Server Error")


if __name__ == "__main__":
    app.run(debug=True)
