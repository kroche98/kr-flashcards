import pandas as pd

FILENAME = 'data.csv'
REPS_REQUIRED = 2 # number of times each question must be answered correctly
ADDITIONAL_REPS = 1 # additional reps required for each incorrect answer

df = pd.read_csv(FILENAME, names=['term', 'definition'], dtype='str')
df['reps_left'] = REPS_REQUIRED

while df['reps_left'].sum() > 0:
    row = df.loc[df['reps_left']>0].sample().iloc[0]
    term, definition, _ = row
    inp = input(f'{definition}: ')
    if inp == term:
        df.loc[row.name, 'reps_left'] -= 1
        print(f'Correct!')
    else:
        df.loc[row.name, 'reps_left'] += ADDITIONAL_REPS
        print(f'Incorrect! Correct answer: {term}')
    input()

print('Complete!')
