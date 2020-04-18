from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .resources import CustomEntryResource

import requests
from cryptography.fernet import Fernet
import json

def customentry_csv(request, gender):
    entries = CustomEntryResource()
    query = CustomEntry.objects.filter(gender=gender, submitted = True)
    dataset = entries.export(query)
    return HttpResponse(dataset.csv)
    return dataset.csv


def clue(request, techid):
    techid = techid.upper()
    winners  = Winner.objects.all()
    for winner in winners:
        if winner.half1.technexid == techid or winner.half2.technexid == techid:
            winnerid = winner.id
            if request.method == "POST":
                clue_id = request.POST['clueid']
                if clue_id == "1":
                    if winner.clue1 == True:
                        msg = "Clue answer already submitted. Wait for the next clue, till then stay Technexed!"
                        return render(request, 'form_already_submitted.html', {'msg':msg})
                    else:
                        winner.clue1 = True
                elif clue_id == "2":
                    if winner.clue2 == True:
                        msg = "Clue answer already submitted. Wait for the next clue, till then stay Technexed!"
                        return render(request, 'form_already_submitted.html', {'msg':msg})
                    else:
                        winner.clue2 = True
                elif clue_id == "3":
                    if winner.clue3 == True:
                        msg = "Clue answer already submitted. Wait for the next clue, till then stay Technexed!"
                        return render(request, 'form_already_submitted.html', {'msg':msg})
                    else:
                        winner.clue3 = True  
                elif clue_id == "4":
                    if winner.clue4 == True:
                        msg = "Clue answer already submitted. Wait for the next clue, till then stay Technexed!"
                        return render(request, 'form_already_submitted.html', {'msg':msg})
                    else:
                        winner.clue4 = True  
                elif clue_id == "5":
                    if winner.clue5 == True:
                        msg = "Clue answer already submitted. Wait for the next clue, till then stay Technexed!"
                        return render(request, 'form_already_submitted.html', {'msg':msg})
                    else:
                        winner.clue5 = True
                elif clue_id == "6":
                    if winner.clue6 == True:
                        msg = "Clue answer already submitted. Wait for the next clue, till then stay Technexed!"
                        return render(request, 'form_already_submitted.html', {'msg':msg})
                    else:
                        winner.clue6 = True
                elif clue_id == "7":
                    if winner.clue7 == True:
                        msg = "Clue answer already submitted. Wait for the next clue, till then stay Technexed!"
                        return render(request, 'form_already_submitted.html', {'msg':msg})
                    else:
                        winner.clue7 = True
                
                winner.save()

                user_answer = request.POST['user_answer']
                answer = Answer(
                    clue = Clue.objects.get(id=clue_id),
                    source = winner,
                    label = user_answer
                )
                answer.save()
                msg = "Answer recorded. Now wait for the next question, till then stay technexed!"
                return render(request, 'form_already_submitted.html', {'msg':msg})
            else:
                clues = Clue.objects.all()
                return render(request, 'clue.html', {
                    'winnerid':winnerid,
                    'techid':techid,
                    'clues':clues
                })
    else:
        msg = "Sorry we were unable to find your tech other half :-("    ### msg need to be changed
        return render(request, 'form_already_submitted.html', {'msg':msg})

def entry(request, techid, winnerid):
    pass


