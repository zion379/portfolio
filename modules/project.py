from enum import Enum

class proj_content_type(Enum):
    VIDEO = "video"
    IMAGE = "img"
    TEXT = "text"
    GIF = "gif"

class proj_content_obj:
    def __init__(self, content_type: proj_content_type, text_content: str = None, content_url: str = None):
        self.content_type = content_type
        self.text_content = text_content
        self.content_url = content_url

class Project_obj:
    def __init__(self, project_name: str, project_desc: str):
        self.project_name = project_name
        self.project_desc = project_desc
        self.project_content: list = []

    def add_content(self, proj_content: proj_content_obj):
        self.project_content.append(proj_content)