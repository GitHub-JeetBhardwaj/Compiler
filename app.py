import os
import sys
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

# Store code separately for each language
code_storage = {
    "python": "",
    "cpp": "",
    "java": ""
}

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    error = ""
    language = request.form.get("language", "python")  # Default language

    if request.method == "POST":
        code = request.form.get("code", "")  # Get code
        code_storage[language] = code  # Store code for selected language

        filename = ""
        try:
            if language == "python":
                filename = "temp.py"
                with open(filename, "w") as f:
                    f.write(code)
                result = subprocess.run([sys.executable, filename], capture_output=True, text=True, timeout=5)

            elif language == "cpp":
                filename = "temp.cpp"
                executable = "temp_exe"
                with open(filename, "w") as f:
                    f.write(code)

                compile_process = subprocess.run(["g++", filename, "-o", executable], capture_output=True, text=True)
                if compile_process.returncode == 0:
                    result = subprocess.run([f"./{executable}"], capture_output=True, text=True, timeout=5)
                else:
                    result = compile_process

            elif language == "java":
                filename = "Main.java"
                with open(filename, "w") as f:
                    f.write(code)

                compile_process = subprocess.run(["javac", filename], capture_output=True, text=True)
                if compile_process.returncode == 0:
                    result = subprocess.run(["java", "Main"], capture_output=True, text=True, timeout=5)
                else:
                    result = compile_process

            if result.returncode != 0:
                error = result.stderr
            else:
                output = result.stdout

        except subprocess.TimeoutExpired:
            error = "Execution timed out. Please optimize your code."
        except Exception as e:
            error = str(e)
        finally:
            cleanup_files(["temp.py", "temp.cpp", "temp_exe", "Main.java", "Main.class"])

    return render_template("index.html", output=output, error=error, language=language, code=code_storage[language])


def cleanup_files(file_list):
    """
    Removes temporary files created during execution if they exist.
    """
    for file in file_list:
        if os.path.exists(file):
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error deleting file {file}: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
