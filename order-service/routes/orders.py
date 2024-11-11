# order-service/routes/orders.py
from flask import Blueprint, jsonify

# Create a Blueprint for the orders
order_bp = Blueprint('orders', __name__)

# Dummy order data (this can be replaced with actual database logic)
orders_data = [
    {"order_id": 1, "product": "Laptop", "quantity": 1, "price": 1200},
    {"order_id": 2, "product": "Smartphone", "quantity": 2, "price": 500},
    {"order_id": 3, "product": "Headphones", "quantity": 3, "price": 150}
]

# Define the route for fetching orders
@order_bp.route('/', methods=['GET'])
def get_orders():
    return jsonify(orders_data)

# Define the route for fetching a specific order by ID
@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders_data if order['order_id'] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"message": "Order not found"}), 404
