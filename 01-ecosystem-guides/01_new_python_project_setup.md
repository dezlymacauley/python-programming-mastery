# New Python Project Setup
_______________________________________________________________________________

Create the directory
```sh
mkdir new-python-project
```
_______________________________________________________________________________

Enter the project directory
```sh
cd new-programming-mastery
```

For the rest of this guide, all commands must be run from this directory.
_______________________________________________________________________________

Decide on which version of `uv` you want your project to use.

`uv` is a package manager that is specifically for Python projects.

It was created by a company called Astral that use Rust to create 
high performance Python tools with an excellent developer experience.

You can view is what the latest version of uv by running this command.
```sh
mise latest uv
```

Or you can view all the available versions of uv that you can select
```sh
mise ls-remote uv
```
_______________________________________________________________________________

This is how to set the version of uv that all Python projects 
in the directory will use
```sh
mise use uv@0.10.4
```
______________________________________________________________________________

This will create a `mise.toml` file in your project

mise.toml
```sh
[tools]
uv = "0.10.4"
```
______________________________________________________________________________

Add this to the end your `mise.toml` file

```toml
[settings]
python.uv_venv_auto = true
```

This tells `mise` to automatically activate the virtual environment created
by uv when you enter the project directory, 
and to also deactivate the virtual environment when 
you are not in your project directory.

This virtual environment will be created later in this guide.
_______________________________________________________________________________

Create a `.gitignore` file

```sh
touch .gitignore
```

Add this to the file. 

If a gitignore file already exists, replace the contents with this
```gitignore
# The Python virtual environment
# This is where uv will install the Python version required for the project
# and the project dependencies
.venv/

# Used by ruff to speed up code formatting
.ruff_cache/ 

# Created by Python to speed up importing of modules
__pycache__/
```
_______________________________________________________________________________

Add a `ruff.toml` file

```sh
touch ruff.toml
```

Add this to the file:
```toml
line-length = 80
```
_______________________________________________________________________________

The next step is to decide what version 
of Python you want your project to use.

NOTE: I am using using mise to check the Python version.

I will have uv install the Python version in my project.

```sh
mise latest python
```
Or you can view a list of specific versions:
```sh
mise ls-remote python
```
_______________________________________________________________________________

For the guide I have chosen Python version 3.14.2

Initialize the project
```sh
uv init --bare -p 3.14.3
```

This will create a `pyproject.toml` file
_______________________________________________________________________________

Open the `pyproject.toml` file and change `>=` to `==`

So this line:
```toml
requires-python = ">=3.14.3"
```

Should be changed to 
```toml
requires-python = "==3.14.3"
```
_______________________________________________________________________________

Create a .python-version file:

```sh
touch .python-version
```

Add your python version to the file:
```sh
echo 3.14.3 > .python-version
```
_______________________________________________________________________________

Please note:

At this point, your project is NOT using the Python version that is listed 
in your `pyproject.toml` or your `.python-version`

You can confirm this by running `which python`

If you get something like this:
```
/usr/bin/python
```

That means that your project is using the Python version 
of your operating system.

This is because you have not created and activated 
a Python virtual environment.

_______________________________________________________________________________

Run this command to remind yourself of what Python version you chose:
```sh
cat .python-version
```

Create a Python virtual environment.
```sh
uv venv -p 3.14.3
```

This is where `uv` will install the Python version required for this project.

When you install project dependencies later, 
they will also be installed in this directory.
_______________________________________________________________________________

The last step to this:
```sh
uv sync
```

Then exit the project directory
```sh
cd ..
```

And re-enter the project directory
```sh
cd new-python-project
```

If you see this at the end of your path,
then that means that your project is using the virtual enviroment 
that was set by uv.
```
.venv/bin/python
```
_______________________________________________________________________________

Create a `.mise-tasks` directory
```sh
mkdir .mise-tasks
```

Then create the following files:
```sh
touch .mise-tasks/clean.sh
touch .mise-tasks/rebuild.sh
touch .mise-tasks/start.sh
```

_______________________________________________________________________________

Make the scripts in mise-tasks executable,
by running this command from the root of your project directory.
```sh
chmod +x .mise-tasks/*.sh
```
_______________________________________________________________________________

Add this to the `.mise-tasks/clean.sh` file
```sh
#!/usr/bin/env bash
#MISE description="clean the '.ruff_cache/', '__pycache__' and '.venv/' directories"
#MISE quiet=true

rm -rf __pycache__
rm -rf .ruff_cache
rm -rf .venv
```
_______________________________________________________________________________

Add this to the `.mise-tasks/rebuild.sh` file
```sh
#!/usr/bin/env bash
#MISE description="rebuild the virtual environment and project dependencies"
#MISE quiet=true

# Ensure that this is a clean build
rm -rf __pycache__
rm -rf .ruff_cache
rm -rf .venv

# Rebuild the the virtual environment and install the dependencies
uv sync
```
_______________________________________________________________________________

Add this to the `.mise-tasks/start.sh` file:
```sh
#!/usr/bin/env bash
#MISE description="start the project by running main.py"
#MISE quiet=true

python main.py
```
_______________________________________________________________________________

Create a `main.py` file

```sh
touch main.py
```

Add this to the file:
```sh
def main():
    print()
    print("New Python Project")
    print()

if __name__ == "__main__":
    main()
```
_______________________________________________________________________________

To star your project:

```sh
mise start
```

NOTE: You can't create a command call `run` because `run`
is a reserved word in `mise`. That's why I named the command `start`

If you see this, then that means everything is working.
```

New Python Project

```

_______________________________________________________________________________

To see the list of commands in your project:
```sh
mise tasks
```

```
Name     Description
clean    clean the '.ruff_cache/', '__pycache__' and '.venv/' directories
rebuild  rebuild the virtual environment and project dependencies
start    start the project by running main.py
```
_______________________________________________________________________________

If you know you won't be working on your project for a while,
you can save on disk space by running the custom command:

```sh
mise clean
```
_______________________________________________________________________________

If you ever want to setup your project after cleaning it, 
or your have just cloned it. Just run:

First give `mise` permission to read the `mise.toml` file
```sh
mise trust
```

This will automatically use `uv` to get the correct Python version from 
your `.python-version`, install it if it isn't installed, 
and then create a virtual environment in your project directory.

_______________________________________________________________________________

Use this command to setup your project 
```sh
mise rebuild
```
_______________________________________________________________________________
