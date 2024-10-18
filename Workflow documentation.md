# Workflow Documentation

### Course:  
Introduction to Digital Humanities and Social Analytics  
Vrije Universiteit Amsterdam

Group 6  
Robert Cornelis  
Rob Goudriaan  
Joanna Rejnowska  
Nikol Velkova  
Xingyun Wang

## Introduction, context & project’s objectives
The present study analyses data on French novels from the eighteenth century, also known as the 'Enlightenment'. The term 'Enlightenment' refers to a set of ideas, ideals and cultural practices that emerged from an existing intellectual and socio-political order. This emergence may be characterised as occurring either by opposing the existing order from the outside, or by reshaping it from within<sup>1</sup>. Specifically, new attempts were made within the Enlightenment to establish a new foundation for knowledge and to adopt a different epistemological approach<sup>1</sup>. 

A particular focus of this study is the emergence and development of a new literary form during this period: the novella. This literary form describes stories of a contemporary individual in a recognisable social and cultural context<sup>2</sup>. In order to gain an understanding of this development, it is essential to consider the prevailing view at the end  of the seventeenth century. At that time, literature was subject to generic conventions and rules and was only accessible to a limited part of the population, specifically the upper class<sup>1</sup>. This resulted in the creation of literature that conformed to the established principles of aestheticians such as Aristotle and Horace. This gave the elite a sense of historical continuity and elevation, which was an important aspect of their identity<sup>1</sup>.  

During the Enlightenment, however, authors began to question this view. Indeed, they were convinced that democracy could be strengthened through the aesthetic use of language, which enabled the expression of ideas and became increasingly robust when spread among citizens.  Additionally, the perception of everyday fictional narratives underwent a transformation. Novels were initially seen as deceptive and detrimental to moral behaviour, but then emerged as a means of depicting, interpreting and critiquing contemporary social relations<sup>1</sup>.  

In this study, we will therefore focus on three variables provided to us within an existing data set concerning novellas published between 1750 and 1800: first, the narrative form in which they were written, second, the gender of the author by whom they were written, and third, the time in which they were published. To investigate these aspects, we formulated the following research question:  

*'What trends can we observe in the choice of narrative form in French novels between 1750 and 1800, and how does this relate to the gender of the author over time?'*  

The main aim of our approach is to shed light on an aspect of the writing style of female and male novella writers during the Enlightenment. This objective is important for several reasons. First, research on novellas was overlooked for a long time, as they were seen as sensationalist works and considered unsuitable for academic research<sup>2</sup>. Second, the central cultural value of novellas was often ignored<sup>2</sup>. Most importantly, however, the role, influence and practices of women in traditional historiography and their position in public life have not been sufficiently studied<sup>2</sup>.

As perspectives on the first two points have shifted within the academic community, our aim is to contribute to the advancement of research on Enlightenment novels. We aim to make specific contributions to existing research concerning gender and the potentially associated aesthetic features, specifically narrative form. In doing so, we shine as much light on the male gender as the female gender. We think this is important to point out, as women's contributions in classical history are overshadowed, while new cultural history seeks to shine additional light on them. Their work deserves equal attention and analysis.  

### Thesis Statement  
During the Enlightenment, the novella gained in popularity as a more widely accepted literary form, largely due to the expansion of reading beyond the upper class to the middle class, especially young women<sup>2</sup>. Women of this period were increasingly asserting their right to both emotion and reason, with the novella - particularly the epistolary form - serving as an important vehicle for this expression<sup>1,2</sup>. This was reflected in the fact that more women began to read and the profession of authorship was no longer exclusively for men<sup>1,2</sup>. Given the growing acceptance of such narratives, we expect to see a rise in the number of women writers employing the epistolary format in their works.  

