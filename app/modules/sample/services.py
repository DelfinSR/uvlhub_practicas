from app.modules.sample.repositories import SampleRepository
from core.services.BaseService import BaseService


class SampleService(BaseService):
    def __init__(self):
        super().__init__(SampleRepository())
