# Flashcard App

This is a simple app for learning and studying terms. It's pretty basic and only has a command line interface at the moment.

The items to be studied go in data.csv. The first column is the answers, and the second column is the prompts.

The flashcards are presented in random order. By default, you must get each term correct twice, and if you get one wrong, an additional repitition is added to reinforce it. These can be changed by modifying the ```REPS_REQUIRED``` and ```ADDITIONAL_REPS``` constants.

Sample data with US state capitals is provided.

## TODO

- Better UI
- Better method of adding terms
- Handle differences in capitalization and other acceptable variants