### Documentation of the Introduction, context & project’s objectives
The current section has proven to be the most challenging aspect of the ongoing project. Formulating a well-defined and pertinent research question that aligns with the available data proved to be a significant hurdle, largely due to a lack of comprehensive knowledge and expertise in the domain of French novels. Additionally, our focus was predominantly on the execution of the project, rather than on the theoretical underpinnings.
The consequence of this approach was protracted meetings that yielded few tangible outcomes. There was an undue emphasis on the tasks that needed to be completed, rather than on the possibilities offered by the data set and how they might contribute to the field of digital humanities.  

A review of the project proposal reveals an undue emphasis on the 'literary form' component, with insufficient attention paid to the historical context of novellas in the Enlightenment era. This is evidenced by the literature consulted, which did not align with the specified dataset.  

Consequently, we commenced a more in-depth investigation into the Age of Enlightenment, with a particular emphasis on social culture, gender, and literature. Additionally, we sought to expand our research scope by:  
1) refining the primary inquiry  
2) formulating supplementary sub-questions  
3) augmenting our dataset with authors' occupational information.  

This resulted in the formulation of the following primary question:  

**“What trends can we observe in the dataset of French novellas between 1751 and 1800?”**  

Furthermore, two additional sub-questions were formulated as follows:  

- *“Are there noticeable correlations between specific authors' occupations and literary form trends during this period?"*  

- *“What is the relationship between gender and literary forms in these novellas?”*  

However, this approach had other shortcomings. These shortcomings are named within the ‘Challenges, solutions and ethical considerations’ section, within our Workflow. It also describes why it would have been an interesting addition anyway, which is indicated by means of literature. Unfortunately, to our disappointment, we had to limit ourselves to a relatively simple research question.

---
#### Notes
<small>

1) Brewer, D. (Ed.). (2014). *The Cambridge companion to the French enlightenment*. Cambridge University Press.
2) Hunter, J. P. (1996). The novel and social/cultural history. *The Cambridge Companion to the Eighteenth-Century Novel*, 9-40.
</small>

## Data acquisition
The dataset consists of 200 french novels written during the enlightenment era, and their metadata. This era is characterized by its exploration of contrasting ideas, social diversity, and the complex synthesis of material and spiritual realms, often challenging rigid societal roles and conventional forms of knowledge, especially in relation to self-understanding<sup>1</sup>  .

![Fig. 1 - Comparison of proportion of narrative forms per decade](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/2efbe0b8bc1ac3324ddda0e1da98c3ac2e6e878b/img/Screenshot%202024-09-22%20at%2022.09.42.png)  
Fig. 1 - Comparison of proportion of narrative forms per decade<sup>2</sup>

The authors / compilers of the corpus have stated that they have composed the body to reflect the historical distribution of the parameters gender, year of first publication, and narrative form<sup>1</sup> based on the 1977 “Bibliographie du genre romanesque français, 1751-1800”. Given that we are thus working with a balanced database representative of the general body of works of the time, our conclusions can to an extent be extrapolated to this larger body of data. 

However; not all parameters are balanced, and thus we do need to be attentive to not introduce unbalanced parameters into our analysis when intending to extrapolate our findings towards the general french enlightenment literary corpus. Additionally, the accuracy of the body of works listed by the bibliography which the corpus represents can be debated: As argued by Robert Darnton<sup>1</sup>, literature during the enlightenment period was subject to strong state censorship prompting authors to resort to publishing their work clandestinely, outside of legal channels. As women were expected to write about topics and to use forms that were deemed appropriate to their gender, we can expect their publications often to have landed in that domain. A bibliography of the french enlightenment based on archived publishing data therefore is a questionable source at best.

Furthermore; As the novels themselves are written in the French language and translation will take away from the needed nuance in the texts, we have chosen not to use the corpus itself initially, but rather focus on the metadata at hand for our analysis. However the data is available in case we do find observable trends in the metadata that we further wish to analyze based on keywords.

![fig. 2 - List of metadata parameters](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/2efbe0b8bc1ac3324ddda0e1da98c3ac2e6e878b/img/Screenshot%202024-09-22%20at%2022.40.22.png)  
Fig. 2 - List of metadata parameters


