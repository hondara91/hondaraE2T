

select NOMBREARTÍCULO,PRECIO from productos
    where SECCIÓN = 'CERÁMICA'
    order by PRECIO


select NOMBREARTÍCULO,PRECIO from productos
    WHERE SECCIÓN = 'CERÁMICA'
    order by PRECIO

select NOMBREARTÍCULO,PRECIO from productos
    WHERE SECCIÓN = 'CERÁMICA' or SECCIÓN = 'DEPORTES'
    order by SECCIÓN,PRECIO
 
 select NOMBREARTÍCULO,FECHA from productos
    WHERE SECCIÓN = 'DEPORTES' AND PAÍSDEORIGEN = 'USA'

select avg(PRECIO),SECCIÓN from productos
    WHERE SECCIÓN = 'DEPORTES'
    GROUP BY SECCIÓN

select avg(PRECIO),SECCIÓN from productos
    GROUP BY SECCIÓN
    HAVING SECCIÓN = 'DEPORTES'


SELECT distinct POBLACIÓN from clientes

select count(RESPONSABLE) AS NOMBRE_CLIENTE, EMPRESA from clientes 
    WHERE RESPONSABLE like 'JOSÉ%'
    GROUP BY EMPRESA

select count(RESPONSABLE) AS [NOMBRE CLIENTE], EMPRESA from clientes 
    GROUP BY EMPRESA, RESPONSABLE
    HAVING responsable like 'JOSÉ%'

SELECT NÚMERO_DE_PEDIDO, RESPONSABLE
    FROM pedidos inner join clientes
    ON pedidos.CÓDIGO_CLIENTE = clientes.CÓDIGOCLIENTE
    WHERE clientes.RESPONSABLE like '%ngel M%'

SELECT count(NÚMERO_DE_PEDIDO) AS TOTAL_PEDIDOS, RESPONSABLE
    FROM pedidos inner join clientes
    ON pedidos.CÓDIGO_CLIENTE = clientes.CÓDIGOCLIENTE
    WHERE clientes.RESPONSABLE like '%ngel M%'
    GROUP BY RESPONSABLE


SELECT *
    FROM pedidos right join clientes
    ON pedidos.CÓDIGO_CLIENTE = clientes.CÓDIGOCLIENTE
    WHERE clientes.POBLACIÓN like 'MADRID'

SELECT count(NÚMERO_DE_PEDIDO) AS TOTAL_PEDIDOS, RESPONSABLE
    FROM pedidos inner join clientes
    ON pedidos.CÓDIGO_CLIENTE = clientes.CÓDIGOCLIENTE
    WHERE clientes.POBLACIÓN like 'MADRID'
    GROUP BY RESPONSABLE

SELECT avg(PRECIO) AS MEDIA_PRECIO, EMPRESA
    FROM productos inner join [productos-pedidos]
    ON productos.CÓDIGOARTÍCULO = [productos-pedidos].CÓDIGO_ARTÍCULO 
    inner join pedidos
    ON  [productos-pedidos].NÚMERO_DE_PEDIDO = pedidos.NÚMERO_DE_PEDIDO 
    inner join clientes
    ON pedidos.CÓDIGO_CLIENTE  = clienteS.CÓDIGOCLIENTE
    WHERE EMPRESA <> 'EXPORTASA'
    GROUP BY EMPRESA

--UNION (MISMO NUMERO DE CAMPOS, MISMO TIPO DE CAMPOS) COGE CAMPO DEL PRIMERO !!!

--NOMBRE EMPRESA Y DIRECCIÓN, RESPONSABLE JUAN GARCIA Y LA SECCIÓN Y NOMBRE PRECIO 43 EUROS

SELECT empresa AS dato_1, dirección AS dato_2 from clientes
    WHERE responsable like 'JUAN GARC%'
UNION
SELECT sección,nombreartículo from productos
    WHERE PRECIO = 43
   

    

SELECT convert(nvarchar(30), getdate(), 103)

-- CONSULTA NOMBREARTICULO, SECCION, PRECIO Y PRECIO 21%

SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO, round(PRECIO+(PRECIO*0.21),2) AS PRECIO_CON_IVA from productos

SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO, convert(money,round(PRECIO+(PRECIO*0.21),2),2) AS PRECIO_CON_IVA from productos

--ACTUALIZAR RESPONSABLE EMPRESA MUÑECA ANDADORA POR DANILO MORALES

