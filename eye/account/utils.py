from datetime import datetime
from os.path import splitext

def user_avatar_upload_path(model, filename):
    return f'{model.username}/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/{splitext(filename)[1]}'