from bottle import route, run, template, request
import psycopg2 as pgsql
import datetime

def db_connect():
    conn = pgsql.connect(dbname="ah7515_ah7370", user="ah7515", password="82vaz32k", host="pgserver.mah.se")
    return conn.cursor()

def commit_changes():
    conn = pgsql.connect(dbname="ah7515_ah7370", user="ah7515", password="82vaz32k", host="pgserver.mah.se")
    conn.commit()

def get_article():
    cursor = db_connect()
    cursor.execute("begin")
    cursor.execute("select aid, title, content, published from article")
    article = cursor.fetchall()
    cursor.execute("select name from author where AuthorID = '{}'".format(article[0]))
    author = cursor.fetchall()


@route('/')
def index():
    cursor = db_connect()
    cursor.execute("select title, published from article")
    result = cursor.fetchall()
    #cursor.close()
    print(result)
    return template('index', result=result)

@route('/admin/add-author')
def add_author():
    return template('index')

@route('/admin/add-article')
def add_article():
    return template('add_article')

@route('/create-article', method="POST")
def create():
    cursor = db_connect()
    #image = request.forms.get('image')

    data = {
        "title" : request.forms.get('title'),
        "content" : request.forms.get('content'),
        "published" : datetime.datetime.now().strftime("%Y-%m-%d"),
        "author" : request.forms.get('author')
    }

    cursor.execute("begin")
    cursor.execute("insert into Article (title, content, published) values ('{}', '{}', '{}') returning aID".format(data['title'], data['content'], data['published']))
    newRow_ID = cursor.fetchone()[0]
    cursor.execute("insert into WrittenBy (AuthorID, ArticleID) values ('{}', '{}')".format(data['author'], newRow_ID))
    cursor.execute("commit")
    commit_changes()
    cursor.close()

run(host='127.0.0.1', port='8080')




