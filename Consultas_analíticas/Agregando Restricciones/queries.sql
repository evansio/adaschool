--Calcular el precio promedio de los productos en cada categoría.
SELECT
    c.nombre AS categoria_nombre,
    AVG(p.precio_unitario) AS precio_promedio
FROM
    categorias c
JOIN
    productos p ON c.id = p.categoria_id
GROUP BY
    c.nombre;

--Obtener la cantidad total de productos en stock por categoría.
SELECT
    c.nombre AS categoria_nombre,
    SUM(s.cantidad) AS total_productos_en_stock
FROM
    categorias c
JOIN
    productos p ON c.id = p.categoria_id
JOIN
    stocks s ON p.id = s.producto_id
GROUP BY
    c.nombre;

--Calcular el total de ventas por sucursal.
SELECT
    s.nombre AS sucursal_nombre,
    SUM(i.monto_venta) AS total_ventas
FROM
    sucursales s
JOIN
    ordenes o ON s.id = o.sucursal_id
JOIN
    items i ON o.id = i.orden_id
GROUP BY
    s.nombre;

--Obtener el cliente que ha realizado el mayor monto de compras.
SELECT
    c.nombre AS cliente_nombre,
    SUM(i.monto_venta) AS total_compras
FROM
    clientes c
JOIN
    ordenes o ON c.id = o.cliente_id
JOIN
    items i ON o.id = i.orden_id
GROUP BY
    c.nombre
ORDER BY
    total_compras DESC
LIMIT 1;
