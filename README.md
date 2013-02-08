golem
=====

golem - file-copy and backup tool

An animated anthropomorphic being, created entirely from inanimate matter.

Usage
-----

	python golem.py <source> [<dest>]

config.json
-----------

Put a **config.json** inside your project to tell something to **golem**.

###Ignored
Ignore specified files and/or folders.

Exemple

	{
	    "Ignored": ["file1", "file2", "folder/file3"]
	}

With this configuration, golem not will copy and backup **file1**, **file2** and **file3** in **folder**

###Destination
Define the file-copy and backup destination. Params **dest** is optional if **Destination** is set in **config.json**

Exemple

	{
	    "Destination": "path/to/a/folder"
	}
