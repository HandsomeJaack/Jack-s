# Разработайте своё первое веб-приложение с помощью Django 1.10 - Часть 0

![Django 1.10 - Часть 0](http://blog.adnansiddiqi.me/wp-content/uploads/2017/03/Screen-Shot-2017-03-11-at-11.36.10-PM-1024x499.png)

   Django - очень популярная и мощная платформа для создания от малых до крупных web-приложений на языке Python. В этой серии статей я собираюсь сделать простой трекер для отслеживания багов (Bug Tracking System) с помощью  Django 1.10.

## OhBugz
   Приложение, которое я собираюсь сделать, назовем OhBugz("Опа, баги"). Это простое приложени, которое помогает отслеживать проблемы (баги), свзанные с проектом. Это приложение не заставит ребят из [JIRA](https://ru.wikipedia.org/wiki/Jira) нервно курить в сторонке, но достаточно хорошо, чтобы научиться делать web-приложения с помощь Django. Вот некоторые скрины:

![OhBugz-1](http://blog.adnansiddiqi.me/wp-content/uploads/2017/03/Screen-Shot-2017-03-12-at-12.01.34-AM.png)
![OhBugz-2](http://blog.adnansiddiqi.me/wp-content/uploads/2017/03/Welcome-to-Oh-Bugz-Issue-List.png)
![OhBugz-3](http://blog.adnansiddiqi.me/wp-content/uploads/2017/03/Welcome-to-Oh-Bugz-Add-Issue.png)

## Установка
   С тех пор, как Django стал частью Python (т.е. с момента создания Django), вполне очевидно, что для дальнейшей работы у вас должен быть установлен Python. Жизнь становится еще легче, если вы знаете язык Python. В данном туториале я использую версию Python 3.5.

Подразумевается, что Python и _pip_ уже установлены, введем в терминал (консоль) следующую команду:

<pip install django>
 
 Если все прошло успешно, то на экране должно появиться примерно что-то следующее: 
 ![Installation-1](http://blog.adnansiddiqi.me/wp-content/uploads/2017/03/Screen-Shot-2017-03-12-at-12.32.21-AM.png)
 В моём случае это что-то говорит, что установлена версия __Django 1.10.5__.
 
 ## Создание проекта
 Предварительные приготовления завершены, самое время перейти к созданию проекта.
  
  '''django-admin startproject ohbugztracker'''
  
  _django-admin_ - утилита, загруженная вместе с Django, выше она создает проект с именем ohbugztracker(опабагитрекер).
  
  '''./manage.py runserver'''
  
  Команда выше запускает сервер приложения Django. В ходе запуска вы увидите текст в консоли такой же, что и приведенный ниже. Не волнуйтесь насчет миграций, об этом будет подребонее в следующих статьях. 
  
 <cd ohbugztracker/
./manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

March 11, 2017 - 19:57:01
Django version 1.10.5, using settings 'ohbugztracker.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.>

Сообщщение, на котором вы должны остановить внимание __Starting development server at http://127.0.0.1:8000/__. Откройте браузер и введите ссылку на локальный хост, приведенную выше и вы должны увидеть следующую картинку:

![Success!](http://blog.adnansiddiqi.me/wp-content/uploads/2017/03/Screen-Shot-2017-03-12-at-1.03.50-AM.png)

Юхууу! Мы создали наш первый проект Django. Но это не значит, что это уже конечный проект. Когда я сказал, что проект создан, имелось ввиду,что команды сработали успешно и сервер приложения Django создан и работает. В следующей статье мы разберем разницу между проектом и приложением и что это означет в мире Django.  А пока наслаждайтесь текущими достиженисями :)

#### Перевод: Handsome Jack (Дмитрий Бутаков)
#### Оригинал: [http://blog.adnansiddiqi.me/develop-your-first-web-application-in-django-1-10-part-0/]



