from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import stripe
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['STRIPE_TEST_PUBLIC_KEY'] = os.getenv('STRIPE_TEST_PUBLIC_KEY')
app.config['STRIPE_TEST_SECRET_KEY'] = os.getenv('STRIPE_TEST_SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
stripe.api_key = os.getenv('STRIPE_TEST_SECRET_KEY')

@app.route('/')
def index():
    return "Welcome to the Restaurant Order Web Application"

@app.route('/order', methods=['POST'])
def create_order():
    # Handle order creation
    pass

@app.route('/orders', methods=['GET'])
def get_orders():
    # Handle retrieving orders
    pass

if __name__ == '__main__':
    app.run(debug=True)
