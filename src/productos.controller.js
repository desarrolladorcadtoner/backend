const sql = require('mssql');
const config = require('./config');

// Obtener todos los productos
const obtenerProductos = async (req, res) => {
    try {
        let pool = await sql.connect(config);
        let productos = await pool.request().query('SELECT * FROM Productos$');
        res.json(productos.recordset);
        pool.close();
    } catch (err) {
        res.status(500).send({ mensaje: 'Error al obtener productos', error: err.message });
    }
};

// Crear nuevo producto
const crearProducto = async (req, res) => {
    const { nombre, descripcion, precio, stock, imagen } = req.body;

    if (!nombre || !descripcion || !precio || !stock || !imagen) {
        res.status(400).send({ mensaje: 'Todos los campos son obligatorios' });
        return;
    }

    try {
        let pool = await sql.connect(config);
        let resultado = await pool.request()
            .input('nombre', sql.NVarChar, nombre)
            .input('descripcion', sql.NVarChar, descripcion)
            .input('precio', sql.Decimal(10, 2), precio)
            .input('stock', sql.Int, stock)
            .input('imagen', sql.NVarChar, imagen)
            .query(
                'INSERT INTO Productos (nombre, descripcion, precio, stock, imagen) VALUES (@nombre, @descripcion, @precio, @stock, @imagen)'
            );
        res.status(201).send({ mensaje: 'Producto creado con éxito' });
        pool.close();
    } catch (err) {
        res.status(500).send({ mensaje: 'Error al crear producto', error: err.message });
    }
};

module.exports = {
    obtenerProductos,
    crearProducto
};