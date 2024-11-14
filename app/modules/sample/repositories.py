from app.modules.sample.models import Sample
from core.repositories.BaseRepository import BaseRepository


class SampleRepository(BaseRepository):
    def __init__(self):
        super().__init__(Sample)
