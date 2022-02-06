from django.shortcuts import render

def marksheet(request):
    if request.method=='POST':
        Math = int(request.POST.get('subject1'))
        English = int(request.POST.get('subject2'))
        Science = int(request.POST.get('subject3'))
        History = int(request.POST.get('subject4'))
        Geography = int(request.POST.get('subject5'))
        Total = (Math + English + Science + History + Geography)
        Percentage = Total*100/500
        print(Math)

        if Percentage >= 80:
            grade = 'O Grade'
        elif Percentage >= 65:
            grade = 'A Grade'
        elif Percentage >= 50:
            grade = 'B Grade'
        elif Percentage >= 35:
            grade = 'C Grade'
        else:
            grade = 'FAIL'

        data = {
            's1': Math,
            's2': English,
            's3': Science,
            's4': History,
            's5': Geography,
            'total' :Total,
            'percentage' : Percentage,
            'grade' : grade
        }
        return render (request,'marksheet.html',data)
    return render (request,'marksheet.html')
