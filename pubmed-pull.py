from pymed import PubMed

pubmed = PubMed(tool="MyTool", email="your email")

query = "TSLP"

results = pubmed.query(query, max_results=1000)

for article in results:

print(type(article))
print(article.toJSON())
