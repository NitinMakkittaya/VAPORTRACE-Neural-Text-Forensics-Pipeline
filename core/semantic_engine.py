from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from core.entity_engine import detect_entity_tampering
from core.reasoning_agent import generate_forensic_report

# Load lightweight model into memory once
model = SentenceTransformer('all-MiniLM-L6-v2')

def build_graph(doc1, doc2):
    paragraphs1 = [p.strip() for p in doc1.split('\n') if len(p.strip()) > 10]
    paragraphs2 = [p.strip() for p in doc2.split('\n') if len(p.strip()) > 10]

    embed1 = model.encode(paragraphs1) if paragraphs1 else []
    embed2 = model.encode(paragraphs2) if paragraphs2 else []

    nodes, edges = [], []

    # Map Original Document
    for i, p in enumerate(paragraphs1):
        nodes.append({
            "id": f"O_{i}", "label": f"Orig Para {i+1}", "title": p, "text_data": p,
            "color": {"background": "#1f1f1f", "border": "#555"}, "font": {"color": "#fff"}
        })

    # Map Modified Document & Run Forensics
    for j, p2 in enumerate(paragraphs2):
        bg_color, border_color, edge_label = "#1a4d2e", "#33ff77", "Unchanged"
        report = "Node structurally sound. No semantic anomalies detected."
        
        if len(embed1) > 0:
            similarities = cosine_similarity([embed2[j]], embed1)[0]
            best_match_idx = np.argmax(similarities)
            highest_sim = similarities[best_match_idx]
            orig_text = paragraphs1[best_match_idx]

            # Run Entity Tampering Check
            tampered_entities = detect_entity_tampering(orig_text, p2)

            # Failure Check: Vector drift OR Entity swapping
            if highest_sim < 0.96 or tampered_entities: 
                bg_color, border_color = "#4a0000", "#ff2a2a"
                edge_label = f"DRIFT: {100 - (highest_sim*100):.1f}%"
                report = generate_forensic_report(orig_text, p2, highest_sim, tampered_entities)
            
            edges.append({
                "from": f"O_{best_match_idx}", "to": f"M_{j}", "label": edge_label,
                "color": {"color": border_color}, "font": {"color": border_color, "align": "middle"}
            })

        nodes.append({
            "id": f"M_{j}", "label": f"Mod Para {j+1}", "title": "Click for forensic report",
            "text_data": p2, "forensic_report": report,
            "color": {"background": bg_color, "border": border_color}, "font": {"color": "#fff"}
        })

    return {"nodes": nodes, "edges": edges}