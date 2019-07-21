from django.shortcuts import render
from django.http import HttpResponse

def index(request):
        return render(request,'index.html')

def prediction(request):
   if request.method == "POST":
        Itching = int(request.POST['Itching'])
        SkinRash = int(request.POST['SkinRash'])
        NodalSkinEruptions = int(request.POST['NodalSkinEruptions'])
        ContinuousSneezing = int(request.POST['ContinuousSneezing'])
        Shivering = int(request.POST['Shivering'])
        Chills = int(request.POST['Chills'])
        JointPain = int(request.POST['JointPain'])
        StomachPain = int(request.POST['StomachPain'])
        Acidity = int(request.POST['Acidity'])
        UlcersOnTongue = int(request.POST['UlcersOnTongue'])
        MuscleWasting = int(request.POST['MuscleWasting'])
        Vomiting = int(request.POST['Vomiting'])
        BurningMicturition = int(request.POST['BurningMicturition'])
        SpottingUrination = int(request.POST['SpottingUrination'])
        Fatigue = int(request.POST['Fatigue'])
        WeightGain = int(request.POST['WeightGain'])
        Anxiety = int(request.POST['Anxiety'])
        ColdHandsAndFeet = int(request.POST['ColdHandsAndFeet'])
        MoodSwings = int(request.POST['MoodSwings'])
        WeightLoss = int(request.POST['WeightLoss'])
        Restlessness = int(request.POST['Restlessness'])
        Lethargy = int(request.POST['Lethargy'])
        PatchesInThroat = int(request.POST['PatchesInThroat'])
        IregularSugarLevel = int(request.POST['IregularSugarLevel'])
        Cough = int(request.POST['Cough'])
        HighFever = int(request.POST['HighFever'])
        SunkenEyes = int(request.POST['SunkenEyes'])
        Breathlessness = int(request.POST['Breathlessness'])
        Sweating = int(request.POST['Sweating'])
        Dehydration = int(request.POST['Dehydration'])
        Indigestion = int(request.POST['Indigestion'])
        Headache = int(request.POST['Headache'])
        YellowishSkin = int(request.POST['YellowishSkin'])
        DarkUrine = int(request.POST['DarkUrine'])
        Nausea = int(request.POST['Nausea'])
        LossOfAppetite = int(request.POST['LossOfAppetite'])
        PainBehindEyes = int(request.POST['PainBehindEyes'])
        BackPain = int(request.POST['BackPain'])
        Constipation = int(request.POST['Constipation'])
        AbdominalPain = int(request.POST['AbdominalPain'])
        Diarrhoea = int(request.POST['Diarrhoea'])
        MildFever = int(request.POST['MildFever'])
        YellowUrine = int(request.POST['YellowUrine'])
        p=[[Itching, SkinRash, NodalSkinEruptions, ContinuousSneezing, Shivering,Chills, JointPain, StomachPain, Acidity, 
        UlcersOnTongue, MuscleWasting, Vomiting, BurningMicturition, SpottingUrination, Fatigue,WeightGain, Anxiety,
        ColdHandsAndFeet, MoodSwings, WeightLoss, Restlessness, Lethargy, PatchesInThroat, IregularSugarLevel, Cough, HighFever,
        SunkenEyes, Breathlessness, Sweating, Dehydration, Indigestion, Headache, YellowishSkin, DarkUrine, Nausea, LossOfAppetite,
        PainBehindEyes, BackPain, Constipation, AbdominalPain, Diarrhoea, MildFever, YellowUrine]]
        res= makePredictions(p)
        return render(request,'result.html',{"result":res})
   else:
        return render(request,'index.html')


def makePredictions(p):
    import pandas as pd
    import pickle
    try:
        predictor = pickle.load(open('C:/Users/Anil Adhikari/Desktop/medico/SVM_Model.sav','rb'))
    except:
        print("File is not loaded")
    result = predictor.predict(p)
    print(result)
    return result