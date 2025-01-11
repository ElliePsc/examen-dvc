import os
import yaml

def generate_mermaid_with_alias(dvc_file, mermaid_file):
    with open(dvc_file, "r") as f:
        dvc_data = yaml.safe_load(f)

    aliases = {}
    alias_counter = 65  # ASCII 'A'

    def get_alias(node):
        nonlocal alias_counter
        if node not in aliases:
            aliases[node] = chr(alias_counter)
            alias_counter += 1
        return aliases[node]

    lines = ["graph TD"]
    for stage, details in dvc_data.get("stages", {}).items():
        stage_alias = get_alias(stage)
        lines.append(f'    {stage_alias}["{stage}"]')

        for dep in details.get("deps", []):
            dep_alias = get_alias(dep)
            lines.append(f'    {dep_alias}["{dep}"] --> {stage_alias}')

        for out in details.get("outs", []):
            out_alias = get_alias(out)
            lines.append(f'    {stage_alias} --> {out_alias}["{out}"]')

    # Write to Mermaid file
    with open(mermaid_file, "w") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    dvc_file = "dvc.yaml"  # Adjust to your file location
    mermaid_file = "pipeline_with_alias.mmd"
    generate_mermaid_with_alias(dvc_file, mermaid_file)


