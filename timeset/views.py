from django.shortcuts import render

def set_time(request):
    if request.method == "POST":
        # 이후 구현될 기능: 데이터 저장
        pass
    return render(request, 'timeset.html')