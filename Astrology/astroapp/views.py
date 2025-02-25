from django.shortcuts import render
import datetime,random
# Create your views here.
def home_view(request):
    time = datetime.datetime.now()
    hr = time.hour
    if hr > 12:
        s = 'Morning'
    elif hr > 16:
        s = "Afternoon"
    elif hr > 21:
        s = "Evening"
    else:
        s = "Night"
    name_list = ["Kiara ","Rashmika","Tamannah","Sonam Bajwa","Kashish","Sonal","Jennifer","Dakota","Shradha"]
    candidate_list = ["SANDEEP","Yashif","Monu","sahil","Ishaan","Yash","Shivam","Parteek","Kartik"]
    msg_list = ["Don't drink water drink beer",
           "Today is best day to pupose your crush",
           "Scroll reels before sleep",
           "Work is workship",
           "Better to smoke",
           "Tomorrow is best day for study"]
    name = random.choice(name_list)
    candidate = random.choice(candidate_list)
    msg = random.choice(msg_list)
    my_dict = {"name":name,"candidate":candidate,"msg":msg,"wish":s,"time":time}
    return render(request,'index.html',my_dict)