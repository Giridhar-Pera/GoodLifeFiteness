from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def bfcal(request):
    # return HttpResponse('Hello info page')
    return render(request, 'bfcalnew.html')


def bfcalResults(request):
    context = {}
    requestData = request.POST

    if requestData:
        data = getUserInformation(requestData)
        print(data)
        name = data['name']
        email = data['email']
        gender = data['gender']
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])

        bmi = getBMI(height, weight)
        context['bmi'] = bmi
        print(bmi)
        if gender == 'male':
            bodyfat = (1.20 * bmi) + (0.23 * age) - 16.2
        else:
            bodyfat = (1.20 * bmi) + (0.23 * age) - 5.4

        context['bodyFat'] = round(bodyfat, 2)
        context['name'] = name

        print(context)

    return render(request, 'bfcalResult.html', context)


def getUserInformation(requestData):
    data = {'name': requestData.get('customer_name'), 'email': requestData.get('email_address'),
            'gender': requestData.get('gender'), 'height': requestData.get('customer_height'),
            'weight': requestData.get('customer_weight'), 'age': requestData.get('customer_age')}

    return data


def getBMI(height, weight):
    squareHeight = height * height
    calculation = weight / squareHeight

    return round(calculation * 703, 2)
