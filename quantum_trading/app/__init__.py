from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)

from app.core.engine import trading_engine, risk_engine # Import ciclico intenzionale