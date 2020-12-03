# AoC-2020
https://adventofcode.com/2020

## day 1

Do the usual code, refactor, refactor... slap wrist, no tests!

Seeing a functional submission that used combinations was a lightbulb moment... hold on `itertools` has `combinations`, that's way neater and more readable.

I did a list comprehension version but the downside is you can't break out of that so it runs for the whole list, whereas the one using a `for` can just do a return with the result as soon as it finds it.

## day 2

Ok some tests this time (bit late still, next time... TDD)

Again a code, refactor to make it neater/readable, faster?

Started to use `re` as you can do a split on multiple strings, but then thought, just replace the '-' with a space, then split it all in one go.

Left previous way of splitting into a list and working on that, but you can split to a tuple (very fragile but hey, the data is clean)

I did steal the idea of doing the total increment based on True = 1, False = 0 but part of me thinks it's less readable than using an `if`

Python doesn't have an xor for the 2nd part of the challenge, but doing a `bool != bool` gave me the same thing