The metadata covers a wide range of parameters, divided between subjects ranging from data covering the author, the publisher, the place of birth and place of publication. Though the larger part of this data is valuable to the project, some of it is not, or refers to external data which is already present in the project. Furthermore, various observations are missing (multiple) parameters. Therefore we have scrutinized and filtered the data before use, initially coding missing data as (null), and later removing them. 


While working on a preliminary line of inquiry, in which we intended to look for correlations or trends between the author and other parameters, we added data about the author’s occupation(s). This line of inquiry was however dropped as it was deemed too time-intensive and the author data was only balanced according to their birth-year. This results in a significantly skewed distribution of authors.

---
#### Notes
<small>

1)  DiPiero, Thomas. “Enlightenmentliterature.” Chapter. In *The Cambridge Companion to the French Enlightenment*, edited by Daniel Brewer, 137–52. Cambridge Companions to Literature. Cambridge: Cambridge University Press, 2014.
2) Röttgermann, Julia. “The Collection Of Eighteenth-Century French Novels 1751–1800”, *Journal Of Open Humanities Data 10* (1 januari 2024), https://doi.org/10.5334/johd.201.
</small>

## Data Preprocessing Steps
The dataset was initially filtered to include only records from the period between 1750 and 1800. One novel from the year 1904 was excluded as it fell outside the temporal scope of interest.

Next, narrative forms were mapped to standardised categories. Specifically, 'autodiegetic' and 'homodiegetic' were both mapped to 'First-person'; 'heterodiegetic' was mapped to 'Third-person'; 'epistolary' remained as 'Epistolary'; and both 'mixed' and 'dialogue novel' were classified under 'Mixed/Dialogue'. This step reduced the complexity of narrative categories while preserving key differences that align with our research aims.  

We then filtered the dataset to retain only those records with complete narrative form and clearly specified author gender ('M' or 'F'), as our core research question focuses on examining gender-based trends in narrative form use. In this process, one record was removed due to missing narrative form, and six records were excluded because the author's gender was unknown.  

For the temporal analysis, the data was divided into 5-year intervals rather than decades (e.g., 1751-1755, 1756-1760, and so on). Using shorter time intervals allowed for a more nuanced exploration of shifts in narrative preferences over the course of the latter half of the eighteenth century.

## Methodology
### Tools Used
Python (Pandas, NumPy): Used for data preprocessing, such as filtering records by time frame and mapping narrative forms.
SciPy: Conducted Chi-square tests of independence, allowing us to assess the association between gender and narrative form for each 5-year period.
Seaborn and Matplotlib: Generated various visualizations, including stacked bar charts, line plots of p-values across time, and heatmaps of standardized residuals to highlight gender-based deviations for significant associations.

### Chi-Square Test and Residual Analysis
To assess the association between author gender and narrative form during each 5-year period, we used the Chi-square test of independence to determine whether there were statistically significant relationships between gender and narrative choice. The Chi-square test is well-suited for analyzing categorical data, particularly when exploring relationships between two categorical variables. In our study, both narrative form and author gender are categorical in nature:
Narrative Form: Categorical with different types such as 'First-person,' 'Third-person,' 'Epistolary,' etc.

### Gender: Categorical with two groups, 'Male' and 'Female.'
For time intervals that showed statistically significant associations between gender and narrative form, we performed standardized residual analysis to identify specific deviations. Residuals helped us determine which narrative forms were overrepresented or underrepresented for each gender, compared to the expected distribution. 

### Visualization
We employed a series of visualizations:
- Stacked Bar Plot: The stacked bar plot displayed the distribution of narrative forms used by male and female authors for each 5-year period. We enhanced readability through positive-negative axis design.Narrative contributions by male authors were shown above the axis, while female contributions were represented below it. 

- P-Value Line Plot: We conduct a line plot of p-values to see the overview of statistical significance across time intervals. The plot included a significance threshold line at p = 0.05, making it easy to identify periods that need further exploration.
- Heatmaps of Standardized Residuals: Heatmaps were employed to provide visual insights into significant periods identified by the Chi-square tests. The standardized residuals revealed which narrative forms deviated significantly from expected counts based on gender during the certain periods.

