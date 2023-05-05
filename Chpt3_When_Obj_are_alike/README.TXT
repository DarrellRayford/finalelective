Exercises
Look around you at some of the physical objects in your workspace and see if you can describe them in an inheritance hierarchy.
Humans have been dividing the world into taxonomies like this for centuries, so it shouldn't be difficult. 
Are there any non-obvious inheritance relationships between classes of objects? If you were to model these objects in a computer application, 
what properties and methods would they share? Which ones would have to be polymorphically overridden? 
What properties would be completely different between them?

Now write some code. No, not for the physical hierarchy; that's boring. Physical items have more properties than methods. 
Just think about a pet programming project you've wanted to tackle in the past year, but never gotten around to. 
For whatever problem you want to solve, try to think of some basic inheritance relationships and then implement them. 
Make sure that you also pay attention to the sorts of relationships that you actually don't need to use inheritance for. 
Are there any places where you might want to use multiple inheritance? Are you sure? Can you see any place where you would want to use a mixin?
 Try to knock together a quick prototype. It doesn't have to be useful or even partially working. 
 You've seen how you can test code using python -i already; just write some code and test it in the interactive interpreter. 
 If it works, write some more. If it doesn't, fix it!

Now, take a look at the various distance computations in the case study. 
We need to be able to work with testing data as well as unknown samples provided by a user. What do these two kinds of samples have in common?
 Can you create a common superclass and use inheritance for these two classes with similar behavior? 
 (We haven't looked closely at the k-NN classification yet, but you can provide a "mock" classifier that will provide fake answers.)

When we look at the distance computation, we can see how a Hyperparameter is a composition that includes a distance algorithm plug-in as one 
of the parameters. Is this a good candidate for a mixin? Why or why not? What limitations does a mixin have that a plug-in does not have?