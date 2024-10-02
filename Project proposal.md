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
The research question we have chosen to answer, using our dataset is as follows: 
”What trends are we able to observe in the dataset of French novellas between 1751 and 1800?”

Furthermore, we will endeavor to respond to the following sub-question, which will assist us in developing a more comprehensive response to our primary query:
“What trends are we able to observe based on the parameter gender”
“What trends are we able to observe based on the parameter form”
“What trends are we able to observe based on the parameter Publication Date”
“What trends are we able to observe based on the author’s date of birth?
“What trends are we able to observe based on the author’s occupation?

  Several points need clarification in relation to our main question. This is due to the fact that our primary inquiry comprises two key elements: gender distribution on the one hand and the novel's stylistic approach on the other. In this investigation, we will examine the potential interrelationship between these two aspects.
	Firstly, it is important to clarify that the term 'gender' refers to the gender of the author of the novella. This is an interesting parameter, as it can provide valuable insights into gender dynamics during the French early modern period. Secondly, the term "novel narrative forms" refers to the narrative techniques and strategies employed in novel corpora, with a particular focus on the narrator's perspective. This parameter is worthy of further investigation, as it may yield insights into gender dynamics during the French early modern period. Accordingly, this is subjected to further scrutiny within the context of our sub-question.

## Thesis statement
“The latter half of the 18th century was marked by a growth in the prominence of female authors and their influence on novel narrative forms. A clarification is needed in relation to our main question. The term "novel narrative forms" refers to the narrative techniques and strategies employed in novel corpora, with a particular focus on the narrator's perspective. The period from 1751 to 1800 witnessed a move towards introspective and emotion-based narratives. Examples are epistolary and first-person narratives, reflecting cultural shifts and movements rooted in the Romantic focus on individual emotion.”

## Relevance of research question
  The dataset assigned to us concerns 'A Collection of Eighteenth-Century French Novels 1751-1800'. This dataset was first released in 2020 and last updated in December 2023. First, the available literature focuses on the creation of the dataset <sup>1</sup>, which allows us to identify its strengths and weaknesses. Second, existing research based on the created dataset has mainly focused on 'topic modeling', research based on complex computational techniques <sup>2</sup>. This reveals a gap for research using the dataset as a tool to explore Humanities questions.
  We can see that there is concrete work being done with humanities data, but what seems to be missing is research that focuses concretely on a humanities question, using the available dataset merely as a tool. 
  The existing (meta)data offers us three interesting points on which research can be done, namely (1.) gender, (2.) narrative perspective, and (3.) date of publication. As Digital Humanities students, given the available data, we are interested in normative realities, linguistic issues and gender norms. We think it would be interesting to connect these issues in order to arrive at interesting findings.
  The form in which stories are written, created by patterns, sequence and perspective, reflects not only the literary object, in this case the novel, but also the normative reality of the time in which they were written, as well as the lives of the people living in that period<sup>3</sup>. As stories reflect the natural world and its context, they offer a stable understanding of the social, cultural and historical context of their era<sup>3, 4</sup>. 
  From our perspective, the most significant aspect of this form is the narrative perspective, which, in conjunction with the action, exerts a profound influence on the reader's perspective and comprehension<sup>4</sup>. This is because facts and incidents are shaped on paper by the authors' techniques, structure, and perspectives.

### Notes
1. Hinzmann, Marc, Julian Röttgermann, Andreas Klee, Marc Steffes, and Christof Schöch. 2021. *"The French Enlightenment Novel as a Graph? Potentials and Challenges in the Construction of a Knowledge Network."* DOI: 10.5281/zenodo.5840088
2. Klee, Anne, und Julia Röttgermann. 2022. *„„Nuit, Correspondance, sentiment”: Topic Modeling Auf Einem Korpus Von französischen Romanen 1750-1800“*. Apropos [Perspektiven Auf Die Romania], Nr. 9 (Dezember):57-86. https://doi.org/10.15460/apropos.9.1888.
3. Famà, Santi Luca. 2023. *“Decentering the Human through Narrative Forms: The ‘Impossible Closure’ of Gadda’s That Awful Mess and VanderMeer’s Southern Reach Trilogy”*. Incontri. Rivista Europea Di Studi Italiani 37 (1). https://doi.org/10.18352/inc12758.
4. Zeller, Nancy. 1995. *“Narrative Strategies for Case Reports.”* International Journal of Qualitative Studies in Education 8 (1): 75–88. doi:10.1080/0951839950080108.  


## Nature of the Dataset

  The dataset consists of 200 french novels written during the enlightenment era and their metadata. This era is characterized by its exploration of contrasting ideas, social diversity, and the complex synthesis of material and spiritual realms, often challenging rigid societal roles and conventional forms of knowledge, especially in relation to self-understanding<sup>4</sup>.

