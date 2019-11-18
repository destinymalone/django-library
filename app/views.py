from django.shortcuts import render, redirect
from app.models import Book, Transaction
from django.contrib import messages
from django.contrib.auth import login
from django.utils import timezone
from django.urls import reverse_lazy
from app import forms
from django.views.generic import FormView


def home(request):
    return render(request, "book_list.html", {"books": Book.objects.all()})


def borrow_book(request, id):
    book = Book.objects.get(id=id)
    if book.in_stock:
        book.in_stock = False
        book.save()
        book.transaction_set.create(datetime=timezone.now(), action="CHECKOUT")
        messages.success(request, f"Borrowed {book.title} by {book.author}")
    else:
        messages.error(request, f"{book.title} by {book.author} is unavailable")
    return redirect("home")


def return_book(request, id):
    book = Book.objects.get(id=id)
    if not book.in_stock:
        book.in_stock = True
        book.save()
        book.transaction_set.create(datetime=timezone.now(), action="CHECKIN")
        messages.success(request, f"Returned {book.title} by {book.author}")
    else:
        messages.error(request, f"{book.title} by {book.author} is already here")
    return redirect("home")


class SignUpView(FormView):
    form_class = forms.SignUpForm
    template_name = "auth/user_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.signup()
        login(self.request, user)
        return super().form_valid(form)
