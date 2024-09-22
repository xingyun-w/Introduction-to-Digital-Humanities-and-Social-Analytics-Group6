# Assignment 1: Project Proposal and Group Charter


### Course:
Introduction to Digital Humanities and Social Analytics  
Vrije Universiteit Amsterdam


### Group 6
*Robert Cornelis  
Rob Goudriaan  
Joanna Rejnowska  
Nikol Velkova  
Xingyun Wang*


## Research Question
*”How did the distribution of authors by gender change between 1751 and 1800, and 
what was the relationship between this and the narrative forms of the novel?”  
Subquestion:  
“To what extent does the narrative form from 1751 to 1800 reflect societal changes and developments within cultural movements?”*


## Thesis statement
The latter half of the 18th century saw a rise in female authors and their impact on novel narrative forms. By "novel narrative forms," we refer to the narrative techniques, especially the narrator's perspective. From 1751 to 1800, there was a shift toward introspective, emotion-driven narratives, such as epistolary and first-person forms, reflecting Romanticism's focus on individual emotion.

Existing literature primarily addresses the creation of the dataset<sup>1</sup> and focuses on 'topic modeling' using computational techniques<sup>2</sup>. This reveals a gap for research using the dataset as a tool to explore Humanities questions.

The form of stories, shaped by patterns, sequence, and perspective, reflects not only the novel itself but also the normative realities of the time<sup>3</sup>. Stories offer insights into the social, cultural, and historical contexts of their era<sup>3, 4</sup>.

The most critical aspect is narrative perspective, which, combined with action, profoundly influences reader comprehension (Zeller, 1995). Authors' techniques shape how facts and events are presented.

### Notes
1. Hinzmann, Marc, Julian Röttgermann, Andreas Klee, Marc Steffes, and Christof Schöch. 2021. "The French Enlightenment Novel as a Graph? Potentials and Challenges in the Construction of a Knowledge Network." DOI: 10.5281/zenodo.5840088
2. Klee, Anne, und Julia Röttgermann. 2022. „„Nuit, Correspondance, sentiment”: Topic Modeling Auf Einem Korpus Von französischen Romanen 1750-1800“. Apropos [Perspektiven Auf Die Romania], Nr. 9 (Dezember):57-86. https://doi.org/10.15460/apropos.9.1888.
3. Famà, Santi Luca. 2023. “Decentering the Human through Narrative Forms: The ‘Impossible Closure’ of Gadda’s That Awful Mess and VanderMeer’s Southern Reach Trilogy”. Incontri. Rivista Europea Di Studi Italiani 37 (1). https://doi.org/10.18352/inc12758.
4. Zeller, Nancy. 1995. “Narrative Strategies for Case Reports.” International Journal of Qualitative Studies in Education 8 (1): 75–88. doi:10.1080/0951839950080108.


## Nature of the Dataset

![Fig. 1 - Comparison of proportion of narrative forms per decade<sup>5</sup>](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/main/Screenshot%202024-09-22%20at%2022.09.42.png?raw=true)  
Fig. 1 - Comparison of proportion of narrative forms per decade<sup>5</sup>

The authors of the corpus designed it to reflect the historical distribution of gender, publication year, and narrative form, creating a balanced dataset representative of the broader body of works<sup>5</sup>. This allows us to extrapolate conclusions to a larger extent, though caution is needed regarding unbalanced parameters. Since the novels are in French and translation may lose nuance, we opted to focus initially on the metadata, though the text data is available if keyword-based trends warrant further analysis.


![fig. 2 - List of metadata parameters](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/main/Screenshot%202024-09-22%20at%2022.09.33.png?raw=true)  
fig. 2 - List of metadata parameters

The metadata spans a wide range of parameters, including details about the author, publisher, birthplace, and place of publication. While much of this data is useful, some is redundant or irrelevant, and various observations lack certain parameters. Thus, the dataset requires careful scrutiny and filtering, with missing data properly coded.

### Notes
5. Röttgermann, Julia. “The Collection Of Eighteenth-Century French Novels 1751–1800”, Journal Of Open Humanities Data 10 (1 januari 2024), https://doi.org/10.5334/johd.201.


## Pre-processing of the dataset
### Data Modeling and Selection
The metadata is sufficient for our research. Key entities are:
- au-name: Author's name
- au-gender: Author's gender
- firsted-yr: Year of first publication
- form: Narrative form
- author_MimoText-ID: Author's identifier in MiMoTextBase, a knowledge graph on 18th-century French novels.
We chose firsted-yr for its relevance to the original cultural context, unlike printSource-yr, which reflects later editions. The MiMoText-ID allows for broader cross-examination if needed.

