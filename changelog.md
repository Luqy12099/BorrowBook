### Changelog `Todolist`
<b>Full Changelog</b>

---
#### v 0.0.8-- 2024/01/25
###### Change:
* API (views)
    * todolist_app/todolist_update
        * Change argument to response.POST.get('is_checked') != 'True'
        * Add return value

* Templates 
    * todolist_app/todolist_edit.html
        * Add in style header
        * Change style button add item

        * Change checked item to synchronous
        * Delete script tag that related to checked and reodering
        * Change form (item_delete), to its button (before in input group)
        * Change style in input group item (make button is aligned with below button)

---
#### v 0.0.7-- 2024/01/24
###### New:
* API (views)
    * todolist_app/item_delete

* urls
    * item/delete/<int:item_id>/

###### Change:
* API (views)
    * todolist_app/todolist_update
        * Add new logic if new_name != None: 

* Templates
    * todolist_app/todolist_edit.html
        * Add button in each item
        * Add <form></form> before first iterate
        

---
#### v 0.0.6 -- 2024/01/24
###### Change:
* API (views)
    * todolist_app/item_update
        * Add new parameter ('item.text')
        * Change parameter ('is_checked')

* Templates
    * todolist_app/todolist_edit.html
        * Add script to handle editebale item text
        * Change form(id="updateForm with div class="{% if item.complete %}completed-item{% endif %}"), so item is editable
        * Change script to handle editebale todo name
        * Delete form and add div class="todo-name" in header 

---
#### v 0.0.5 -- 2024/01/22
###### New:

###### Change:
* Templates 
    * todolist_app/todolist_edit.html
        * Add script to handle line through, so everytime item checked, it will have line through
        * Add script to handle reordering, so everytime item checked, it will be on the bottom of the list
        * Add style
        * Change form(id="updateForm") to have 2 iterate for (one for complete)

---
#### v 0.0.4 -- 2024/01/21
###### New:
* API (views)
    * todolist_app/item_create
    * todolist_app/item_update

* urls
    * item/create
    * item/update

###### Change:
* Templates 
    * todolist_app/todolist_edit.html
        * Add 2 column in class="container-fluid" (for add item and read item)
        * Add script to handle async checkbox for "completed" item

---
#### v 0.0.3 -- 2024/01/20
###### New:
* Make django app (todolist_app)
* Add Db (models) todolist_app (ToDoList and item) (done makemigrations and migrate)
* Add todolist\todolist_app\form.py class "form_create"

* API (views)
    * todolist_app/todolist_create
    * todolist_app/todolist_read
    * todolist_app/todolist_delete
    * todolist_app/todolist_update

* urls
    * todolist/create
    * todolist/
    * todolist/delete/<int:todo_id>/

* Templates 
    * todolist_app/todolist_create
    * todolist_app/todolist_read
    * todolist_app/todolist_edit.html


###### Change:
* API (views)
    * register/register
        * Change HttpResponseRedirect('/login')
    
* Lainnya :
    * settings.py 
        * Add INSTALLED_APPS ['todolist_app.apps.TodolistAppConfig', ]
    * first_django\urls.py
        * Add path('todolist/', include("todolist_app.urls")),
    * register\base.html
        * Add lokasi sidebar ToDo

---
#### v 0.0.2 -- 2024/01/20
###### New:

    

---

#### v 0.0.1 -- 2024/01/28
###### New:
* Pip install in readme.md
* Make initial file {changelog, pip_req}
* Make django project
* Make django app (register)
* Add register\form.py

* API (views)
    * register/base
    * register/register
    * register/logout_view

* Templates ()
    * register/base
    * register/register
    * registration/login
    * register/base_wo_sidebar

* urls
    * /
    * register/register
    * register/logout_view

###### Change:
* Lainnya :
    * settings.py 
        * Add INSTALLED_APPS ['register.apps.RegisterConfig', "crispy_forms", "crispy_bootstrap4",]
        * Add CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
        * Add CRISPY_TEMPLATE_PACK = "bootstrap4"
        * Add LOGIN_REDIRECT_URL = '/'
        * Add LOGIN_URL = '/login/'
        * Add LOGOUT_REDIRECT_URL = '/login/'
    * first_django\urls.py
        * Add path('', include('django.contrib.auth.urls')),
        * Add path('', include("register.urls")),

---
