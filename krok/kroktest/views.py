from django.shortcuts import render, HttpResponse
from models import *
from random import *


def random_question(request):
    quest_query = Question.objects.all()
    quest_num = randint(0, len(quest_query))
    quest = quest_query[quest_num]
    answers = ['A', 'B', 'C', 'D', 'E']
    shuffle(answers)
    var = {}
    var['A'] = quest.ansA
    var['B'] = quest.ansB
    var['C'] = quest.ansC
    var['D'] = quest.ansD
    var['E'] = quest.ansE
    variants = []
    for i in answers:
        variants.append(var[i])
    print quest.question
    print answers
    print var['A']
    return render(request, "random.html", {'quest': quest,
                                           'answers': answers,
                                           'variants': variants})


def rnd(request):
    quest_query = Question.objects.all().order_by('id')
    quest_numbers = range(len(quest_query))
    shuffle(quest_numbers)
    quest = [0 for i in range(20)]
    answers = []
    variants = []
    print quest_numbers
    for i in range(20):
        quest[i] = quest_query[quest_numbers[i]]
        ans = ['A', 'B', 'C', 'D', 'E']
        shuffle(ans)
        answers.extend(ans)
        var = {}
        var['A'] = quest[i].ansA
        var['B'] = quest[i].ansB
        var['C'] = quest[i].ansC
        var['D'] = quest[i].ansD
        var['E'] = quest[i].ansE
        for a in ans:
            variants.append(var[a])
    return render(request, "random.html", {'quest': quest,
                                           'quest_numbers': quest_numbers,
                                           'answers': answers,
                                           'variants': variants})


def results(request):
    if request.method == 'POST':
        quest_query = Question.objects.all().order_by('id')
        quest_numbers = [0 for i in range(20)]
        quest = [0 for i in range(20)]
        usrans = [0 for i in range(20)]
        postdata = request.POST
        for i in range(20):
            s = postdata[str(i)]
            q, ans = s.split('_')
            quest_numbers[i] = (quest_query[int(q)].id)
            quest[i] = quest_query[quest_numbers[i]-1]
            var = {}
            var['A'] = quest[i].ansA
            var['B'] = quest[i].ansB
            var['C'] = quest[i].ansC
            var['D'] = quest[i].ansD
            var['E'] = quest[i].ansE
            usrans[i] = var[ans]
            if ans == 'A':
                quest[i].answered = True
                quest[i].save()
            print s, i, quest_numbers[i], usrans[i]

    return render(request, "results.html", {'quest': quest,
                                            'usrans': usrans,
                                            'quest_numbers': quest_numbers})


def home(request):
    if request.method == 'POST':
        postdata = request.POST
        print postdata
        for i in postdata:
            if i != 'csrfmiddlewaretoken':
                quest_query = Question.objects.get(pk=int(i))
                quest_query.checked = True
                quest_query.save()
    return render(request, "home.html")


def checked(request):
    quest_query = Question.objects.filter(checked=True)
    return render(request, "checked.html", {'quest_query': quest_query})
