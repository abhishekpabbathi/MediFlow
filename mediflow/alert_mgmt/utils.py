from patient_mgmt.models import Patient
from .models import Alert

def check_and_create_alerts():
    patients = Patient.objects.filter(status='waiting')
    for patient in patients:
        if patient.wait_time > 30:
            already_exists = Alert.objects.filter(
                patient_name=patient.name,
                is_resolved=False
            ).exists()
            if not already_exists:
                Alert.objects.create(
                    message=f"{patient.name} has been waiting {patient.wait_time} minutes in {patient.department}!",
                    level='critical',
                    patient_name=patient.name
                )
        elif patient.wait_time > 15:
            already_exists = Alert.objects.filter(
                patient_name=patient.name,
                is_resolved=False
            ).exists()
            if not already_exists:
                Alert.objects.create(
                    message=f"{patient.name} waiting {patient.wait_time} minutes in {patient.department}.",
                    level='warning',
                    patient_name=patient.name
                )
