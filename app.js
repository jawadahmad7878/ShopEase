// product-service/app.js

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Import routes
const productRoutes = require('./routes/products');

// Use routes
app.use('/products', productRoutes);

// Start the server
app.listen(port, () => {
    console.log(`Product Service running at http://localhost:${port}`);
});
