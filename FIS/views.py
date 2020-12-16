from bokeh.embed import components
from bokeh.plotting import figure
from numpy import pi
from bokeh.palettes import *
from bokeh.transform import cumsum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from .json import *
from rest_framework.views import APIView
from rest_framework import viewsets

from django.http import JsonResponse , HttpResponse

from . import models
from django.http import JsonResponse
from django.shortcuts import render
from FIS.models import Desktop

from django.core import serializers

from django.shortcuts import render, render_to_response
from chartit import DataPool, Chart, PivotDataPool, PivotChart

from bokeh.models import *

def index(request):
    return render(request,'index.html')
#########dislays functions (buttons activation)
def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header':'Laptops'
    }

    return render(request,'index.html',context) #3 rguments
def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktops'
    }

    return render(request,'index.html',context)
#########dislays functions (buttons activation)

################add devices functions
def add_device(request,cls):
    if request.method == "POST":
        form=cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request,'add_new.html',{'form':form})
def add_laptot(request):
    return add_device(request,LaptopForm)
def add_desktop(request):
    return add_device(request,DesktopForm)
################add devices functions

#########Edit functions:
def edit_device(request, pk, model,cls):
    item=get_object_or_404(model,pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)
        return render (request,'edit_item.html',{'form':form})

def edit_laptop(request,pk):
    return edit_device(request,pk,Laptop,LaptopForm)

def edit_desktop(request,pk):
    return edit_device(request,pk,Desktop,DesktopForm)
#########Edit functions:




###############Delet functions:
def delet_laptop(request, pk):
    Laptop.objects.filter(id=pk).delete()
    items = Laptop.objects.all()
    context={
        'items':items
    }
    return render(request,'index.html',context)

def delet_desktop(request, pk):
    Desktop.objects.filter(id=pk).delete()
    items = Desktop.objects.all()
    context={
        'items':items
    }
    return render(request,'index.html',context)
###############Delet functions:

############API(method 1 sur les desktops)
class desktop_list(APIView):

    def get(self,request):
        s1=Desktop.objects.all()
        s2=jsonFis(s1,many=True)
        return Response(s2.data)
    def post(self):
        pass
#############API(method 1 sur les desktops)

#############API(method 2 sur les laptops)
class laptop_list(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = jsonFis2
#############API(method 2 sur les laptops)

#############API users#############
class user_list(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = json_user
#############API users#############

###################################
###        register             ###
###################################
def register(request):
    return render(request,'register.html',{})
def register_backend(request):
    try:
        user=User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.save()
        return redirect('index')
    except:
        return HttpResponse('Username Is Exist!')
###################################
###        register             ###
###################################

###################################
###        Log-In               ###
###################################
def log(request):
    return render(request,'login.html',{})
def log_backend(request):
    username=request.POST['username']
    password=request.POST['password']
    result=authenticate(username=username,password=password)
    if result is not None:
        print('login')
        login(request,result)
        return redirect('index')
    else:
        return HttpResponse('User is not Exist')

###################################
###        Log-In               ###
###################################

###################################
###        Log-Out              ###
###################################

def logout_backend(request):
    logout(request)
    return redirect('log')

###################################
###        Log-Out               ###
###################################

##########################################
####        flexmonster          ####
##########################################


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})
def pivot_data(request):
    dataset = Desktop.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

####################
import pandas as pd
def main_view(request):
    qs= Desktop.objects.all().values()
    #qs2= Desktop.objects.all().values_list()
    data= pd.DataFrame(qs)

    #data2= pd.DataFrame(qs2)
    print(data)
    context = {
        'df': data.to_html(),
        'describe': data.describe().to_html()
    }
    #print('#######')
    #print(data2)
    #data=pd.DataFrame(qs)
    #print(data.shape)
    return render(request,'main.html', context)

#################

