import os
import pyminizip

def zip_folder_with_password(folder_path, zip_path, password, compression_level=5):
    files = []
    relative_paths = []

    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, os.path.dirname(folder_path))
            files.append(full_path)
            relative_paths.append(relative_path)

    pyminizip.compress_multiple(
        files,
        relative_paths,
        zip_path,
        password,
        compression_level
    )

    return zip_path

