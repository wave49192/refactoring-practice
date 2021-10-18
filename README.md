## Refactoring Practice

Copy this template repository to your own Github account. Then clone it to your computer and do the refactorings.  Push your work to Github.

Each subdirectory contains some code that needs refactoring.

1. In this README, write one line describing each refactoring you apply and why.
2. Perform the refactoring in the subdirectory code.


## `time/timestamp.py`

Refactor timestamp.py.  2 or 3 refactorings are possible.
1. Rename method to create_time_from_timestamp
2. Extract method is_valid_time
3. Rewrite the condition from else to elif

## `game_framework/gamelib.py`

Look for refactorings in the class `GameApp`.

* Avoid side-effects: replace side effect with return value (the caller must use the return value)

* Encapsulate a collection - provide behavior that subclasses of GameApp need instead of requiring them to manipulate a collection that belongs to the GameApp class.
  - Hint: `elements`
1. Create `add_element()` and `remove_element()` method
2. Create global variable for some parameters
3. Now  `create_canvas()` return the object and set the canvas attribute in the `__init__` instead


## `recipe/recipe.py` and `recipe/main.py`

This uses a `dataclass`, which requires Python 3.7.

The Recipe class defines a recipe for a hot beverage with attributes:
* name - name of the recipe
* coffee - units of coffee
* chocolate - units of chocolate
* milk - units of milk
* sugar - units of sugar
* price - (float) price in Baht

Refactor `main.py`.  What can you do to eliminate the long, boring code?






## Resources

* <https://refactoringguru.com/refactoring> 
* *Refactoring - Improving the Design of Existing Code* by Martin Fowler.  The bible on refactoring.  The first 4 chapters explain the fundamentals.
* <https://refactoring.com> Online version of Fowler's book, but lacks explanation of the refactorings.
