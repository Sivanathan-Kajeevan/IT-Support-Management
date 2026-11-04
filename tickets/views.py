from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from .models import Ticket
from .forms import RegisterForm, TicketForm, TicketUpdateForm


# ==========================================
# USER REGISTRATION
# ==========================================

def register_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# ==========================================
# EMPLOYEE DASHBOARD
# ==========================================

@login_required
def dashboard(request):

    if request.user.is_staff:
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(
            created_by=request.user
        )

    context = {
        'tickets': tickets.order_by('-created_at'),
        'total_tickets': tickets.count(),
        'open_tickets': tickets.filter(
            status='Open'
        ).count(),
        'resolved_tickets': tickets.filter(
            status='Resolved'
        ).count(),
    }

    return render(request, 'dashboard.html', context)


# ==========================================
# CREATE SUPPORT TICKET
# ==========================================

@login_required
def create_ticket(request):

    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()

            return redirect('dashboard')
    else:
        form = TicketForm()

    return render(
        request,
        'create_ticket.html',
        {'form': form}
    )


# ==========================================
# VIEW TICKET DETAILS
# ==========================================

@login_required
def ticket_detail(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    if not request.user.is_staff and ticket.created_by != request.user:
        raise PermissionDenied

    return render(
        request,
        'ticket_detail.html',
        {'ticket': ticket}
    )


# ==========================================
# ADMIN DASHBOARD
# ==========================================

@staff_member_required(login_url='login')
def admin_dashboard(request):

    tickets = Ticket.objects.select_related(
        'created_by'
    ).all()

    # Dashboard statistics
    total_tickets = tickets.count()

    open_tickets = tickets.filter(
        status='Open'
    ).count()

    progress_tickets = tickets.filter(
        status='In Progress'
    ).count()

    resolved_tickets = tickets.filter(
        status='Resolved'
    ).count()

    # Search and filter
    search = request.GET.get('search', '').strip()
    status_filter = request.GET.get('status', '')

    if search:
        tickets = tickets.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(created_by__username__icontains=search)
        )

    if status_filter in ['Open', 'In Progress', 'Resolved']:
        tickets = tickets.filter(
            status=status_filter
        )

    context = {
        'tickets': tickets.order_by('-created_at'),
        'total_tickets': total_tickets,
        'open_tickets': open_tickets,
        'progress_tickets': progress_tickets,
        'resolved_tickets': resolved_tickets,
        'search': search,
        'status_filter': status_filter,
    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )


# ==========================================
# ADMIN UPDATE TICKET
# ==========================================

@staff_member_required(login_url='login')
def update_ticket(request, ticket_id):

    ticket = get_object_or_404(
        Ticket,
        id=ticket_id
    )

    if request.method == 'POST':

        form = TicketUpdateForm(
            request.POST,
            instance=ticket
        )

        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')

    else:
        form = TicketUpdateForm(
            instance=ticket
        )

    return render(
        request,
        'update_ticket.html',
        {
            'form': form,
            'ticket': ticket
        }
    )