def index(request, techid):
    return redirect('clue', techid=techid)
    techid = techid.upper()
    if techid[0:4] == "TX20" or techid[0:4] == "tx20":
        url = "https://api.technex.co.in/profile/" + techid[4:]
        payload = {}
        headers = {
        'Authorization': 'Token 74dc29f6a4191f4671140a4213aed6da69fa0d48'
        }
        response = requests.request("GET", url, headers=headers, data = payload) 
        try:
            entry = Entry.objects.get(technexid=techid)
            if entry.submitted == True:
                msg = "You can fill the form only once."
                return render(request, 'form_already_submitted.html', {'msg': msg})
        except:
            pass
        try:
            r = json.loads(response.text)
            print(r)
            gender = "Other"
            if r['gender']==0:
                gender = "Male"
            elif r['gender']==1:
                gender = "Female"
            entry = Entry(
                technexid = techid,
                name = r['name'],
                year = r['year'],
                gender = gender
            )
            entry.save()
            customentry = CustomEntry(
                technexid = techid,
                name = r['name'],
                year = r['year'],
                gender = gender
            )
            customentry.save()
            user = Participant(
                technexid = techid,
                name = r['name'],
                gender = gender,
                year = r['year'],
                college = r['college'],
                email = r['email'],
                phone = r['phone'],
                city = r['city']
            )
            user.save()
            print(entry.technexid)
        except:
            msg = "Invalid Technex ID"
            return render(request, 'form_already_submitted.html', {'msg': msg})
        #key = b'yGdG7zJ1XNB5BpHnlPDH3cBXSvWbcEw2AEjSg90XGQg='   ##
        #cipher_suit = Fernet(key)                               ##
        #tid = techid.encode('utf-8')                            ## 
        #cipher_text = cipher_suit.encrypt(tid)                  ##
        #token = cipher_text.decode('utf-8')                     ##
        #request.session['token'] = techid

        if entry.submitted == False:
            return render(request, 'index.html', {'techid': techid})
            return redirect('home', techid=techid)
        else:
            msg = "You can fill the form only once."
            return render(request, 'form_already_submitted.html', {'msg': msg})
    else:
        msg = "Invalid Technex ID"
        return render(request, 'form_already_submitted.html', {'msg': msg})
        return render(request, 'verify.html', {'msg': msg})               
    return render(request, 'index.html')

def tandc(request, techid):
    techid = techid.upper()
    try:
        entry = Entry.objects.get(technexid=techid)
        if entry.submitted == True:
            msg = "You can fill the form only once."
            return render(request, 'form_already_submitted.html', {'msg': msg})
    except:
        pass
    return render(request, 'tandc.html', {'techid': techid})

def about(request, techid):
    techid = techid.upper()
    try:
        entry = Entry.objects.get(technexid=techid)
        if entry.submitted == True:
            msg = "You can fill the form only once."
            return render(request, 'form_already_submitted.html', {'msg': msg})
    except:
        pass
    return render(request, 'about.html', {'techid': techid})

def end(request):
    return render(request, 'end.html')

