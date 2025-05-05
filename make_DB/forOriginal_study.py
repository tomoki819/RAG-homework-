import requests
from bs4 import BeautifulSoup

# 論文のURL
url = "https://www.nature.com/articles/s42005-025-02059-4"
headers = {"User-Agent": "Mozilla/5.0"}

# Webページの取得
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# タイトルの抽出
title = soup.find("h1").text.strip()

# 著者情報までの主要セクションを抽出
sections_to_get = [
    "Abstract", "Introduction", "Results", "Discussion", "Methods",
    "Data availability", "Code availability", "References",
    "Acknowledgements", "Author information"
]

text_data = f"Title: {title}\n\n"

# 各セクションの見出しと内容を抽出
for section in sections_to_get:
    section_tag = soup.find("h2", string=section)
    if section_tag:
        content = []
        for sibling in section_tag.find_next_siblings():
            if sibling.name == "h2":
                break
            content.append(sibling.text)
        text_data += f"\n\n## {section}\n" + "\n".join(content)

print(text_data)
