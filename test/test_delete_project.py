from model.project import Project
import random


def test_delete_project(app):
    app.session.ensure_login("administrator", "root")
    if len(app.project.get_projects_list()) == 0:
        app.project.create_new_project(Project(name="Abrakadabra"))
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_projects_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
