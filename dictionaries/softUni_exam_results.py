def process_submission(submissions, username, language, points, number_of_submissions):
    if language not in number_of_submissions:
        number_of_submissions[language] = 1
    else:
        number_of_submissions[language] += 1

    if username in submissions:
        if language in submissions[username]:
            submissions[username][language] = max(submissions[username][language], points)
        else:
            submissions[username][language] = points
    else:
        submissions[username] = {language: points}


def print_results(submissions):
    print('Results:')
    for username, languages in submissions.items():
        max_points = max(languages.values())
        print(f'{username} | {max_points}')


def print_submissions(number_of_submissions):
    print('Submissions:')
    for language, count in number_of_submissions.items():
        print(f'{language} - {count}')


submissions = {}
bans = []
number_of_submissions = {}

while True:
    command = input()

    if command == 'exam finished':
        break

    tokens = command.split('-')

    if len(tokens) == 3:
        username, language, points = tokens
        points = int(points)
        process_submission(submissions, username, language, points, number_of_submissions)

    elif len(tokens) == 2:
        username, action = tokens
        if action == 'banned':
            bans.append(username)


for username in bans:
    if username in submissions:
        del submissions[username]

print_results(submissions)
print_submissions(number_of_submissions)