from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>test page</title>
        </head>
        <body class="mybody" id="js-body">
            <p class="text odd">first <b>bold</b> paragraph</p>
            <p class="text even">second <a href="https://mail.ru">link</a></p>
            <p class="list odd">third <a id="paragraph"<b>bold link</b></a></p>    
        </body>
    </html>
    """
if __name__ == '__main__':
    soup = BeautifulSoup(html, 'lxml')
    # Finding parent
    print(soup.p.b.find_parent("body")['id'])
    # Find next neighbour
    print(soup.p.find_next_sibling(class_="odd"))
    print(soup.p.find_next_siblings())

    # Search
    print(soup.p.find('b'))
    print(soup.find(id='js-body')['class'])
    print(soup.find('b', text='bold'))
    print(soup.find_all('p'))
    print(soup.find_all('p', 'text odd'))

    # Select CSS Selectors
    print(soup.select('p.text.odd'))
    print(soup.select('p:nth-of-type(3)'))

    # Find all tags
    print([i for i in soup(['a', 'b'])])

    # Changing tags
    tag = soup.b
    print(tag)
    tag.name = 'i'
    tag['id'] = 'myid'
    tag.string = 'italic'
    print(soup.prettify())
