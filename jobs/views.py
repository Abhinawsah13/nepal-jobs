
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Job


def job_list(request):
    query = request.GET.get('q', '')
    job_type = request.GET.get('job_type', '')

    jobs = Job.objects.all().order_by('-created_at')

    # Search by title, company, or location
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query)
            | Q(company__icontains=query)
            | Q(location__icontains=query)
        )

    # Filter by job type
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    return render(
        request,
        'jobs/job_list.html',
        {
            'jobs': jobs,
            'query': query,
            'selected_job_type': job_type,
        }
    )


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)

    return render(
        request,
        'jobs/job_detail.html',
        {'job': job}
    )
