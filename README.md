## Selenium + Python + Pytest + Github Actions + pytest-html reporter

# Project setup on local machine

1. `git clone <repo link>`
2. Install and activate virtual environment. Check more here https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
3. Set Python interpreter in Settings > Python Interpreter > select dropdown > choose <path_to_your_local_project_folder>
4. Navigate to the folder where is 'requirements.txt' module
5. Run `pip install -r requirements.txt` in CLI

# Run tests project setup

> Project allows to run tests in parallel with headless/headed mode using passed browser name and version (desktop or mobile/tablet) with 'pytest -m=regression -n=2 -v --browser=chrome --headless=true' command. Note! If there are more CPU's set than test modules with opened browsers are launched => tests may fail unexpectedly.
