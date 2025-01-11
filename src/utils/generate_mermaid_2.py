import os
from generate_mermaid import generate_mermaid_from_dvc  # Importez la fonction depuis un autre fichier

def generate_mermaid_and_image(dvc_file, mermaid_file, output_image):
    # Générer le fichier Mermaid
    generate_mermaid_from_dvc(dvc_file, mermaid_file)
    
    # Vérifiez si `mmdc` (Mermaid CLI) est installé
    if os.system("which mmdc") == 0:
        # Générez une image à partir du fichier Mermaid
        os.system(f"mmdc -i {mermaid_file} -o {output_image}")
    else:
        print("Mermaid CLI (mmdc) n'est pas installé. Veuillez l'installer pour générer une image.")

# Appel de la fonction principale
generate_mermaid_and_image("dvc.yaml", "pipeline.mmd", "pipeline.png")

