import re
import datetime
from dicttoxml import dicttoxml


def to_datetime(datetime_string):
    match = re.match(
        '^(.*)-(.*)-(.*)( |T)(.*):(.*):(.*)(\+|Z).*$', datetime_string)

    if match:
        return datetime.datetime(
            year=int(match.group(1)),
            month=int(match.group(2)),
            day=int(match.group(3)),
            hour=int(match.group(5)),
            minute=int(match.group(6)),
            second=int(match.group(7)),
        )
    else:
        return None


def to_date(date_string):
    match = re.match('^(.*)-(.*)-(.*)$', date_string)
    if match:
        return datetime.datetime(
            year=int(match.group(1)),
            month=int(match.group(2)),
            day=int(match.group(3)),
        ).date()


def prepare_obj(highrise_model):
    data = {}
    data['id'] = highrise_model.highrise_id
    for attr in type(highrise_model).OPTIONAL_FIELDS:
        if hasattr(highrise_model, attr.replace('-', '_')):
            data[attr] = getattr(highrise_model, attr.replace('-', '_'))

        elif hasattr(highrise_model, attr):
            data[attr] = getattr(highrise_model, attr)

    return data


def prepare_highrise_xml(obj_type, obj):
    data = {}
    data[obj_type] = obj
    data = dicttoxml(data, attr_type=False, root=False)
    return data
