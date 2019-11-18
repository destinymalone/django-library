# Django Library

In this assignment you will create the software required
for a small library to manage its inventory. You have been
provided the general application setup, tests, and templates.

Almost all of the material for this assignment should be familiar,
but there is 1 new component. Similar to other assignments
you will develop the required urls, views, and models.
New to this assignment, you will use Django's `messages`
framework to provide 1-time messages to your users.

To make sure your solution is correct, you can run the tests
with the following command:

`python3 manage.py test`

## `messages` Tutorial

**documentation**: https://docs.djangoproject.com/en/2.2/ref/contrib/messages/

The basic idea of the `messages` framework is to provide
a tool for developers to render 1-time messages inside
a template. It is commonly used for alerts to your user
after redirecting. We will generally constrain our use
of the framework to the following lines:

```python
# import messages
from django.contrib import messages

# add a success message
messages.success(request, "You did it! Hooray!")

# add an error message
messages.error(request, "Oh no! Something bad happened!")
```

You will use this code inside your views to add messages.
The provided templates are already set up to use the messages
that your views will add.

```python
from django.contrib import messages

def example_view(request):
    messages.error(request, "Fooey")
    return redirect("somewhere_else")
```

## Requirements

### Required Models

#### `Book`

`Book` should have the following fields:

- `title` - the title of the book
- `author` - the name of the author of the book
- `published` - the date the book was published
- `genre` - the genre of the book
- `in_stock` - whether or not the book is currently in stock
- `description` - a description of the book

#### `Transaction`

`Transaction` should have the following fields:

- `datetime` - the datetimewhen the transaction was created
- `action` - either `"CHECKIN"` for a return or `"CHECKOUT"` for a borrow
- `book` - the book being borrowed or returned

### Required URLs

- `""` should route to `home`
- `book/<id>/borrow` should route to `borrow_book`
- `book/<id>/return` should route to `return_book`

### Required Views

#### `home`

`home` renders `book_list.html` with all the books in the database
using the context key `"books"`.

#### `borrow_book`

`borrow_book` has two cases:

- If the book is in stock, the book is updated for `in_stock` to be
  `False` and a success message of `Borrowed <title> by <author>` is
  added. Also, a `"CHECKOUT"` `Transaction` should be created.
- if the book is not in stock, the an error message of
  `<title> by <author> is unavailable` is added

either way, the user is redirected to `home`

#### `return_book`

`return_book` has two cases:

- if the book is not in stock, the book is updated for `in_stock` to be
  `True` and a success message of `Returned <title> by <author>` is
  added. Also, a `"CHECKIN"` `Transaction` should be created.
- if the book is in stock, the an error message of
  `<title> by <author> is already here` is added

either way, the user is redirected to `home`
