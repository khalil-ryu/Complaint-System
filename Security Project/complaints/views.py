from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm
from .models import Complaint, cipher_suite
from cryptography.fernet import Fernet
from accounts.models import UserProfile 

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user

            # Encrypt the title and description
            complaint.encrypted_title = cipher_suite.encrypt(form.cleaned_data['title'].encode())
            complaint.encrypted_description = cipher_suite.encrypt(form.cleaned_data['description'].encode())

            complaint.save()
            return redirect('profile')
    else:
        form = ComplaintForm()

    return render(request, 'complain/submit_complaint.html', {'form': form})

@login_required
def list_complaints(request):
    is_responsible = request.user.userprofile.is_responsible

    # Query complaints based on user role
    if is_responsible:
        complaints = Complaint.objects.all()
    else:
        complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'complain/list_complaints.html', {'complaints': complaints})

@login_required
def view_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, user=request.user) 
    return render(request, 'complain/view_complaint.html', {'complaint': complaint})
