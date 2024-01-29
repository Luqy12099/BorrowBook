### Changelog `Todolist`
<b>Full Changelog</b>

---
#### v 0.0.3 -- 2024/01/29











---
#### v 0.0.2 -- 2024/01/29
###### New:
* Make django app (managementUser)
* Make "model user" to accessed by admin (register/admin) 
* Add managementUser\form.py class "form_edit_user"

* API (views)
    * managementUser/user_read
    * managementUser/user_update
    * managementUser/user_delete
* urls
    * user/
    * user/<int:id>/
* Templates 
    * managementUser/user_read
    * managementUser/user_update

###### Change:
* Lainnya :
    * settings.py 
        * Add INSTALLED_APPS ['managementUser.apps.ManagementuserConfig', ]
    * library\urls.py
        * Add path('user/', include("managementUser.urls")),
    * register\base.html
        * Add lokasi sidebar User (only for superadmin)

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
    * library\urls.py
        * Add path('', include('django.contrib.auth.urls')),
        * Add path('', include("register.urls")),

---
