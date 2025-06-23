from app import app 
import json

def test_result():
    response_def = app.test_client().get('/')
    assert response_def.status_code==200
    assert response_def.data==b"Welcome to Iris Flower prediction API"

    # testing with features [5.1, 3.3, 1.7, 0.5]
    test_data={'features:' [5.1, 3.3, 1.7, 0.5]}

    # predicting with post request
    response_predict = app.test_client().post(
            '/predict',
            data=json.dumps(test_data),
            content_type='application/json'
        )
    assert response_predict.status_code==200

    # 
    response_json = response_predict.get_json()
    assert "prediction" in response_json
    assert "source" in response_json
    expected_class = [0, 1, 2, 3]
    assert response_json['prediction'] in expected_class