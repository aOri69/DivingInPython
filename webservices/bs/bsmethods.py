from bs4 import BeautifulSoup

if __name__ == '__main__':
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
    soup = BeautifulSoup(html, 'lxml')
    print(type(soup.p['class']), soup.p['class'])
    print(type(soup.body['id']), soup.body['id'])
    print(type(soup.p.b.parent), soup.p.b.parent)
    print(type(soup.p.b.parents), soup.p.b.parents)
    print([tag.name for tag in soup.p.b.parents])  # Generator
    print(soup.p.contents)  # List
    print(list(soup.p.children))  # Generator
