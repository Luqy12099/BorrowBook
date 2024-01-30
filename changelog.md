### Changelog `Todolist`
<b>Full Changelog</b>

---
#### v 0.0.3 -- 2024/01/30
###### New:
* Make django app (location)
* Add model (location/library_location)
* Add model (location/library_location) to admin
* Add location\form.py class "form_create_loc", "form_edit_loc"

* Add model (managementUser/admin_library)
* Add model (managementUser/admin_library) to admin
* Add managementUser\form.py class "AdminLibraryForm"

* API (views)
    * location/location_create
    * location/location_read
    * location/location_update
    * location/location_delete
* urls
    * location/create/
    * location/
    * location/<int:id>/
    * location/<int:id>/delete/
* Templates 
    * location/location_create
    * location/location_read
    * location/location_update

###### Change:
* API (views):
    * managementUser/user_update
        * Delete admin_library if role change from 'admin' to another
        * Add form2 if dropdown seleceted role is 'admin'
* Templates 
    * register\base.html
        * Add lokasi sidebar Location
    * managementUser/user_update
        * Add form2
        * Add async form2 
            * When dropdown role is 'admin', form2 will appear

* Lainnya :
    * settings.py 
        * Add INSTALLED_APPS ['location.apps.LocationConfig', ]
    * library\urls.py
        * Add path('location/', include("location.urls")),
    

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
* Add model (register/user)
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
