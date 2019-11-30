from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import datetime
import pyowm


#################################################################33#
####################################################################

              #############  Second window ##############

def Second(cityname):
#    temp={"N":"Null","Nu":"Null","Nul":"Null"}
#    humidity,hum,a,e="Null","Null","Null","Null";
#    d={'speed':'Null','deg':'Null'}
    city=str(cityname)
    try:
        owm = pyowm.OWM("a7f74df59fa82e9e50674eb6801fb7c5")

        location= owm.weather_at_place(city)

        weather= location.get_weather()

        temp = weather.get_temperature('celsius')

        humidity = weather.get_humidity();

        hum = weather.get_detailed_status()

        a= weather.get_visibility_distance()

       # b= weather.get_weather_icon_name()

       # c = weather.get_weather_code()

        d = weather.get_wind()

        e = weather.get_clouds()

        print(temp)
        print(humidity)
        print(hum)
        print(a);
#print(b)
#print(c)
        print(d)
        print(e)
        temperature=list(temp.values())
        hawa=list(d.values())
        k=len(d)
 #######$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        
        temp1=temperature[0]
        temp2=temperature[1]
        temp3=temperature[2]
        hu=int(humidity)
        st=str(hum)
        if a==None:
            vis=None
        else :
            vis=int(a)
        if(k==2):
            wind1=hawa[0]
            wind2=hawa[1];
        else:
            wind1=hawa[0]
            wind2=None
        cl=int(e)
   ###################################
        root.destroy()
        r = Tk()
        r.title("Weather")
        r.geometry("600x600+400+90")
        r.resizable(False,False)
        titlefont = Font(size="16")

        # First Frame
        firstframe= Frame(r,width="600",height="600",bg="blue")
        firstframe.pack()

        
        # Title Lable
        TitleLable = Label(firstframe,text="WEATHER REPORT",font=titlefont,bg="blue",fg="white");
        TitleLable.place(x=200,y=10)
        line = Label(firstframe,text="=x=x=x=x=x=x=x=x=x=x=",font=titlefont,bg="blue",fg="white")
        line.place(x=180,y=40)
        #Location Lable
        LF=Font(size=14);
        Locationlabel = Label(firstframe,text="Location : " ,font=LF,bg="blue")
        LocationName  = Label(firstframe,text=cityname,font=LF,bg="blue",fg="white")
        Locationlabel.place(x=30,y=100)
        LocationName.place(x=120,y=100)
        #Temperature Lable
        temperature = Label(firstframe,text="Temprature : ",font=LF,bg="blue")
        temperature.place(x=30,y=150)

        sf=Font(size=13)
        mintemp = Label(firstframe,text="Min : ",font=sf,bg="blue")
        maxtemp = Label(firstframe,text="Max : ",font=sf,bg="blue")
        mintemp.place(x=150,y=200)
        maxtemp.place(x=350,y=200)
       
        #Humidity Label
        humidity = Label(firstframe,text="Humidity : ",font=LF,bg="blue")
        humidity.place(x=30,y=250)

       
        #Status Label
        statuslabel =Label(firstframe,text="Status : ",font=LF,bg="blue")
        statuslabel.place(x=30,y=300)

        
        #Visibility_distance
        Visibility_distance =Label(firstframe,text="Visibility : ",font=LF,bg="blue")
        Visibility_distance.place(x=30,y=350)

       
        #wind
        wind = Label(firstframe,text="Wind : ",font=LF,bg="blue")
        wind.place(x=30,y=400)

        windspeed = Label(firstframe,text="Speed : ",font=sf,bg="blue")
        winddeg = Label(firstframe,text="deg : ",font=sf,bg="blue")
        windspeed.place(x=150,y=430)
        winddeg.place(x=350,y=430)


       
        #clouds
        clouds = Label(firstframe,text="Clouds : ",font=LF,bg="blue")
        clouds.place(x=30,y=480)

        Okbutton = Button(firstframe,text=" OK ",bg="blue",command=r.destroy,width=20,bd=4,fg="orange")
        Okbutton.place(x=240,y=560)

        
   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
         ######
        tempvalue = Label(firstframe,text=str(temp1)+" C",font=LF,bg="blue",fg="white")
        tempvalue.place(x=170,y=150)

        minvalue= Label(firstframe,text=str(temp3)+" C",font=sf,bg="blue",fg="white")
        maxvalue= Label(firstframe,text=str(temp2)+" C",font=sf,bg="blue",fg="white")
        minvalue.place(x=200,y=200)
        maxvalue.place(x=400,y=200)

        ##################
        humidityvalue = Label(firstframe,text=str(hu)+" %",font=LF,bg="blue",fg="white")
        humidityvalue.place(x=170,y=250)


        ##########
        statusvalue = Label(firstframe,text=st,font=LF,bg="blue",fg="white")
        statusvalue.place(x=120,y=300)


         ####################################
        Visibility_value = Label(firstframe,text=str(vis)+" (m)",font=LF,bg="blue",fg="white")
        Visibility_value.place(x=120,y=350)

         ###################################################

        windspeedvalue= Label(firstframe,text=str(wind1)+" (Km)",font=sf,bg="blue",fg="white")
        winddegvalue= Label(firstframe,text=wind2,font=sf,bg="blue",fg="white")
        windspeedvalue.place(x=220,y=430)
        winddegvalue.place(x=420,y=430)


        ##################################33
        cloudsvalue=Label(firstframe,text=str(cl)+" %",font=LF,bg="blue",fg="white")
        cloudsvalue.place(x=120,y=480)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    except Exception as e:
        root.destroy()
        print("Check You Internet connection ",e)
        message=str(e)
        show = Tk()
        show.title("Weather")
        show.geometry("600x600+400+90")
        show.resizable(False,False)
        f=Frame(show,width="600",height="600",bg="blue")
        f.pack();
        e=Font(size=14)
        size1=Font(size=24)
        head=Label(f,text="You're not connected to a network",font=size1,bg="blue",fg="orange")
        head.place(x=30,y=70);
        E1=Label(f,text="• Check that all network cables are plugged in.",font=e,bg="blue")
        E2=Label(f,text="• Verify that airplane mode is turned off.",font=e,bg="blue")
        E3=Label(f,text="• Make sure your wireless switch is turned on.",font=e,bg="blue")
        E4=Label(f,text="• See if you can connect to mobile broadband.",font=e,bg="blue")
        E5=Label(f,text="• Restart your router.",font=e,bg="blue")
        Error=Text(f,width=70,height=9,bd=4,wrap=WORD)
        Error.insert(INSERT,message)
        Cancel=Button(f,text="Cancel",command=show.destroy,bg="blue",width="30",bd=4,fg="orange")
        E1.place(x=50,y=150)
        E2.place(x=50,y=200)
        E3.place(x=50,y=250)
        E4.place(x=50,y=300)
        E5.place(x=50,y=350)
        Error.place(x=10,y=400)

        Cancel.place(x=60,y=570)
 ##










    ########################################################################3
    ###################   info function ###################################

