Django の教科書 基礎編

### Best Practices

1. Django default project structure has the same name between project and config folder. This is not a good practice. It is better to have different names for project and config folder. For example, project name is `myproject` and config folder name is `config`. This is a good practice.

1-1. Create a project folder and config folder inside the project folder. Then, create a project inside the config folder.

```bash
mkdir myproject
cd myproject
django-admin startproject config .
```

1-2. Create a templates folder and static folder inside the project folder. Then, create a base.html file inside the templates folder.

```bash
|-- myproject
    |-- config
    |-- templates
        |-- base.html
        |-- myapp
            |-- index.html
    |-- static
        |-- css
            |-- style.css
        |-- js
            |-- script.js
```
