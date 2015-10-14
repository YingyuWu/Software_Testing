from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item
from django.shortcuts import redirect, render
# Create your views here.
def home_page(request):
	#return HttpResponse('<html><title>To-Do lists</title></html>')
	#if request.method == 'POST':
		#return HttpResponse(request.POST['item_text'])
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		#new_item_text = request.POST['item_text']
		return redirect('/')

	items = Item.objects.all()
	return render(request, 'home.html',{'items': items})
		#Item.objects.create(text=new_item_text)
	#else:
		#new_item_text = ''

	#return render(request,'home.html',{
		#'new_item_text': new_item_text
	#})