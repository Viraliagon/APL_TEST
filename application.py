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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/theme/dracula.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/addon/hint/show-hint.min.css">
    <style>
        body { margin: 0; font-family: 'Segoe UI', sans-serif; display: flex; height: 100vh; background-color: #1e1e2f; color: #d4d4d4; }
        .sidebar { width: 220px; background: #202032; padding: 1rem; display: flex; flex-direction: column; justify-content: space-between; }
        .main { flex: 1; display: flex; flex-direction: column; }
        .topbar { background: #2e2e40; padding: 0.5rem 1rem; color: #ccc; font-weight: bold; }
        .tab-bar { display: flex; gap: 1rem; padding: 0.5rem 1rem; background: #2a2a3b; }
        .tab { color: #ddd; cursor: pointer; padding: 0.4rem 1rem; border-bottom: 2px solid transparent; }
        .tab.active { border-color: #8ab4f8; color: #8ab4f8; }
        .close-tab { color: red; margin-left: 8px; font-weight: bold; cursor: pointer; }
        .workspace { display: flex; flex: 1; }
        .editor, .right { width: 50%; display: flex; flex-direction: column; }
        .run-wrapper-fixed { background: #1e1e2f; padding: 0.75rem 1rem; display: flex; justify-content: space-between; border-top: 1px solid #333; }
        .run-btn { background-color: #22c55e; color: white; border: none; padding: 0.4rem 2rem; font-weight: bold; border-radius: 5px; cursor: pointer; }
        .upload-btn { background-color: #3b82f6; color: white; border: none; padding: 0.4rem 1rem; font-weight: bold; border-radius: 5px; cursor: pointer; }
        .output { background: #121217; color: #98c379; padding: 1rem; font-family: monospace; overflow-y: auto; }
        .output-title { background: #2a2a3b; padding: 0.5rem 1rem; font-weight: bold; }
        strong { color: #fbc02d; }
    </style>
</head>
<body>
    <div class="sidebar">
        <div>
            <h2>SimpliPy-Ja</h2>
            <button onclick="addNewTab()">+ New Tab</button>
        </div>
        <footer style="font-size: 0.8rem; color: #888; text-align: center;">&copy; 2025 SimpliPy-Ja</footer>
    </div>
    <div class="main">
        <div class="topbar" id="filename">main.simja</div>
        <div class="tab-bar" id="tabBar"></div>
        <form method="POST" enctype="multipart/form-data">
            <div class="workspace">
                <div class="editor" id="editorPanel"></div>
                <div class="right">
                    <div class="output-title">📤 Output & Feedback</div>
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
            <div class="run-wrapper-fixed">
                <input type="file" name="file" accept=".txt" class="upload-btn" onchange="loadFile(event)" />
                <button type="submit" class="run-btn">Run Code ▶️</button>
            </div>
            <textarea name="code" id="hiddenCode" style="display:none;"></textarea>
        </form>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/addon/hint/show-hint.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/addon/hint/anyword-hint.min.js"></script>

    <script>
        var tabCount = 0;
        var currentTab = 0;
        var editors = {};
        var tabNames = {};

        CodeMirror.registerHelper("hint", "simplipyja", function(editor) {
            const cursor = editor.getCursor();
            const token = editor.getTokenAt(cursor);
            const word = token.string;
            const start = token.start;
            const end = cursor.ch;

            const keywords = {
                "begin": "done",
                "f": "for i in range():\\n\\t",
                "fl": "fling ",
                "if": "if condition:\\n\\t",
                "while": "while condition:\\n\\t",
            };

            const list = [];
            for (const key in keywords) {
                if (key.startsWith(word)) {
                    list.push({
                        text: keywords[key],
                        displayText: key + " → " + keywords[key],
                        render: function(el, self, data) {
                            el.innerHTML = "<strong>" + data.displayText + "</strong>";
                        }
                    });
                }
            }

            return {
                list: list,
                from: CodeMirror.Pos(cursor.line, start),
                to: CodeMirror.Pos(cursor.line, end)
            };
        });

        function addNewTab() {
            var tabId = tabCount++;
            var tabName = tabId === 0 ? "main.simja" : "tab" + tabId + ".simja";
            tabNames[tabId] = tabName;

            var tab = document.createElement("div");
            tab.className = "tab";
            tab.id = "tab" + tabId;
            tab.innerHTML =
                "<span ondblclick='renameTab(" + tabId + ")'>" + tabName + "</span>" +
                "<span class='close-tab' onclick='closeTab(event, " + tabId + ")'>×</span>";
            tab.onclick = function () { switchTab(tabId); };
            document.getElementById("tabBar").appendChild(tab);

            var editorDiv = document.createElement("textarea");
            editorDiv.id = "codeArea" + tabId;
            document.getElementById("editorPanel").appendChild(editorDiv);

            var cm = CodeMirror.fromTextArea(editorDiv, {
                lineNumbers: true,
                mode: "python",
                theme: "dracula",
                extraKeys: { "Ctrl-Space": "autocomplete" },
                hintOptions: {
                    hint: CodeMirror.hint.simplipyja,
                    completeSingle: false
                }
            });

            cm.setSize("100%", "100%");
            cm.on("inputRead", function(cm, change) {
                const cur = cm.getCursor();
                const token = cm.getTokenAt(cur);
                const word = token.string;

                if (/^[a-zA-Z_]\w*$/.test(word)) {
                    CodeMirror.commands.autocomplete(cm, null, { completeSingle: false });
                }

                if (change.text[0] === " " || change.text[0] === "\\n") {
                    const line = cm.getLine(cur.line);
                    if (line.includes("begin") && !line.includes("done")) {
                        cm.replaceRange("\\n\\tdone", { line: cur.line + 1, ch: 0 });
                    }
                }
            });

            editors[tabId] = cm;
            switchTab(tabId);
        }

        function switchTab(tabId) {
            currentTab = tabId;
            document.querySelectorAll(".tab").forEach(tab => {
                tab.classList.toggle("active", tab.id === "tab" + tabId);
            });
            Object.keys(editors).forEach(id => {
                editors[id].getWrapperElement().style.display =
                    parseInt(id) === tabId ? "block" : "none";
            });
            document.getElementById("filename").innerText = tabNames[tabId];
        }

        function renameTab(tabId) {
            var newName = prompt("Rename this tab:", tabNames[tabId]);
            if (newName) {
                tabNames[tabId] = newName;
                var tab = document.getElementById("tab" + tabId);
                tab.querySelector("span").innerText = newName;
                switchTab(tabId);
            }
        }

        function closeTab(event, tabId) {
            event.stopPropagation();
            var tab = document.getElementById("tab" + tabId);
            var editor = editors[tabId]?.getWrapperElement();
            if (tab) tab.remove();
            if (editor) editor.remove();
            delete editors[tabId];
            delete tabNames[tabId];
            if (Object.keys(editors).length > 0) {
                switchTab(parseInt(Object.keys(editors)[0]));
            }
        }

        function loadFile(event) {
            const file = event.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                const content = e.target.result;
                editors[currentTab].setValue(content);
            };
            reader.readAsText(file);
        }

        window.onload = function () {
            addNewTab();
            editors[currentTab].setValue({{ code | tojson | safe }});
        };

        document.querySelector("form").addEventListener("submit", function () {
            const hidden = document.getElementById("hiddenCode");
            hidden.value = editors[currentTab].getValue();
        });
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
