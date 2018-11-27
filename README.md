# Overview
The purpose of the repo is to practice some Python (both for solving the problems and testing the solutions).

# Tasks
You can find the latest version of the problem set [here](https://github.com/oy-vey/PythonMentoring/issues). You are welcomed to discuss it in the comment section.

# Prerequisites
You may want to install the `pytest` [framework](https://docs.pytest.org/en/latest/contents.html) which is used to perform automatic unit testing. It can be installed via pip:

```shell
sudo pip install pytest
````

Before committing a change you may test it by executing `pytest` command in the repository root folder via CLI.
However, you can rightfully omit this step, since all of the tests are performed via CircleCI when the code is pushed to the remote.

If you want to learn more about `pytest`, please visit this [page](https://docs.pytest.org/en/latest/example/index.html). 

# IDE
There are no strict requirements regarding the development environment, however, if you want to feel the charms of debugging your own code, you may want to try out using the latest version of the [PyCharm community edition](https://www.jetbrains.com/pycharm/download/). It is free and will cover all of your development necessities over and above. 

# Coding style
The Zen of Python teaches us that it is always better when something is beautiful than when something is ugly. PyCharm IDE has an automatic PEP integration, so it'll highlight all of the code snippets which are not in accordance with the PEP standard. Please, pay attention to it, and I'll be grateful to you!


# Testing
As mentioned above, automatic testing is performed via `pytest`. The testing scenario is based on the `run_test.py` file. Additional trivial test cases will come up alongside with the problem definition. You may enhance and adjust them with a more advanced logic.  

# Task submission workflow
1. Create a separate branch (e.g. task5). **You are supposed to create a separate branch for each task.**
1. Create a solution file in the tasks folder (e.g. `./tasks/task5.py`). If you need any manual auxiliary modules, please put them in the tasks folder as well.
1. Commit your code in the newly created branch.
1. (Optional) When the task seems to be completed, test it via `pytest`.
1. If all the tests run seamless, push the change to the remote, create a pull request to the master branch and add me to the reviewer's section.

# Contact
Should you have any questions or suggestions, feel free [to contact me](mailto:Daniil_Skokleenko@epam.com).
