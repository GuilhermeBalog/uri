/* https://www.urionlinejudge.com.br/judge/pt/problems/view/2606 */

SELECT products.id, products.name
FROM products
JOIN categories
ON id_categories = categories.id
WHERE categories.name LIKE 'super%';
