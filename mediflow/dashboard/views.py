from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patient_mgmt.models import Patient, Department
from staff_mgmt.models import Bed
from alert_mgmt.models import Alert
from alert_mgmt.utils import check_and_create_alerts
import json

@login_required
def dashboard(request):
    check_and_create_alerts()
    patients = Patient.objects.all()
    beds = Bed.objects.all()
    alerts = Alert.objects.filter(is_resolved=False).order_by("-created_at")[:5]
    departments = Department.objects.all()
    zone_data = {
        "red": patients.filter(zone="red").count(),
        "yellow": patients.filter(zone="yellow").count(),
        "green": patients.filter(zone="green").count(),
    }
    bed_data = {
        "clean": beds.filter(status="clean").count(),
        "occupied": beds.filter(status="occupied").count(),
        "dirty": beds.filter(status="dirty").count(),
    }
    context = {
        "patients": patients,
        "beds": beds,
        "alerts": alerts,
        "departments": departments,
        "total_patients": patients.count(),
        "waiting": patients.filter(status="waiting").count(),
        "red_zone": patients.filter(zone="red").count(),
        "clean_beds": beds.filter(status="clean").count(),
        "zone_data": json.dumps(zone_data),
        "bed_data": json.dumps(bed_data),
        "bed_data_raw": bed_data,
        "dept_names": json.dumps([d.name for d in departments]),
        "dept_queues": json.dumps([d.queue_count for d in departments]),
        "dept_waits": json.dumps([d.avg_wait_time for d in departments]),
    }
    return render(request, "dashboard/index.html", context)
