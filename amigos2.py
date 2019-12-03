from instapy_cli import client

username = 'amigoosdemadrid'
password = '20million'
image = '1.png'
text = ''

with client(username, password) as cli:
    cli.upload(image, text)

