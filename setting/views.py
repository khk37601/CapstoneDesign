from django.shortcuts import render
from .index import menu3
from .index import menu1
from .index import meun1_1

key = ''
date_s = ''
date_e = ''
flag = False
good = 0
bad = 0
# 날짜.
date = None
# 검색량.
value = None

def index(request):
    return render(request, 'blog/index.html')


def crawling(request):
    global key, date_s, date_e, flag
    if request.method == "POST":
        flag = False
        key = request.POST['userKeyword']
        date = request.POST['userDate']
        date = date.split('-')
        date_s = date[0]
        date_e = '2019.' + date[1]
    return render(request, 'blog/crawling.html')


def index1(request):
    global key, date_s, date_e, flag, good, bad, date, value
    if not flag:
        menu = menu3.menu3(key, '0', date_s, date_e)
        menu.main()
        date, value = meun1_1.google_trend(key)
        good = 0
        bad = 0
        flag = True
        bad, good = menu1.Crawling().Crawling_run_naver(date_s, date_e, key, '0')



    return render(request, 'blog/index1.html')


def index2(request):
    global good, bad, date, value, key
    return render(request, 'blog/index2.html', {'good': good, 'bad': bad, 'value': value, 'key': key, 'date': date})


def index3(request):
    return render(request, 'blog/index3.html')