## Work Packages
Throughout the project, each team member contributed to discussions and decision-making. The team used weekly group meetings and WhatsApp to ensure that everyone remained informed and that tasks progressed smoothly. 


| Work Package | Team Member(s) | Description |
|--------------|----------------|-------------|
| Project Overview | Rob | Framing the scope of the project, including objectives, research question, and thesis statement
| Thesis statement | Nikol and Joanna | 
| Data Acquisition | Robert and Xingyun | Sourcing and preprocessing the dataset
| Methodology and Workflow Steps | Xingyun | Selecting statistical methodologies, documenting the workflow |
| Challenges, Solutions, and Ethical Considerations | Nikol and Joanna | Addressing challenges faced during the project, formulating solutions, and ensuring ethical data use
| Results, Documentation, and Sustainability | Robert and Xingyun | Summarizing the results, connecting them to the research question, and providing documentation for accessing and maintaining project outputs.|
| Reflection | Nikol and Joanna | Evaluating workflow effectiveness, identifying lessons learned, and suggesting future research directions. |

### Workflow Steps
1) Research and Formulation of Research Question: The initial stage focused on formulating an appropriate research question (RQ) aligned with both the dataset and historical context.
2) Data Augmentation: Authors' occupational data was fetched from Wikidata to enrich the dataset. However, after evaluating the reliability of the data, the data was discarded.
3) Refinement of Research Question: Following further literature review, the RQ was refined. 
4) Data Preprocessing: The dataset was filtered to include relevant years (1750-1800) and processed to remove incomplete records. Narrative forms were mapped into standardized categories.
5) Statistical Analysis: Chi-square tests were conducted to examine the association between author gender and narrative form across each 5-year period. Standardized residuals were used to gain deeper insights into significant periods.
6) Results, documentation, reflection: Summarizing the results, connecting them to the research question and reflection

### Alternative Approaches Considered:
We considered using logistic regression to assess gender-based trends in narrative form use, with narrative form as the dependent variable, gender as the independent variable, and an interaction term between time and gender to examine changes over time. However, despite some observable trends, the results were not statistically significant in our context. Therefore, we proceeded with Chi-square tests, as they were more suitable for analyzing categorical relationships.

### Documentation and Sustainability:
The project's data and code are accessible through our [GitHub repository](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6). This repository includes all necessary files, such as the metadata, Python scripts, README file. In the README file, We ensure clear documentation for environment setup and dependencies, providing transparency and easy reproducibility. Additionally, the repository contains an 'img' folder with all visualizations created during the project.

