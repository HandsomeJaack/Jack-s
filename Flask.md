## Серевер на Flask

Минимальное приложение на Flask начинается следующим образом:
```python
from flask import Flask     # импорт класса Flaskдля созданияинтерфейса и связи между пользователем и сервером
app = Flask(__name__)       # декларация элементов класса, к которым будет производиться обращения (переменные, статические файлы)

@app.route('/')             # route() говорит по какой ссылке обращться к файлам
def hello_world():          # именованая функция говорит браузеру, что вернуть по ссылке описанной выше
  return 'Hello, World!'
```
Чтобы запустить приложение в терминале необходимо прописать превую строку, если все прошло успешно, то должно вывестись следующее:
```bash
$ export FLASK_APP=hello.py
$ flask run
* Running on http://127.0.0.1:5000/
```
Чтобы просмотреть содержимое приложения необходимо перейти по ссылке в браузере __http://127.0.0.1:5000/__ . 
На данный момент на сервер можем зайти только мы, чтобы сделать его доступным для других, необходимо ввести следующее: 
```bash
flask run --host=0.0.0.0
```
Каждый раз при изменении кода сервер приходится перезапускать, Flask позволяет не делать этого, и работать в режиме прямой отладки без отключения сервера.
Для этого нужно экспортировать модуль FLASK_DEBUG:
```bash
$ export FLASK_DEBUG=1
$ flask run
```
Чтобы сделать видимую ссылку, следует прописать имя в route():
```python
@app.route('/')
def index():
return 'Index Page'

@app.route('/hello')
def hello():
return 'Hello, World'
```
Для создания динамических ссылок , можно использовать следующие типизаторы:
* _string_ - принимает любой текст без знака '\'
* _int_ - принимает целые числа
* _float_ - принимает точки с плавающей запятой
* _path_ - как дефолтное, но принимает знак '\'
* _uuid_ - принимает UUID строки
Пример:
```python 
@app.route('/user/<username>')
def show_user_profile(username):
  # show the user profile for that user
  return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  # show the post with the given id, the id is an integer
  return 'Post %d' % post_id
```
Для самостоятельной генерации ссылок используется функция ulr_for(), в качестве первого ургумента - назваение, последующие - ключевые переменные.
Пример:
```python
>>> from flask import Flask, url_for
>>> app = Flask(__name__)
>>> @app.route('/')
... def index(): pass
...
>>> @app.route('/login')
... def login(): pass
...
>>> @app.route('/user/<username>')
... def profile(username): pass
...
>>> with app.test_request_context():
... print url_for('index')
... print url_for('login')
... print url_for('login', next='/')
... print url_for('profile', username='John Doe')
...
/
/login
/login?next=/
/user/John%20Doe
```
### HTTP методы
По умолчанию ссылка отвечает только на зарос GET, но это может быть изменено с помощью передачи дополнительных параметров в route():
```python
from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
do_the_login()
else:
show_the_login_form()
```
Следующие методы HTTP позволяют понять серверу, чего ждет пользователь:
* __GET__ <-- Браузер говорит серверу , что хочет получить информацию хранящаюся на сервере
* __HEAD__ <-- Браузер запрашивает информацию не со всей страниц, а от отдельных заголовков
* __POST__ <-- Браузер говорит, что хочет разместить новую информацию на сервере
* __PUT__ <-- Аналогично предыдущему, но не позволяет обновлять переменные на сервере не однократно (идеально для обработки входных сигналов)
* __DELETE__ <-- Удаляет информацию в заданной локации
* __ OPTIONS__ <-- Обеспечивает быстрый путь пользователю, для просмотра использующихся методов

_*Примечание*_ : версии HTML4 b и ниже могут воспринимать только методы __GET__ и __POST__, в версиях выше остальные методы работают успешно.

### Статические файлы
Предназначены для хранения файлов CSS и JavaScript. Рядом с файлом Flask необходимо создать папку с названием _static_ , а в ней создать необходимые файлы:
```python
url_for('static', filename='style.css')
```

### Шаблоны визуализации
Чтобы менят интерфейс страницы можно использовать метод render_template(). Все, что необходимо, это передать имя шаблона и 
переменные, которые хотим передать в шаблонный движок. Пример
```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)
```
Flask будет искать шаблоны в соседней папке templates, именно туда и нужно разместить шаблоны.
Пример шаблона:
```html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
<h1>Hello {{ name }}!</h1>
{% else %}
<h1>Hello, World!</h1>
{% endif %}
```

###Доступ к запрашиваемым данным




















