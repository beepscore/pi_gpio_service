from flask import Flask, jsonify, request

app = Flask(__name__)
# app.debug = True

# / is the website root, the entry point
# http://127.0.0.1:5000
# home http://127.0.0.1
# port :5000
@app.route('/')
@app.route("/api/v1/ping/", methods=['GET'])
def api_status():
    if request.method == 'GET':
        data = {'api_name': 'pi_gpio_service',
                'version': '1.0',
                'status': 'SUCCESS',
                'response': 'pong'}
        return jsonify(data)


if __name__ == '__main__':
    # '0.0.0.0' accessible to any device on the network
    app.run(host='0.0.0.0', debug=True)
