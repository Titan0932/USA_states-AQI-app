from tkinter import *
import requests
import json

from requests import exceptions


root=Tk()
root.title("How's the weather?")
#root.configure(background='grey')            #the background colour of the window

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=87122&distance=25&API_KEY=CBCD9E1E-CAA5-4968-B88F-75AAFB5ADBFF

def enter_zip():
    
    zipcode=zip.get()

    try:
        api_request=requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=5&API_KEY=CBCD9E1E-CAA5-4968-B88F-75AAFB5ADBFF")
        api=json.loads(api_request.content)
        aqi=api[0]['AQI']
        location=api[0]['ReportingArea']
        quality=api[0]['Category']['Name']
        result='AQI: '+"  " + str(aqi) + " \t\t"+ quality.upper()

        if quality=='Good':
            colour='green'
        elif quality=='Moderate':
            colour='yellow'
        elif quality=='Unhealthy for Sensitive Groups':
            colour='orange'
        elif quality=='Unhealthy':
            colour='purple'
        elif quality=='Hazardous':
            colour='maroon'
        
        

        Label(root,text=location,font=('Helveica Bold',20)).pack(pady=5)
        my_label=Label(root,text=result,padx=5,pady=5,bg=colour,width=40,fg='grey',font=('Helveica Bold',20))
        my_label.pack()
    except Exception as e:
        result="ERROR! " + str(e)
        my_label=Label(root,text=result,padx=5,pady=5,width=40,fg='grey',font=('Helveica Bold',20))

    

    zip.delete(0,END)

def clear_screen():
    
    for label in root.pack_slaves():
        label.pack_forget()
    
    zip=Entry(root,text="Enter Zip Here:")
    zip.pack()
    submit=Button(root,text="Search",command=enter_zip).pack()
    clear=Button(root,text='CLEAR',command=clear_screen).pack()

    
zip=Entry(root,text="Enter Zip Here:")
zip.pack()
submit=Button(root,text="Search",command=enter_zip).pack()
clear=Button(root,text='CLEAR',command=clear_screen).pack()

root.mainloop()