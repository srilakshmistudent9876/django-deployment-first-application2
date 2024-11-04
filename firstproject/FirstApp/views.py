from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    print("welcome/url is requested& display() is executed")
    ss='''
        <center>
        <h2 style="color:Blue;">
        Hello user,welcome to django First-Project Frist-App
        </h2>
            <hr>
            </center>
            ''';
    return HttpResponse(ss);
    
    
def show(request):
    ss='''
    <!--
html  webpage to display "welcomemessage
-->
<html>
<head>
<title>***welcome2-page**</title>
<style>
h1{
color:blue;
}
h2{
color:green;
}
h3{
color:hot pink;
}
h4{
color:violet;
}
h5{
color:red;
}
h6{
color:orange;
}
h1,h3,h5
{
background-color:yellow;
border:2px solid rgb(123,125,146);
}
h2,h4,h6{
background-color:lightgreen;
border:2px dotted rgb(253,206,196);
}
</style>


</head>
<body>
<center>
	<h1>welcome to Django Html Webpage</h1>
	<hr color="brown" width="95%"/>
	<h2>welcome to Django Html Webpage</h2>
	<hr color="brown" width="85%"/>
		<h3>welcome to Django Html Webpage</h3>
		<hr color="brown" width="75%"/>
	<h4>welcome to Django Html Webpage</h4>
	<hr color="brown" width="65%"/>
	<h5>welcome to Django Html Webpage</h5>
	<hr color="brown" width="55%"/>
	<h6>welcome to Django Html Webpage</h6>
	<hr color="brown" width="45%"/>
	</center>
</body>
</html>
	
	

</body>
</html>
    ''';
    return HttpResponse(ss);
        
        
        
def hello(request):
    ss='''
<html>
<head>
<head>
<title>Hello webpage</title>
<style>
h1{
color:blue;
width:90%;
}
h2{
color:green;
width:80%;
}
h3{
color:red;
width:70%;
}
h1,h2,h3{
background-color:lightgreen;
border:2px solid brown;

</style>
<body>
<center>
<h1>Hello User...!!!</h1>
<hr color="brown" width="80%"/>
<h2>Welcome to Django-App</h2> 
<hr color="brown" width="60%"/>
<h3>have anice day</h3>
<hr color="brown" width="40%"/>
</center>
</body>
</html>
    ''';
    return HttpResponse(ss);
    
    
    
import time;
def senddatetime(request):
    print(":dtime/url is requested &senddatetime() is executed");
    ct=time.ctime()
    print("client request date &time on server::",ct);
    ss='''
    <head>
<title>Date-time Webpage</title>
<style>
h1{
color:blue;
width:90%;
}
h2{
color:green;
width:80%;
}
h3{
color:red;
width:70%;
}
h1,h2,h3{
background-color:lightgreen;
border:2px solid brown;
}
</style>
</head>
<body>
<center>
<h1>welcome to Django user..!</h1>
<hr color="brown" width="80%"/>
<h2>server=Date & Time::</h2>
<h3>''',ct,'''</h3>
<hr color="brown" width="60%"/>
</center>
</body>
</html>
    ''';
    return HttpResponse(ss);
def  demo(request):
    print("multiple-Requests-Urls same response")
    htmldata='''<center>
    <h1>welcome Demo User!!!</h1>
    <hr/>
    <h2>this is same output for dif- multiple -request-urls</h2>
    <hr/>
    <h3>Have a great day</h3>
    <center>''';
    return HttpResponse(htmldata);
    
def homepage(request):
    htmldata='''<center>
    <h1>welcome to Default home page!!!</h1>
    <hr/>
    <h2>your Request page is Not-Found...</h2>
    <hr/>
    <h3>plz tryother url or link!!!</h3>
    <center>''';
    return HttpResponse(htmldata);
    