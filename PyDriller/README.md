# cogitate_tool

Tool to analyze contributions when working in a team.

## Installing Pydriller

To install the program, type in the following command in your terminal:

```
> pip install pydriller
```

This installs necessary dependencies as well.

## Helpful links

Here is a link to a video to install and use the program. It helpfully explains
what methods and repositories Pydriller contains, as well as what objects to instantiate in order to track specific commit information.

[Youtube Link](https://www.youtube.com/watch?v=7Oui4bP9eN8)

Here is a link to a research article that goes into detail about the productivity
and effectiveness of the Pydriller tool. It makes several conclusions about Pydriller, the most prominent of which state that Pydriller helps write, on average, half the amount of code needed, as well as making the code 60% less complex when compared to similar tools. The tool was evaluated by developers as well as similar tools, and all developers agreed that Pydriller was much better.

[PDF Link](https://www.sback.it/publications/fse2018td.pdf)

## Important features

- Pydriller is able to check commits during certain dates. To perform this action,
use the function `datetime`.
- Pydriller checks to see if a single commit is finished with exit code 0. While
it is checking the commit, you can see the commit message that was used. With This
you can see if someone broke or if someone fixed code.
- Another feature is you can see what people have added and/or deleted. Therefore, 
you can tell if a big or small change has been made.