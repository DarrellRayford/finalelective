Exercises
Write some object-oriented code. The goal is to use the principles and syntax you learned in this chapter to ensure you understand the topics we've covered. 
If you've been working on a Python project, go back over it and see whether there are some objects you can create and add properties or methods to. If it's large, try dividing it into a few modules or even packages and play with the syntax. While a "simple" script may expand when refactored into classes, there's generally a gain in flexibility and extensibility.

If you don't have such a project, try starting a new one. It doesn't have to be something you intend to finish; just stub out some basic design parts. 
You don't need to fully implement everything; often, just a print("this method will do something") is all you need to get the overall design in place. 
This is called top-down design, in which you work out the different interactions and describe how they should work before actually implementing what they do. 
The converse, bottom-up design, implements details first and then ties them all together. Both patterns are useful at different times, 
but for understanding object-oriented principles, a top-down workflow is more suitable.

If you're having trouble coming up with ideas, try writing a to-do application. It can keep track of things you want to do each day. 
Items can have a state change from incomplete to completed. You might want to think about items that have an intermediate state of started, 
but not yet completed.

Now try designing a bigger project. A collection of classes to model playing cards can be an interesting challenge. Cards have a few features, 
but there are many variations on the rules. A class for a hand of cards has interesting state changes as cards are added. Locate a game you like and create classes to model cards, hands, and play. (Don't tackle creating a winning strategy; that can be hard.)

A game like Cribbage has an interesting state change where two cards from each player's hand are used to create a kind of third hand, called "the crib." 
Make sure you experiment with the package and module-importing syntax. 
Add some functions in various modules and try importing them from other modules and packages. Use relative and absolute imports. 
See the difference, and try to imagine scenarios where you would want to use each one.