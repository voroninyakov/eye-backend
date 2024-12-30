from os.path import splitext

def user_avatar_upload_path(model, filename):
    return f'avatars/{model.username}{splitext(filename)[1]}'

def profile_cover_upload_path(model, filename):
    return f'covers/{model.user.username}{splitext(filename)[1]}'