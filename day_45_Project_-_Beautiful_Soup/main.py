from bs4 import BeautifulSoup
# import lxml


with open("website.html") as file:
    contents = file.read()
    

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml")    
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)  # prints only the first p

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find_all(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

headingClass = soup.select(".heading")
print(headingClass)