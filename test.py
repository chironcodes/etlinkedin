# _author_ = ["Diego Alves", "Adilton Costa Anna"]
# _license_ = "Beerware"
# _version_ = "0.0.1"
from tabulate import tabulate

table = [["Quimico","Azure"],["Biologo","AWS"]]

with open('results.html', 'w') as f:
    f.write("<html><body>")
    f.write(tabulate(table, headers=["Nome coluna A","Nome coluna B"],tablefmt="html"))
    f.write("</body></html>")
