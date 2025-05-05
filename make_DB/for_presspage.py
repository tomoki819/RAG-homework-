import requests
from bs4 import BeautifulSoup

# URL指定とHTML取得
url = 'https://www.riken.jp/press/2025/20250417_1/index.html'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

# タイトル・サブタイトル
title = soup.select_one('h1.hdg01')
subtitle = soup.select_one('p.hdg02')

# 発表日と発表機関
pub_info = soup.select_one('div.pubData')
date = pub_info.select_one('span').text.strip() if pub_info else ''
institute = pub_info.find_all('p')[1].text.strip() if pub_info else ''

# 概要
summary = soup.select_one('p#summary')
summary_text = summary.text.strip() if summary else ''

# 各セクションヘッダに対応するテキストを辞書に格納
sections = ['背景', '研究手法と成果', '今後の期待', '補足説明', '研究支援', '原論文情報', '発表者']
data = {}
for header in sections:
    tag = soup.find('h2', string=header)
    content = []
    if tag:
        for sibling in tag.find_next_siblings():
            if sibling.name == 'h2':
                break
            content.append(sibling.get_text(strip=True))
    data[header] = '\n'.join(content)

# すべてを1つの文字列にまとめる
press_release_text = f"""【タイトル】 {title.text.strip() if title else ''}
【サブタイトル】 {subtitle.text.strip() if subtitle else ''}
【発表日】 {date}
【発表機関】 {institute}
【概要】
{summary_text}
"""

for section, content in data.items():
    press_release_text += f"\n【{section}】\n{content}\n"

# 表示確認
print(press_release_text) 

