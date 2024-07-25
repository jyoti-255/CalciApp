from django.shortcuts import render

def sqrt(request):
    if request.method == "POST":
        try:
            num = float(request.POST.get("num"))
            sqrt_value = num ** 0.5
            msg = f"Square root of {num} is {round(sqrt_value, 2)}"
        except (TypeError, ValueError):
            msg = "Please enter a valid number."
            num = None
        return render(request, "sqrt.html", {"msg": msg, "num": num})
    else:
        return render(request, "sqrt.html")