The dataset used for this project is sourced from [MiMoText/balance_novels](https://github.com/MiMoText/roman18/blob/master/metadata.tsv) for the Digital Humanities course. 
The code has been designed in a modular way, which makes it easy to modify or extend specific parts of the analysis without affecting other components. The dataset used in the project is publicly available and distributed under an open-source license, permitting other researchers to freely use, modify, and distribute the code and data, as long as proper credit is given to the original authors.
Reuse Potential
Linguistic Analysis: Researchers can use the dataset for linguistic tasks, such as analyzing language used by male versus female authors.
Cultural Analysis: Further studies can investigate shifts in cultural representation based on narrative form, especially in the context of Enlightenment-era literature.

## Challenges, solutions & ethical considerations
### Challenges and solutions

#### Incomplete metadata:  
Some novels in the dataset are missing key metadata such as the author’s occupation, gender, or specific narrative form, which limits the analysis potential for those works. To manage this, the metadata was scrutinised and filtered before analysis. When applicable, metadata gaps were supplemented using external authoritative sources, such as Wikidata.
#### Wikidata and its reliability :  
During the research, multiple sub questions were considered, including "Are there noticeable correlations between specific authors' occupations and literary form trends during this period?". This led to the enrichment of the dataset with an additional parameter, 'author_occupation', which relied on the pre-existing 'author_wikidata' parameter. After further research, it was confirmed that Wikidata is a sister project of Wikipedia, both of which can be edited by anyone. This allowed us to question the reliability of the information added to the dataset, as there was no indication whether it was correct/confirmed by official institutions.
#### Validity:  
Consequently, the reliability issue raises validity concerns which made us consider forsaking the use of additionally acquired data. It posed a threat to the outcome of our research as the process of gathering data in Wikidata is not transparent. Validity is crucial in quantitative research because it ensures that the data accurately represents the variables being studied, allowing for meaningful and trustworthy conclusions. If data cannot be verified, the findings of the research may be skewed or misinterpreted, leading to erroneous conclusions<sup>1</sup>. 
#### Classification of occupations :  
Many individuals had multiple professions, and Wikipedia/data classifications or similar references do not always accurately reflect whether these individuals made a living off a particular occupation or simply held a title. Noticing a correlation involving the parameter ‘occupation’ proves hard, as career shifts are not always adequately captured, leaving researchers with no contextualisation as to the specific period in the individual's life connected to the primary occupation. Thus, the relevance of authors' occupations in relation to the dataset could not be directly established.  
Nevertheless, subsequent research revealed that by 1750, the novella had become a significant force in literary history, capable of influencing the careers of both male and female writers. It would have been intriguing to examine which authors were able to sustain themselves financially through their writing and which were compelled to pursue other professions. This approach could have shed light on the evolution of literary careers and the shifting dynamics of authors' livelihoods. It became evident that this idea was untenable, given that there were insufficient opportunities to obtain reliable data on writers' occupations in the time preceding the deadline. Therefore we restricted the scope of our analysis to gender as a factor influencing narrative form. This was a more straightforward approach and was also more aligned with the specific dataset of French novels under examination.  
#### Emphasis on balanced parameters :  
The authors of the dataset claim that "the parameters gender, year of first publication and narrative form" are 'balanced'. The term entails that there is no significant over or under representation of any particular category or group, allowing for a more reliable and unbiased analysis. As gender and form are balanced, focusing on them allowed us to notice correlations without over-relying on other imbalanced parameters. This approach contrasts with “solutions to the class-imbalance problem” such as random oversampling or directed undersampling, which attempt to mitigate imbalance by artificially adjusting the dataset. Contextualising these trends within the known societal roles of men and women in the 18th century provided historical depth to our analysis.
#### Representativeness of the dataset:  
Despite efforts to create a balanced dataset, the 200 novels may not fully capture the diversity of literary production during the period due to limitations in available digitized materials or the small sample size compared to the total production of novels in France during 1751–1800. We acknowledge and transparently document the limitations in representativeness when interpreting results. The dataset could also be expanded in future research to improve representativeness.

### Ethical considerations
Focusing on the balanced parameters gender and form allowed us to minimise the impact of biases connected to representation of groups, such as female authors or marginalised social classes
Handling modern-day bias :  our modern day perspective could introduce bias in interpreting trends, especially related to gender and occupation. The used methodology allowed us to minimise subjective bias, focusing on observable trends, rather than speculative interpretations. For example, the way gender roles or narrative forms were understood in the eighteenth century differs significantly from today. Imposing contemporary values on historical data could lead to misinterpretation of trends or the erasure of important cultural nuances.
Documenting the decision-making processes within the group is a key ethical consideration. Keeping a record of data collection, analysis methods and interpretation processes, ensured that our work is transparent and open to critique. Acknowledging the limitations of the dataset allowed us to maintain accountability when it comes to the representation of historical trends, making sure the steps taken during the research can be traced in a later point in time. 

---
#### Notes
<small>

1) Bryman, Alan. 2015. *Social Research Methods*. 6th ed. London, England: Oxford University Press.
2) Ganganwar, Vaishali. "An Overview of Classification Algorithms for Imbalanced Datasets." *International Journal of Emerging Technology and Advanced Engineering 2, no. 4* (2012): 42-47. Accessed October 12, 2024. https://www.researchgate.net/profile/Vaishali-Ganganwar/publication/292018027_An_overview_of_classification_algorithms_for_imbalanced_datasets/links/58c7707a458515478dc4c68b/An-overview-of-classification-algorithms-for-imbalanced-datasets.pdf.  
</small>

