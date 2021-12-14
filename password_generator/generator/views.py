from django.shortcuts import render
from django.http import HttpResponse
import random

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special = ['!', '@', '#', '$', '%', '^', '&', '^', '*', '?']

def password_generator(size = 16, chars = upper + lower + nums + special):  
    errorMessage = "Your password must be at least 8 characters long for complexity"
    if (size >= 8):
        password = ''
        for i in range(size):
            password += (random.choice(chars))
            if (len(password) >= size):
                if any(s in password for s in upper) and any(t in password for t in lower) and any(u in password for u in nums) and any(v in password for v in special):
                    return password
                else:
                    return password_generator()
    else:
        return errorMessage

def home(request):
    return HttpResponse('<h3>Generated password: </h3>' + password_generator())
