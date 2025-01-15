require('dotenv').config();
const express = require('express');
const cors = require('cors');
const productosRoutes = require('./productos.routes');

const app = express();
app.use(express.json());
app.use(cors());

// Rutas
app.use('/api/productos', productosRoutes);

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});

const sql = require('mssql');
const config = require('./config');

const probarConexion = async () => {
    try {
        let pool = await sql.connect(config);
        console.log('🔗 Conexión exitosa a SQL Server');
        pool.close();
    } catch (err) {
        console.error('❌ Error al conectar a SQL Server:', err);
    }
};

probarConexion();