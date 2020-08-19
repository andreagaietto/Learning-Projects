from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
#select returns a list
"""soup = BeautifulSoup(html, "html.parser")
d = soup.select("[data-example]")
print(d)
print(soup.body)
print(soup.body.div)
print(soup.find("div"))
d  = soup.find_all("div")
print(d)


#finding via id:
d = soup.find(id="first")
print(d)
#d = soup.select("#first") this is slightly better

#on a class; use find_all

#d = soup.find_all(class_  ="first")
d = soup.select(".special")


#search based on data attribute (in this case the data-example set to yes)

d = soup.find_all(attrs={"data-example": "yes"})
d = soup.select("[data-example]")
"""