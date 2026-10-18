
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Job


def job_list(request):
    query = request.GET.get('q', '')

    jobs = Job.objects.all().order_by('-created_at')

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query)
            | Q(company__icontains=query)
            | Q(location__icontains=query)
        )

    return render(
        request,
        'jobs/job_list.html',
        {'jobs': jobs, 'query': query}
    )


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)

    return render(
        request,
        'jobs/job_detail.html',
        {'job': job}
    )
