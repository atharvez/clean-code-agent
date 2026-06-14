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
