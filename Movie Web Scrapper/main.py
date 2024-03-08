from bs4 import BeautifulSoup
import  requests

response = requests.get(url= "https://www.empireonline.com/movies/features/best-movies-2/")

empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, 'html.parser')

titles = soup.find_all(class_="listicleItem_listicle-item__title__hW_Kn")
print(titles)

movie_titles = [title.getText() for title in titles]

print(movie_titles)

with open('movies.txt','w',encoding='UTF-8') as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")


#
# articles = soup.find_all(class_ = 'titleline')
# article_texts = []
# article_links = []
#
# for article_tag in articles:
#     article_text = article_tag.text
#     article_texts.append(article_text)
#
#     article_link = article_tag.find('a')['href']
#     article_links.append(article_link)
#
# print(article_texts)
# print(article_links)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_='score')]
# print(article_upvotes)
#
# biggest_index = article_upvotes.index(max(article_upvotes))
# print(article_texts[biggest_index])
# print(article_links[biggest_index])
#
#

# with open("index.html",encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents,'html.parser')
#
#
# heading = soup.find('div',class_="top_container").find('h1')
# print(heading)
#
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
#
# clases = soup.select(".top_container")
# print(clases)