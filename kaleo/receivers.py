from django.db.models.signals import post_save
from django.dispatch import receiver

#from django.contrib.auth.models import User
from .compat import get_user_model
User = get_user_model()

from account.models import SignupCodeResult, EmailConfirmation
from account.signals import signup_code_used, email_confirmed, user_signed_up

from kaleo.models import JoinInvitation, InvitationStat


@receiver(signup_code_used, sender=SignupCodeResult)
def handle_signup_code_used(sender, **kwargs):
    result = kwargs.get("signup_code_result")
    try:
        invite = result.signup_code.joininvitation
        invite.accept(result.user)
    except JoinInvitation.DoesNotExist:
        pass


@receiver(email_confirmed, sender=EmailConfirmation)
def handle_email_confirmed(sender, **kwargs):
    email_address = kwargs.get("email_address")
    JoinInvitation.process_independent_joins(
        user=email_address.user,
        email=email_address.email
    )


@receiver(user_signed_up)
def handle_user_signup(sender, user, form, **kwargs):
    email_qs = user.emailaddress_set.filter(email=user.email, verified=True)
    if user.is_active and email_qs.exists():
        JoinInvitation.process_independent_joins(
            user=user,
            email=user.email
        )


@receiver(post_save, sender=User)
def create_stat(sender, instance=None, **kwargs):
    if instance is None:
        return
    InvitationStat.objects.get_or_create(user=instance)
