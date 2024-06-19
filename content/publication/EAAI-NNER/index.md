---
title: "Named Entity Recognition Based on Anchor Span for Manufacturing Text Knowledge Extraction"
authors:
- Yahui Li
- admin
- Chunjie Zhou
- Lu Liu
- Yu-Chu Tian
date: "2024-06-19T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-06-19T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Engineering Applications of Artificial Intelligence"
publication_short: ""

abstract: Intelligent industrial manufacturing heavily relies on structured knowledge. Named Entity Recognition (NER), an essential technique for extracting structured knowledge from text, has garnered significant research interest. However, current NER approaches face difficulties in handling multiple levels of entity nesting in knowledge extraction, especially within the manufacturing context. To address this issue, we present an Anchor Span-based NER (ASNER) approach for accurately and efficiently extracting manufacturing text knowledge. This method combines token and span classification. Initially, the head and tail features of the entity are extracted, with the corresponding anchor span of potential entities generated based on a boundary match neural network to localize the entities. Subsequently, token spatial contextual features are extracted using biaffine attention and convolutional neural networks, and classification categories are assigned to the anchor span-filtered entity features. Experimental studies demonstrate the effectiveness of the proposed ASNER approach.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Source Themes
featured: false

links:
#- name: Custom Link
#  url: http://example.org
#url_pdf: http://arxiv.org/pdf/1512.04133v1
#url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_dataset: '#'
#url_poster: '#'
#url_project: ''
#url_slides: ''
#url_source: '#'
#url_video: '#'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/s9CC2SKySJM)'
  focal_point: ""
  preview_only: true

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
#- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---

This is a paper of nested named entity recognition of industrial text.
