from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from core.document_parser import parse_input
from core.semantic_engine import build_graph

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_documents():
    try:
        # Route to parsing engine (handles both text and PDFs)
        doc1 = parse_input(request, prefix='orig')
        doc2 = parse_input(request, prefix='mod')

        if not doc1 or not doc2:
            return jsonify({'error': 'Insufficient data provided for analysis.'}), 400

        # Route to semantic/agentic engine
        graph_payload = build_graph(doc1, doc2)
        return jsonify(graph_payload)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Helper function to grab correct form data depending on request type
def parse_input(request, prefix):
    file = request.files.get(f'{prefix}_pdf')
    
    # Check if a file was actually uploaded (filename is not empty)
    if file and file.filename != '':
        from core.document_parser import extract_text_from_pdf
        return extract_text_from_pdf(file.read())
        
    # If no valid file, fallback to the text area
    return request.form.get(f'{prefix}_text', '')
if __name__ == '__main__':
    print("VAPORTRACE Router Active. Awaiting payloads on port 5000.")
    app.run(debug=True, port=5000)