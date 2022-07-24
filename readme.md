For the last 100+ days I have been comparing my wordle guess to what wordle-bot thinks are the optimum guesses.
https://www.nytimes.com/interactive/2022/upshot/wordle-bot.html
The great thing about wordle-bot is that is looks at every guess you make and gives you recommendations about how you did. As I used wordle-bot more and more, I came to realize that the bot plays the second guess in a very different way than I normally do (did). I used to think "I got a green letter here, so I need to make sure my next guesses always keep that letter there (like hard mode, but optional)". Same for yellow letters. I would always make sure I used those letters again, but in a different place of course. What I have seen from wordle-bot is that it almost ALWAYS abandons some of the clues given from the first response (I use the term "clue" to refer to the response given from wordle after you make a guess).

For example, a couple of weeks ago the answer was PHASE. Here's how I played it (which matched wordle-bot)
 C R A N E
⬛⬛🟩⬛🟩

 S L O T H
🟨⬛⬛⬛🟨

 P H A S E
🟩🟩🟩🟩🟩

You can see that the second guess did not use the 'A' or 'E' from the first guess, and instead went for maximum information with one new vowel and four new consonants. After those two guesses and clues, there was only one possible answer left. Had I wanted to keep the 'A' and 'E', I might have tried something like GLAZE for the second guess, which would have left several possible answers (FLAME, SHAME, etc, and of course, PHASE). SLOTH was the optimum second guess because it eliminates the most answers on average.

There's no shortage of websites, videos and people offering what they think are the best possible start words for wordle. I hope to come up with some good strategies for the second guess.

Wordle-bot likes CRANE for the first guess, and that's what I always use. I screen-shot every game I complete and record the first clue information in a spreadsheet. I then look at wordle-bot and see what, if anything, I could have done better. I have 100 games worth of data and I would like to share with you what I have learned from those games.

In those 100 games, I have seen 44 different patterns of clues: GGXXY, GGYXY, etc. One pattern I have seen ten times: XXYXX and there are 26 patterns that I have only seen once. The first thing I was curious about was how many possible patterns are there when CRANE is the start word, and what is the distribution frequency for the patterns. I wrote a python program that compares a given start word to all 2309 answers and shows all of the possible clues and the frequency. It turns out that with just 100 games played, I have seen clues that will relate to 76.6% of all games. There are a handful of clues that will only relate to one answer and that's it, so they are pretty rare. Although I have seen one of them so far! So for now, I can expect one out of four games to have a first clue different from any that I have seen so far. As I play more, that percentage will go up. And whenever I get a new clue pattern that I have never seen before, I check wordle-bot to see what it would have done.

Out of all of the second guess words I currently have (38), only three of them are related to more than one clue pattern. SLOTH is used any time there are all blanks in the clue, which is by far the most common clue (I think this will be the most common clue for any start word, but I haven't tested that yet). SLOTH is also the prefered response for two other clue patterns (XXGXG and XXGXX), for a total of 355 answer words. TOILS and PILOT are also the prefered second guess for three clue patterns (TOILS: XXXXG, XXYXX, YXXXX; PILOT: XGXXX, XXXYX, YXXXY), accounting for a total of 290 and 126 answer words respectively. There are also two second guess words that are paired with a single clue pattern but have pretty high frequencies, and that is SLEET (XXXXY) and BESET (XYXXY). Of course all of this is only based on the 100 games I have had analysed by wordle-bot. There will almost certainly be more clue patterns that will apply to some of these words that I just haven't seen yet.

So, what's the best word to use when faced with a new pattern? I think SLOTH and TOILS are great second words. PILOT, SLEET and BESET could also be considered. I also like the idea of "abandoning" the greens and yellows from the first (CRANE) guess, and almost think of the second guess as a continuation of the first guess. I (almost) never play to win on the second guess--I play to gather as much information as possible.

I don't see any way to simplify or generalize the optimum second guesses so far. I was hoping for something like "whenever there is a green E and any other yellows, use this word", or "if there are no green letters, use this word". So far, it doesn't seem to be playing out like that. If any of you see any useful patterns, then let me know.

That's it for my analysis. I will continue to keep checking my work against wordle-bot, and I feel like I have learned some good strategies for the second guesses, even if I haven't come up with any great simple second-guess rules.


Here is my python source code for checking my first guess against the entire answer list:


And here is a spreadsheet with all of the supporting data:
https://docs.google.com/spreadsheets/d/1skpmQ-yDAQmIb1nRWRRpSg_QSk137K4yeRBSq_MbfTg/edit?usp=sharing