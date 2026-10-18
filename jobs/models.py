from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    JOB_TYPES = [
        ('full', 'Full-time'),
        ('part', 'Part-time'),
        ('intern', 'Internship'),
    ]
    job_type = models.CharField(max_length=10, choices=JOB_TYPES, default='full')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title