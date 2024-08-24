---
title: Basic Knowledge of Recurrent Neural Networks
subtitle: 
  
# Summary for listings and search engines
summary: Basics of recurrent neural networks and the difference between the long short-term memory (LSTM) and gated neural unit (GRU).
  
# Link this post with a project
projects: []

# Date published
date: '2024-8-24T00:00:00Z'

# Date updated
lastmod: '2024-8-24T00:00:00Z'

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

authors:
  - admin

tags:
  - Deep Learning

categories:
  - Deep Learning

---

In this post, the basic knowledge of recurrent neural networks will be introduced. 

### Neural Networks without Hidden States

Let's take a look at an MLP with a single hidden layer. Let the hidden layer's activation function be 
{{< math >}}
$$
\phi
$$.

{{< /math >}}
