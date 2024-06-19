---
title: 'Anomaly Diagnosis of Catalytic Cracking Process Based on Causal Model and Anomaly Detection'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Yue Zhang
  - Zhenpeng Hu
  - admin
  - Chunjie Zhou

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
publication: China Automation Congress
publication_short: China Automation Congress

abstract: The regeneration process of catalytic cracking reaction is a highly coupled and complex industrial control process, and local anomalies can cascade and propagate, leading to serious consequences. Aiming at this characteristic, this paper proposes a method to monitor the anomalies of the reaction regeneration process and identify the root causes of the anomalies. First, a diagonal state space autoencoder (DS2AE) is used to monitor the process variables of the reaction regeneration process and identify the abnormal conditions and abnormal variables. Then, a causal analysis method (MIC-TDTE) based on maximum mutual information coefficient (MIC) and time delay transfer entropy (TDTE) is used to construct a causal model between the variables, where MIC calculates the correlation between the abnormal variables and TDTE explores the causality between the relevant variables. Finally, the causal diagram is used to traverse the propagation path of the anomalies in order to identify the root causes of the anomalies. The accuracy of the proposed method is demonstrated by applying it to the anomalous working condition dataset constructed by the FCC process simulation system.
  
# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: []

# Display this page in the Featured widget?
featured: false

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
  preview_only: false

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

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/).
