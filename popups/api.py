from django.http import HttpResponse

def hide_popup(request):
    """Store the information to hide the popup in the session."""
    popup = request.POST.get("popup", None)
    if popup is None:
        return HttpResponse("0")
    request.session["popups_" + popup] = False
    return HttpResponse("1")
