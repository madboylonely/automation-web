g_reportRawData = []
g_status = False

class GlobalConstants:
    LOGGER = None
    LINK_DEMO_PAGE = None
    WAIT_EXPLICIT = None
    WAIT_IMPLICIT = None
    WEBDRIVER = None

class ReportRawDatas: 
    def __init__(self, desc, status):
        self.desc = desc
        self.status = status