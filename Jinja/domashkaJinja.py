from jinja2 import Template

links = [
    {"url": "/index", "title": "Главная"},
    {"url": "/news", "title": "Новости"},
    {"url": "/about", "title": "О компании"},
    {"url": "/shop", "title": "Магазин"},
    {"url": "/contacts", "title": "Контакты"}
]

html = """
<ul>
    {% for el in l %}
        {% if el['title'] == 'Главная' %}
        <li><a class='active' href='{{ el.url }}'>{{el['title']}}</a></li>
        {% else %}
        <li><a href='{{ el.url }}'>{{el['title']}}</a></li>
        {% endif %}
    {% endfor %}
</ul>
"""

tm = Template(html)
message = tm.render(l=links)
print(message)

attrs = [
    {"type": "text", "name": "firstname", "placeholder": "Имя"},
    {"type": "text", "name": "lastname", "placeholder": "Фамилия"},
    {"type": "text", "name": "address", "placeholder": "Адрес"},
    {"type": "tel", "name": "phone", "placeholder": "Телефон"},
    {"type": "email", "name": "email", "placeholder": "Почта"}
]

html1 = """
{% macro create_input(t,n,p) %}
<input type='{{t}}' name='{{n}}' placeholder='{{p}}'>
{% endmacro %}
    {% for el in a %}
<p>{{create_input(el.type, el.name, el.placeholder)}}</p>
    {% endfor %}

"""
tm1 = Template(html1)
message1 = tm1.render(a=attrs)
print(message1)
