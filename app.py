from flask import Flask, request, jsonify
import json 
import logging
import redis
import joblib
import numpy as np
import os 

# load environment variables 
MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1:8000")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename = os.path.join(log_dir, "app.log"),
    level=logging.DEBUG, 
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)

logger  = logging.getLogger("module 1")

app = Flask(__name__)
model = joblib.load("model.pkl")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def home():
    logger.debug("inside home page of the app")
    return "Welcome to Iris Flower prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    logger.debug("get the json data")

    # redis only takes string
    input_data = json.dumps(data)
    logger.debug("converted json to string")
    
    # if redis has already data present in cache then get the key 
    if r.exists(input_data):
        prediction=r.get(input_data)
        source = "cache"
        logger.debug(f"get prediction from cache {prediction}")
    else:
        input_data = np.array(data["features"]).reshape(-1, 1)
        prediction = model.predict(input_data)[0]
        r.set(input_data, prediction)
        source = "model"
        logger.debug(f"predict input from the model {prediction}")

    # prediction = model.predict([data["features"]])
    logger.debug("return prediction")
    return jsonify({"prediction": prediction, "source": source})

## include entry point 
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)