def info():
    sf=Font(size=14)
    city= CityInput.get()
    if city=="" or city=="Enter City":
           messagebox.showerror("Error","Enter City Name ");
    else:
           print(city)
           Searching=Label(frame,text="Searching.....",bg="blue",fg="orange",font=sf)
           Searching.place(x=250,y=500)
           Second(city)
       







###########################################################################
###########################################################################

              ########   FIRST     WINDOW   #########



root =Tk()
root.title("Weather")
todaydate=datetime.date.today();
my_font =Font(size=17)
datefont=Font(family="Courier",size=11)
font_type=Font(family="Courier",size=32)
root.geometry("600x600+400+90")
root.resizable(False,False)
frame = Frame(root,width="600",height="600",bg="blue")
frame.pack()

canvas = Canvas(frame,width=600,height=200,bg="orange")
canvas.place(x=0,y=0)

canvas.create_oval(100,100,300,300,fill="yellow",outline="white")
datelabel=Label(frame,text="Date : " + str(todaydate),font=datefont,bg="blue",fg="orange")
t1=Label(frame,text="City Weather",font=font_type,bg="blue",fg="orange")
CityInput=Entry(frame,width="50",bd=4)
CityInput.insert(0,"Enter City")
CityInput.place(x=150,y=400)

OkButton=Button(frame,text="SEARCH",bg="blue",command=info,width="30",bd=4,fg="orange")
OkButton.place(x=190,y=430)

datelabel.place(x=420,y=210)
t1.place(x=140,y=300)


root.mainloop()

########################################################
    ############## First Function Call ################

