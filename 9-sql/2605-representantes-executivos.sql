/* https://www.urionlinejudge.com.br/judge/pt/problems/view/2605 */

SELECT products.name, providers.name 
FROM products 
JOIN providers
ON id_providers = providers.id
WHERE id_categories = 6;
