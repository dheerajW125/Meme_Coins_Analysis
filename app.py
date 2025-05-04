from flask import Flask
from utils.coin_routes import coin_routes 

app = Flask(__name__)
app.register_blueprint(coin_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
