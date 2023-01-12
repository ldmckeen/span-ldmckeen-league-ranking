# Documented Notes for Span Reviewers

Below is a brief outline of some items for the Span team Reviewing:
### Caveats
This could have been just a single one script file solution. The setting up of classes and
env files and optional variables wasn't exactly necessary, but for the sake of showcasing
a simple python application with some optional extras I decided to add the ‘fluff' in.

Other files in repo for git ignores, pep8 checks, per-commits etc are standard files for
good git practices I've used previously, these are common to many of the repos I use on a
daily basis so I’ve referenced those and implemented them on this repo as well.

*Comment on the comments:* Normally I would not write as many comments file header summaries
and descriptions in the files themselves as ideally the code should be readable and intuitive
enough to derive meaning, context and logic flow from the code itself, but again for the sake
of ‘demo’ purposes in this case it was just for an in depth showcase of the solution to the
problem statement presented and tasked.

Same goes for print statements, but as it’s a command line application I figured printing
to the console to update the user with as much infor as possible, this was a valid and
necessary use case.

Any further info please don’t hesitate to reach out to me.
I can disclaim this code was written entirely by myself (albeit with some references to online
python resources and stack overflow for some non in-brain-memory syntax's and library
functions etc. :-P

### Troubleshooting
Handling multiple line input paste from the command line was tricky with newlines not being
handled correctly by default, in the end the best solution I could find was to loop through
python’s built in `input` method, store in a list and then join list into a string to remove
newlines added and replicate reading from a file.
