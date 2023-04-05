from django.db.models import QuerySet


class ProjectServiceQuerySet(QuerySet):
    def edit(self, project_service):
        service = self.filter(pk=project_service['id'])
        service.update(parcent=project_service['percent'][0], max_parcent=project_service['max_parcent'][0])
        service.first().user.clear()

        for user in project_service.get('username', []):
            service.first().user.add(user)

        return service[0]
