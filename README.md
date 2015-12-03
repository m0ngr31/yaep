YAEP - Yet Another Environment Package
======================================

As the name says, this package enters the crowded field of 
environment related packages.  The main goal of this package
is to provide you with the ability to populate your
environment with a a source (by default reading a .env file)
and then use a simple function in your configuration files
to read these values or use defaults.

It's worth noting that this software is under active
development and interfaces will change without warning.

Usage
-----

Usage is simple. Early in the execution of your project, or
in a dedicated module for configuration, import `populate_env`
from the yaep package.  Running this will populate your
environment with values from your .env file.  You can
alternatively set the env_file argument or the ENV_FILE
environment variable to read from another env file.

    from yaev import populate_env
    populate_env()

Now you can setup your configuration. For example, in a
settings.py or config.py:

    from yaev import env
    DATABASE_URL = env('DATABASE_URL', 'sqlite://:memory:')

The env function has a few other useful tricks.  For example,
allowing for a default that is "sticky" - meaning if it is
employed it is set in the environment.

    os.getenv('foo')  # Returns None
    FOO = env('FOO', 'bar', sticky=True)
    os.getenv('FOO')  # Returns 'bar'

Additionally, you can by default allow for boolean-like values
to be changed to booleans on the fly.

    os.getenv('SOMETHING')  # Returns 'True'
    env('SOMETHING')  # Returns True

By default a case-insensitive comparison to 'True' and 'False'
is done, along with 1 and 0.  You can change the available
values by modifying `yaep.boolean_map`.

Using Other Environment Sources
-------------------------------

A goal of the project is to be able to override or add to the
default of pulling values in from an env file. Supporting
alternate sources such as credential servers is the goal.

Work in this area is slated for a future release.
