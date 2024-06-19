---
title: "Anomaly Detection of Reaction Regeneration Process in Catalytic Cracking Unit Based on DS2AE"
authors:
- Zhenpeng Hu
- admin
- Yue Zhang
- Chunjie Zhou
- Deshun Cao
date: "2024-06-19T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-06-19T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "Journal of Computer Applications"
publication_short: ""

abstract: Anomaly detection for multi-dimensional time series generated by chemical process variables is an important means to ensure operational safety. Once detection fails, local anomalies will cascade and propagate, leading to major accidents. However, there are complex coupling relationships between variables in the catalytic cracking reaction regeneration process, and it is difficult for traditional models to fully extract the complex spatial-temporal characteristics of multi-dimensional time series. In order to solve the above problems, a diagonal state space autoencoder DS2AE is proposed for anomaly detection, which uses the diagonal state space model and the multi-layer perceptron with residual connections to extract the temporal and spatial dependencies of the multi-dimensional time series and enables parallel inference at all time steps. In addition, a ternary search method is designed to automatically select the threshold so that the threshold has a certain degree of objectivity. On the anomaly detection dataset constructed by the catalytic cracking process simulation system, experiments show that the F1 score of the proposed model for the binary classification task of anomaly detection reaches 92.55%, and it shows strong robustness in the selection of hyper-parameters, which has the potential to be applied to the actual process.

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

This is a paper of anomaly detection of reaction regeneration processes.