# Beautiful Soup Documentation:- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests

# with open("Day 45/bs4-start/website.html",'r') as file:
#     contents=file.read()


# soup=BeautifulSoup(contents,'html.parser')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# #print(soup.h1.string)

# # print(soup.prettify())
# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))


# heading_tag=soup.find(name="h1",id="name")
# print(heading_tag)

# section_heading=soup.find(name="h3",class_="heading")
# print(section_heading.get("class"))
# print(section_heading)

# company_url=soup.select_one(selector="p a")
# print(company_url)

#Scraping a live website


response=requests.get("https://news.ycombinator.com/news")
yc_webpage=response.text

soup=BeautifulSoup(yc_webpage,'html.parser')
print(soup.title)

article_tag=[tag.find(name="a") for tag in soup.find_all(name="span",class_="titleline")]
article_text=[i.getText() for i in article_tag]
article_link=[i.get("href") for i in article_tag]
article_upvote=[int(i.getText().split()[0]) for i in soup.find_all(name="span",class_="score")]
max_vote_index = article_upvote.index(max(article_upvote))


# print(article_text)
# print(article_link)
# print(article_upvote)
print("article text: ",article_text[max_vote_index],
      "\nArticle link: ",article_link[max_vote_index],
      "\nUpvotes: ",article_upvote[max_vote_index])