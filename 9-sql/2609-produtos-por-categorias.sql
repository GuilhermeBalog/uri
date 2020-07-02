/* https://www.urionlinejudge.com.br/judge/pt/problems/view/2609 */

SELECT categories.name, sum(amount) AS sum 
FROM products 
JOIN categories 
ON products.id_categories = categories.id 
GROUP BY categories.name