def form(request, key):
    key = key.upper()
    #try:
    #key = b'yGdG7zJ1XNB5BpHnlPDH3cBXSvWbcEw2AEjSg90XGQg='   ##
    #cipher_suit = Fernet(key)                               ##
    #tok = token.encode('utf-8')                             ## 
    #cipher_text = cipher_suit.decrypt(tok)                  ##
    #key = cipher_text.decode('utf-8')                       ##
    #print(key)
    #try:
    #if request.session['token'] == key:
    #    print('session token successfully readed')
    try:
        entry = Entry.objects.get(technexid=key)
        if entry.submitted == True:
            msg = "You can fill the form only once."
            return render(request, 'form_already_submitted.html', {'msg': msg})
    except:
        pass
    if request.method == "POST":
        customentry = CustomEntry.objects.get(technexid=key)
        customentry.ques1 = request.POST['ques1']
        customentry.ques2 = request.POST['ques2']
        customentry.ques3 = request.POST['ques3']
        customentry.ques4 = request.POST['ques4']
        customentry.ques5 = request.POST['ques5']
        customentry.ques6 = request.POST['ques6']
        customentry.ques7 = request.POST['ques7']
        customentry.ques8 = request.POST['ques8']
        customentry.ques9 = request.POST['ques9']
        customentry.ques10 = request.POST['ques10']
        customentry.ques11 = request.POST['ques11']
        customentry.ques12 = request.POST['ques12']
        customentry.ques13 = request.POST['ques13']
        customentry.ques14 = request.POST['ques14']
        customentry.ques15 = request.POST['ques15']
        customentry.ques16 = request.POST['ques16']
        customentry.ques17 = request.POST['ques17']
        customentry.ques18 = request.POST['ques18']
        customentry.ques19 = request.POST['ques19']
        customentry.ques20 = request.POST['ques20']
        customentry.ques21 = request.POST['ques21']
        customentry.ques22 = request.POST['ques22']
        customentry.ques23 = request.POST['ques23']
        customentry.ques24 = request.POST['ques24']
        customentry.ques25 = request.POST['ques25']
        customentry.ques26 = request.POST['ques26']
        customentry.ques27 = request.POST['ques27']
        customentry.ques28 = request.POST['ques28']
        customentry.ques29 = request.POST['ques29']
        customentry.ques30 = request.POST['ques30']
        customentry.submitted = True
        customentry.save()

        entry = Entry.objects.get(technexid=key)

        q1 = Question.objects.get(qid='ques1')
        answercode = request.POST['ques1']
        if answercode == '1' :
            entry.ques1 = q1.option1
        elif answercode == '2':
            entry.ques1 = q1.option2
        elif answercode == '3':
            entry.ques1 = q1.option3
        elif answercode == '4':
            entry.ques1 = q1.option4
        elif answercode == '5':
            entry.ques1 = q1.option5
        else:
            entry.ques1 = "X"

        q1 = Question.objects.get(qid='ques2')
        answercode = request.POST['ques2']
        if answercode == '1' :
            entry.ques2 = q1.option1
        elif answercode == '2':
            entry.ques2 = q1.option2
        elif answercode == '3':
            entry.ques2 = q1.option3
        elif answercode == '4':
            entry.ques2 = q1.option4
        elif answercode == '5':
            entry.ques2 = q1.option5
        else:
            entry.ques2 = "X"
        
        q1 = Question.objects.get(qid='ques3')
        answercode = request.POST['ques3']
        if answercode == '1' :
            entry.ques3 = q1.option1
        elif answercode == '2':
            entry.ques3 = q1.option2
        elif answercode == '3':
            entry.ques3 = q1.option3
        elif answercode == '4':
            entry.ques3 = q1.option4
        elif answercode == '5':
            entry.ques3 = q1.option5
        else:
            entry.ques3 = "X"
        
        q1 = Question.objects.get(qid='ques4')
        answercode = request.POST['ques4']
        if answercode == '1' :
            entry.ques4 = q1.option1
        elif answercode == '2':
            entry.ques4 = q1.option2
        elif answercode == '3':
            entry.ques4 = q1.option3
        elif answercode == '4':
            entry.ques4 = q1.option4
        elif answercode == '5':
            entry.ques4 = q1.option5
        else:
            entry.ques4 = "X"
        
        q1 = Question.objects.get(qid='ques5')
        answercode = request.POST['ques5']
        if answercode == '1' :
            entry.ques5 = q1.option1
        elif answercode == '2':
            entry.ques5 = q1.option2
        elif answercode == '3':
            entry.ques5 = q1.option3
        elif answercode == '4':
            entry.ques5 = q1.option4
        elif answercode == '5':
            entry.ques5 = q1.option5
        else:
            entry.ques5 = "X"
        
        q1 = Question.objects.get(qid='ques6')
        answercode = request.POST['ques6']
        if answercode == '1' :
            entry.ques6 = q1.option1
        elif answercode == '2':
            entry.ques6 = q1.option2
        elif answercode == '3':
            entry.ques6 = q1.option3
        elif answercode == '4':
            entry.ques6 = q1.option4
        elif answercode == '5':
            entry.ques6 = q1.option5
        else:
            entry.ques6 = "X"
        
        q1 = Question.objects.get(qid='ques7')
        answercode = request.POST['ques7']
        if answercode == '1' :
            entry.ques7 = q1.option1
        elif answercode == '2':
            entry.ques7 = q1.option2
        elif answercode == '3':
            entry.ques7 = q1.option3
        elif answercode == '4':
            entry.ques7 = q1.option4
        elif answercode == '5':
            entry.ques7 = q1.option5
        else:
            entry.ques7 = "X"
        
        q1 = Question.objects.get(qid='ques8')
        answercode = request.POST['ques8']
        if answercode == '1' :
            entry.ques8 = q1.option1
        elif answercode == '2':
            entry.ques8 = q1.option2
        elif answercode == '3':
            entry.ques8 = q1.option3
        elif answercode == '4':
            entry.ques8 = q1.option4
        elif answercode == '5':
            entry.ques8 = q1.option5
        else:
            entry.ques8 = "X"
        
        q1 = Question.objects.get(qid='ques9')
        answercode = request.POST['ques9']
        if answercode == '1' :
            entry.ques9 = q1.option1
        elif answercode == '2':
            entry.ques9 = q1.option2
        elif answercode == '3':
            entry.ques9 = q1.option3
        elif answercode == '4':
            entry.ques9 = q1.option4
        elif answercode == '5':
            entry.ques9 = q1.option5
        else:
            entry.ques9 = "X"
        
        q1 = Question.objects.get(qid='ques10')
        answercode = request.POST['ques10']
        if answercode == '1' :
            entry.ques10 = q1.option1
        elif answercode == '2':
            entry.ques10 = q1.option2
        elif answercode == '3':
            entry.ques10 = q1.option3
        elif answercode == '4':
            entry.ques10 = q1.option4
        elif answercode == '5':
            entry.ques10 = q1.option5
        else:
            entry.ques10 = "X"
        
        q1 = Question.objects.get(qid='ques11')
        answercode = request.POST['ques11']
        if answercode == '1' :
            entry.ques11 = q1.option1
        elif answercode == '2':
            entry.ques11 = q1.option2
        elif answercode == '3':
            entry.ques11 = q1.option3
        elif answercode == '4':
            entry.ques11 = q1.option4
        elif answercode == '5':
            entry.ques11 = q1.option5
        else:
            entry.ques11 = "X"
        
        q1 = Question.objects.get(qid='ques12')
        answercode = request.POST['ques12']
        if answercode == '1' :
            entry.ques12 = q1.option1
        elif answercode == '2':
            entry.ques12 = q1.option2
        elif answercode == '3':
            entry.ques12 = q1.option3
        elif answercode == '4':
            entry.ques12 = q1.option4
        elif answercode == '5':
            entry.ques12 = q1.option5
        else:
            entry.ques12 = "X"
        
        q1 = Question.objects.get(qid='ques13')
        answercode = request.POST['ques13']
        if answercode == '1' :
            entry.ques13 = q1.option1
        elif answercode == '2':
            entry.ques13 = q1.option2
        elif answercode == '3':
            entry.ques13 = q1.option3
        elif answercode == '4':
            entry.ques13 = q1.option4
        elif answercode == '5':
            entry.ques13 = q1.option5
        else:
            entry.ques13 = "X"
        
        q1 = Question.objects.get(qid='ques14')
        answercode = request.POST['ques14']
        if answercode == '1' :
            entry.ques14 = q1.option1
        elif answercode == '2':
            entry.ques14 = q1.option2
        elif answercode == '3':
            entry.ques14 = q1.option3
        elif answercode == '4':
            entry.ques14 = q1.option4
        elif answercode == '5':
            entry.ques14 = q1.option5
        else:
            entry.ques14 = "X"
        
        q1 = Question.objects.get(qid='ques15')
        answercode = request.POST['ques15']
        if answercode == '1' :
            entry.ques15 = q1.option1
        elif answercode == '2':
            entry.ques15 = q1.option2
        elif answercode == '3':
            entry.ques15 = q1.option3
        elif answercode == '4':
            entry.ques15 = q1.option4
        elif answercode == '5':
            entry.ques15 = q1.option5
        else:
            entry.ques15 = "X"
        
        q1 = Question.objects.get(qid='ques16')
        answercode = request.POST['ques16']
        if answercode == '1' :
            entry.ques16 = q1.option1
        elif answercode == '2':
            entry.ques16 = q1.option2
        elif answercode == '3':
            entry.ques16 = q1.option3
        else:
            entry.ques16 = "X"
        
        q1 = Question.objects.get(qid='ques17')
        answercode = request.POST['ques17']
        if answercode == '1' :
            entry.ques17 = q1.option1
        elif answercode == '2':
            entry.ques17 = q1.option2
        elif answercode == '3':
            entry.ques17 = q1.option3
        else:
            entry.ques17 = "X"
        
        q1 = Question.objects.get(qid='ques18')
        answercode = request.POST['ques18']
        if answercode == '1' :
            entry.ques18 = q1.option1
        elif answercode == '2':
            entry.ques18 = q1.option2
        elif answercode == '3':
            entry.ques18 = q1.option3
        else:
            entry.ques18 = "X"
        
        q1 = Question.objects.get(qid='ques19')
        answercode = request.POST['ques19']
        if answercode == '1' :
            entry.ques19 = q1.option1
        elif answercode == '2':
            entry.ques19 = q1.option2
        elif answercode == '3':
            entry.ques19 = q1.option3
        else:
            entry.ques19 = "X"
        
        q1 = Question.objects.get(qid='ques20')
        answercode = request.POST['ques20']
        if answercode == '1' :
            entry.ques20 = q1.option1
        elif answercode == '2':
            entry.ques20 = q1.option2
        elif answercode == '3':
            entry.ques20 = q1.option3
        else:
            entry.ques20 = "X"
        
        q1 = Question.objects.get(qid='ques21')
        answercode = request.POST['ques21']
        if answercode == '1' :
            entry.ques21 = q1.option1
        elif answercode == '2':
            entry.ques21 = q1.option2
        elif answercode == '3':
            entry.ques21 = q1.option3
        else:
            entry.ques21 = "X"
        
        q1 = Question.objects.get(qid='ques22')
        answercode = request.POST['ques22']
        if answercode == '1' :
            entry.ques22 = q1.option1
        elif answercode == '2':
            entry.ques22 = q1.option2
        elif answercode == '3':
            entry.ques22 = q1.option3
        else:
            entry.ques22 = "X"
        
        q1 = Question.objects.get(qid='ques23')
        answercode = request.POST['ques23']
        if answercode == '1' :
            entry.ques23 = q1.option1
        elif answercode == '2':
            entry.ques23 = q1.option2
        elif answercode == '3':
            entry.ques23 = q1.option3
        else:
            entry.ques23 = "X"
        
        q1 = Question.objects.get(qid='ques24')
        answercode = request.POST['ques24']
        if answercode == '1' :
            entry.ques24 = q1.option1
        elif answercode == '2':
            entry.ques24 = q1.option2
        elif answercode == '3':
            entry.ques24 = q1.option3
        else:
            entry.ques24 = "X"
        
        q1 = Question.objects.get(qid='ques25')
        answercode = request.POST['ques25']
        if answercode == '1' :
            entry.ques25 = q1.option1
        elif answercode == '2':
            entry.ques25 = q1.option2
        elif answercode == '3':
            entry.ques25 = q1.option3
        else:
            entry.ques25 = "X"
        
        q1 = Question.objects.get(qid='ques26')
        answercode = request.POST['ques26']
        if answercode == '1' :
            entry.ques26 = q1.option1
        elif answercode == '2':
            entry.ques26 = q1.option2
        elif answercode == '3':
            entry.ques26 = q1.option3
        else:
            entry.ques26 = "X"
        
        q1 = Question.objects.get(qid='ques27')
        answercode = request.POST['ques27']
        if answercode == '1' :
            entry.ques27 = q1.option1
        elif answercode == '2':
            entry.ques27 = q1.option2
        elif answercode == '3':
            entry.ques27 = q1.option3
        else:
            entry.ques27 = "X"
        
        q1 = Question.objects.get(qid='ques28')
        answercode = request.POST['ques28']
        if answercode == '1' :
            entry.ques28 = q1.option1
        elif answercode == '2':
            entry.ques28 = q1.option2
        elif answercode == '3':
            entry.ques28 = q1.option3
        else:
            entry.ques28 = "X"
        
        q1 = Question.objects.get(qid='ques29')
        answercode = request.POST['ques29']
        if answercode == '1' :
            entry.ques29 = q1.option1
        elif answercode == '2':
            entry.ques29 = q1.option2
        elif answercode == '3':
            entry.ques29 = q1.option3
        else:
            entry.ques29 = "X"
        
        q1 = Question.objects.get(qid='ques30')
        answercode = request.POST['ques30']
        if answercode == '1' :
            entry.ques30 = q1.option1
        elif answercode == '2':
            entry.ques30 = q1.option2
        elif answercode == '3':
            entry.ques30 = q1.option3
        else:
            entry.ques30 = "X"
        
        entry.submitted = True
        entry.save()

        #
        #  SUCCESS PAGE 
        #
        return redirect('end')
        return HttpResponse('entry success')
    else:
        questions = Question.objects.filter(qtype__exact="mcq").order_by('qid')
        rpquestions = Question.objects.filter(qtype__exact="rapidfire").order_by('qid')
        total = len(questions)+len(rpquestions)
        return render(request, 'form.html', {'questions': questions,'rpquestions':rpquestions ,'total':total})
    #else:
        #return HttpResponse('good try, stay_technexed')
        #except:
        #    return redirect('index')
    #except:
    #    return redirect('index')
    
