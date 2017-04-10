# coding: utf-8


from datetime import datetime

from django.db.models import Q

from models import Panel


def panels(request):
    user = request.user
    groups = user.groups.all()
    path = request.path if request.path != '/' else 'home page'
    now = datetime.now()

    final_panels = set()

    panels = Panel.objects.filter(visible=True).filter(Q(end_date__gt=now) | Q(end_date__isnull=True))

    for p in panels:
        if p.urls_denorm == None:
            p.urls_denorm = ''
        url_paths = [x.strip() for x in p.urls_denorm.split(',') if x.strip()]

        if not url_paths or any(x in path for x in url_paths):
            if not p.groups.all():
                final_panels.add(p)
                continue

            if set(p.groups.all()).intersection(set(groups)) or user.is_superuser:
                final_panels.add(p)

    return {'panels': final_panels}
