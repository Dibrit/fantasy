from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings


def buy_send_mail(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            "Ваш игрок успешно продан",
            "Деньги зачисленны",
            settings.EMAIL_HOST_USER,
            [user.email]
        )
    except UserModel.DoesNotExist:
        print('User does not exist')


def sell_post_send_mail(user_id):
     UserModel = get_user_model()
     try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            "Ваш игрок выставлен на продажу",
            "Если вы не выстовляли игрока на продажу , обратитесь к техподержке",
            settings.EMAIL_HOST_USER,
            [user.email]
        )
     except UserModel.DoesNotExist:
         print('User does not exist')