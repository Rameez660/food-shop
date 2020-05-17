from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from shop.models import User,Contact,Order
from django.contrib.sessions.models import Session
def home(request):
    return render(request,'shop/index.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        
    #    print(name,email,phone,desc)
	   	
        if len(name) > 6  and len(email) > 15 and len(desc) > 5:
        	# messages.error(request,"error")
		# else:
            contact = Contact(name=name, email=email, desc=desc,timeStamp=datetime.today())

            # ,timestamp=datetime.today()
            contact.save()
            messages.success(request, 'Thanks for your response')
        else:
            messages.error(request,"Form Not Submitted Successfully. Please Fill The Form Correctly")
            return redirect('contact')
    else:
        return render(request, 'shop/contact.html')
    return render(request,'shop/contact.html')



def ordernow(request):
	if request.session.has_key('is_logged'):
		if request.method=="POST":
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			cnic = request.POST.get('cnic', '')
			address = request.POST.get('address', '')
			addresss = request.POST.get('addresss', '')
			number = request.POST.get('number', '')
			country = request.POST.get('country', '')
			city = request.POST.get('city', '')
			item1 = request.POST.get('item1', '')
			item2 = request.POST.get('item2', '')
			item3 = request.POST.get('item3', '')
			item4 = request.POST.get('item4', '')
			item5 = request.POST.get('item5', '')
			item6 = request.POST.get('item6', '')
			item7 = request.POST.get('item7', '')
			item8 = request.POST.get('item8', '')
			quantity1 = request.POST.get('quantity1', '')
			quantity2 = request.POST.get('quantity2', '')
			quantity3 = request.POST.get('quantity3', '')
			quantity4 = request.POST.get('quantity4', '')
			quantity5 = request.POST.get('quantity5', '')
			quantity6 = request.POST.get('quantity6', '')
			quantity7 = request.POST.get('quantity7', '')
			quantity8 = request.POST.get('quantity8', '')
			total = (int(quantity1) * 100 ) + (int(quantity2) * 100 ) +   (int(quantity3) * 100 )+   (int(quantity4) * 100 ) + (int(quantity5) * 100 ) + (int(quantity6) * 100 ) + (int(quantity7) * 100 ) + (int(quantity8) * 100 )
			if  len(name) > 5 and len(email) > 16 and len(cnic) > 12 and len(cnic) < 14 and len(number) == 11 and len(address) > 6 and len(addresss) > 6:
				order= Order(name=name, email=email, cnic=cnic, address=address, addresss=addresss, number=number, country=country, city=city, item1=item1,  item2=item2, item3=item3, item4=item4, item5=item5, item6=item6, item7=item7, item8=item8,quantity1=quantity1,quantity2=quantity2,quantity3=quantity3,quantity4=quantity4,quantity5=quantity5,quantity6=quantity6,quantity7=quantity7,quantity8=quantity8,timeStamp=datetime.today(),total=total)		
				order.save()
				messages.success(request, 'Your order has been created successfully. Please wait for our response. Thank You (Your total items amount is RS: ' + str(total) + '). Delivery charges is RS: 200' + '. Your total Amount including delivery charges is RS: '   + str(total + 200) )
				return redirect('/')
				# else:
					# messages.success(request, "'ERROR' Your order didn't created sucessfully. Please enter valid credentials. Thank You")
					# return redirect('/')
			else:
       
				messages.error(request,"'ERROR' Your order didn't created sucessfully. Please enter valid credentials. Thank You")
				return redirect('ordernow')
		else:
			return render(request, 'shop/ordernow.html')
		return render(request,'shop/ordernow.html')
	return redirect('login')
def blog(request):
    return render(request,'shop/blog.html')
def search(request):
    query=request.GET['query']
    # if len(query)>100 or len(query) == 0:
    #     # allPosts=[]
    #     allPosts=Post.objects.none()
    # else:
    #     allPoststitle=Post.objects.filter(title__icontains=query)
    #     allPostscontent=Post.objects.filter(content__icontains=query)
    #     allPostsslug=Post.objects.filter(slug__icontains=query)

    #     allPosts=allPoststitle.union(allPostscontent,allPostsslug)
    # if allPosts.count() == 0:
    #     messages.error(request,"No search results found plear search with another query")
       
    # allPosts:Post.objects.all()
    params={'query':query}
    return render(request,'shop/index.html',params)


def login(request):
	if request.session.has_key('is_logged'):
		return redirect('home')
	if request.POST:
		email = request.POST['email']
		password = request.POST['password']
		count=User.objects.filter(email=email,password=password).count()
		if count > 0:
			request.session['is_logged'] = True
			messages.success(request,'You are successfully login')
			return redirect('ordernow')
		else:
			messages.error(request,'You are enter invalid credentials')
			return redirect('login')
	return render(request,'shop/login.html')

def signup(request):
	return render(request,'shop/signup.html')

def register_user(request):
	if request.POST:
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		passwordd = request.POST['passwordd']
  
		# password2 = request.POST['password2']
		if len(username) > 4 and len(email) > 15 and len(password) > 7 and len(passwordd) > 7 and password == passwordd:
			obj = User(firstname=firstname,lastname=lastname,username=username,email=email,password=password,passwordd=passwordd,timeStamp=datetime.today())
			obj.save()
			messages.success(request,'You are successfully Registered')
			return redirect('login')
		else:
			messages.error(request,'You are not registered. Please enter valid credentials')
			return redirect('signup')			

def handlelogout(request):
	if request.session.has_key('is_logged'):
		del request.session['is_logged']
		messages.success(request,'You are successfully logged out')
		return redirect('login')
	else:
		return redirect('login')