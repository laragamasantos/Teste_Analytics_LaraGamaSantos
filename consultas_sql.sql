SELECT Product, Category, ROUND(SUM(Amount*Price),2) AS TotalSales FROM sales
    GROUP BY Product
    ORDER BY TotalSales DESC;

/*
Soma o total das vendas para cada produto (Group By une as ocorrências de mesmo produto em uma só).
Em seguida, ordena em ordem decrescente de acordo com o valor calculado.
*/

SELECT Product, Category, SUM(Amount) AS AmountOfSales, MONTH(Date) AS Month FROM sales
    WHERE Month = '06'
    GROUP BY Product
    ORDER BY AmountOfSales DESC;

/*
Soma o total das quantidades vendidas para cada produto (Group By une as ocorrências de mesmo produto em uma só).
Seleciona apenas o mês de dentro da data e exibe em uma coluna (Fiz isso apenas para facilitar a verificação).
Filtra somente aqueles produtos cujo mês de venda é junho
Em seguida, ordena em ordem decrescente de acordo com o valor calculado.
*/