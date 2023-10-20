# Search Improvements

This is an outline of the improvements I have planned to optimize the search engine.

## Fuzziness

One of the most important things to implement is to give the search engine somewhat of a feel of "fuzziness." This means that search terms don't have to be perfectly exact, and the user only has to give a general location of where the sound is to actually find it.

However, there's a fine line between having the search terms be exactly matched and having them be "too" fuzzy. An example of each end of the spectrum is running a `Ctrl+F` "Find" on a "List of Consonants" Wikipedia page, and on the other side going into ChatGPT and trying to describe the sound you're looking for.

### Place of Articulation

One of the categories that will be searched is the place of articulation(bilabial, labiodental, etc.). Although some of the sounds' locations are easy to identify like bilabial, other ones might not come to mind immediately or might be mistaked(post-alveolar vs. alveolar).

*Solution*: To give some leniency, we can create a map of different places of articulation that are described in the `ipa-typer.json` file, and figure out what the threshold for what constitutes a "similar place of articulation" that is the most useful in finding sounds.

### Terminology

One of the problems with searching for sounds is that you don't always know the name of the sound. A sound might actually be an approximant, but unless you already know that you might not look for it in the search engine.

*Solution*: [describe solution here]

### Similar sounds

In the initial version of the search engine, only sounds that matched perfectly with what the user was describing are displayed. The central problem that I am trying to fix is that we want to be able to move in any direction possible. Instead of just being able to move to a narrower and narrower filter, we might also want to look to the side and zoom out.

In more real terms, the problem is that we need to be able to find sounds that are similar to sounds that we already know.

*Solution*: [describe solution here]