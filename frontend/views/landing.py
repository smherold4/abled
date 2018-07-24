from django.shortcuts import render

class LandingViewSet(object):
  @staticmethod
  def show(request):
    return render(request, 'landing/show.html')