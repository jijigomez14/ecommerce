from django.shortcuts import render


from django.shortcuts import render

def index(request):
    # Any logic or data retrieval can be done here before rendering the template
    return render(request, 'index.html')
def header(request):
    # Any logic or data retrieval for the about page can be done here
    return render(request, 'header.html')
def footer(request):
    # Any logic or data retrieval for the about page can be done here
    return render(request, 'footer.html')
def product(request):
    # Replace this with your actual logic to retrieve product details
    
    return render(request, 'product.html')

def login_view(request):
    return render(request, 'login.html')
    
def signup_view(request):
    return render(request, 'signup.html')   
  
def about_view(request):
    return render(request, 'about.html')   

  
def blog_view(request):
    return render(request, 'blog.html')   
def about_view(request):
    return render(request, '.html')   