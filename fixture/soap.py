from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_projects_list(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        project_list = []
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for element in projects:
                project_list.append(Project(name=element.name, id=element.id))
            return project_list
        except WebFault:
            return False
