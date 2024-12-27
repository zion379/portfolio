from enum import Enum

class proj_content_type(Enum):
    VIDEO = "video"
    IMAGE = "img"
    TEXT = "text"
    GIF = "gif"
    GROUP = "group"
    CAROUSEL = "carousel"
    MODEL = "model"
    PDF = "pdf"

class content_position(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class proj_content_obj:
    def __init__(self, content_type: proj_content_type, text_content: str = None, content_url: str = None, position: content_position = content_position.CENTER):
        self.content_type:proj_content_type = content_type
        self.text_content: str = text_content
        self.content_url: str = content_url
        self.position: content_position = position

class Carousel_Item:
    def __init__(self, content_url: str, desc: str):
        self.content_url = content_url
        self.desc = desc
class Carousel_obj(proj_content_obj):
    def __init__(self, content_title: str, position: content_position = content_position.CENTER):
        self.position: content_position = position
        self.content_type: proj_content_type = proj_content_type.CAROUSEL
        self.carousel_items: list[Carousel_Item] = [] # carousel content lives here.
        self.content_title: str = content_title

    def add_item(self, new_item:Carousel_Item):
        self.carousel_items.append(new_item)

class Project_obj:
    def __init__(self, project_name: str, project_desc: str, project_date: str = None, thumbnail_src: str = None):
        self.project_name = project_name
        self.project_desc = project_desc
        self.project_date = project_date
        self.thumbnail_src = thumbnail_src
        self.project_content: list = []

    def add_content(self, proj_content: proj_content_obj):
        self.project_content.append(proj_content)

class Content_group:
    def __init__(self, heading: str = None):
        self.group_contents: list[proj_content_obj] = []
        self.content_type = proj_content_type.GROUP
        self.heading = heading
    
    def add_content(self, new_content: proj_content_obj):
        self.group_contents.append(new_content)