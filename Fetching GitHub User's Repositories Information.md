# Fetching GitHub User's Repositories Information

### ✅ Objective:
In this task will learn how to use the GitHub API to fetch information about a GitHub user's repositories and display relevant details using Python.

### ✅ Requirements:
Basic knowledge of Python programming.
Understanding of APIs and HTTP requests.
Python libraries: requests.

### ✅ Tasks:
1. Fetch User's Repository Data - Write a Python function fetch_user_repositories(username) that takes a GitHub username as input and fetches information about the user's repositories from the GitHub API. The function should return a list of dictionaries, with each dictionary representing a repository and containing details such as name, description, language, and number of stars.
2. Display Repository Information - Write a function display_repository_info(repositories) that takes a list of repository dictionaries as input and displays relevant information about each repository, such as its name, description, language, and number of stars.
3. Main Function - Write a main function main() that prompts the user to enter a GitHub username, fetches the user's repositories using fetch_user_repositories() function, and displays the repository information using display_repository_info() function.

EXAMPLE API - https://api.github.com/users/{username}/repos


### 🌟 **What is an API?**

API stands for Application Programming Interface. In the context of software development, an API is a set of rules and protocols that allows different software applications to communicate with each other. It defines the methods and data formats that developers can use to interact with a particular software component, service, or platform.

**Purpose of APIs:**

1. **Integration:** APIs allow different software systems to communicate and share data with each other seamlessly. For example, social media platforms often provide APIs that allow third-party applications to access user data, post updates, and interact with the platform's features.

2. **Extensibility:** APIs enable developers to extend the functionality of existing software applications by integrating additional features and services. For instance, developers can integrate payment gateways, mapping services, or messaging services into their applications using APIs provided by those services.

3. **Automation:** APIs facilitate automation by enabling software programs to interact with each other programmatically. This automation streamlines processes, reduces manual intervention, and improves efficiency. For example, an e-commerce website can use APIs to automatically retrieve shipping rates, track shipments, and update inventory levels.

4. **Standardization:** APIs define a standardized way for different software components to interact, promoting interoperability and compatibility across various systems and platforms. This standardization simplifies development and integration efforts, making it easier for developers to build robust and scalable software solutions.

5. **Access to Data:** APIs provide access to data and resources hosted by external systems or services. This access allows developers to leverage existing data sources and utilize external functionalities without having to recreate them from scratch. For instance, weather APIs provide real-time weather data that developers can integrate into their applications to display weather forecasts.

APIs play a crucial role in modern software development by enabling interoperability, extensibility, automation, and access to data. They empower developers to build innovative and integrated software solutions that leverage the capabilities of external services and platforms.
