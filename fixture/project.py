from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill project form
        wd.find_element_by_name("name").send_keys(project.name)
        if project.status is not None:
            Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("inherit_global").click()
        if project.description is not None:
            wd.find_element_by_name("description").send_keys(project.description)
        # accept creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def get_projects_list(self):
        wd = self.app.wd
        self.open_projects_page()
        table = wd.find_elements_by_tag_name("table")
        tr = table[2].find_elements_by_tag_name("tr")[2:]
        project_list = []
        for element in tr:
            a = element.find_element_by_tag_name("a")
            name = a.text
            id = a.get_attribute('href').split('=')[1]
            project_list.append(Project(name=name, id=id))
        return list(project_list)

    def delete_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//a[contains(text(),'%s')]" % project.name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
