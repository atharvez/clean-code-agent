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

# update: 2026-05-25 08:59:32.161199

# update: 2026-05-26 08:34:31.776340

# update: 2026-05-27 08:39:56.640821

# update: 2026-05-28 08:44:23.714116

# update: 2026-05-29 08:44:00.887277

# update: 2026-05-30 07:42:35.463620

# update: 2026-05-31 08:16:45.707332

# update: 2026-06-01 10:23:50.640476

# update: 2026-06-02 09:11:25.016487

# update: 2026-06-03 09:54:36.947543

# update: 2026-06-04 08:52:25.275545

# update: 2026-06-05 08:44:26.739772

# update: 2026-06-06 07:47:56.175600

# update: 2026-06-07 08:25:57.522213

# update: 2026-06-08 09:25:57.806251

# update: 2026-06-09 08:32:08.825041

# update: 2026-06-10 08:51:53.095896

# update: 2026-06-11 09:14:20.547888

# update: 2026-06-12 09:01:27.041313

# update: 2026-06-13 08:23:54.868614

# update: 2026-06-14 08:42:44.307071

# update: 2026-06-15 10:56:20.275629

# update: 2026-06-16 10:12:11.546543

# update: 2026-06-17 09:52:24.220713

# update: 2026-06-18 09:18:09.168178

# update: 2026-06-19 09:46:20.400960

# update: 2026-06-20 08:23:11.668223

# update: 2026-06-21 08:58:22.324382

# update: 2026-06-22 10:42:52.994869

# update: 2026-06-23 08:31:04.878369

# update: 2026-06-24 08:24:28.523682

# update: 2026-06-25 08:24:57.846408

# update: 2026-06-26 08:31:46.987532

# update: 2026-06-27 07:51:40.483238

# update: 2026-06-28 08:24:04.805496

# update: 2026-06-29 09:50:48.248926

# update: 2026-06-30 08:32:05.285206

# update: 2026-07-01 08:50:38.611239

# update: 2026-07-02 08:13:25.988419

# update: 2026-07-03 08:12:30.510446

# update: 2026-07-04 07:49:44.207938

# update: 2026-07-05 08:04:33.305414

# update: 2026-07-06 09:01:52.442199
