#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate placeholder .md files for all entries in manifest.json files"""

import json
import os
import re
from pathlib import Path

def slugify(title):
    """Convert title to slug format (kebab-case)"""
    # Remove accents and special characters
    slug = re.sub(r'[àáâãäå]', 'a', title.lower())
    slug = re.sub(r'[èéêë]', 'e', slug)
    slug = re.sub(r'[ìíîï]', 'i', slug)
    slug = re.sub(r'[òóôõö]', 'o', slug)
    slug = re.sub(r'[ùúûü]', 'u', slug)
    slug = re.sub(r'[ç]', 'c', slug)
    # Convert spaces and underscores to hyphens
    slug = re.sub(r'[\s_]+', '-', slug)
    # Remove any remaining non-alphanumeric characters except hyphens
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug

def generate_placeholder_content(title, slug, doc_type="concept"):
    """Generate placeholder markdown content with YAML front matter"""
    
    # Extract folder name from path
    folder_prefix = slug.split('-')[0] if '-' in slug else "00"
    
    content = f"""---
title: "{title}"
slug: "{slug}"
doc_type: "{doc_type}"
summary: "Placeholder IA-ready. Preencher com conteúdo definitivo sobre {title}."
tags: ["placeholder", "pendente"]
related: []
---

## O que faz

[Escrever descrição do objetivo e propósito - máx 3 parágrafos]

## Sintaxe

```
[Documentar sintaxe, parâmetros, retornos]
```

## Quando usar

- [Casos ideais]
- [Pré-condições]
- [Limitações]

## Exemplo

```
[Exemplo funcional mínimo]
```

Saída esperada:
```
[Output esperado]
```

## Observações

- [Compatibilidade]
- [Performance]
- [Comportamento em cache]
- [Impacto SEO/Mobile]

## Erros comuns

### Erro frequente 1
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
"""
    
    return content

def main():
    base_path = Path("/home/andre/Documents/Projects/cloned/templates-documentation/docs")
    
    # Dictionary to track created files
    created_files = {}
    total_files = 0
    
    # Iterate through all folders
    for folder_dir in sorted(base_path.iterdir()):
        if not folder_dir.is_dir():
            continue
        
        manifest_file = folder_dir / "manifest.json"
        if not manifest_file.exists():
            continue
        
        # Read manifest
        with open(manifest_file, 'r', encoding='utf-8') as f:
            entries = json.load(f)
        
        folder_name = folder_dir.name
        created_files[folder_name] = []
        
        # Create files for each entry
        for entry in entries:
            title = entry.get('title', 'Untitled')
            path = entry.get('path', '')
            
            # Extract filename from path
            if path:
                filename = path.split('/')[-1]
            else:
                filename = f"{slugify(title)}.md"
            
            file_path = folder_dir / filename
            
            # Skip if file already exists
            if file_path.exists():
                print(f"  ⏭️  SKIP: {file_path.relative_to(base_path)} (já existe)")
                continue
            
            # Generate slug from filename
            slug = filename.replace('.md', '')
            
            # Determine doc_type (simple heuristic)
            doc_type = "concept"
            if "exemplo" in filename.lower():
                doc_type = "example"
            elif "como" in filename.lower() or "guia" in filename.lower():
                doc_type = "how-to"
            elif "funcao" in filename.lower() or "metodo" in filename.lower():
                doc_type = "reference"
            
            # Generate content
            content = generate_placeholder_content(title, slug, doc_type)
            
            # Create file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            created_files[folder_name].append(filename)
            total_files += 1
            print(f"  ✅ CRIADO: {file_path.relative_to(base_path)}")
    
    # Summary
    print("\n" + "="*70)
    print("📊 RESUMO DE CRIAÇÃO")
    print("="*70)
    
    for folder, files in sorted(created_files.items()):
        if files:
            print(f"\n📁 {folder}: {len(files)} arquivo(s) criado(s)")
            for f in files:
                print(f"   - {f}")
    
    print(f"\n📈 Total: {total_files} arquivo(s) criado(s)")
    print("="*70)

if __name__ == "__main__":
    main()
