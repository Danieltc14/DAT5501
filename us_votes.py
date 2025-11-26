
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('US-2016-primary.csv', sep=';')

# Filter for Hillary Clinton
df_candidate = df[df['candidate'] == 'Hillary Clinton']

# Group by state and calculate average fraction of votes per state
state_fraction = df_candidate.groupby('state')['fraction_votes'].mean().reset_index()

# Set style for better aesthetics
sns.set(style="whitegrid", palette="muted")

# Create histogram
plt.figure(figsize=(10,6))
sns.histplot(state_fraction['fraction_votes'], bins=15, color='royalblue', edgecolor='black')

# Add labels and title
plt.title('Distribution of Hillary Clinton Vote Fraction by State', fontsize=16)
plt.xlabel('Average Fraction of Votes per State', fontsize=14)
plt.ylabel('Number of States', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the improved plot
plt.tight_layout()
plt.savefig('hillary_votes_histogram_better.png')
plt.show()
