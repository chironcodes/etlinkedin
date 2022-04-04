# ETLinkedin


> Follow your dream, work hard, practice and persevere .



<img src="./.src/capa.jpeg" alt="classic ETL template">






## :hammer: Extract:

    After we enter our credentials, Selenium starts the whole extraction process. First, selenium access your contacts page and dynamically loads your whole list. 
    After that, we scrap the whole page for profile's urls applying a List Comprehension rule to filter only those that are no commercial account(those with '/in/' on it). Later on we iterate through our list and its where our next takes place...






##  :mag:Transform:

    For each profile visit we scrap only for the infos we want: experience, education, licenses and certifications and courses; all those who can tell us a bit about someone's hard skills and knowledge.






## :floppy_disk:  Load:

    Both previous processes of our pipeline happens sequentially and so does our load. For each page we scrap we load, the info in our SQL db(sqlite). We assign a unique id for each account, only so we can make relations between tables taking care to *NOT STORE ANY PERSONAL DATA* eg:name,e-mail etc.






<img src="./.src/dashboard.jpeg" alt="classic ETL template">

> After we finish our ETL pipeline, all the data is exported to a `.csv` format so you can build your own dashboard using any known BI tool like Google Data Studio, Qlik, Power Bi, Tableau.



After the whole process you get substantial data from your network and now it's your time:

# What history can you tell about this?









Authors:

:bust_in_silhouette: Diego Alves inboxdgo@gmail.com

:bust_in_silhouette: Adilton Costa Anna adiltoncss@gmail.com

