from flask import Flask, render_template, request
import paho.mqtt.publish as publish

app = Flask(__name__)

mqtt_broker_ip = "mqtt-broker-ip"  # Replace with your MQTT broker IP

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    color = request.form['color']
    if color == "off":
        publish.single("neopixel/control", "off", hostname="broker.emqx.io")
    else:
        publish.single("neopixel/control", color, hostname="broker.emqx.io")
    return render_template('index.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)
