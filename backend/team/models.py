from django.db import models


class Member(models.Model):
    TEAM_NAME = [
    ('StepTech', 'StepTech'),
    ('StepMark', 'StepMark'),
    ('StepPro', 'StepPro'),
    ('StepCon', 'StepCon'),
    ('StepMan', 'StepMan'),
    ]

    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200, choices=TEAM_NAME, default='StepTech')
    description = models.TextField()
    image = models.ImageField(upload_to='team/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