#################
def products(request):
    delle2009wt	 = 0
    Dell17 = 0
    none = 2
    counts = []
    items = ["dell e2009wt", 'Dell 17"', "None"]
    prod = Desktop.objects.values()

    for i in prod:
        if "dell e2009wt" in i.values():
            delle2009wt	 += 1
        elif ('Dell 17"' in i.values()):
            Dell17 += 1
        elif ("" in i.values()):
            none += 1
    counts.extend([delle2009wt, Dell17, none])

    plot = figure(x_range=items, plot_height=600, plot_width=800, title="FIS-Products",
                  toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
    plot.title.text_font_size = '20pt'

    plot.xaxis.major_label_text_font_size = "14pt"
    plot.vbar(items, top=counts, width=.4, color="dodgerblue", legend="Product Counts")
    plot.legend.label_text_font_size = '14pt'

    script, div = components(plot)

    return render(request, 'products.html', {'script': script, 'div': div})
#################

################chart2
def weatherByCity(request):
    ds = DataPool(
        series=[{
            'options': {
                'source': Desktop.objects.all()
            },
            'terms': [
                'Model_USBheadset',
                'Secreen1_Model',
                'houston_temp'
            ]
        }]
)

    cht = Chart(
        datasource=ds,
        series_options=[{
            'options': {
                'type': 'line'
            },
            'terms': {
                'month': ['boston_temp']
            }}, {
            'options': {
                'type': 'pie',
                'center': [150, 100],
                'size': '50%'
            },
            'terms': {
                'month': ['houston_temp']
            }}
        ],
        chart_options={
            'title': {
                'text': 'Weather Data of Boston (line) and Houston (pie)'
            }
        },
        x_sortf_mapf_mts=[(None, False),
                          (None, False)])

    return render_to_response('weatherByCity.html', {'weatherByCity': cht})
##########################
#### Chart model name ####
##########################


def model_name(request):
    HP_EliteDesk_800_G1_SFF	 = 0
    HP_Compaq_Elite_8300_SFF = 2
    HP_Compaq_8200_Elite_SFF = 0
    HP_Compaq_Elite_8200_SFF = 2
    HP_Elitedesk_800G2 = 0
    HP_EliteBook_840_G1 = 0
    HP_Elitedesk_800G1 = 16
    counts = []
    items = ["HP EliteDesk 800 G1 SFF", "HP Compaq Elite 8300 SFF", "HP Compaq 8200 Elite SFF", "HP Compaq Elite 8200 SFF",
             "HP Elitedesk 800G2", "HP EliteBook 840 G1", "HP Elitedesk 800G1"]
    prod = Desktop.objects.values()

    for i in prod:
        if "HP EliteDesk 800 G1 SFF" in i.values():
            HP_EliteDesk_800_G1_SFF	 += 1
        elif ("HP Compaq Elite 8300 SFF" in i.values()):
            HP_Compaq_Elite_8300_SFF += 1
        elif ("HP Compaq 8200 Elite SFF" in i.values()):
            HP_Compaq_8200_Elite_SFF += 1
        elif ("HP Compaq Elite 8200 SFF" in i.values()):
            HP_Compaq_Elite_8200_SFF += 1
        elif ("HP Elitedesk 800G2" in i.values()):
            HP_Elitedesk_800G2 += 1
        elif ("HP EliteBook 840 G1" in i.values()):
            HP_EliteBook_840_G1 += 1
        elif ("HP Elitedesk 800G1" in i.values()):
            HP_Elitedesk_800G1 += 1

    counts.extend([HP_EliteDesk_800_G1_SFF, HP_Compaq_Elite_8300_SFF, HP_Compaq_8200_Elite_SFF, HP_Compaq_Elite_8200_SFF, HP_Elitedesk_800G2, HP_EliteBook_840_G1, HP_Elitedesk_800G1])

    plot = figure(x_range=items, plot_height=600, plot_width=999, title="Products",
                  toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
    plot.title.text_font_size = '20pt'

    plot.xaxis.major_label_text_font_size = "7.5pt"
    plot.vbar(items, top=counts, width=.8, color="slategray", legend="Product Counts")
    plot.legend.label_text_font_size = '20pt'

    script, div = components(plot)

    return render(request, 'model_name.html', {'script': script, 'div': div})

##########################
#### Chart model name ####
##########################

#########################
####  pie chart desk ####
#########################
def pie(request):
    JabraUCV_550 = 0
    PLANTRONIC_C_420 = 0
    JabraUCV_750 = 0
    SENNHEISER_SC_60_USB_CTRL = 0

    prod = Desktop.objects.values()
    for i in prod:
        if "Jabra UCV - 550" in i.values():
            JabraUCV_550 += 1
        elif ("PLANTRONIC C 420" in i.values()):
            PLANTRONIC_C_420 += 1
        elif ("Jabra UCV - 750" in i.values()):
            JabraUCV_750 += 1
        elif ("SENNHEISER SC 60 USB CTRL" in i.values()):
            SENNHEISER_SC_60_USB_CTRL += 1
    x = {'Jabra UCV - 550': JabraUCV_550 , 'PLANTRONIC C 420': PLANTRONIC_C_420 , 'SENNHEISER SC 60 USB CTRL': SENNHEISER_SC_60_USB_CTRL, 'Jabra UCV - 750': JabraUCV_750}

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=600, plot_width=800, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@country: @value")

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="royalblue", fill_color='color', legend='country', source=data)


    script, div = components(p)

    return render(request, 'pie.html' , {'script': script, 'div':div})
#########################
####  pie chart desk ####
#########################
##########################
####### Pie Chart ########
##########################
def piel(request):
    dell = 0
    HP = 0
    nan = 0

    prod = Laptop.objects.values()
    for i in prod:
        if ("Dell" in i.values()):
            dell += 1
        elif ("Hewlett Packard" in i.values()):
            HP += 1
        elif ("nan" in i.values()):
            nan += 1

    x = {'Dell': dell, 'Hewlett Packard': HP, 'nan': nan}

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=600, plot_width=800, title="FIS-Products", toolbar_location=None,
            tools="hover", tooltips="@country: @value")

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='country', source=data)


    script, div = components(p)

    return render(request, 'piel.html' , {'script': script, 'div':div})
