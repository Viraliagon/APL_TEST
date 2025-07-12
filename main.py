from flask import Flask, request, render_template_string
import io
import sys
import simplipyja_parser
import semanticAnalyzer

# OPTIONAL: Handle missing llm gracefully
try:
    import llm
    llm_available = True
except ImportError:
    llm_available = False

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SimpliPy-Ja Online IDE</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', 'Roboto', sans-serif;
            background: linear-gradient(to right, #e3f2fd, #ffffff);
            color: #333;
        }
        .header {
            background: #2196f3;
            color: white;
            padding: 16px 24px;
            font-size: 1.5rem;
            font-weight: bold;
            text-shadow: 1px 1px #1976d2;
        }
        .container {
            display: flex;
            height: calc(100vh - 64px);
        }
        .editor, .right {
            flex: 1;
            display: flex;
            flex-direction: column;
            margin: 12px;
            border-radius: 10px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
            overflow: hidden;
            background: #fff;
        }
        .tabs {
            background: #e3f2fd;
            color: #0d47a1;
            padding: 10px 16px;
            font-weight: bold;
            border-bottom: 1px solid #90caf9;
        }
        textarea {
            flex: 1;
            width: 100%;
            border: none;
            resize: none;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            padding: 14px;
            outline: none;
            background: #f9f9f9;
            color: #333;
        }
        .output {
            flex: 1;
            background: #212121;
            color: #f1f1f1;
            padding: 16px;
            overflow-y: auto;
            font-family: monospace;
        }
        .controls {
            padding: 12px;
            background: #f0f0f0;
            text-align: right;
            border-top: 1px solid #ddd;
        }
        button {
            background: #4caf50;
            color: white;
            border: none;
            padding: 10px 18px;
            font-size: 14px;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: #388e3c;
        }
        strong {
            color: #fbc02d;
        }
    </style>
</head>

<body>
    <div class="header">SimpliPy-Ja: Learning IDE for Students</div>
    <form method="POST">
        <div class="container">
            <div class="editor">
                <div class="tabs">📝 Write Your Code Below</div>
                <textarea name="code" placeholder="e.g:\nbegin\n     mek name = \"SimpliPy\"\n     fling(\"Hello, \" + name + \"!\")\ndone">{{ code }}</textarea>
                <ul id="suggestions" style="position: absolute; background: white; border: 1px solid #ccc; list-style: none; padding: 0; margin: 0; display: none; z-index: 10;"></ul>
                <div class="controls">
                    <button type="submit">Run Code ▶️</button>
                </div>
            </div>
            <div class="right">
                <div class="tabs">📤 Output & Feedback</div>
                <div class="output">
                    {% if output %}
                        {{ output.replace('\\n', '<br>')|safe }}
                    {% endif %}
                    {% if explanation %}
                        <br><br><strong>🤖 AI Explanation:</strong><br>
                        {{ explanation.replace('\\n', '<br>')|safe }}
                    {% endif %}
                </div>
            </div>
        </div>
    </form>

<script>
window.onload = function () {
    const keywords = [
        "begin", "done", "mek", "set", "fling",
        "if", "else", "for", "to", "=", "+", "-", "*", "/", "%"
    ];

    const textarea = document.querySelector('textarea');
    const suggestions = document.getElementById('suggestions');

    textarea.addEventListener('input', () => {
        const text = textarea.value;
        const lastWord = text.split(/\\s+/).pop().toLowerCase();

        const matches = keywords.filter(k => k.startsWith(lastWord) && lastWord !== '');

        suggestions.innerHTML = '';
        if (matches.length > 0) {
            matches.forEach(word => {
                const li = document.createElement('li');
                li.textContent = word;
                li.style.padding = '4px 8px';
                li.style.cursor = 'pointer';
                li.addEventListener('click', () => {
                    const words = textarea.value.split(/\\s+/);
                    words.pop();
                    words.push(word);
                    textarea.value = words.join(' ') + ' ';
                    suggestions.style.display = 'none';
                });
                suggestions.appendChild(li);
            });

            const rect = textarea.getBoundingClientRect();
            suggestions.style.left = rect.left + 'px';
            suggestions.style.top = (rect.top + textarea.offsetHeight) + 'px';
            suggestions.style.display = 'block';
        } else {
            suggestions.style.display = 'none';
        }
    });

    document.addEventListener('click', (e) => {
        if (e.target !== textarea) {
            suggestions.style.display = 'none';
        }
    });
};
</script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    output = ""
    explanation = ""

    if request.method == "POST":
        code = request.form.get("code", "")
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect print()

        try:
            semanticAnalyzer.reset_scope()
            simplipyja_parser.parser.parse(code)

            print("\nFinal Variables:")
            for var, val in semanticAnalyzer.symbol_table.items():
                print(f"{var} = {val}")

            if llm_available:
                explanation = llm.explain_code(code)
            else:
                explanation = "LLM module not available."

        except Exception as e:
            print(f"Error: {e}")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

    return render_template_string(HTML_TEMPLATE, code=code, output=output, explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
