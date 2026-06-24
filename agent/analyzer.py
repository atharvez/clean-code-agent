import os

def get_python_files(repo_path):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))
    return files


def analyze_repo(repo_path):
    files = get_python_files(repo_path)
    return "\n".join(files[:10])
# update: 2026-06-10 08:51:53.076295

# update: 2026-06-12 09:01:27.023651

# update: 2026-06-13 08:23:54.849045

# update: 2026-06-14 08:42:44.287247

# update: 2026-06-15 10:56:20.260322

# update: 2026-06-16 10:12:11.527099

# update: 2026-06-17 09:52:24.201454

# update: 2026-06-18 09:18:09.153752

# update: 2026-06-19 09:46:20.381980

# update: 2026-06-20 08:23:11.649535

# update: 2026-06-21 08:58:22.304428

# update: 2026-06-22 10:42:52.972093

# update: 2026-06-23 08:31:04.859445

# update: 2026-06-24 08:24:28.503753
