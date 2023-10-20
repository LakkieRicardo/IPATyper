# IPA Typer

This is a tool to find the exact symbol for the sound you're trying to describe. I often find myself having to look up with Google to find the Wikipedia page for a certain sound. And, often I have to go to the chart, which isn't that quick or helpful.

Instead, I want to describe the location of a vowel for instance, or the type of sound and have the application try to narrow it down for me.

## Solution

The way that I chose to solve this problem was to make a list of all of the IPA sounds and give each symbol a list of characteristics. Then, you can search from a multitude of characteristics to continuously narrow down the possibilities until you find the right character you're looking for.

For example, if you want to search the symbol "P" you could look up "plosive" and get a list of plosive characters. Then, you can use the arrow keys and 

## Usage

To find the symbol simply specify characteristics of the sound and press "Tab". Then, use the arrow keys to select the sound and once you've found it, press "Tab" again to copy it to your clipboard.

If the list isn't specific enough you can press enter and query exclusively from the filter you defined earlier. This narrows down the list and you can choose a specific characteristic you're looking for. For example, to find a _Voiceless bilabial plosive_, or [p], you might first type "plosive" and press "Tab". If you can't find the [p] in that list but are sure that it's voiceless, you can press "Enter" to narrow it down to that list and start a new query. From there, you rinse and repeat until you find the sound.

## Areas of Improvement

This was made with my single use case in mind and there are areas which can be improved to make the application more useable for different people. Here is a brief list of those possible improvements

- **Fuzzy searching.** Most of the time you don't know the exact manner of articulation, so if the app can know the distance between places of articulation, it might help the user find the sound they're looking for.
  - One option for this might be to have a model of which places of articulation are close to which, and add some sort of margin of error.
- **Non-scientific terminology.** For example instead of searching "plosive" for [p], you could search through different transcriptions depending on your native language, or combinations of letters to help narrow it down.
- **Integration with Apps.** Discord, Google Docs, etc. integration.
- **Look up symbols.** Press a certain button and look up exactly what that symbol sounds like, or actually play the sound.
  - It could also be a configurable option(play sound, open Wikipedia page, open page from another source, copy to clipboard, etc.). However, this would require user setting storage and would complicate the app.
- **Tutorial.** A tutorial for how to use all of the features in the software.
- **Sound varieties.** Make the lookup dictionary more comprehensive, including variants of each sound.
- **Scrollable results.** Make the history of queries scrollable.
- **Undo query.** Make it possible to undo a query by pressing "Escape" in the query dialog, or by pressing "Backspace" with nothing typed.