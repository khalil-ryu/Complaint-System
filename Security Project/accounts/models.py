from django.contrib.auth.models import User
from django.db import models
from cryptography.fernet import Fernet

JOB_POSITIONS = [
    ('architect', 'Architecte Logiciel'),
    ('functional_analyst', 'Analyste Fonctionnel'),
    ('mission_leader', 'Chef de Mission'),
    ('project_manager', 'Chef de Projet'),
    ('developer', 'Développeur'),
    ('tester', 'Testeur'),
    ('app_maintenance', 'Maintenance Applicative'),
    ('project_specialist', 'Spécialiste en Gestion de Projet'),
]

GRADES = [
    ('senior_engineer', 'Ingénieur Principal'),
    ('lead_engineer', 'Ingénieur Major'),
    ('junior_engineer', 'Ingénieur Junior'),
    ('technician', 'Technicien'),
    # ... add all other grades here
]
key = Fernet.generate_key()

class UserProfile(models.Model):
    is_responsible = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    job_position = models.CharField(max_length=50, choices=JOB_POSITIONS)
    grade = models.CharField(max_length=50, choices=GRADES)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def __str__(self):
        return self.user.username