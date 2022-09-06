from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt


nextId = 4
topics = [
    {'id': 1, 'title': 'Routing', 'body': 'Routing is ...'}, 
    {'id': 2, 'title': 'View', 'body': 'View is ...'}, 
    {'id': 3, 'title': 'Model', 'body': 'Model is ...'}
]


def htmlTemplate(article, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="POST">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li>
                <a href="/update/{id}">update</a>
            </li>
        '''
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
            <ul>
                <li><a href='/create/'>create</a></li>
                {contextUI}
            </ul>
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
    return HttpResponse(htmlTemplate(result, id))


@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(htmlTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        print(title)
        body = request.POST['body']
        print(body)
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId += 1
        return redirect(url)
    else:
        pass


@csrf_exempt
def update(request, id):
    global topics
    if request.method == "GET":
        for i in topics:
            if i['id'] == int(id):
                selectedTopic = {
                    "title": i["title"], 
                    "body": i["body"]
                }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic["body"]}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(htmlTemplate(article, id))
    elif request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        for i in topics:
            if i["id"] == int(id):
                i["title"] = title
                i["body"] = body
        return redirect(f'/read/{id}')


@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST['id']
        newTopics = []
        for i in topics:
            if i["id"] != int(id):
                newTopics.append(i)
        topics = newTopics
        return redirect("/")