# What is this website?
The goal of this website is to curate links of resources that explain the reality of the Israeli occupation to Palestine. 

# What is this website is NOT?
We are not trying to bet yet another resource of information. We don't want to host any content or data ourselves. We simply direct people to trustworthy resources.

# How can I contribute?
You can suggest links to resources. All what you need to do is to create a file with a unique name in the "posts" folder. This file should have two sections:

### 1) Hugo Front Matter section.

This section should have the following attributes:

- title: which will be the text that represents the link
- tags: list of tags this link can be labeled with. Please try your best to look into the other posts and re-use other tags before create new ones.
- categories: list of categories that this post categorised under. (currently we are not using Categories).
- ex_url: this is the link to the resource
- weight: an integer that represents the weight of the page, the lower the number the higher the post will be.
- Date: the data this link is added.

Below is an example.

```
+++
title = "Report: Israel’s apartheid against Palestinians"
categories = ["web"]
tags = ["apartheid"]
ex_url = "https://www.amnesty.org/en/documents/mde15/5141/2022/en/?utm_source=annual_report&utm_medium=epub&utm_campaign=2021"
Date = "2023-11-16"
+++
```

### 2) Link Description
The remainder of the file is text that explains what this link is.