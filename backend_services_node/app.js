const express = require('express');
const app = express();
require('dotenv').config();
const { getDbs, getDealerships } = require('./db');

app.get('/api/dbs', async (req, res) => {
    const params = {
        COUCH_URL: process.env.COUCH_URL,
        IAM_API_KEY: process.env.IAM_API_KEY
    };

    try {
        const dbs = await getDbs(params);
        if (dbs.error) {
            throw new Error(dbs.error);
        } else {
            res.status(200).json(dbs);
        }
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.get('/api/dealerships', async (req, res) => {
    const params = {
        COUCH_URL: process.env.COUCH_URL,
        IAM_API_KEY: process.env.IAM_API_KEY
    };
    const state = req.query.state; // Get state from query parameters

    try {
        const dealerships = await getDealerships(params, state);
        res.status(200).json(dealerships);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}`));