from django.shortcuts import render
def post_list(request):
    assert isinstance(request, object)
    return render(request, 'blog/post_list.html', {})
# Create your views here.
