require('dotenv').config();

const config = {
    server: process.env.DB_SERVER,
    database: process.env.DB_DATABASE,
    options: {
        encrypt: false,  // No cifra la conexión (ajústalo según sea necesario)
        trustServerCertificate: true
    },
    authentication: {
        type: 'ntlm',  // Autenticación de Windows
        options: {
            domain: process.env.DB_DOMAIN,  // Dominio de Windows
            userName: process.env.DB_USER,  // Usuario de Windows
            password: process.env.DB_PASSWORD  // Contraseña de Windows
        }
    },
    port: parseInt(process.env.DB_SERVER_PORT)
};

module.exports = config;
