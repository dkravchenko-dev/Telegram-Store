import os
import re
import shutil


async def move_configs(source_dir: str, type_file: str, id_telegram: int, count: int = 2):
    dest_dir = os.path.join(source_dir, str(id_telegram))
    os.makedirs(dest_dir, exist_ok=True)

    def extract_number(filename):
        match = re.match(r"(\d+)", filename)
        return int(match.group(1)) if match else float('inf')

    conf_files = sorted(
        [f for f in os.listdir(source_dir)
         if f.endswith(type_file) and os.path.isfile(os.path.join(source_dir, f))],
        key=extract_number
    )

    files_to_move = conf_files[:count]

    for filename in files_to_move:
        src_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        shutil.move(src_path, dest_path)
