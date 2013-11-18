# Django Unleashed

This repository holds all of the code for [Django Unleashed](https://Django-Unleashed.com). If you find this code helpful, please buy the book.

All of this code is open-source under 2-clause BSD-license.

The code is written using [Django 1.8](https://djangoproject.com). The [full reference documentation for Django 1.8 may be found here](https://docs.djangoproject.com/en/1.8/).

## IMPORTANT

This repository is **frozen**. To allow for the commit hashes in the book to link to the code in this repository, errors will not be fixed, and pull requests will be ignored. Errata will instead be listed on the [Django Unleashed](https://Django-Unleashed.com) website.

For any help with Django, please ask questions on [the official Django User mailing list](https://groups.google.com/d/forum/django-users). This will be a far quicker way of getting help than contacting me directly (and if you use the word "unleashed" in your email, my email will flag it. I will try to respond, if possible).

## Walking the Repository

To make perusing the code in this repository as simple as possible, the project defines its own `.gitconfig` file with custom commands (aliases).

To enable the commands, you must first point your local git configuration at the file provided. Either of the two commands below will work.

```shell
# relative path
git config --local include.path "../.gitconfig"
# absolute path
git config --local include.path "`pwd`/.gitconfig"
```

This will enable the following git commands:

- `git chapter #` <br />
This will list all of the commits relevant to that chapter. For example, `git chapter 17` will show all of the commits used in Chapter 17.

- `git next` <br />
Move to the next example in the book.

- `git prev` <br />
Move to the previous example in the book.

For those who prefer a GUI, [Atlassian's SourceTree](https://www.atlassian.com/software/sourcetree/overview) is a good alternative to the commands above.
