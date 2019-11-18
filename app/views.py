from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import Book, Transaction, User
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.


class Home(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "book_list.html", {"books": books})


@login_required
class BorrowBook(View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
        if book.in_stock:
            book.in_stock = False
            book.save()
            Transaction.objects.create(user=user, action="CHECK OUT", book=book)
            messages.success(
                request, f"{book.title} by {book.author} is now out of stock"
            )
            return redirect("home")
        else:
            messages.error(
                request, f"Borrowed {book.title} by {book.author} is unavailable"
            )
            return redirect("home")


@login_required
class ReturnBook(View):
    def post(self, request, id):
        item = Book.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
        if not item.in_stock:
            item.in_stock = True
            item.save()
            Transaction.objects.create(user=user, action="CHECK IN", book=item)
            messages.success(
                request, f"Returned {item.title} by {item.author} is now in stock"
            )
            return redirect("home")
        else:
            messages.error(request, f"{item.title} by {item.author} is already here")
            return redirect("home")
