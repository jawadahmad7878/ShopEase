// product-service/routes/products.js

const express = require('express');
const router = express.Router();

// Mock product data
const products = [
    { id: 1, name: 'Product 1', price: 10.00 },
    { id: 2, name: 'Product 2', price: 20.00 },
];

// Get all products
router.get('/', (req, res) => {
    res.json(products);
});

// Get a specific product by ID
router.get('/:id', (req, res) => {
    const product = products.find(p => p.id === parseInt(req.params.id));
    if (!product) return res.status(404).send('Product not found');
    res.json(product);
});

module.exports = router;
