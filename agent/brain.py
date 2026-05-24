from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_plan(repo_summary):
    prompt = f"""
    You are an AI developer.

    Repo:
    {repo_summary}

    Give ONE simple improvement idea.
    Keep it under 10 words.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print("Gemini failed:", e)
        return "Minor code cleanup"
# update: 2026-05-16 07:18:03.273584

# update: 2026-05-17 07:34:22.621833

# update: 2026-05-18 08:47:23.388296

# update: 2026-05-19 08:30:10.018891

# update: 2026-05-20 08:28:08.955607

# update: 2026-05-21 08:35:36.217434

# update: 2026-05-22 08:23:26.927946

# update: 2026-05-23 07:33:26.188622

# update: 2026-05-24 07:50:39.577898
