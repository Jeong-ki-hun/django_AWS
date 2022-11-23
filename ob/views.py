from django.shortcuts import render
from django.http import Http404
from .models import Question, ShopList, SeoulTable, streetTable, ObResttable
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator

def index(request):
    latest_question_list = streetTable.objects.order_by('id')[:1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'ob/index_5.html', context)

def shop_list(request):
    if request.method=="POST":
        searched = request.POST['search']
        data = ObResttable.objects.filter(name__contains=searched)
        page = request.POST.get('page', '1')
        paginator = Paginator(data, '10')
        page_obj = paginator.page(page)
        return render(request, 'ob/index_3.html', {'page_obj' : page_obj})
    data = ObResttable.objects.all()
    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(data, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'ob/index_3.html', {'page_obj' : page_obj})

def map(request):
    with open('static/json/file_name.json', encoding='utf-8') as json_file:
        js = json.load(json_file)
        js = js['data']
        seoul_t = []
    for i in js:
        content = {
                "title":i['식당명'],
                "mapx": str(i['식당경도']),
                "mapy": str(i['식당위도']),
            }
        seoul_t.append(content)

    seoul = json.dumps(seoul_t, ensure_ascii=False)
    return render(request,'ob/map.html',{'seoul':seoul})

def Dashborad(request):
    rest = streetTable.objects.all().order_by('-id')
    standard_row = streetTable.objects.all().order_by('-id').first()
    standard_time = standard_row.time
    
    year = int(standard_time[:4])
    month = int(standard_time[6:8])
    day = int(standard_time[10:12])

    # 시간별 혼잡도 추이
    line_count_list = []
    line_label_list = []
    target_hour = 0
    while target_hour <= 23:
        count_list = []
        line = streetTable.objects.filter(time__contains = f"{year}년_{month}월_{day}일_{target_hour}시")
        line_label_list.append(f"{target_hour}시")
        
        for i in line:
            count_list.append(int(i.count)) # 1시간동안 모든 count data

        line_count_list.append(round(sum(count_list)/len(count_list),2)) # 1시간 평균 count data
        
        target_hour += 1
    
    
    # 일별 혼잡도 추이 ( 현재는 2일 기준 )
    bar_count_list = []
    bar_label_list = []
    target_day = day
    for rows in range(2): # 원하는 범위로 설정하기
        count_list = []
        bar = streetTable.objects.filter(time__contains = f"{year}년_{month}월_{target_day}일")
        bar_label_list.append(f"{target_day}일")

        for i in bar:
            count_list.append(int(i.count)) # 하루 동안 모든 count data
        bar_count_list.append(round(sum(count_list)/len(count_list),2)) # 하루 평균 count data

        if target_day == 1 and month in (1,3,5,7,8,10,12): 
            target_day = 31
        elif target_day == 1 and month in (4,6,9,11) :
            target_day = 30
        elif target_day == 1 and month == 2 :
            target_day = 29
        else:
            target_day = target_day-1

    context = {
        'rest' : rest, 
        'standard_row':standard_row,
        'standard_time':standard_time,
        'line_count_list':line_count_list,
        'line_label_list':line_label_list,
        'bar_count_list':bar_count_list,
        'bar_label_list':bar_label_list 
    }
    return render(request,'ob/Dash/dashboard.html',context)

