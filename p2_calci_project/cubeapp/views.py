from django.shortcuts import render

def cube(request):
    if request.method == "POST":
        try:
            num = float(request.POST.get("num"))
            cube_value = num ** 3
            msg = f"Cube of {num} is {round(cube_value, 2)}"
        except (TypeError, ValueError):
            msg = "Please enter a valid number."
            num = None
        return render(request, "cube.html", {"msg":msg, "num":num})
    else:
        return render(request, "cube.html")
