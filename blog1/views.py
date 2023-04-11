from django.shortcuts import render,HttpResponse
from .models import short_descriptions
from .models import types
from .models import template
from .models import profile

# Create your views here.
def index(request):
    data=short_descriptions.objects.all()
    if request.method=="GET":
         st=request.GET.get('q')
         if st!=None:
            data=short_descriptions.objects.filter(Desc__icontains=st)
            print(st)
    A=request.GET.get('A')
    if(A!=None):
        data=short_descriptions.objects.filter(choose=A)
   
    count1=short_descriptions.objects.filter(choose=A).count()
             
    data1=types.objects.all()
    p=profile.objects.all()
    contex= {
        'my_data':data,
        'my_data1':data1,
        'count1':count1,
        'profile':p
        
        }
  
    return render(request,'index.html',contex)
def blog(request,slug):

  
    data4=template.objects.all()
    p=profile.objects.all()
  
    data5=short_descriptions.objects.all()[:4]
    
    blog=short_descriptions.objects.get(new_slug1=slug)
    data9=template.objects.all().filter(share_key2=blog.share_key1)
    count=data9.count()



    data6=types.objects.all()

    c={
         'm_d':data9,
         'm_1':data5,
         'm_2':data6, 
        'profile':p         }
    
    if(count>0):
           return render(request,'template.html',c)
    else:
         return(render(request,'error.html'))
def con(request):
     return(render(request,"Contact.html"))
def privacy(request):
     return(render(request,"policy.html"))






     
     
 



