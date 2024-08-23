from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ehtx7132'
csrf = CSRFProtect(app)

from app import routes
