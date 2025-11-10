def update_incident_status(instance, new_status):
    instance.status = new_status
    instance.save()
    return instance
