from django.shortcuts import render, HttpResponse


topics = [
    {'id': 1, 'title': 'Routing', 'body': 'Routing is ...'}, 
    {'id': 2, 'title': 'View', 'body': 'View is ...'}, 
    {'id': 3, 'title': 'Model', 'body': 'Model is ...'}
]


def htmlTemplate(article):
    global topics
    ol = ''
    for i in topics:
        ol += f'<li><a href="/read/{i["id"]}">{i["title"]}</a></li>'
    html_str = f'''
        <html>
        <body>
            <h1><a href='/'>Django</a></h1>
            <ul>
                {ol}
            </ul>
            {article}
        </body>
        </html>
    '''
    return html_str


# Create your views here.
def index(request):
    article = '''
        <h2>Welcome</h2>
        Hello, Django
    '''
    return HttpResponse(htmlTemplate(article))


def read(request, id):
    global topics
    article = [f'<h2>{i["title"]}</h2>{i["body"]}' for i in topics if i["id"] == int(id)]
    result = ''.join(article)
    return HttpResponse(htmlTemplate(result))


def create(request):
    return HttpResponse('Create')