#!/usr/bin/env bash

: <<'DOCUMENTATION'

Poetry does not provide monorepo support, but exploratory work in Jupyter notebooks,
and other custom Python scripts may need additional Python packages not specified in
the Poetry environment. And not all exploratory work ends up in production.

Adding exploratory Python packages to the Poetry environment may overcomplicate, and
introduce unwanted dependency issues. However, when moving towards production,
issues may occur if a package version used in exploration cannot be added to the Poetry
environment due to conflicts. This script attempts to solve this issue.

Poetry installs into an underlying exploratory Python environment. This script uses
`pip` to modify this exploratory environment for exploratory use, without affecting the
Poetry environment package list, but uses this Poetry environment package list as
constraints. This means any `pip install`-ed packages will not conflict with those in
the Poetry environment.

This exploratory environment is then frozen for version control purposes, and can then
be reproduced in the future (if necessary).

New, or updated packages for the exploratory work can be added by deleting any existing
`requirements.txt` file, and recreating the exploratory environment.

The Poetry environment can be restored by running the `make contributor-requirements`
command in your terminal.

DOCUMENTATION

# Show the help message
if [ $# -eq 0 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ] ; then
    echo ""
    echo "Description:\n  Install Python packages for exploratory work into the" \
      "Python environment, constrained\n  by, but not affecting, the project's Poetry" \
      "environment.\n\n  If a \`requirements.txt\` file already exists, the" \
      "underlying exploratory Python\n  environment will be updated from this" \
      " file.\n\n  If this file does not exist, the desired Python packages will be" \
      "installed into the\n  exploratory environment, with all their dependencies" \
      "constrained by the Poetry\n  environment. This will then be frozen into a new" \
      "\`requirements.txt\` file for future\n  reproducibility. Any desired Python" \
      "packages must be pinned to specific versions\n  unless the \`--not-strict\`" \
      "option is supplied.\n\n  You must delete an existing \`requirements.txt\` file" \
      "before adding, or updating Python\n  packages for the notebook.\n\n  To" \
      "restore the exploratory environment to match the Poetry environment, run" \
      "the\n  \`make contributor-requirements\` command in your terminal.\n"
    echo "Usage:\n  source $0 [options] <name>...\n"
    echo "Arguments:\n  name\t\t\t\tThe packages to add.\n"
    echo "Options:\n  -h, --help\t\t\tShow help.\n  --not-strict\t\t\tDo not check" \
      "that packages have versions pinned."
    return
fi

# Restore the exploratory Python environment from an existing `requirements.txt` file
# constrained by the Poetry environment.
#
# To add or update packages in the exploratory environment, delete any existing
# `requirements.txt` file first, and re-run this script
if [ -f requirements.txt ]; then
  if (pip install -q --constraint constraints.txt -r requirements.txt); then
    echo "Exploratory environment restored; to add or update packages, delete the" \
      "\`requirements.txt\` file first, and re-run this script."
    return
  else
    echo "Could not restore the exploratory environment from \`requirements.txt\` file!"
    return 1
  fi
else
  echo "No \`requirements.txt\` file found. Will attempt to add exploratory Python" \
    "packages constrained by the project's Poetry environment."
fi;

# Check if the Python packages have been pinned
if [ "$1" = "--not-strict" ]; then
  shift
else

  # Iterate across every Python package specified, and check the version has been pinned
  for arg in "$@"
  do
      if [[ ! "$arg" == *"=="* ]]; then
        echo "Could not set the exploratory environment! Python package needs to be" \
          "pinned to a specific version: \`$arg\`"
        return 1
      fi;
  done

fi;

# Restore the Poetry environment before adding exploratory packages; dump `stdout`
# outputs are not noisy
if ! (make -s --directory ../../ contributor-requirements 1>/dev/null); then
  echo "Could not restore Poetry environment!"
  return 1
fi;

# Create a temporary folder for the `pip` constraints file
constraints_directory=$(mktemp -d)
constraints="$constraints_directory"/constraints.txt

# Freeze the Poetry environment as a `pip` constraints file
if ! (pip freeze --quiet --exclude-editable > "$constraints"); then
  echo "Could not freeze Poetry environment as constraints!"
  return 1
fi;

# If there is no `requirements.txt` file, install required packages for this notebook
# to run, constrained by the Poetry environment
if (pip install --quiet --constraint "$constraints" "$@"); then
  echo "Exploratory environment set for this notebook."
else
  echo "Could not restore, or set the exploratory environment for this notebook!"
  rm -rf "$constraints_directory"
  return 1
fi;

# Export the exploratory environment for version control
if (pip freeze --quiet > requirements.txt); then
  echo "Exploratory environment exported to \`requirements.txt\`."
else
  echo "Could not export newly-created exploratory environment!"
  rm -rf "$constraints_directory"
  return 1
fi;

rm -rf "$constraints_directory"
