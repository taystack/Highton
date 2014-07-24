

class Tag:

    TYPE = 'tag'

    OPTIONAL_FIELDS = [
        'name',
    ]

    def __init__(
        self,
        highrise_id,
        name
    ):
        self.highrise_id = highrise_id.pyval
        self.name = name.pyval