UPDATE clientes SET RESPONSABLE = 'DANILO MORALES' 
    FROM clientes inner join pedidos
    ON clientes.CÓDIGOCLIENTE =  pedidos.CÓDIGO_CLIENTE
    inner join  [productos-pedidos]
    ON pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
    inner join productos
    ON [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
    WHERE NOMBREARTÍCULO like 'MUÑECA%'

SELECT * into clientes_madrid from clientes
    WHERE POBLACIÓN = 'MADRID'


--SELECCIONAR EMPRESA Y NUMERO DE PEDIDOS

SELECT count(NÚMERO_DE_PEDIDO) AS PEDIDOS, EMPRESA from pedidos
    INNER JOIN clientes
    ON pedidos.CÓDIGO_CLIENTE = clientes.CÓDIGOCLIENTE
    GROUP BY EMPRESA
    

--CANTIDAD PEDIDOS CERAMICAS DE BELTRAN E HIJOS


SELECT count(pedidos.NÚMERO_DE_PEDIDO) AS NUM_PEDIDOS, SECCIÓN, EMPRESA from pedidos
    
    INNER JOIN clientes
    ON clientes.CÓDIGOCLIENTE= pedidos.CÓDIGO_CLIENTE
    INNER JOIN [productos-pedidos]
    ON pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
    INNER JOIN productos
    ON [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
    
    WHERE EMPRESA LIKE 'BELT%' AND SECCIÓN = 'CERÁMICA' 
    GROUP BY SECCIÓN, EMPRESA


-- PRODUCTOS QUE SEAN SUPERIORES A LA MEDIA NOMBRE SECCIÓN


SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO, EMPRESA from PRODUCTOS
    
    INNER JOIN [productos-pedidos]
    ON [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
    INNER JOIN pedidos
    ON pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
    INNER JOIN clientes
    ON clientes.CÓDIGOCLIENTE= pedidos.CÓDIGO_CLIENTE
     
    WHERE PRECIO > (SELECT avg(productos.precio))


SELECT NOMBREARTÍCULO, SECCIÓN FROM PRODUCTOS
    WHERE PRECIO > (SELECT AVG(PRECIO) FROM PRODUCTOS)

-- CONSULTA QUE NOS DEVUELVA PRECIO SUPERIOR A TODOS LOS ARTÍCULOS DE CERÁMICA

SELECT NOMBREARTÍCULO, SECCIÓN FROM PRODUCTOS
    WHERE PRECIO > (SELECT max(PRECIO) from productos WHERE SECCIÓN = 'CERÁMICA')

SELECT NOMBREARTÍCULO, SECCIÓN FROM PRODUCTOS
    WHERE PRECIO > all (select precio from productos WHERE SECCIÓN = 'CERÁMICA')

SELECT NOMBREARTÍCULO, SECCIÓN FROM PRODUCTOS
    WHERE PRECIO > any (select precio from productos WHERE SECCIÓN = 'CERÁMICA')

SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO FROM PRODUCTOS
    WHERE PRECIO > (select top 1 precio from productos WHERE SECCIÓN = 'CERÁMICA' ORDER BY PRECIO DESC)


-- NOMBRE Y PRECIO PRODUCTOS QUE SE HAN PEDIDO MÁS DE 20 UNIDADES

SELECT NOMBREARTÍCULO, PRECIO FROM productos
    INNER JOIN [productos-pedidos]
    ON productos.CÓDIGOARTÍCULO = [productos-pedidos].CÓDIGO_ARTÍCULO
    where [productos-pedidos].unidades > 20

SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO FROM PRODUCTOS
    WHERE CÓDIGOARTÍCULO in (select CÓDIGO_ARTÍCULO from [productos-pedidos] where unidades > 20) order by PRECIO DESC

-- CLIENTES QUE NO HAN PAGADO CON TARJETA

SELECT POBLACIÓN, EMPRESA FROM clientes
    WHERE CÓDIGOCLIENTE in (select CÓDIGO_CLIENTE from pedidos where FORMA_DE_PAGO <> 'TARJETA')

SELECT POBLACIÓN, EMPRESA FROM clientes
    WHERE CÓDIGOCLIENTE NOT in (select CÓDIGO_CLIENTE from pedidos where FORMA_DE_PAGO = 'TARJETA') 

SeleCT count(número_de_pedido), FORMA_DE_PAGO from pedidos
    where FORMA_DE_PAGO = 'TARJETA'
    group by FORMA_DE_PAGO

SeleCT count(número_de_pedido), FORMA_DE_PAGO from pedidos
    where FORMA_DE_PAGO <> 'TARJETA'
    group by FORMA_DE_PAGO

SeleCT count(número_de_pedido), FORMA_DE_PAGO from pedidos
    group by FORMA_DE_PAGO

-- PRECIO, NOMBRE DEL PRODUCTO QUE MÁS SE HA PEDIDO EN DEPORTES
    
SELECT NOMBREARTÍCULO, PRECIO, SECCIÓN FROM productos--MAL
    where CÓDIGOARTÍCULO in (select CÓDIGO_ARTÍCULO from [productos-pedidos] where SECCIÓN = 'deportes' and [productos-pedidos].unidades = max(unidades))--MAL

SELECT NOMBREARTÍCULO, PRECIO, SECCIÓN FROM productos-- MAL
    INNER JOIN [productos-pedidos]
    ON productos.CÓDIGOARTÍCULO = [productos-pedidos].CÓDIGO_ARTÍCULO
    where unidades = (SELECT max(UNIDADES) FROM [productos-pedidos] where (select CÓDIGOARTÍCULO from productos where SECCIÓN = 'deportes')
    GROUP BY NOMBREARTÍCULO, PRECIO, SECCIÓN, UNIDADES
    HAVING SECCIÓN = 'DEPORTES' --ESTA MAL

--DECLARES

SELECT @@servername

-- DECLARES

DECLARE @PEPE CHAR(10)
DECLARE @MANOLI CHAR(10)

SET @PEPE = 'HOY ES EL DÍA'
SET @MANOLI = CONVERT(varchar(10), getdate(), 105)

print @PEPE+@MANOLI


--CREAR UNA TABLA PRODUCTOS_ESCAÑO DONDE ESTÉN TODOS LOS PRODUCTOS PEDIDOS POR BAZAR LA FARAONA

Select EMPRESA, productos.NOMBREARTÍCULO, UNIDADES, FECHA_DE_PEDIDO into productos_escaño4
    from clientes 
        inner join pedidos
        on clientes.CÓDIGOCLIENTE = pedidos.CÓDIGO_CLIENTE
        inner join [productos-pedidos]
        on pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
        inner join productos
        on [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
    where EMPRESA = 'BAZAR LA FARAONA'


Select productos.* into productos_escaño2 
    from clientes 
        inner join pedidos
        on clientes.CÓDIGOCLIENTE = pedidos.CÓDIGO_CLIENTE
        inner join [productos-pedidos]
        on pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
        inner join productos
        on [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
    where EMPRESA = 'BAZAR LA FARAONA'


-- FUNCIONES ESCALARES
-- Create function nombre (  @NOMBRE tipo  ) returns tipo as begin 

Create function calcular_área(@base int, @altura int) returns int as 
    begin 
    return (@base*@altura)/2 
    end

print dbo.calcular_área(5,6)



Create function pepe5 (@X varchar(20), @Y varchar(20)) returns varchar(50) as
    begin
    return 'hola '+ @X + @Y
    end

declare @n varchar(20)
print dbo.pepe5('florecita', ' de los cojones')
print 'cambio de tema'
set @n = dbo.pepe5('Iván', ' ')
print @n


-- FUNCIONES DE TABLA

Create function articulos_empresa3(@X nvarchar(50), @Y nvarchar(50)) returns table as
    return 
        (Select EMPRESA, productos.NOMBREARTÍCULO, productos.PRECIO, UNIDADES, FECHA_DE_PEDIDO
            from clientes 
                inner join pedidos
                on clientes.CÓDIGOCLIENTE = pedidos.CÓDIGO_CLIENTE
                inner join [productos-pedidos]
                on pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
                inner join productos
                on [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
            where RESPONSABLE = @X AND FECHA_DE_PEDIDO = @Y)



print dbo.articulos_empresa2('ELVIRA GÓMEZ', '2001-05-01')

   
   
Select productos.NOMBREARTÍCULO, productos.PRECIO, FORMA_DE_PAGO, UNIDADES, FECHA_DE_PEDIDO
            from clientes 
                inner join pedidos
                on clientes.CÓDIGOCLIENTE = pedidos.CÓDIGO_CLIENTE
                inner join [productos-pedidos]
                on pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
                inner join productos
                on [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
            where RESPONSABLE = 'ELVIRA GÓMEZ' AND FECHA_DE_PEDIDO = '2001-05-01'




Create function articulos_empresaXXX(@X nvarchar(50)) returns table as
    return 
        (Select productos.NOMBREARTÍCULO
            from clientes 
                inner join pedidos
                on clientes.CÓDIGOCLIENTE = pedidos.CÓDIGO_CLIENTE
                inner join [productos-pedidos]
                on pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
                inner join productos
                on [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
            where EMPRESA = @X)
    
    
Select * from dbo.articulos_empresaXXX('bazar la faraona')




Create function pedido_articuloXX(@X nvarchar(50)) returns table as
    return 
        (Select count([productos-pedidos].NÚMERO_DE_PEDIDO) AS NUMERO_PEDIDOS
            from clientes 
                inner join pedidos
                on clientes.CÓDIGOCLIENTE = pedidos.CÓDIGO_CLIENTE
                inner join [productos-pedidos]
                on pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
                inner join productos
                on [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
            WHERE NOMBREARTÍCULO = @X)    

Select * from dbo.pedido_articuloXX('DESTORNILLADOR')

Select count([productos-pedidos].NÚMERO_DE_PEDIDO) AS NUMERO_PEDIDOS
            from clientes 
                inner join pedidos
                on clientes.CÓDIGOCLIENTE = pedidos.CÓDIGO_CLIENTE
                inner join [productos-pedidos]
                on pedidos.NÚMERO_DE_PEDIDO = [productos-pedidos].NÚMERO_DE_PEDIDO
                inner join productos
                on [productos-pedidos].CÓDIGO_ARTÍCULO = productos.CÓDIGOARTÍCULO
            WHERE NOMBREARTÍCULO = 'DESTORNILLADOR'

Select * from dbo.pedido_articuloXX('BALÓN RUGBY')


Create procedure actualizarX(@X money, @Y nvarchar(50)) as
    update productos
    set PRECIO = @X
    where CÓDIGOARTÍCULO = @Y
            


exec actualizarX 999, 'AR01'



--LOS TRIGGERS ESTÁN ASOCIADOS A UNA TABLA, PUEDEN SALTAR ANTES O DESPUES, PUEDEN SER:

                -- DE INSERT   ANTES (INSTEAD OF) Y DESPUÉS (FOR)
                -- UPDATE        "                     "
                -- DELETE        "                     "

--Create trigger loquesea on tabla 
    --instead of/for insert/update/delete as
       
--Crear una tabla que registre nombre, precio, codigo, usuario, fecha, tipo de delito

Create table Registro2(
    código nvarchar(50) null,
    nombre nvarchar(50) null,
    precio money null,
    usuario nvarchar(50) null,
    fecha datetime null,
    tipo_delito nvarchar(50) null
    check (tipo_delito in ('insertado', 'borrrado', 'actualizado')))
   

Create trigger inserArticulo3 on productos
    for insert as
    declare @cod nvarchar(50)
        select @cod = CÓDIGOARTÍCULO from inserted
    declare @ar nvarchar(50)
        select @ar = NOMBREARTÍCULO from inserted
    declare @pre money
        select @pre = PRECIO from inserted
    insert into Registro2 values
    (@cod, @ar, @pre, SYSTEM_USER, getdate(), 'insertado')


Insert into productos values
('ar285','tci','pelotita de pin pon', 1325, '2025-05-05', 'false', 'Mauritania', null)


Create trigger inserArticulo4 on productos
    for update as
    declare @cod nvarchar(50)
        select @cod = CÓDIGOARTÍCULO from inserted
    declare @ar nvarchar(50)
        select @ar = NOMBREARTÍCULO from inserted
    declare @pre money
        select @pre = PRECIO from inserted
    insert into Registro2 values
    (@cod, @ar, @pre, SYSTEM_USER, getdate(), 'insertado')   
 

Update productos set
    CÓDIGOARTÍCULO = 'ar666', 
    SECCIÓN = 'nuevasección', 
    NOMBREARTÍCULO = 'tridente', 
    PRECIO = 99999, 
    FECHA = '2024-08-08', 
    IMPORTADO = 'false', 
    PAÍSDEORIGEN = 'Mali', 
    FOTO = null
    where CÓDIGOARTÍCULO = 'ar285'
   