##########################
####### Pie Chart ########
##########################

##########################
####### bar-Chart ########
##########################
def programming(request):
    SENNHEISER_SC_230 = 0
    SENNHEISER_SC_260 = 0
    Jabra_GN_2000 = 18
    JABRA_GN_2000_BIZ = 6
    JABRA_GN_1216 = 0
    JABRA_SC_260 = 0
    JABRA_BIZ620 = 0
    JABRA_2300 = 0
    Jabra = 0
    none = 0

    lang = ['SENNHEISER SC 230', 'SENNHEISER SC 260', 'Jabra  GN 2000', 'JABRA - GN 2000 - BIZ', 'JABRA GN 1216',
            'JABRA -SC 260', 'JABRA - BIZ620', 'JABRA 2300', 'JABRA', 'None']
    prod = Laptop.objects.values()
    for i in prod:
        if ("SENNHEISER SC 230" in i.values()):
            SENNHEISER_SC_230 += 1
        elif ("SENNHEISER SC 260" in i.values()):
            SENNHEISER_SC_260 += 1
        elif ("Jabra  GN 2000" in i.values()):
            Jabra_GN_2000 += 1
        elif ("JABRA - GN 2000 - BIZ" in i.values()):
            JABRA_GN_2000_BIZ += 1
        elif ("JABRA GN 1216" in i.values()):
            JABRA_GN_1216 += 1
        elif ("JABRA -SC 260" in i.values()):
            JABRA_SC_260 += 1
        elif ("JABRA - BIZ620" in i.values()):
            JABRA_BIZ620 += 1
        elif ("JABRA 2300" in i.values()):
            JABRA_2300 += 1
        elif ("JABRA" in i.values()):
            Jabra += 1
        elif ("None" in i.values()):
            none += 1
    counts = [SENNHEISER_SC_230, SENNHEISER_SC_260, Jabra_GN_2000, JABRA_GN_2000_BIZ, JABRA_GN_1216, JABRA_SC_260, JABRA_BIZ620,
              JABRA_2300, Jabra, none]
    p = figure(x_range=lang, plot_height=450, plot_width=1000, title="FIS-Products",
               toolbar_location="below", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")

    source = ColumnDataSource(data=dict(lang=lang, counts=counts, color=Spectral6))
    p.add_tools(LassoSelectTool())
    p.add_tools(WheelZoomTool())

    p.vbar(x='lang', top='counts', width=.3, color='color', legend="lang", source=source)
    p.legend.orientation = "vertical"
    p.legend.location = "top_right"

    p.xgrid.grid_line_color = "#E2E2D7"
    p.y_range.start = 0
    p.line(x=lang, y=counts, color="#27F9E3", line_width=0.5)

    script, div = components(p)

    return render(request, 'programing.html', {'script': script, 'div': div})
##########################
####### bar-Chart ########
##########################

##########################
######principal_chart#####
##########################
def principal_chart(request):
    laptop = 0
    desktop = 0
    nan = 0

    lap = Laptop.objects.values()
    desk = Desktop.objects.values()
    for i in lap:
        if ("Laptop" in i.values()):
            laptop += 1
    for j in desk:
        if ("Desktop" in j.values()):
            desktop += 1

    x = {'Laptop': laptop, 'Desktop': desktop, 'nan': nan}

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=600, plot_width=800, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@country: @value")

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='country', source=data)


    script, div = components(p)

    return render(request, 'principal_chart.html' , {'script': script, 'div':div})
##########################
######principal_chart#####
##########################

##########################
#####Dell or HP(Desk)#####
##########################
def Dell_HP_desk(request):
    dell = 0
    HP = 0
    nan = 0

    prod = Desktop.objects.values()
    for i in prod:
        if ("Dell" in i.values()):
            dell += 1
        elif ("Hewlett Packard" in i.values()):
            HP += 1
        elif ("nan" in i.values()):
            nan += 1

    x = {'Dell': dell, 'Hewlett Packard': HP, 'nan': nan}

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=600, plot_width=800, title="FIS-Products", toolbar_location=None,
            tools="hover", tooltips="@country: @value")

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='country', source=data)


    script, div = components(p)

    return render(request, 'piel2.html' , {'script': script, 'div':div})
##########################
#####Dell or HP(Desk)#####
##########################
def navbar(request):
    return render(request, 'navbar.html', {})
