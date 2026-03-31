#!/usr/bin/python3

import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def validate_model(model):
    stages = set(model.get('stages', []))
    queues = set(model.get('queues', []))

    for c in model.get('connections', []):
        src = c['from']
        dst = c['to']

        if src not in stages and src not in queues:
            raise ValueError(f"Unknown source: {src}")

        if dst not in stages and dst not in queues:
            raise ValueError(f"Unknown destination: {dst}")

def main():
    # Load the YAML file
    with open('model.yaml', 'r') as yaml_file:
        model = yaml.safe_load(yaml_file)
    validate_model(model)

    env = Environment(loader=FileSystemLoader('templates'),
            trim_blocks=True,
            lstrip_blocks=True)

    output_dir = Path(model.get('output', 'generated'))
    output_dir.mkdir(parents=True, exist_ok=True)

    files_to_generate = [
        ('measurements.h.j2', output_dir / 'measurements.h'),
        ('queues.h.j2', output_dir / 'queues.h'),
        ('stages.h.j2', output_dir / 'stages.h'),
        ('pipelines.h.j2', output_dir / 'pipeline.h'),
    ]

    for template_name, output_path in files_to_generate:
        template = env.get_template(template_name)
        output = template.render(model=model)

        with open(output_path, 'w') as f:
            f.write(output)

if  __name__ == "__main__":
    main();
