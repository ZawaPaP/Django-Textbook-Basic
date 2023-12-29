## Template

With the template method pattern, we can use variables and tags in the template file.

1. Variables

   ```html
   <p>{{ variable }}</p>
   ```

2. Filters

   ```html
   <p>{{ variable|filter:argument }}</p>
   ```

   ```html
   <p>{{ user.first_name|default:"" }}</p>
   ```

3. Template Tag

```html
{% if user.is_authenticated %}
<p>Hi, authenticated user!</p>
{% else %}
<p>Hi, anonymous user!</p>
{% endif %}
```

4. Extend
   extends is used to inherit the base template.

   ```html
   {% extends "base.html" %}
   ```

5. Include
   include is used to include the template file.
   ```html
   {% include "header.html" %}
   ```

### Best Practice

Create a base template and inherit it in other templates.