## Results

![Fig. 3 - Distribution of Narrative Forms by Gender and Time Period]
Fig. 3 - Distribution of Narrative Forms by Gender and Time Period

On first sight, it becomes apparent that the distribution of authors based on gender is skewed heavily towards male authors across the observed time frame, with a slow rise of female authorship visible towards the end of the century. French women’s role in literature was particularly notable in the evolution of the female role. Early on, women primarily wrote in genres considered acceptable for them, such as moral treatises, educational novels, and children’s literature. However, as time progressed, female authors began to explore a broader range of genres, reflecting their growing presence and influence in the literary world.<sup>1</sup>

![Fig. 4 - Distribution of Narrative Forms by Gender and Time Period](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/2efbe0b8bc1ac3324ddda0e1da98c3ac2e6e878b/img/p_values_acrossTime.png)  
Fig. 4 - P values across time

Fig. x: Distribution of Narrative Forms by Gender and Time Period
Our data show that over time, there has been a modest increase in the number of women writing novellas. This increase is statistically significant during three distinct periods: 1766-1770, 1786-1790, and 1796-1800.

Between period 1766 -1770, and period 1796 -1800 we observed a significant association between gender and narrative form, with female writers favoring the epistolary form more than men. During the period 1786-1790, female authors strongly preferred the Mixed/Dialogue form while male authors under-used it.

The results indicate that our thesis statement, which predicted an increase in women writers writing in the epistolary/mixed dialogue form, is only partially confirmed. Furthermore, it is essential to interpret the results with caution, as the observed significance is minimal.

The results of the chi-square tests reveal varying levels of association between gender and narrative form.The analysis begins with the overall finding that for many periods, there was no statistically significant association between these two variables, as indicated by p-values above the common significance threshold (p > 0.05).

However, three key periods stood out with significant associations. The periods 1766-1770 (p = 0.047), 1786-1790 (p = 0.019), and 1796-1800 (p = 0.024). To further investigate these significant periods, a residual analysis was conducted to understand the specific patterns underlying the chi-square results. This analysis of standardised residuals provides insights into which narrative forms were disproportionately associated with each gender.

![Fig. 5 - Standardized Residuals for Narrative Forms in 1766 - 1770](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/2efbe0b8bc1ac3324ddda0e1da98c3ac2e6e878b/img/sr_1766-1770.png)  
Fig. 5 - Standardized Residuals for Narrative Forms in 1766 - 1770

Between 1766 and 1770, we are able to observe a significant association between gender and narrative form for the first time; it becomes apparent that in this period, female writers favor epistemological writing more than men,as evidenced by consistently positive residuals.
This period was one of political and social unrest, partucilarly surrounding the debates on personal freedom and national identity following the 7 years war and the rise of enlightenment ideals

![Fig. 6 - Standardized Residuals for Narrative Forms in 1786 and 1790](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/2efbe0b8bc1ac3324ddda0e1da98c3ac2e6e878b/img/sr_1786-1790.png)  
Fig. 6 - Distribution of Narrative Forms by Gender and Time Period

Between 1786 and 1790, the Mixed/Dialogue form is strongly preferred by female authors, while male authors under-use the form. This is confirmed by positive residuals for females and negative residuals for males.
This period coincides with the aftermath of the american revolution and the beginning of the french revolution, two events concerned with issues of liberty, equality and rights 

![Fig. 7 - Standardized Residuals for Narrative Forms in 1796 - 1800](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/2efbe0b8bc1ac3324ddda0e1da98c3ac2e6e878b/img/sr_1796-1800.png)  
Fig. 7 - Standardized Residuals for Narrative Forms in 1796 - 1800

