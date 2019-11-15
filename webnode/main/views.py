from django.shortcuts import render


def main(request):
    '''
    Render the main page
    '''
    context = {'like':'我們的服務技術,協助您快速架設網站'}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')