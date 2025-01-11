import yaml

def generate_mermaid_from_dvc(dvc_file, output_file):
    # Charger le fichier dvc.yaml
    with open(dvc_file, 'r') as file:
        dvc_pipeline = yaml.safe_load(file)
    
    stages = dvc_pipeline.get('stages', {})
    
    # Construire le graphe Mermaid
    mermaid_lines = ["graph TD"]
    for stage, details in stages.items():
        command = f"{stage}[{details.get('cmd', stage)}]"
        dependencies = details.get('deps', [])
        outputs = details.get('outs', [])
        
        # Lier les dépendances aux étapes
        for dep in dependencies:
            dep_node = dep.replace("/", "_").replace(".", "_")
            mermaid_lines.append(f"{dep_node} --> {stage}")
        
        # Lier les sorties aux étapes
        for out in outputs:
            out_node = out.replace("/", "_").replace(".", "_")
            mermaid_lines.append(f"{stage} --> {out_node}")
    
    # Écrire dans le fichier Mermaid
    with open(output_file, 'w') as file:
        file.write("\n".join(mermaid_lines))
    
    print(f"Diagramme Mermaid généré dans {output_file}")

# Exemple d'utilisation
generate_mermaid_from_dvc('dvc.yaml', 'pipeline_mermaid.md')
