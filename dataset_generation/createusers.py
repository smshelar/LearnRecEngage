import pandas as pd
import numpy as np
from faker import Faker
import random
import datetime

# --- SETTINGS ---
NUM_USERS = 100000

# --- DATA GENERATION ---
fake = Faker()
Faker.seed(0)
np.random.seed(0)

print("Starting data generation...")

# 1. USERS TABLE
print("Generating Users table...")

# Define job titles by seniority level
job_titles_by_seniority = {
    'Student': [
        'Student (Data Science)',
        'Student (Software Engineering)',
        'Student (Business Analyst)',
        'Student (Marketing)'
    ],
    'Fresher': [
        'Fresher (Data Analyst)',
        'Fresher (Junior Developer)',
        'Fresher (Business Analyst)',
        'Fresher (Marketing Associate)'
    ],
    'Junior': [
        'Junior Data Analyst',
        'Junior Data Scientist',
        'Junior Software Engineer',
        'Junior Machine Learning Engineer',
        'Junior Business Analyst',
        'Marketing Assistant'
    ],
    'Mid': [
        'Data Analyst',
        'Data Scientist',
        'Software Engineer',
        'Machine Learning Engineer',
        'Business Intelligence Analyst',
        'Product Manager',
        'Marketing Manager'
    ],
    'Senior': [
        'Senior Data Analyst',
        'Senior Data Scientist',
        'Senior Software Engineer',
        'Senior Machine Learning Engineer',
        'Senior Product Manager'
    ],
    'Lead': [
        'Lead Data Scientist',
        'Principal Engineer',
        'Data Science Manager',
        'Director of Data'
    ]
}

# Combine all job titles for a flat list
all_jobs = []
for jobs in job_titles_by_seniority.values():
    all_jobs.extend(jobs)

# Define weights for each job title. The values are relative, not probabilities.
# The number of weights must match the number of total job titles.
weights = [
    15, 10, 10, 10,  # Students
    10, 10, 5, 5,    # Freshers
    5, 5, 5, 5, 5, 3, # Juniors
    2, 2, 2, 1, 1, 1, 1, # Mid
    1, 1, 1, 1, 1, # Seniors
    0.5, 0.5, 0.5, 0.5, # Leads
]

# Check if the number of weights matches the number of jobs
if len(weights) != len(all_jobs):
    raise ValueError(f"Number of weights ({len(weights)}) does not match number of jobs ({len(all_jobs)})")

# Normalize the weights to create probabilities that sum to 1
probabilities = np.array(weights) / np.sum(weights)

# Create a mapping from job title to seniority level
job_to_seniority = {}
for seniority, jobs in job_titles_by_seniority.items():
    for job in jobs:
        job_to_seniority[job] = seniority

# Generate a random selection of titles based on the normalized probabilities
titles = np.random.choice(
    all_jobs,
    NUM_USERS,
    p=probabilities
)

# Use the mapping to get the correct seniority level for each user
seniority_levels = [job_to_seniority[job] for job in titles]

users_data = {
    'user_id': np.arange(1, NUM_USERS + 1),
    'title': titles,
    'department': [
        'Engineering' if 'Engineer' in title or 'Developer' in title or 'Principal' in title else
        'Data' if 'Data' in title or 'Scientist' in title or 'Analyst' in title else
        'Product' if 'Product' in title else
        'Marketing' if 'Marketing' in title else
        'N/A' # For students/freshers not yet tied to a department
        for title in titles
    ],
    'seniority_level': seniority_levels,
    'learning_style': np.random.choice(
        ['Visual', 'Auditory', 'Kinesthetic', 'Reading/Writing'],
        NUM_USERS
    )
}
users_df = pd.DataFrame(users_data)
users_df.to_csv('users.csv', index=False)
print(f"Users table created with {len(users_df)} records.")

# --- The rest of the script for Content and Engagements remains the same ---
# You can append the rest of the code from the previous responses here.