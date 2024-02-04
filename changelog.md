### Changelog `Todolist`
<b>Full Changelog</b>

---
#### v 0.0.6 -- 2024/02/04
###### New:

###### Change:
* API (views):
    * book/book_create
        * Add argument user from object response.user
        * Only admin library from book.library_location can add (Prevent unauthorization library admins)
    * book/book_update
        * Add argument user from object response.user
        * Only admin library from book.library_location can edit

* Templates 
    * book/book_read
        * Add library location and stock in detail
    * book/author_read
        * Change login in Author Name

* Lainnya :
    * book\model\book
        * Add field library_location (foreignkey)
        * Add field stock
    * book\form\form_create_book
        * Add field stock
        * Add field library_location (foreignkey)
            * Admin library can add book into another library location
    * book\form\form_edit_book
        * Add field stock
        * Add field library_location (foreignkey)
            * Admin library can change library location into another
    * book\model\author
        * Add null=True in field middle_name
        * Change return to full name

---
#### v 0.0.5 -- 2024/02/02
###### New:
* Add model (book/publisher)
* Add model (book/publisher) to admin
* Add book\form.py class "form_create_publisher", "form_edit_publisher"

* Add model (book/book)
* Add model (book/book) to admin
* Add book\form.py class "form_create_book", "form_edit_book"

* API (views)
    * book/publisher_read
    * book/publisher_create
    * book/publisher_update
    * book/publisher_delete
    * book/book_read
    * book/book_create
    * book/book_update
    * book/book_delete
* urls
    * publisher/
    * publisher/create
    * publisher/<int:id>/
    * publisher/<int:id>/delete/
    * book/
    * book/create
    * book/<int:id>/
    * book/<int:id>/delete/
* Templates 
    * book/publisher_read
    * book/publisher_create
    * book/publisher_edit
    * book/book_read
    * book/book_create
    * book/publisher_edit

###### Change:
* Lainnya :
    * register\base.html
        * Submenu publisher
        * Submenu book


---
#### v 0.0.4 -- 2024/01/31
###### New:
* Make django app (book)
* Add model (book/author)
* Add model (book/author) to admin
* Add book\form.py class "form_create_author", "form_edit_author"

* Add model (book/genre)
* Add model (book/genre) to admin
* Add book\form.py class "form_create_genre", "form_edit_genre"

* API (views)
    * book/author_read
    * book/author_create
    * book/author_update
    * book/author_delete
    * book/genre_read
    * book/genre_create
    * book/genre_update
    * book/genre_delete
* urls
    * author/
    * author/create
    * author/<int:id>/
    * author/<int:id>/delete/
    * genre/
    * genre/create
    * genre/<int:id>/
    * genre/<int:id>/delete/
* Templates 
    * book/author_read
    * book/author_create
    * book/author_edit
    * book/genre_read
    * book/genre_create
    * book/genre_edit

###### Change:
* Lainnya :
    * settings.py 
        * Add INSTALLED_APPS ['book.apps.BookConfig', ]
    * library\urls.py
        * Add path('', include("book.urls")),
    * register\base.html
        * Add catalog sidebar with submenu
            * Submenu author
            * Submenu genre
        * Add stylesheet for icon
        * Add style
        * Add icon in each item sidebar

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
