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

## day 4
Yes I fell into the; do part one without thinking that "I bet part two adds validation"

Sample data starting to not do enough, i.e. multiple validations all in one go, but I was in that need to get the result to get up the (private) scoreboard a bit.

## day 5
Oh I wrote some rubbish before the binary hit me in refactoring, then I could simplify the first part down to one line with a function to calc the ticket id

Part two is still annoying, I know there's a gap in the list, what's the quickest/neatest way to find it...

And as for writing a test for part 2 meant writing a function to create a list of tickets with a gap in it.... test the test?


## day 6
Another input data where each group can bve over multiple lines, so switch to reading data split by 2 line breaks `\n\n` rather than each line. I didn't think this would include the last line but it does (could go back and refactor the earlier days but onwards...)

This did mean I needed to sort tests and how to pass in a multi line string and parse into same list as the file input does to then enable calling the functions.

Part one pretty easy, remove newlines in data, use list to break all the string into individual characters and then use a set to get unique values. Then just count the length and add to the total. I bet this is easier in functional languages.

Part two then breaks the above that we need to consider the common values for each passenger (line)... hmmm intersection useful here? yes it was

[later] refactoring, I got part 1 down to 1 line, must remember to use sum() more often

part 2 condensed things by using *args for the intersection, but cant see how to reduce it further

## day 7
Oh boy this got more complex. Could see there was a parent/child relationship but took ages to work out both parts today

### part 1
I created a set of "rules", a parent colour and all its children colours. Then the count was a case of using recursion to find them all, do a set to get a unique list and return the length = total

### part 2
Of course my original rules was not enough, now we need the counts included. Write a new rules generator (no not a python generator!) and used that.

Recursion again to work through the list of parent/children and count it all up.

Now I have 2 rules generators so refactored into a single one, but it complicated part 1 (as I needed to ignore the number and just look at colours)

> If this is the step up for day 7, I dread to think of tomorrow...

## day 8

Part 1 seemed ok but needs refactoring after my q&d stab at it

Part 2 recursion again, modified part 1 to be able to be called with the modified program (jmp/nop change) to see if it'd complete to the end. I used negative to indicate it had, ok for here but what if the answer had been a negative? Well, it wasn't and that's all that matters here.

I've now got 2 processors that are similar, so more refactoring to do.
