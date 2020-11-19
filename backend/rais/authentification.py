from rais.models import User, Post


def authenticate_user_token(request):
    if 'token' in request.COOKIES:
        if len(request.COOKIES['token']) != 0:
            user = None
            try:
                user = User.objects.get(token=request.COOKIES['token'])
            except User.DoesNotExist:
                return False
            else:
                return True
        else:
            return False
    else:
        return False


def authenticate_user_password(request):
    user = None
    try:
        user = User.objects.get(email=request.POST['email'])
    # Если пользователя с такой почтой не существует
    except User.DoesNotExist:
        return False
    else:
        # Если пароль введён верно
        if user.password == request.POST['password']:
            return True
        else:
            return False
