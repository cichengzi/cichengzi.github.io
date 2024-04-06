---
title: "Capacity Estimation of Lithium-ion Battery with Multi-task Autoencoder and Empirical Mode Decomposition"
authors:
- admin
- Fangshu Cui
- Mingrui Shi
date: "2024-04-06T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-04-06T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: The estimation of lithium-ion battery capacity is a commonly used method in health diagnosis and management. Its mainstream method involves using data-driven time series forecasting models to learn the patterns of changes in lithium-ion battery capacity. However, the capacity regeneration of lithium-ion batteries poses a challenge for training time series forecasting models. Therefore, we propose a hybrid method that applies empirical mode decomposition and a multi-task autoencoder to accurately capture capacity regeneration. In detail, empirical mode decomposition is applied to the capacity time series, decomposing it into intrinsic mode functions and a residual. Then, a novel multi-task autoencoder based on diagonal state space models is applied to estimate the intrinsic mode functions while support vector regression is utilized for the residual. Therefore, the proposed hybrid method can capture both the long-term dependency of capacity and uncertainty brought by capacity regeneration. Experiments were conducted on three public datasets, and the proposed method surpassed nine baselines and achieved an average root mean square error of 0.0103, 0.0111, and 0.0004. In addition, the proposed method takes up less resources and has high real-time efficiency.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Source Themes
featured: true

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
  preview_only: false

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

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).