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

## day 3

### part 1

Did this by working through the terrain and keep a count of my x position (y is the line I'm processing). After checking if there's a tree I can increment the x position by the offset (3) and if it runs off the side of the map, then just rotate back to the start by how far it went over by.

### part 2

As the offset was variable it was easy to pass this as a parameter and worked out of the gate, but the change to the vertical offset meant I changed to an enumerate to allow me to know the line I was on and then do a mod to see if the line is processed or skipped.

Getting a total just means doing all the calls and multiplying them together (didn't see a need to test this)

I do like the ability to parametrize pytest tests with `@pytest.mark.parametrize`, it made extending the test using AoC's example data to cover the various offsets easy to add.

### day 4

Yes I fell into the; do part one without thinking that "I bet part two adds validation"

Sample data starting to not do enough, i.e. multiple validations all in one go, but I was in that need to get the result to get up the (private) scoreboard a bit.

### day 5

Oh I wrote some rubbish before the binary hit me in refactoring, then I could simplify the first part down to one line with a function to calc the ticket id

Part two is still annoying, I know there's a gap in the list, what's the quickest/neatest way to find it...

And as for writing a test for part 2 meant writing a function to create a list of tickets with a gap in it.... test the test?
