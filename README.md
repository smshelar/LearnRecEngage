# 🎯 Learning Engagement Recommendation Engine

# 📑 Table of Contents

- [🧩 Overview](#-overview)
- [🚀 Features](#-features)
  - [Personalized Recommendations](#p-ersonalized-recommendations)
  - [Hybrid Model](#-hybrid-model)
  - [Data Simulation](#-data-simulation)
  - [Evaluation Metrics](#-evaluation-metrics)
  - [Data Insights](#-data-insights)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Requirements](#-requirements)
- [🧠 Setup and Usage](#-setup-and-usage)
  - [1. Generate Datasets](#1-generate-datasets)
  - [2. Run the Notebook](#2-run-the-notebook)
  - [📊 Example Output](#-example-output)
  - [📈 Evaluation](#-evaluation)
- [🧮 Model Details](#-model-details)
  - [Data Schemas](#data-schemas)
    - [Users](#users)
    - [Content](#content)
    - [Engagements](#engagements)
  - [🔄 Simulation Logic](#-simulation-logic)
  - [⚖️ Hybrid Blending Formula](#h-ybrid-blending-formula)
  - [🔍 Key Insights](#-key-insights)
- [🧭 Limitations and Future Work](#-limitations-and-future-work)


## 🧩 Overview
This project implements a **hybrid recommendation system** designed to enhance learning experiences by suggesting personalized educational content.  
It combines **content-based filtering** (leveraging metadata like titles, domains, and difficulty levels) with **collaborative filtering** (using user interaction patterns) to recommend relevant materials such as videos, articles, quizzes, and case studies.

The system aims to improve **retention**, **engagement**, and **content relevance** by factoring in user preferences, seniority, and interaction history.

Datasets are **synthetically generated** to simulate real-world conditions — including user profiles, content items, and engagement logs.  
The core implementation is done in a **Jupyter notebook**, supported by Python scripts for data generation.

---

## 🚀 Features

- **Personalized Recommendations**  
  Tailors suggestions based on user roles (e.g., students, juniors, seniors), learning styles (visual, auditory, etc.), and past interactions.

- **Hybrid Model**
  - **Content-based:** Uses TF-IDF vectorization on content titles and categorical matching for domains/subtopics.
  - **Collaborative:** Employs SVD (Singular Value Decomposition) to uncover latent user-content interaction patterns.

- **Data Simulation**  
  Generates realistic datasets with skewed distributions to mimic real-world learning behaviors (e.g., more beginner-level content, casual vs. power users).

- **Evaluation Metrics**  
  Implements `Precision@K`, `Recall@K`, and `NDCG@K` to evaluate recommendation quality.

- **Data Insights**  
  Extracts correlations, engagement trends, and content imbalances to refine the model.

---

## 📂 Repository Structure

```text
├── createusers.py # Generates users.csv with profiles & seniority
├── create_datasets.py # Generates content.csv & engagements.csv
├── recommedation_engine.ipynb # Core notebook for model building & evaluation
├── Presentation.pdf # Project overview slides (for reference)
└── README.md # Documentation
```
---

## ⚙️ Requirements

- **Python:** 3.8+
- **Libraries:**
  ```bash
  pip install pandas numpy matplotlib seaborn scikit-learn surprise faker
  ```

> **Note**: The notebook includes a pin for numpy<2 due to compatibility with surprise.

---

## 🧠 Setup and Usage

### 1. Generate Datasets

Run the following commands **in order**:

```bash
python createusers.py
python create_datasets.py
```
**Description of Scripts**

- createusers.py → Generates users.csv containing 100,000 users.
- create_datasets.py → Generates:
    - content.csv with 10,000 items
    - engagements.csv with 3,000,000 interactions

These scripts leverage:
- Faker → For realistic names and domains
- NumPy → For skewed statistical distributions (e.g., durations, user selection probabilities)

### 2. Run the Notebook

Open recommedation_engine.ipynb in Jupyter Notebook or Google Colab.

Steps inside the notebook:
1. Load and explore datasets 
2. Build a content-based recommender (TF-IDF + cosine similarity)
3. Train SVD model on engagement scores (0–10 scale)
4. Combine into a hybrid model using a tunable α (e.g., α = 0.7 for collaborative emphasis)
5. Generate recommendations for a sample user 
6. Evaluate model using offline metrics

### 📊 Example Output
Sample **top-5 recommendations**:

| content_id | title                                  | predicted_score |
|------------|----------------------------------------|----------------|
| 9621       | Vision-oriented regional toolset       | 7.042          |
| 5206       | Open-architected contextually-based approach | 7.029          |
| 7310       | Adaptive modular knowledge flow        | 6.982          |
| 1982       | Cross-domain learner interface         | 6.951          |
| 8427       | Progressive knowledge ecosystem        | 6.923          |


### 📈 Evaluation

The notebook includes helper functions to compute the following metrics:

- **Precision@5**  
- **Recall@5**  
- **NDCG@5**

> **Note**: Run evaluations on a **subset of users** for efficiency. Full evaluation may take longer due to the large dataset size.

---

## 🧮 Model Details

### Data Schemas

#### Users

| Column           | Description                         |
|-----------------|-------------------------------------|
| user_id          | Unique user identifier               |
| title            | Job title (e.g., Junior Data Analyst) |
| department       | Department name                     |
| seniority_level  | Role level (Student → Lead)          |
| learning_style   | Visual, Auditory, or Kinesthetic    |

#### Content

| Column           | Description                         |
|-----------------|-------------------------------------|
| content_id       | Unique content ID                   |
| title            | Content title                       |
| domain           | High-level domain (e.g., Data Science) |
| subtopic         | Specific sub-area                   |
| difficulty_level | Beginner, Intermediate, Advanced    |
| content_type     | Video, Article, Quiz, etc.          |

#### Engagements

| Column           | Description                         |
|-----------------|-------------------------------------|
| user_id          | Linked to Users                     |
| content_id       | Linked to Content                   |
| timestamp        | Interaction timestamp               |
| duration_seconds | Time spent                          |
| liked            | Boolean or null                     |
| engagement_type  | Viewed, Completed, etc.             |

### 🔄 Simulation Logic

- Engagements are simulated over a **1-year span**.  
- Scores blend **implicit feedback** (e.g., duration) and **explicit feedback** (e.g., likes).  
- Addresses **data sparsity** by focusing on key interaction signals, such as **recency** and **depth**.

### ⚖️ Hybrid Blending Formula

The final recommendation score is computed as:

`Final Score = α × Collaborative + (1 - α) × Content-Based`

**Tuning α based on use case:**

- **Higher α** → Favors collaborative learning (returning users)  
- **Lower α** → Favors content similarity (new users)

🔍 Key Insights

- **Feature Importance**: Titles dominate TF-IDF similarity; domains/subtopics enhance diversity.
- **User Behavior**: Casual users (1–5 interactions) dominate, but power users drive content trends.
- **Content Distribution**: Skewed toward beginner videos; advanced materials less frequent.
- **Challenges Addressed**: Mitigates cold-start via metadata, balances personalization vs. diversity.

---

## 🧭 Limitations and Future Work

- **Synthetic data**: Replace with real engagement logs for production.
- **Scalability**: Optimize SVD or migrate to distributed engines (e.g., Spark ALS).
- **Enhancements**:
    - Integrate deeper learning-style modeling.
    - Add real-time recommendation updates.
    - Explore deep learning (e.g., Neural Collaborative Filtering).
- **Evaluation**: Current metrics are offline — A/B testing recommended for live platforms.

---

## 📬 Contact

For questions or collaboration, reach out via 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Shraddha_Shelar-blue?logo=linkedin&logoColor=white&style=for-the-badge)](https://www.linkedin.com/in/shraddhashelar/)
[![GitHub](https://img.shields.io/badge/GitHub-Shraddha_Shelar-black?logo=github&logoColor=white&style=for-the-badge)](https://github.com/smshelar)

This project demonstrates a scalable and interpretable approach to educational recommender systems, adaptable for e-learning platforms like Coursera, Udemy, or internal corporate learning ecosystems.
