const Cloudant = require('@cloudant/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function getDbs(params) {
    const cloudant = Cloudant({
        url: params.COUCH_URL,
        plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } },
    });

    return new Promise((resolve, reject) => {
        cloudant.db.list()
            .then(body => {
                console.log(body); // Print the list of databases to the console
                resolve({ dbs: body });
            })
            .catch(err => {
                reject({ err: err.message });
            });
    });
}

function getDealerships(params, state) {
    const cloudant = Cloudant({
        url: params.COUCH_URL,
        plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
    });

    return new Promise((resolve, reject) => {
        const dealershipsDb = cloudant.use('dealerships');
        const selector = state ? { "state": state } : {}; // If state is provided, filter documents by state
        dealershipsDb.find({ selector: selector }) 
            .then(body => {
                const dealerships = body.docs;
                console.log(JSON.stringify(dealerships, null, 2)); // This will print the JSON to the console
                resolve(dealerships);
            })
            .catch(err => {
                reject(err);
            });
    });
}

module.exports = { getDealerships, getDbs };