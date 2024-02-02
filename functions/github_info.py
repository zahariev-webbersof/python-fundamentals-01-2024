import requests


def fetch_user_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print('Error!')
        return None


def display_repository_info(repositories):
    if repositories:
        print("\nUser's Repositories:")
        print(repositories)
        for repo in repositories:
            print('\nRepository Name:', repo['name'])
            print('Description:', repo['description'])
            print('Language:', repo['language'])
            print('Stars:', repo['stargazers_count'])


def main():
    username = input('Enter GitHub username: ')
    repositories = fetch_user_repositories(username)
    if repositories:
        display_repository_info(repositories)


if __name__ == '__main__':
    main()