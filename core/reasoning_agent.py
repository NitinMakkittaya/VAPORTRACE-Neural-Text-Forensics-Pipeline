def generate_forensic_report(orig_text, mod_text, similarity_score, tampered_entities):
    report = f"Semantic Drift detected. Vector similarity dropped to {similarity_score:.2f}."
    
    if tampered_entities:
        report += f" WARNING: Entity swap detected. New variables injected: {', '.join(tampered_entities)}."
        return report

    if similarity_score < 0.90:
        report += " The structural vocabulary matches, but the legal or functional meaning has been fundamentally inverted or altered."
    return report