from django.shortcuts import render

def square(request):
    if request.method == "POST":
        num = float(request.POST.get("num"))
        sqr = num ** 2
        msg = "square = " + str(round(sqr, 2))
        return render(request, "square.html", {"msg": msg, "num": num})
    else:
        return render(request, "square.html")

