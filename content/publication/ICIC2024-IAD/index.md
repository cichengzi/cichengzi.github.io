---
title: 'Spatial-Temporal Dependency Based Multivariate Time Series Anomaly Detection for Industrial Processes'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Yahui Li
  - Zhenpeng Hu
  - Chunjie Zhou
  - Lu Liu

# Author notes (optional)
author_notes:
#  - 'Equal contribution'
#  - 'Equal contribution'

date: '2024-04-06T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2024-04-06T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: International Conference on Intelligent Computing
publication_short: International Conference on Intelligent Computing

abstract: Multivariate time series anomaly detection is crucial for ensuring equipment and systems’ safe operation in the industrial process. However, detecting anomalies in multivariate time series is challenging due to the complex temporal and spatial dependencies among variables. To address this issue, we propose a multi-task variational autoencoder for multivariate time series anomaly detection. Structurally, it combines multi-task learning with a variational autoencoder structure to obtain a robust representation of time series with noise. In detail, graph attention networks and selective state space models are utilized to capture spatial and temporal dependencies effectively. Experimental results show that the proposed model outperforms six baselines on three datasets, including an anomaly detection dataset of the catalytic cracking process, achieving F1 scores of 0.9389, 0.8151, and 0.9524. In addition, anomaly scores and a causal graph of variables can provide a highly interpretable analysis of results to assist on-site safety managers in timely handling anomalies.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

#url_pdf: 'https://cichengzi.github.io/publication/CCC2024-RCA/conference-paper.pdf'
#url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_dataset: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_video: 'https://youtube.com'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: true

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
#  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---

This is a paper about anomaly detection of industrial process multivariate time series.
