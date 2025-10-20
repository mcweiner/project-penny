# Project Penney

The intended audience is students of mine taking DATA 440 in Fall 2025.

Use this repository as a general guideline for how to structure you own repositories.

First of all, always have a README.md like this one. The goal of your README should be to give users a high-level explanation of what your code is about and how to use it.

You will often need to create more detailed documentation/instructions as well. Place those in a separate file, and link to them from the README.

---

## Overview

Penney's game, AKA Penney Ante, is an example of a three-bit sequence game invented by Walter Penney. It is played by two players using standard pennies (One side is heads and the other is tails).  The 1st player selects a sequence of heads and tails (of length 3 or larger), and shows this sequence to the 2nd player. The 2nd player then determines their own sequence of the same length as the 1st player's. The coin is then tossed until the 1st or 2nd player's sequence appears as a consecutive subsequence of the coin toss outcomes. The player whose sequence appears first wins. 

## Purpose

This codes goal is to score 

This code generates random numbers and plots them.

---

## Quick-Start Guide

Everyone loves one of these! Give users a quick, short and to the point way to make your code work, for example:

This project is managed using [UV](https://docs.astral.sh/uv/guides/install-python/). If you do not yet have UV installed or need help troubleshooting issues with UV, refer to [their documentation](https://docs.astral.sh/uv/guides/install-python/).

Once you have UV installed, simply download the repository, navigate to the directory and run: `uv sync` to install dependencies.

To run the program:

`uv run main.py`

---

## Contents

You should provide a high-level description of the contents of your repository. You do not need to go into excruciating detail here. You can also place individual README.md files in each folder that go into more depth of the contents of that folder.

`main.py`: This is the main entry point to the program. It should be named `main.py`, unless you have a good reason to deviate from that. This way the user does not need to guess about what they should be running.

`src/`: The source code. This should contain all of the code that is needed to make your project work. We place it in a separate folder so that:

- it is clear to the user that this is the source code, and they do not need to look at it unless they want to
- the root directory of the repository does not get cluttered

`data/`: As the name implies, put data in this folder. If you have a project containing raw and processed versions of the data, then you should create subdirectories such as `data/raw` and `data/processed`, for example. Use your best judgment and stay organized!

`figures/`: Similar to above, we should place figures here. If you are keeping older versions of figures, then place the older ones in a subdirectory, and keep only the current versions in the top-level `figures/` directory.