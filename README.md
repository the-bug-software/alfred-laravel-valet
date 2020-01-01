# Laravel Valet Alfred Workflow

### Installation
1. [Download the latest version](https://github.com/thebugsoftware/alfred-laravel-valet/releases/download/v1.0.0/laravel-valet.alfredworkflow)
2. Install the workflow by double-clicking the `.alfredworkflow` file
3. You can add the workflow to a category, then click `Import` to finish importing. You will now see the workflow listed in the left sidebar of your Workflows preferences pane.

### Usage

Just type `valet` and you will see a list with all your projects.

![Screenshot 1](https://raw.githubusercontent.com/thebugsoftware/alfred-laravel-valet/master/screenshots/screenshot-1.png)

In the background, the command will call a Python script that will scan for Laravel Valet's defined paths.

After the script finds the paths, it then scans the pats defined and will list all the directories/projects that it finds.

![Screenshot 2](https://raw.githubusercontent.com/thebugsoftware/alfred-laravel-valet/master/screenshots/screenshot-2.png)

You can then select one project from the list, and it will be opened in your default browser.