![Fig. 1 - Comparison of proportion of narrative forms per decade<sup>5</sup>](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/e3c2db4e6920796d1bc05763f87e075e44d5a484/resources/img/Screenshot%202024-09-22%20at%2022.09.42.png)  
Fig. 1 - Comparison of proportion of narrative forms per decade<sup>5</sup>  

  The authors / compilers of the corpus have stated that they have composed the body to reflect the historical distribution of the parameters gender, year of first publication, and narrative form<sup>5</sup>. Given that we are thus working with a balanced database representative of the general body of works, our conclusions can to an extent be extrapolated to this larger body of data However as not all parameters are balanced, we do need to be attentive to not introduce unbalanced parameters into our analysis. 
  As the novels themselves are written in the French language and translation will take away from the needed nuance in the texts, we have chosen not to use the corpus itself initially, but rather focus on the metadata at hand for our analysis. However the data is available in case we do find observable trends in the metadata that we further wish to analyze based on keywords.

![fig. 2 - List of metadata parameters](https://github.com/xingyun-w/Introduction-to-Digital-Humanities-and-Social-Analytics-Group6/blob/e3c2db4e6920796d1bc05763f87e075e44d5a484/resources/img/Screenshot%202024-09-22%20at%2022.40.22.png)  
fig. 2 - List of metadata parameters  

The metadata covers a wide range of parameters, divided between subjects ranging from data covering the author, the publisher, the place of birth and place of publication. Though the larger part of this data is valuable to us, some of it is not, or refers to data that is already present in the metadataset. Furthermore, various parameters are missing for multiple observations. The set therefore needs to be scrutinized and filtered before use, with missing data coded as such.

### Notes
5. DiPiero, Thomas. “Enlightenmentliterature.” Chapter. In *The Cambridge Companion to the French Enlightenment*, edited by Daniel Brewer, 137–52. Cambridge Companions to Literature. Cambridge: Cambridge University Press, 2014.
6. Röttgermann, Julia. *“The Collection Of Eighteenth-Century French Novels 1751–1800”*, Journal Of Open Humanities Data 10 (1 januari 2024), https://doi.org/10.5334/johd.201.  


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


## References
DiPiero, Thomas. *“Enlightenmentliterature.” Chapter.* In The Cambridge Companion to the French Enlightenment, edited by Daniel Brewer, 137–52. Cambridge Companions to Literature. Cambridge: Cambridge University Press, 2014.

Famà, Santi Luca. 2023. *“Decentering the Human through Narrative Forms: The ‘Impossible Closure’ of Gadda’s That Awful Mess and VanderMeer’s Southern Reach Trilogy”.* Incontri. Rivista Europea Di Studi Italiani 37 (1). https://doi.org/10.18352/inc12758.

Hinzmann, Marc, Julian Röttgermann, Andreas Klee, Marc Steffes, and Christof Schöch. 2021. *"The French Enlightenment Novel as a Graph? Potentials and Challenges in the Construction of a Knowledge Network."* DOI: 10.5281/zenodo.5840088

Klee, Anne, und Julia Röttgermann. 2022. *„„Nuit, Correspondance, sentiment”: Topic Modeling Auf Einem Korpus Von französischen Romanen 1750-1800“.* Apropos [Perspektiven Auf Die Romania], Nr. 9 (Dezember):57-86. https://doi.org/10.15460/apropos.9.1888.

Röttgermann, Julia. *“The Collection Of Eighteenth-Century French Novels 1751–1800”*, Journal Of Open Humanities Data 10 (1 januari 2024), https://doi.org/10.5334/johd.201.

Zeller, Nancy. 1995. *“Narrative Strategies for Case Reports.”* International Journal of Qualitative Studies in Education 8 (1): 75–88. doi:10.1080/0951839950080108.


# Group Charter 
## Group goals
Our main goal is to develop the skills to think like digital humanities researchers, evaluate existing perspectives, and propose original insights. We also aim to learn from each other, drawing on our diverse backgrounds, and foster lively discussions. 

## Individual and group strengths
Table one lists the skills for each team member. It is evident that each individual possesses unique qualities.  

| Robert                 | Rob               | Joanna                 | Nikol               | Xingyun
|------------------------|-------------------|------------------------|---------------------|---------------
| writing & editing      | critical thinking | critical text analysis | literature research | programming
| media design           | design            | academic writing       | summarizing         | data visualization
| controlling/organizing | oral presentation |                        | writing             | critical study

Table 1: Overview of skills  

## Pressures and communication
Deadlines and compulsory attendance are pressures in this course, but with clear planning and communication, they can be easily managed. The latter will take place via WhatsApp, with file sharing happening through GoogleDrive. With both, the main aim is a response within the day. Weekly two-hour meetings at the VU will allow us to brainstorm, divide tasks, and work together.

## Planning
Table two outlines the planning, along with a brief overview of the meetings.  

| Date     | Task                                                                      |
|----------|---------------------------------------------------------------------------|
| 22-09-24 | Deadline: Assignment 1 & Group Charter                                    |
| 25-09-24 | Meeting <br> - discussion of feedback <br> - rehearse presentation        |
| 25-09-24 | Presentation                                                              |
| 02-10-24 | Meeting <br> -data analysis                                               |
| 09-10-24 | Meeting <br> -results and implications of analysis <br> -task assignment  |
| 16-10-24 | Meeting <br> -address challenges <br> -discuss how to present research    |
| 18-10-24 | Deadline: Documentation of the workflow                                   |
| 18-10-24 | Deadline:Project presentation                                             |
| 21-10-24 | Final exam                                                                |

Table 2: Deadline of assignments and time schedule














