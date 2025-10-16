import pandas as pd
import numpy as np
from faker import Faker
import random
import datetime

# --- SETTINGS ---
NUM_CONTENT = 10000
NUM_ENGAGEMENTS = 3000000

# --- DATA GENERATION ---
fake = Faker()
Faker.seed(0)
np.random.seed(0)

print("Starting data generation...")

# 2. CONTENT TABLE
print("Generating Content table...")
content_data = {
    'content_id': np.arange(1, NUM_CONTENT + 1),
    'title': [fake.catch_phrase() for _ in range(NUM_CONTENT)],
    'domain': np.random.choice(
        ['Data Science', 'Business', 'Marketing', 'Mathematics', 'Finance', 'Software Engineering', 'Design'],
        NUM_CONTENT
    ),
    'subtopic': np.random.choice(
        ['linear-algebra', 'social-media-analytics', 'machine-learning', 'financial-modeling', 'product-management', 'sql', 'python', 'r', 'agile-methodology'],
        NUM_CONTENT
    ),
    'difficulty_level': np.random.choice(
        ['Beginner', 'Intermediate', 'Advanced'],
        NUM_CONTENT,
        p=[0.5, 0.35, 0.15]
    ),
    'content_type': np.random.choice(
        ['Video', 'Article', 'Interactive Quiz', 'Case Study'],
        NUM_CONTENT,
        p=[0.6, 0.2, 0.1, 0.1]
    )
}
content_df = pd.DataFrame(content_data)
content_df.to_csv('content.csv', index=False)
print(f"Content table created with {len(content_df)} records.")

# 3. ENGAGEMENTS TABLE
print("Generating Engagements table...")

user_ids = np.random.choice(
    users_df['user_id'],
    size=NUM_ENGAGEMENTS,
    p=np.random.dirichlet(np.ones(NUM_USERS) * 0.5)
)
content_ids = np.random.choice(
    content_df['content_id'],
    size=NUM_ENGAGEMENTS,
    p=np.random.dirichlet(np.ones(NUM_CONTENT) * 0.8)
)

start_date = datetime.datetime.now() - datetime.timedelta(days=365)
timestamps = [
    start_date + datetime.timedelta(seconds=random.randint(0, 365*24*60*60))
    for _ in range(NUM_ENGAGEMENTS)
]

duration_seconds = np.random.normal(loc=900, scale=300, size=NUM_ENGAGEMENTS).astype(int)
duration_seconds = np.clip(duration_seconds, a_min=30, a_max=3600)

liked_probability = (duration_seconds / 3600) * 0.8 + 0.1
liked = np.random.binomial(n=1, p=liked_probability)
# FIX: Convert the array to float to allow for NaN values
liked = liked.astype(float)
liked[liked == 0] = np.nan

engagement_type = np.random.choice(
    ['viewed', 'completed', 'shared', 'bookmarked'],
    size=NUM_ENGAGEMENTS,
    p=[0.7, 0.2, 0.05, 0.05]
)

engagements_data = {
    'user_id': user_ids,
    'content_id': content_ids,
    'timestamp': timestamps,
    'duration_seconds': duration_seconds,
    'liked': liked,
    'engagement_type': engagement_type
}
engagements_df = pd.DataFrame(engagements_data)
engagements_df.to_csv('engagements.csv', index=False)
print(f"Engagements table created with {len(engagements_df)} records.")

print("\nAll datasets have been generated and saved as CSV files.")
print("You can now open 'content.csv', and 'engagements.csv' in Excel.")