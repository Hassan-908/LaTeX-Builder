import os
import subprocess
import tempfile
from django.http import HttpResponse, HttpResponseServerError

def render_tex(request):
    # 1. Absolute path to this app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))

    # 2. Absolute path to resume.tex
    tex_path = os.path.join(app_dir, "resume.tex")

    # 3. Absolute path to pdflatex.exe (IMPORTANT on Windows)
    PDFLATEX = r"C:\Users\Hassan\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"

    if not os.path.exists(tex_path):
        return HttpResponseServerError(f"resume.tex not found at {tex_path}")

    with open(tex_path, "r", encoding="utf-8") as f:
        tex_content = f.read()

    with tempfile.TemporaryDirectory() as tmp:
        temp_tex = os.path.join(tmp, "resume.tex")

        with open(temp_tex, "w", encoding="utf-8") as f:
            f.write(tex_content)

        try:
            subprocess.run(
                [
                    PDFLATEX,
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "resume.tex",
                ],
                cwd=tmp,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=30,
                check=True,
            )

        except subprocess.CalledProcessError as e:
            return HttpResponseServerError(
                e.stdout.decode() + "\n" + e.stderr.decode()
            )

        pdf_path = os.path.join(tmp, "resume.pdf")

        with open(pdf_path, "rb") as pdf:
            return HttpResponse(pdf.read(), content_type="application/pdf")
