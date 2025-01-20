# Python Contacts App

## Project structure

The project structure is the following:

```
contacts/
│
├── .gitignore
├── app.py
├── LICENSE
├── README.md
├── utils.py
└── tests.py
```

### contacts

The project folder is named "*contacts*". Inside it we will have all the files related to the project.

### .gitignore

*.gitignore* is a very important file. It defines which files must be ignored when synching with the remote repository. It is useful when we use configuration files, temporay output file, etc.

### app.py

This python source file implements the main program logic. It is used to start the app and prompt the user with the choice of the action to take.

In this file we do not implement the program functionalities, but only the communication with the user.

In this app we can:
- See all the contacts
- Add a contact
- Delete a contact
- Search for a contact

Contacts are stored as a python dictionary.

```
TODO:
Use sqlite instead of a python dictionary.
```

### utils.py

This python source file implements the operational logic of the Contacts App that *app.py* offers.

Here we have the implementation of all the functions that handle the contacts:
- Add a contact
- Delete a contact
- Search for a contact

### tests.py

No tests, no merge. This is the rule. Every change **_must_** be tested before merging.

Here we can find the test on every program functionality.

## Workflow

1. Il primo commit conterrà solo i file vuoti.

2. Vengono implementati separatamente README.md e app.py (versione base)

3. Viene aggiunta una nuova feature: mostrare tutti i contatti.

4. Viene aggiunta una nuova feature: aggiungere un contatto.

5. Viene aggiunta una nuova feature: eliminare un contatto.

6. Viene aggiunta una nuova feature: cercare un contatto.

Ad ogni step, valutare (e in caso implementare) eventuali casi di test.

## Project Development

### Team

A development team is required. Since the project is qiute simple, every member is a Developer. Chose one member that will also serve as Project manager. 

### Cooperation

To cooperate, every team member should be able to access the repository. The project manager is in charge of creating a new repository and then sharing it with the team members. To share a repository on GitHub, go on the project page. Then go on `Settings > Collaborators > Add people` and enter the information of each team member.

### Pull requests

The only user allowed to merge on the main branch is the project manager. Hence, every team member (even the project manager) should open a new *pull request* instead of merging directly.

When a branch is ready to be merged on the master, push it to the remote repository. Then, go to `Pull requests > New pull request`. Select as *base* your main branch (or the branch that should accept the changes) and as *compare* the branch with the changes. Click on `Create pull request`. 

Within this interface, you can add a title for the pull request and a description. You can also assign one or more Reviewers (in this case, the project manager). At last, click on `Create pull request`.

Now the project manager can review the pull request, add comments and ask for changes or accept it.

Pull request authors can’t approve their own pull request or ask for changes.

