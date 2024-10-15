# Group-6

The latter half of the 18th century saw a rise in female authors and their impact on novel narrative forms. By "novel narrative forms," we refer to the narrative techniques, especially the narrator's perspective. From 1751 to 1800, there was a shift toward introspective, emotion-driven narratives, such as epistolary and first-person forms, reflecting Romanticism's focus on individual emotion.

This project involves analyzing the relationship between gender and narrative forms in French novels from 1750 to 1800. The analysis uses a Chi-square test of independence to determine whether there are significant associations between author gender and the chosen narrative forms for each 5-year period. The project also visualizes standardized residuals for significant periods and presents a summary of p-values across time intervals.

The dataset used for this project is sourced from https://github.com/MiMoText/roman18/blob/master/metadata.tsv as course material for the Digital Humanities course. 

## Prerequisites

To run the provided Python script, you need the following software and libraries installed on your machine:

### Python Environment
- **Python 3.8** or higher is required.

### Libraries
The project relies on several Python libraries. You can install all dependencies using the `requirements.txt` file. Below is the list of required libraries:

- **pandas** (version 1.3.0 or later): For data manipulation and processing.
- **numpy** (version 1.21.0 or later): For numerical computations.
- **matplotlib** (version 3.4.0 or later): For creating visualizations.
- **seaborn** (version 0.11.0 or later): For advanced plotting, including heatmaps and line plots.
- **scipy** (version 1.7.0 or later): For statistical tests, specifically the Chi-square test.


You can install the dependencies with the following command:
```
pip install -r requirements.txt
```

## Running the Code

Clone the Repository
Clone or download this repository to your local machine:
```
git clone [repository-link]
cd [repository-name]
```
### Data File

The dataset file (metadata.tsv) is required to run the analysis. Ensure that the file is placed in the correct directory. The dataset should be in a tab-separated format (.tsv).

### Run the Script
After setting up the environment and placing the dataset, run the Python script:

```
python narrative_analysis.py
```

This script performs the following actions:

- Filters the dataset based on publication years.

- Standardizes narrative forms into four categories.

- Analyzes gender differences in narrative forms using Chi-square tests.

- Plots the distribution of narrative forms by gender and time period, as well as the p-values of the Chi-square tests.


## Notes

Ensure that the dataset contains the correct column names ('firsted-yr', 'form', 'au-gender') to avoid errors.

## Reuse Potential
- Linguistic Analysis: Researchers can use the dataset for linguistic tasks, such as analyzing language used by male versus female authors.
- Cultural Analysis: Further studies can investigate shifts in cultural representation based on narrative form, especially in the context of Enlightenment-era literature.
  
## Sources
- Brewer, D. (Ed.). (2014). The Cambridge companion to the French enlightenment. Cambridge University Press.
- Hunter, J. P. (1996). The novel and social/cultural history. The Cambridge Companion to the Eighteenth-Century Novel, 9-40.
