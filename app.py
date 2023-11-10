#author kiran narayan
from flask import Flask, request, jsonify, render_template, Response
import os
from flask_cors import CORS, cross_origin

from apparel.prediction.predict import WarehouseApparel
from apparel.utils.common import *

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "input_image.jpg"
        self.object_detection = WarehouseApparel(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        print('image')
        decodeImage(image, clApp.filename)
        result = clApp.object_detection.detect()
        
    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)






if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)


