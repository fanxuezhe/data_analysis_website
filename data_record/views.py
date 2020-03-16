from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,FileResponse
from django.template import loader
import datetime
from data_record.forms import ContactForms
# Create your views here.
from .models import History,Project,Users
import os
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
#定义一个登陆的界面
def log_in(request):
    if request:
        request.session.set_test_cookie()
        return render(request,"data_record/login.html",{"error":""})
def check_passwd(request):
    if request.method=="POST":
        #print(request.session.test_cookie_worked()) 
        username=request.POST.get("name")
        password=request.POST.get("passwd")
        #if request.session.test_cookie_worked():
        user=authenticate(username=username,password=password)
        if user is not None:
            return render(request,"data_record/function_choose.html")
        else:
            #return HttpResponse("error")
            return render(request,"data_record/login.html",{"error":"wrong password or username,please check and relogin"})
        #try:
            #m=Member.object.get(user_name=requst.POST["username"])
            #判断密码是否相同
            #username = request.POST.get("name")
            #password = request.POST.get("passwd")
            #if m.password==request.POST["password"]:
            #    request.session["member_id"]=m.id
            #    return HttpResponse("ok you are logging in ")
        #except KeyError:
        #    return HttpResponse("something wrong")
    else:
        return HttpResponse("not login")
        #username=request.post.get("username")
        #e = .objects.filter(email=email).first()
        #user=auth(username="1234",password=password)
        #user=request.user.is_authenticated
        #if username=="fanxuezhe" and password=="123455":
        #if user:
        #    #return render(request,"data_record/upload.html")
        #    return HttpResponse(user)
        #else:
        #    return HttpResponse("wrong number %s   %s "%(username,password))
#def index(request):
#    return HttpResponse("hello,this is the place record the data analysis history")
#定义一个function，该function的功能是指定数据分析的界面
def data_analysis(request):
    render(request,"data_record/data_analysis.html",)
#展示历史数据
def display(request):
    historys=History.objects.order_by("folder_name")
    history_values=historys.values()
    char_list=[]
    [[char_list.append("\t".join([key_n,str(value_n)]))for key_n,value_n in dict_n.items()] for dict_n in history_values] 
    return render(request,"data_record/show_record.html",{"display_data":char_list})
#定义一个homepage的视图,这将会是一个登陆界面
def home_page(request):
    #render(request,"data_record/home_page.html")
    now=datetime.datetime.now()
    target_url="<html><body>it is now %s</body></html>"%now
    #return HttpResponse(target_url)
    path_list=["path_1","path_2","path_3","path_4"]
    html=[]
    #for k,v in request.META.items():
    #    html.append("<tr><td>%s</td><td>%s</td></tr>"%(k,v))
    #return render(request,"data_record/home_page.html",{"path_all":path_list})
    #return HttpResponse("\n".join(html))
    return render(request,"data_record/show_info.html",{"all_info":request.META.items()})
