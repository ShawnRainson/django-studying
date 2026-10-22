base.html:

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Мой блог{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Мой блог</h1>
        {% include "blog/includes/greeting.html" with username="Алексей" %}
        {% include "blog/includes/navigation.html" %}
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>Мой учебный проект на Django</p>
    </footer>
</body>
</html>

home.html:

{% extends "blog/base.html" %}

{% block title %}Главная — Мой блог{% endblock %}

{% block content %}
    <h2>{{ title|title }}</h2>
    <p>{{ message }}</p>

    <h3>Мои статьи</h3>

    {% for post in posts %}
        <article>
            <h4>{{ post }}</h4>
        </article>
    {% empty %}
        <p>Пока статей нет.</p>
    {% endfor %}
{% endblock %}

about.html:

{% extends "blog/base.html" %}

{% block title %}О блоге — Мой блог{% endblock %}

{% block content %}
    <h2>О моём блоге</h2>
    <p>Здесь я изучаю Django и создаю свой первый сайт.</p>
{% endblock %}

navigation.html:
<nav>
    <a href="/">Главная</a>
    <a href="/about/">О блоге</a>
</nav>

greeting.html:
<p>Добро пожаловать, {{ username }}!</p>

🔥 Финальный вызов сенсея
Ответь своими словами:
1 Какую проблему решает наследование шаблонов? - проблему дублирования html
2 Для чего нужны {% extends %} и {% block %}? - включение элементов из шаблона
3 Чем {% include %} отличается от {% extends %}? - первый ключает какой-то конкретный небольшой шаблон, а второй включает весь бащовый шаблон
4 Что произойдёт, если дочерний шаблон не переопределит блок sidebar? - Появится значение по умолчанию
5 Почему лучше хранить меню в отдельном файле, если оно используется на нескольких страницах? - потому-что могут появится страницы, на которых это меню не нужно