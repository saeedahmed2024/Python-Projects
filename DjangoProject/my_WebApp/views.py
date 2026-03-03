
from django.http import HttpResponse
from django.shortcuts import render
import count

def home(request):
    #dict_1 = {'key1':'this is the value from code'}
    return render(request, 'index.html')
def result(request):
    article = request.GET['article']
    word_count, sorted_words = count.count(article)
    return render(request, 'result.html', {'article': article, 'word_count':word_count, 'dict_words':sorted_words} )

# def downloads(request):
#     return HttpResponse("<h1>No downloaded files</h1>")
# def about(request):
#     return HttpResponse("<h3>This is a sample web page made using django.</h3>")