def contact(request):
    if request.method=="POST":
        form=ContactForms(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            #send_email(cd["subject"],cd["message"],cd.get["email","noreply@example.com"],["siteowner@example.com"])
            #return HttpResponseRedirect("search-form/")
            return HttpResponse("another website")
    else:
        form=ContactForms(initial={"subject":"I love your site!"})
    return render(request,"data_record/contact_form.html",{"form":form})
        
       
        
def time_add(request,num_n):
    #num_n=100
    time_now=datetime.datetime.now()
    try:
        int_num=int(num_n)
    except:
        raise Http404
    else:
        time_add=time_now+datetime.timedelta(hours=int_num)
        html='<html><body> this is time %s </body></html>'%time_add
        return HttpResponse(html)
#@login_required
def upload(request):
    if request.method=="POST":
    
        #首先检查当前是否是一个授权的状态（是否已经登陆）
    #if request.user.is_authenticated:
    #    return HttpResponse("%s you are thenticated"%request.user.username)
    #else:
    #    return HttpResponse("%s   dxError "%request.user.username)
        
        #获取当前的分析人和分析的日期，根据这个来创建文件夹储存文件
        username=request.user
        
        #定义文件储存的目录
        dir_store=r"/home/fanxuezhe/files/test_files/django_download"
        #获取post中的文件
        myFile=request.FILES.get("myfile")
        if myFile :
            #return HttpResponse(myFile.name)
            copied_file=os.path.join(dir_store,myFile.name)
            with open(copied_file,"wb") as f:
                for content_n in myFile.chunks():
                    f.write(content_n)
            
            #接下来解压文件并且进行分析
            os.chdir(dir_store)
            all_files=os.listdir(dir_store)
            #解压上传的文件
            os.system("unzip %s >>log_file"%myFile.name)
            os.system("multi_tools FGS .")
            os.chdir(myFile.name.strip(".zip"))
            all_files=os.listdir(os.getcwd())
            
            #os.system("multi_tools FGS . >>logfile")
            #os.system("compress_result . >>logfile")
            #os.system("tar -czvf final_result.tar.gz logfile all_result.tar.gz")
            
            #log_file=open(os.path.join(dir_store,"logfile"),"wb")
            #result_file=open(os.path.join(dir_store,"final_result"),"rb")
            #file_response=FileResponse(result_file)
            #file_response["content_type"]="application/octet_stream"
            #file_response["Content-Disposition"]='attachment;file=result_file'
            #return HttpResponse("all over")
            return HttpResponse("\n".join(all_files))

        else:
            return HttpResponse("none file get")
        #if  myFile:
        #    f=open(r"/home/fanxuezhe/copied_{}".format(myFile.name),"wb")
        #    for line_n in file.chunks():
        #        f.write(line_n)
        #    f.close()
            #values.sorted()
        #    html=[]
            #for k,v in values:
            #    html.append("<tr><td>%s</td><td>%s</td></tr>"%(k,v))
            #    
            #return HttpResponse("<table>%s</table>"%("\n".join(html)))
            #list_values=[]
            #for key,value in values:
            #    list_values.append("%sxxxxxxxxxxxxx%s"%(key,value))
            #return render(request,"data_record/display_all.html",{"info_dict_items":list_values})
        #path_test=r"/home/fanxuezhe/files/test_files/django_test_files"
        #destination=open(os.path.join(path_test,myFile.name),"wb+")
        #for chunk in myFile.chunks():
        #    destination.write(chunk)
        #destination.close()
            
            #return HttpResponse("upload over")
        #else:
        #    return HttpResponse("can not get the file")
    else:
        return render(request,"data_record/upload.html") 
        
def search_form(request):
    if request.GET:
        if "q" in request.GET and request.GET["q"]:
        #message="ok,%s is found"%request.GET["q"]
            try:
                project=Project.objects.filter(project_name=request.GET["q"])
                message=project.project_name
            except:
                message="sorry,nnnnnnn not found"
            return HttpResponse(message)
        else:
            return render(request,"data_record/search_form.html",{"Search":"This is another search","warnings":"can not find or input in empty please check"})
    return render(request,"data_record/search_form.html",{"Search":"This is search","warnings":"the origin"})
        

def search(request):
    if "q" in request.GET and request.GET["q"]:
        #message="ok,%s is found"%request.GET["q"]
        try:
            project=Project.objects.filter(project_name=request.GET["q"])
            message=project.project_name
        except:
            message="sorry,nnnnnnn not found"
        return HttpResponse(message)
    else:
        return render(request,"data_record/search_form.html",{"Search":"This is another search","warnings":"can not find or input in empty please check"})
        

def index(request):
    latest_analysis_list=History.objects.order_by("-pub_date")[:3]
    #template=loader.get_template("data_record/index.html")
    #这里的键和templates中的变量名称是对应的
    context={"latest_analysis_list":latest_analysis_list}
    #output=",".join(q.project_name for q in latest_analysis_list)
    #前面放上请求，后面放上模板和变量
    return render(request,"data_record/index.html",context)

def detail(request,History_id):
    analysis=get_object_or_404(History,pk=History_id)
    return render(request,"data_record/detail.html",{"History":analysis})
#def detail(request,History_id):
#    return HttpResponse("hello you are checking detail of %s"%History_id)

#def detail(request,History_id):
#    try:
#        analysis=History.objects.get(pk=History_id)
#    except History.DoesNotExist:
#        raise Http404("There is no id called %d"%History_id)
#    return render(request,"data_record/detail.html",{"History":analysis})
    #return HttpResponse("hello you are checking detail of %s"%History_id)



def result(request,History_id):
    return HttpResponse("hello you are checking result of %s"%History_id)
def vote(request,History_id):
    return HttpResponse("hello you are checking vote of %s"%History_id)
