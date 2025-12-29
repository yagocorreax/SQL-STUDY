DROP DATABASE IF EXISTS exercicios_sql;
CREATE DATABASE exercicios_sql;
USE exercicios_sql;

CREATE TABLE produtos (
    id_produto INT,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    valor DECIMAL(10,2),
    estoque INT
);

INSERT INTO produtos (id_produto, nome_produto, categoria, valor, estoque) VALUES
    (1, 'notebook', 'eletrônicos', 3500, 10),
    (2, 'mouse gamer', 'periféricos', 450, 20),
    (3, 'teclado meânico', 'periféricos', 850, 30),
    (4, 'Monitor 24pol', 'eletrônicos',  2500, 40),
    (5, 'Cadeira office', 'mobília', 1200, 30);

    -- ex01:
    SELECT * FROM produtos;
    --ex02:
    SELECT nome_produto, valor FROM produtos;
    --ex03:
    SELECT * FROM produtos WHERE categoria = 'periféricos';
    --ex04:
    SELECT * FROM produtos WHERE valor > 1000;
    -- ex05:
    SELECT * FROM produtos ORDER BY valor ASC;
    --ex06:
    INSERT INTO produtos(id_produto, nome_produto, categoria, valor, estoque)
    VALUES (6, 'headset', 'periféricos', 250, 56)
    --ex07:
    UPDATE produtos SET estoque = 8 WHERE id_produto = 1;
    --ex08: 
    UPDATE produtos SET valor = 2250 WHERE id_produto = 4;
    --ex09:
    DELETE FROM produtos WHERE id_produto = 2; 
    --ex10:
    TRUNCATE TABLE produtos;