# Django Simple To-Do List

This is a simple to-do list application built using Django and styled with Bootstrap.

## Features
- Register
- Login
- CRUD todo
- CRUD todo-item 
- Mark todo-items as completed
- Async change (todo.name and item.text) in one page 


## Technologies Used

- Django
- Bootstrap
- crispy-bootstrap4

### Clone, Install, and Run

```bash
# Clone the Repository
git clone https://github.com/Luqy12099/simple-todo.git
cd simple-todo (or your own folder)

# Make new env (Optional)
python -m venv venv_nameYourVenv
venv_nameYourVenv\Scripts\activate

# Install Dependencies
pip install -r pip_req.txt
pip install --upgrade pip
pip install crispy-bootstrap4

# Apply Migrations
cd todolist
python manage.py migrate

# Run the Application
python manage.py runserver