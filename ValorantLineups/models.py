from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from myLineups import settings


class Agent(models.Model):
    ROLE = (
        ('Controller', 'Controllers'),
        ('Duelist', 'Duelists'),
        ('Initiator', 'Initiators'),
        ('Sentinel', 'Sentinel')
    )

    RACE = (
        ('Human', 'Human'),
        ('Radiant', 'Radiant'),
        ('Cybernetic', 'Cybernetic')
    )

    name = models.CharField(max_length=30, unique=True)
    role = models.CharField(null=True, max_length=30, choices=ROLE)
    race = models.CharField(null=True, max_length=30, choices=RACE)
    image = models.ImageField(upload_to='static/agents')
    card_image = models.ImageField(upload_to='static/agents', default=image)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return self.name


# class Role(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name


class Map(models.Model):
    PARTS = (
        ('a b', 'A, B'),
        ('a b c', 'A, B, C'),
    )

    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='static/maps')
    part = models.CharField(max_length=50, choices=PARTS)

    def __str__(self):
        return self.name


class Ability(models.Model):
    default_ability = 'Select an ability'
    ABILITY = (
        ('q', 'ability_1'),
        ('e', 'ability_2'),
        ('c', 'ability_3'),
        ('x', 'ability_4')
    )
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='static/abilities')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    ability = models.CharField(max_length=50, choices=ABILITY, default=default_ability)

    def __str__(self):
        return f"{self.agent}, {self.name}"


class Video(models.Model):
    PART = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )
    TYPE = (
        ('Setup', 'Setup'),
        ('Lineup', 'Lineup'),
        ('Mechanics', 'Mechanics'),
    )

    url = models.CharField(max_length=254)

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    part = models.CharField(null=True, choices=PART, max_length=10)
    type = models.CharField(null=True, choices=TYPE, max_length=50)

    def youtube_id(self):
        return self.url.split('watch?v=')[-1]  # ultimu

    def __str__(self):
        return f"{self.agent}, {self.ability}, {self.map}"


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    attach = models.FileField(upload_to='static/attachemts', null=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.title}, {self.attach}"


class FavoritesVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


@receiver(post_save, sender=ContactRequest)
def contact_request_save(sender, instance, created, *args, **kwargs):
    if created:
        send_mail('New contact request', f'Contact requested: {instance}', settings.EMAIL_HOST_USER,
                  [settings.EMAIL_HOST_USER])
        #
        # subject = 'New contact request'
        # html_body = render_to_string("message_body.html", {'contact_request': instance})
        #
        # msg = EmailMultiAlternatives(subject=subject, from_email=settings.EMAIL_HOST_USER,
        #                              to=[settings.EMAIL_HOST_USER], body='text')
        # msg.attach_alternative(html_body, "text/html")
        # msg.send()
