const express = require('express');
const router = express.Router();
const { obtenerProductos, crearProducto } = require('./productos.controller');

router.get('/', obtenerProductos);
router.post('/agregarProducto', crearProducto);

module.exports = router;