### Normalization
We filtered the dataset to include works published between 1751 and 1800 using the firsted-yr column. Some values in au-gender are marked "U" (unknown), and in form as "mixed" or "unknown." These will be retained for transparency and documented in our findings.

### Classification
Categories for gender and narrative form were defined and encoded for analysis:
- Gender: Male, Female, Unknown
- Narrative Form: First-person (autodiegetic, homodiegetic), Third-person (heterodiegetic), Epistolary, Mixed/Dialogue, Unknown
Data will be grouped by narrative form and gender, and analyzed by decade to track gender distribution changes over time.


## Sources
Famà, Santi Luca. 2023. “Decentering the Human through Narrative Forms: The ‘Impossible Closure’ of Gadda’s That Awful Mess and VanderMeer’s Southern Reach Trilogy”. Incontri. Rivista Europea Di Studi Italiani 37 (1). https://doi.org/10.18352/inc12758.

Hinzmann, Marc, Julian Röttgermann, Andreas Klee, Marc Steffes, and Christof Schöch. 2021. "The French Enlightenment Novel as a Graph? Potentials and Challenges in the Construction of a Knowledge Network." DOI: 10.5281/zenodo.5840088

Klee, Anne, und Julia Röttgermann. 2022. „„Nuit, Correspondance, sentiment”: Topic Modeling Auf Einem Korpus Von französischen Romanen 1750-1800“. Apropos [Perspektiven Auf Die Romania], Nr. 9 (Dezember):57-86. https://doi.org/10.15460/apropos.9.1888.

Röttgermann, Julia. “The Collection Of Eighteenth-Century French Novels 1751–1800”, Journal Of Open Humanities Data 10 (1 januari 2024), https://doi.org/10.5334/johd.201.

Zeller, Nancy. 1995. “Narrative Strategies for Case Reports.” International Journal of Qualitative Studies in Education 8 (1): 75–88. doi:10.1080/0951839950080108.


# Group Charter 
### Group goals
Our main goal is to develop the skills to think like digital humanities researchers, evaluate existing perspectives, and propose original insights. To do this, all team members must engage critically with the relevant literature. We also aim to learn from each other, drawing on our diverse backgrounds, and foster lively discussions. Meeting deadlines is important, not as an end, but as a way to demonstrate our progress to our professors.

### Individual and group strengths
Table one lists the skills for each team member. It is evident that each individual possesses unique qualities. It would be beneficial to utilize this information effectively and learn from one another. When, for instance, a task requires coding, it is important to ensure that the individual with the relevant skills is assigned to it, while others observe and learn from the process. 

| Robert                 | Rob               | Joanna                 | Nikol               | Xingyun
|------------------------|-------------------|------------------------|---------------------|---------------
| writing & editing      | critical thinking | critical text analysis | literature research | programming
| media design           | design            | academic writing       | summarizing         | data visualization
| controlling/organizing | oral presentation |                        | writing             | critical study

Table 1: Overview of skills

### Pressures
Deadlines and compulsory attendance are pressures in this course, but with clear planning and communication, they can be easily managed. Since this minor is voluntary, we expect others to be intrinsically motivated to learn new skills.

### Communication strategies
We’ll communicate via WhatsApp, aiming for a response time of under two hours. Weekly two-hour meetings at the VU will allow us to brainstorm, divide tasks, and work together. All assignment documents will be stored in a shared drive, and we’ll respond to comments within a day.

### Planning
Table two outlines the planning, along with a brief overview of the meetings.

- 25-09-24: We’ll assign tasks for the group project. If we’ve received feedback on our proposal, we’ll discuss, reflect, and adjust our plan. We’ll also rehearse our presentation to check the timing.  
- 02-10-24: This meeting will focus on preparing the data for analysis, ensuring everyone understands the decisions. One person will document the process for inclusion in our research.  
- 09-10-24: By this meeting, the data must be analyzed. We’ll discuss the results and their implications, then reassign tasks for writing the introduction, methods, etc.  
- 16-10-24: We’ll finalize details, address any challenges, and discuss how we want to present our research.


| Date     | Task                                                           |
|----------|----------------------------------------------------------------|
| 22-09-24 | Deadline: Assignment 1 & Group Charter                         |
| 25-09-24 | Meeting                                                        |
| 25-09-24 | Presentation  -discussion of feedback -rehearse presentation   |
| 02-10-24 | Meeting -data analysis                                         |
| 09-10-24 | Meeting -results and implications of analysis -task assignment |
| 16-10-24 | Meeting -address challenges -discuss how to present research   |
| 18-10-24 | Deadline: Documentation of the workflow                        |
| 18-10-24 | Deadline:Project presentation                                  |
| 21-10-24 | Final exam                                                     |

Table 2: Deadline of assignments and time schedule

### Sources













