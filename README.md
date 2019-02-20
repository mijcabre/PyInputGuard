# PyInputGuard

## What it is:
PyInputGuard is a collection of simple functions for enforcing input data types for text-based programs. It takes care of converting strings to the desired type, and includes functions to loop until the user gives valid input.
There is also an included test file with simple unit tests for functions. It was mostly for my own personal use when writing this, but have included it anyway in case it helps anyone else in some way.

## When to use it:
Use a PyInputGuard function in place of the built-in input function to save some time on validating input.

## Why I made it:
I made this because I was tired of writing validation code for user input, and figured I might as well make something sharable while I'm at it. This was also the first time I decided to use GitHub outside of work so it was a bit of an experiment with version control for personal use.
Also, I wanted to start building up a personal Github profile.

## How to use it:
You can just import the methods from this file just like any other. Just put it in the same directory as your main file.
For an example that imports all functions: `from PyInputGuard import *`

## Other personal notes:
Is it perfect? No. Is it pretty? Depends on your standards. However, I think that it's worth using, especially if you're writing programs that rely on a lot of user input.