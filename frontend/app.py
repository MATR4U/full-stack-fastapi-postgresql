from flask import Flask
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

from routes.main import main

app.register_blueprint(main)

if __name__ == '__main__':
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    app.run(port=port)
