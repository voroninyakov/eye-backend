from os.path import splitext

def video_cover_upload_path(model, filename):
    return f'video_covers/{model.author.user.username}_{model.title}{splitext(filename)[1]}'

def video_file_upload_path(model, filename):
    return f'video_files/{model.author.user.username}_{model.title}{splitext(filename)[1]}'
