Our scoring method works by finding the first instance of each player card choice and then comparing which one happens first. We do this by creating a sliding window that breaks the deck into segments of three cards. 

For example, the shortened binary deck of [O,1,1,1,0,1] becomes [[0,1,1],[1,1,1],[1,1,0],[1,0,1]] when applying the windows function. Let's say player 1 picks [1,1,1] and player 2 picks [1,1,0]. Player 1 would have the earliest match, and they would take 4 cards or 1 trick, then we return the index of 4 back to the first instance locator function. So now we start the deck search at card 5. After this there are only 2 cards left, so we stop the scoring. 

Next, we start playing through the deck, and once the first match is found we mark who won and how many cards they won. We then take that index and create a sub deck, and then rerun the same process, finding the first match index. We do this until no more matches remain, or the cards in the deck run out. From here we have a total of cards won or tricks won for each player, and we take these values declare a winner. 

We created a list of all possible interesting choices of combinations. For each deck, we run all combinations and save the win totals for each player choice into an array. We then turn this array into a dataframe for easier visualization and organization. 

We first tested having the tricks counter and card counter all in one function. Then, we tested having two separate functions for counting each deck. Although it is slightly faster to have tricks and cards counter work all at once, we figured it would be better down the line to have them separated when creating the table and heat map. As the number of decks grows, we can track one scoring method at a time, and we figured just for organization purposes it is better to have two functions. 

We created a csv file in our Tables folder that shows 1000 decks scored by the tricks method and card method. 