def verification(request):
    if request.method == "POST":
        #try:
        techid = str(request.POST['technexid'])
        if techid[0:4] == "TX20" or techid[0:4] == "tx20":
            url = "https://api.technex.co.in/profile/" + techid[4:]
            payload = {}
            headers = {
            'Authorization': 'Token 74dc29f6a4191f4671140a4213aed6da69fa0d48'
            }
            response = requests.request("GET", url, headers=headers, data = payload)
            try:
                r = json.loads(response.text)
                print(r)
                gender = "Other"
                if r['gender']==0:
                    gender = "Male"
                elif r['gender']==1:
                    gender = "Female"
                entry = Entry(
                    technexid = techid,
                    name = r['name'],
                    year = r['year'],
                    gender = gender
                )
                entry.save()
                customentry = CustomEntry(
                    technexid = techid,
                    name = r['name'],
                    year = r['year'],
                    gender = gender
                )
                customentry.save()
                user = Participant(
                    technexid = techid,
                    name = r['name'],
                    gender = gender,
                    year = r['year'],
                    college = r['college'],
                    email = r['email'],
                    phone = r['phone'],
                    city = r['city']
                )
                user.save()
                print(entry.technexid)
            except:
                msg = "Invalid Technex ID"
                return render(request, 'verify.html', {'msg': msg})
            key = b'yGdG7zJ1XNB5BpHnlPDH3cBXSvWbcEw2AEjSg90XGQg='   ##
            cipher_suit = Fernet(key)                               ##
            tid = techid.encode('utf-8')                            ## 
            cipher_text = cipher_suit.encrypt(tid)                  ##
            token = cipher_text.decode('utf-8')                     ##
            request.session['token'] = techid

            if entry.submitted == False:
                return redirect('form', token=token)
            else:
                return render(request, 'form_already_submitted.html')
        else:
            msg = "Invalid Technex ID"
            return render(request, 'verify.html', {'msg': msg})                
        #except:
        #    return HttpResponse('Error in POST part of verification view')
    else:
        return render(request, 'verify.html')


def test_form(request):
    return HttpResponse('models questions changed so this view is temporarily unavailable')
    if request.method == "POST":
        print(request.POST['hello'])
        entry = Questions.objects.none()
        entry = Questions(
            name = request.POST['name'],
            age = request.POST['age'],
            gender = request.POST['gender']
        )
        entry.save()
        return HttpResponse('test entry success')
    else:
        return render(request, 'test_form.html')