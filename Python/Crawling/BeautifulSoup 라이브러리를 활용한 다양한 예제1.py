from bs4 import BeautifulSoup

html = """<html> 
            <body> 
                <h1 id='title'>[1]크롤링이란?</h1> 
                <p class='cssstyle'>웹페이지에서 필요한 데이터를 추출하는 것</p> 
                <p id='body' align='center'>파이썬을 중심으로 다양한 웹크롤링 기술 발달</p> 
            </body> 
        </html>"""

separate = '-' * 50

soup = BeautifulSoup(html, "html.parser")

# 태그로 검색하는 방법
# find() -> 가장 먼저 검색되는 태그 반환
title_data = soup.find('h1')

print(title_data)
print(title_data.string) # NavigableString
print(title_data.get_text()) # String
print(separate)

# 가장 먼저 검색되는 태그를 반환
paragraph_data = soup.find('p')
print(paragraph_data)
print(paragraph_data.string)
print(type(paragraph_data.string))
print(paragraph_data.get_text())
print(type(paragraph_data.get_text()))
print(separate)

# 태그에 있는 id로 검색
print("태그에 있는 id로 검색")
title_data = soup.find(id='title')
print(title_data)
print(title_data.string)
print(title_data.get_text())
print(separate)

# HTML 태그와 CSS class를 활용해서 필요한 데이터를 추출하는 방법1
print("HTML 태그와 CSS class를 활용해서 필요한 데이터를 추출하는 방법1")
paragraph_data = soup.find('p', class_='cssstyle')
print(paragraph_data)
print(paragraph_data.string)
print(paragraph_data.get_text())
print(separate)

# HTML 태그와 css class를 활용해서 필요한 데이터를 추출하는 방법2
print("HTML 태그와 css class를 활용해서 필요한 데이터를 추출하는 방법2")
paragraph_data = soup.find('p', 'cssstyle')
print(paragraph_data)
print(paragraph_data.string)
print(paragraph_data.get_text())
print(separate)

# HTML 태그와 태그에 있는 속성:속성값을 활용해서 필요한 데이터를 추출하는 방법
print("HTML 태그와 태그에 있는 속성:속성값을 활용해서 필요한 데이터를 추출하는 방법")
paragraph_data = soup.find('p', attrs = {'align':'center'})
print(paragraph_data)
print(paragraph_data.string)
print(paragraph_data.get_text())
print(separate)

# find_all() : 관련된 모든 데이터를 리스트 형태로 추출하는 함수
print("find_all() : 관련된 모든 데이터를 리스트 형태로 추출하는 함수")
paragraph_data = soup.find_all('p') # p태그와 관련된 모든 데이터를 찾아라
print(paragraph_data)
print(f'paragraph_data[0] = {paragraph_data[0]}')
print(f'paragraph_data[1] = {paragraph_data[1]}')
print(separate)
