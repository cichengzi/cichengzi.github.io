---
title: 'Safety Verification of Advanced Driver Assistance Systems Using Hybrid Automaton Reachability'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Lu Liu
  - admin
  - Liren Yang
  - Yahui Li
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
publication: IEEE International Conference on Systems, Man, and Cybernetics
publication_short: IEEE International Conference on Systems, Man, and Cybernetics

abstract: Advanced driving assistance system (ADAS) is effectively promoting the vehicular automation level and it is critical to ensure its functional safety. While existing analysis mainly focuses on individual functions of ADAS, safety violations in the overall system can be found by extensive road tests, which are not only costly in terms of time and money but also lack a formal safety guarantee. This is because tests may not cover all driving scenarios, especially the ones that involve function mode switching. In this paper, we focus on the longitudinal vehicle motion and provide a pipeline to perform safety verification for all the related ADAS functions. To that end, we specify safety constraints and boundaries for a vehicle’s longitudinal cruising and collision avoidance and validate a longitudinal dynamic model against the high-fidelity simulation software CarSim. Then we define hybrid automata to describe the closed-loop system composed of the vehicle dynamics and the ADAS. Finally, by computing the reachable sets of the hybrid automata and comparing them with the specified safety boundaries, the ADAS is verified. Numerical experiments demonstrate the efficacy of the proposed approach.

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

This is a paper about safety verification of advanced driving assistance systems.
