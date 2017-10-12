# StableMarriage

This code contains a Python script with the implementation of the [Gale-Shapley algorithm](https://en.wikipedia.org/wiki/Stable_marriage_problem)

In the problem of Stable Marriage we are looking for a stable matching between men and women having as input the preferences of both males.

In our case, the preferences are given through JSON files:

```
{
  "men_rankings": {
    "abe": ["cat", "bea", "ada"],
    "bob": ["ada", "cat", "bea"],
    "cal": ["ada", "bea", "cat"]
  },

  "women_rankings": {
    "ada": ["abe", "cal", "bob"],
    "bea": ["bob", "abe", "cal"],
    "cat": ["cal", "abe", "bob"]
  }
}
```
The program's output is also given as a JSON file:

```
{"abe": "cat", "bob": "bea", "cal": "ada"}
```

If we start tackling the problem from men's part, the solution that is produced is optimized for them (as the above). On the other hand, if we tackle it from the women's part, the solution should be optimized for the women:

```
{"ada": "abe", "bea": "bob", "cat": "cal"}
```

The program can be run with the following ways:

* `python3 stable_marriage.py -m <input_filename>`, which outputs the solution that is optimized for the men. The script produces a JSON representation of the solution: `{ "man": "woman", "another_man": "another_woman", ...}`.
* `python3 stable_marriage.py -m <input_filename> -o <output_filename>`, which also outputs the solution that is optimized for the men. The script is saved on a file named `output_filename`.
* `python3 stable_marriage.py -w <input_filename>`, which outputs the solution that is optimized for the women. The script produces a JSON representation of the solution: `{ "woman": "man", "another_woman": "another_man", ...}`.
* `python3 stable_marriage.py -w <input_filename> -o <output_filename>`, which also outputs the solution that is optimized for the women. The script is saved on a file named `output_filename`.

Example files for input-output:

* [example_1.json](example_1.json), optimized solution for men [example_1_m.json](example_1_m.json), optimized solution for women  [example_1_w.json](example_1_w.json).
* [example_2.json](example_2.json), optimized solution for men  [example_2_m.json](example_2_m.json), optimized solution for women  [example_2_w.json](example_2_w.json).
* [example_3.json](example_3.json), optimized solution for men [example_3_m.json](example_3_m.json), optimized solution for women  [example_3_w.json](example_3_w.json).

The full program's description (in Greek) can be found [here](https://github.com/dmst-algorithms-course/assignment-2015-2).