Between 1796 and 1800 there is again a significant favour towards Epistolary forms by female authors in this period, again with male writers under-using the narrative form.
Here, we see the intensification of the french revolution and the rise of napoleon, which created an atmoshpere of uncertainty and personal reflection. Would this be a reason  that the epistolary form of writing allowed female authors to mediate between the public and the private, engaging with public discourses in a style that was accepted for women?

---
#### Notes
<small>

1)  McIlvanney, Siobhán. “Women Writers and Readers: The Beginnings of French Women’s Journals and Le Journal Des Dames (1759–1778).” In *Figurations of the Feminine in the Early French Women’s Press*, 1758–1848, 57–98. Liverpool University Press, 2019. https://doi.org/10.2307/j.ctvqr1bqv.6.  
</small>  
  
## Reflection

### Workflow effectiveness and lessons learned  
Throughout the project, each team member contributed to discussions and decision-making. The team used weekly group meetings and WhatsApp to ensure that everyone remained informed and that tasks progressed smoothly. 
Addressing incomplete or inconsistent entries ensured that our analysis was based on reliable data, like the balanced parameters. The discussions surrounding the main parameters to be used in the research highlighted the importance of transparency in the data documentation. The diverse backgrounds of the team members allowed us to approach the dataset from different angles, focusing on the cultural and social aspects brought forward by a number of our study fields. 

### Future research directions 
as the authors suggest, further research can investigate linguistic differences between genders, as well as literary and cultural trends during the enlightenment could employ nlp to analyse the contents of the novellas themselves, rather than focusing primarily on the metadata [as we’re doing] - identifying thematic trends.  
Partnering with experts in eighteenth-century literature could improve the accuracy and richness of the analysis. These collaborations would help ensure that historical nuances are fully integrated into the interpretation of trends.
Analysing connections between authors, their patrons, or literary circles to uncover how relationships influenced literary production and trends over time?

During the research project, issues connected to historical context and the challenges of working with data were raised. Expanding the dataset and incorporating more advanced analytical techniques can provide richer insights into trends in 18th century literature.



## Team description
| Name | Curicculum|
|------|-----------|
Nikol | Mkda - Art history with a focus on media studies  
Joanna | Communication, american studies  
Robert | Anthropology  
Rob | Information science with a focus on journalism and information interpretation  
Xingyun | Computer science  

## References

- Brewer, D. (Ed.). (2014). *The Cambridge companion to the French enlightenment*. Cambridge University Press.
- Bryman, Alan. 2015. *Social Research Methods*. 6th ed. London, England: Oxford University Press.
- DiPiero, Thomas. “Enlightenmentliterature.” Chapter. In *The Cambridge Companion to the French Enlightenment*, edited by Daniel Brewer, 137–52. Cambridge Companions to Literature. Cambridge: Cambridge University Press, 2014.
- Ganganwar, Vaishali. "An Overview of Classification Algorithms for Imbalanced Datasets." *International Journal of Emerging Technology and Advanced Engineering 2, no. 4* (2012): 42-47. Accessed October 12, 2024. https://www.researchgate.net/profile/Vaishali-Ganganwar/publication/292018027_An_overview_of_classification_algorithms_for_imbalanced_datasets/links/58c7707a458515478dc4c68b/An-overview-of-classification-algorithms-for-imbalanced-datasets.pdf. 
- Hunter, J. P. (1996). The novel and social/cultural history. *The Cambridge Companion to the Eighteenth-Century Novel*, 9-40.
- McIlvanney, Siobhán. “Women Writers and Readers: The Beginnings of French Women’s Journals and Le Journal Des Dames (1759–1778).” In *Figurations of the Feminine in the Early French Women’s Press*, 1758–1848, 57–98. Liverpool University Press, 2019. https://doi.org/10.2307/j.ctvqr1bqv.6.  
- Röttgermann, Julia. “The Collection Of Eighteenth-Century French Novels 1751–1800”, *Journal Of Open Humanities Data 10* (1 januari 2024), https://doi.org/10.5334/johd.201.

