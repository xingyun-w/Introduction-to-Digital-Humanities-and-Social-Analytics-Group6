import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

file_path = '/Users/sauregurkenzeit/Desktop/DH/Group-6/metadata.tsv'
data = pd.read_csv(file_path, sep="\t")


filtered_data = data[(data['firsted-yr'] >= 1751) & (data['firsted-yr'] <= 1800)].copy()


narrative_mapping = {
    'autodiegetic': 'First-person',
    'homodiegetic': 'First-person',
    'heterodiegetic': 'Third-person',
    'epistolary': 'Epistolary',
    'mixed': 'Mixed/Dialogue',
    'dialogue novel': 'Mixed/Dialogue',
}

filtered_data['narrative_group'] = filtered_data['form'].map(narrative_mapping)

# Drop rows with missing narrative forms and keep only male and female authors
filtered_data = filtered_data.dropna(subset=['narrative_group'])
filtered_data = filtered_data[filtered_data['au-gender'].isin(['M', 'F'])]

# Create 5-year periods
filtered_data['five_year_period'] = ((filtered_data['firsted-yr'] - 1751) // 5) * 5 + 1751

# Prepare data for plotting
plot_data = filtered_data.groupby(['five_year_period', 'narrative_group', 'au-gender']).size().unstack(level='au-gender', fill_value=0)
plot_data = plot_data.reset_index()
plot_data['Total'] = plot_data['M'] + plot_data['F']

# Ensure all narrative groups are present for each period
periods = plot_data['five_year_period'].unique()
narrative_forms = plot_data['narrative_group'].unique()
full_index = pd.MultiIndex.from_product([periods, narrative_forms], names=['five_year_period', 'narrative_group'])
plot_data = plot_data.set_index(['five_year_period', 'narrative_group']).reindex(full_index, fill_value=0).reset_index()


plot_data = plot_data.sort_values(['five_year_period', 'narrative_group'])

# Plot the bar chart for gender distribution of narrative forms over time
fig, ax = plt.subplots(figsize=(18, 12))
colors = plt.cm.Set3(np.linspace(0, 1, len(narrative_forms))) 
bar_width = 0.18
index = np.arange(len(periods))

max_value = max(plot_data['M'].max(), plot_data['F'].max())

for i, narrative in enumerate(narrative_forms):
    narrative_data = plot_data[plot_data['narrative_group'] == narrative]
    male_data = narrative_data['M'].values
    female_data = -narrative_data['F'].values  # Negative values for female data

    ax.bar(index + i * bar_width, male_data, bar_width, color=colors[i], label=narrative)
    ax.bar(index + i * bar_width, female_data, bar_width, color=colors[i], alpha=0.5)
    
    for j, (m, f) in enumerate(zip(male_data, female_data)):
        if m > 0:
            ax.text(index[j] + i * bar_width, m, str(int(m)), ha='center', va='bottom', fontsize=8, fontweight='bold')
        if f < 0:
            ax.text(index[j] + i * bar_width, f, str(int(abs(f))), ha='center', va='top', fontsize=8, fontweight='bold')


ax.set_xlabel('Time Period', fontsize=14)
ax.set_ylabel('Number of Works', fontsize=14)
ax.set_title('Distribution of Narrative Forms by Gender and Time Period (1751-1800)', fontsize=16)
ax.set_xticks(index + bar_width * (len(narrative_forms) - 1) / 2)
ax.set_xticklabels([f'{year}-{year+4}' for year in periods], rotation=45, ha='right')

ax.set_ylim(-max_value * 1.1, max_value * 1.1)
yticks = ax.get_yticks()
ax.set_yticks(yticks)
ax.set_yticklabels([abs(int(y)) for y in yticks])

ax.grid(True, linestyle='--', alpha=0.7)
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.legend(title='Narrative Form', bbox_to_anchor=(1.05, 1), loc='upper left')

ax.text(ax.get_xlim()[1], max_value / 2, 'Male', ha='left', va='center', fontsize=10, fontweight='bold')
ax.text(ax.get_xlim()[1], -max_value / 2, 'Female', ha='left', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# calculate standardized residuals
def calculate_standardized_residuals(contingency_table):
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    residuals = (contingency_table - expected) / np.sqrt(expected)
    return residuals, p

# visualize standardized residuals using heatmap
def visualize_residuals(residuals, period):
    plt.figure(figsize=(8, 6))
    sns.heatmap(residuals, annot=True, cmap='coolwarm', center=0, linewidths=0.5)
    plt.title(f'Standardized Residuals for Narrative Forms in {period} - {period+4}')
    plt.xlabel('Gender')
    plt.ylabel('Narrative Form')
    plt.show()

# Chi-square tests for each 5-year period
periods = sorted(filtered_data['five_year_period'].unique())
p_values = []

for period in periods:
    period_data = filtered_data[filtered_data['five_year_period'] == period]
    
    contingency_table = pd.crosstab(period_data['narrative_group'], period_data['au-gender'])

    if contingency_table.shape[1] == 2:
        residuals, p = calculate_standardized_residuals(contingency_table)
        p_values.append({'Period': period, 'p-value': p})
        if p < 0.05:
            print(f"Significant association for period {period} - {period+4}: p-value = {p:.4f}")
            visualize_residuals(residuals, period)
        else:
            print(f"No significant association for period {period} - {period+4}: p-value = {p:.4f}")
    else:
        print(f"Skipping period {period} due to insufficient data.")

# Plot p-values across periods
p_values_df = pd.DataFrame(p_values)
plt.figure(figsize=(10, 6))
sns.lineplot(data=p_values_df, x='Period', y='p-value', marker='o')
plt.title('P-values for Chi-square Tests Across Time Periods')
plt.axhline(0.05, color='red', linestyle='--', label='Significance Threshold')
plt.xlabel('5-Year Period')
plt.ylabel('p-value')
plt.legend()
plt.show()
