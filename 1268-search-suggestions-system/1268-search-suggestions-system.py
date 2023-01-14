class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i, c in enumerate(searchWord):
            products = [p for p in products if len(p) > i and p[i] == c]
            res.append(products[:3])
        
        return res