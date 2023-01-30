from .models import Theme

def theme(request):
    if request.user.is_authenticated:
        try:
            theme = Theme.objects.get(user=request.user)
        except:
            theme = None
        if not theme:
            theme = Theme(user=request.user)
            theme.save()
        theme = theme.theme
    else:
        theme = 'Light'
    return {'theme': theme}