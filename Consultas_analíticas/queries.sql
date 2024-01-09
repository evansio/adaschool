--Obtener el precio mínimo, precio máximo y precio promedio de todos los productos.
SELECT
    MIN(precio_unitario) AS precio_minimo,
    MAX(precio_unitario) AS precio_maximo,
    AVG(precio_unitario) AS precio_promedio
FROM productos;

--Calcular la cantidad total de productos en stock por sucursal.
SELECT
    s.id AS sucursal_id,
    s.nombre AS sucursal_nombre,
    SUM(st.cantidad) AS total_productos_en_stock
FROM
    sucursales s
JOIN
    stocks st ON s.id = st.sucursal_id
GROUP BY
    s.id, s.nombre;


--Obtener el total de ventas por cliente.
SELECT
    c.id AS cliente_id,
    c.nombre AS cliente_nombre,
    SUM(i.monto_venta) AS total_ventas
FROM clientes c
JOIN ordenes o ON c.id = o.cliente_id
JOIN items i ON o.id = i.orden_id
GROUP BY c.id, c.nombre;
