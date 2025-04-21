# FestivalStage Testing Output Template

Your Name: [Your Name]
Did you use Generative AI (e.g. CoPilot, ChatGPT, etc.): [Yes/No] Yes
If yes, how did you use it? [Briefly describe how you used Generative AI in your project]

I used it to help me fix my short functiions like the genre

## Instructions

This template is designed to help you test your `FestivalStage` mini-project implementation. It includes a series of test cases that you can run to check if your code is working as expected.

To use this template, follow these steps:

1. Copy the code snippets for each test case into your Python file.
2. Run each test case and compare the output with the expected output provided.
3. Paste your actual output in the designated areas below each expected output.
4. Save this file in your project folder and commit it with your code.

If your actual output matches the expected output for all test cases, your implementation is correct. If there are any discrepancies, you may need to debug your code to identify and fix the issues.

## Test Case 1: Initialization and Adding Songs

### Code:

```python
# Create the song library
vampire = Song("vampire", "Olivia Rodrigo", 224, "Pop Rock", 8)
milli_vanilli = Song("Milli Vanilli", "Blame it on the Rain", 145, "Hip Hop", 7)
paint_town_red = Song("Paint The Town Red", "Doja Cat", 232, "Hip Hop", 9)
cypress_grove = Song("Cypress Grove", "Ghost", 190, "Metal", 9)
calm_down = Song("Calm Down", "Rema & Selena Gomez", 239, "Beats", 6)

# Initialize the FestivalStage
stage = FestivalStage("WU Main Stage")

# Add songs to the playlist
stage.add_song(vampire)
stage.add_song(milli_vanilli)
stage.add_song(paint_town_red)
stage.add_song(cypress_grove)
stage.add_song(calm_down)

# Display the initial playlist
print("Initial Festival Lineup:")
stage.print_playlist()
```

### Expected Output:

```txt
Initial Festival Lineup:
1. vampire - Olivia Rodrigo (3:44) [Pop Rock] Energy: 8
2. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Cypress Grove - Ghost (3:10) [Metal] Energy: 9
5. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Total Time: 17:10
```

### Your Output:

[Paste your output here]
Initial Festival Lineup:
1. Vampire - Olivia Rodrigo (3:44) [Pop Rock] Energy: 8
2. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Cypress Grove - Ghost (3:10) [Metal] Energy: 9
5. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Estimated Time Remaining: 17:10

---

## Test Case 2: Playing the Current Song

### Code:

```python
print("\nNow Playing: vampire")
stage.play_current_song()  # Automatically removes the song after it finishes
print("\nPlaylist After Playing First Song:")
stage.print_playlist()
```

### Expected Output:

```txt
Now Playing: vampire - Olivia Rodrigo (3:44) [Pop Rock]
Song Complete - Removed from playlist

Playlist After Playing First Song:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
3. Cypress Grove - Ghost (3:10) [Metal] Energy: 9
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Total Time: 13:26
```

### Your Output:

[Paste your output here]
Now Playing: Vampire

Playlist After Playing First Song:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
3. Cypress Grove - Ghost (3:10) [Metal] Energy: 9
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Estimated Time Remaining: 13:26

---

## Test Case 3: Emergency Insert

### Code:

```python
print("\nURGENT: Adding a new viral song!")
queencard = Song("Queencard", "(G)I-DLE", 173, "K-pop", 8)
stage.emergency_insert(queencard, 2)  # Inserting at position 2
print("\nPlaylist After Emergency Insertion:")
stage.print_playlist()
```

### Expected Output:

```txt
Playlist After Emergency Insertion:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Cypress Grove - Ghost (3:10) [Metal] Energy: 9
5. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Total Time: 16:19
```

### Your Output:

[Paste your output here]
URGENT: Adding a new viral song!

Playlist After Emergency Insertion:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Cypress Grove - Ghost (3:10) [Metal] Energy: 9
5. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Estimated Time Remaining: 16:19

---

## Test Case 4: Removing a Song

### Code:

```python
print("\nRemoving song due to technical issues...")
removed_song = stage.remove_song("Cypress Grove")
print(f"Removed: {removed_song.title} by {removed_song.artist}")
print("\nPlaylist After Removal:")
stage.print_playlist()
```

### Expected Output:

```txt
Removed: Cypress Grove by Ghost

Playlist After Removal:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Total Time: 13:09
```

### Your Output:

[Paste your output here]
Removing song due to technical issues...
Removed: Cypress Grove by Ghost

Playlist After Removal:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Estimated Time Remaining: 13:09
---

## Test Case 5: Swapping Songs

### Code:

```python
print("\nSwapping songs to adjust the lineup...")
stage.swap_songs(1, 3)  # Swapping Queencard with Calm Down
print("\nPlaylist After Swap:")
stage.print_playlist()
```

### Expected Output:

```txt
Playlist After Swap:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
Total Time: 13:09
```

### Your Output:

[Paste your output here]
Swapping songs to adjust the lineup...

Playlist After Swap:
1. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
2. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
3. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
4. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
Estimated Time Remaining: 13:09
---

## Test Case 6: Creating an Energy Wave

### Code:

```python
print("\nCreating an Energy Wave for a balanced playlist...")
stage.create_energy_wave()
print("\nPlaylist After Energy Wave:")
stage.print_playlist()
```

### Expected Output:

```txt
Playlist After Energy Wave:
1. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
2. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
3. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
4. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
Total Time: 13:09
```

### Your Output:

[Paste your output here]
Creating an Energy Wave for a balanced playlist...

Playlist After Energy Wave:
1. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
2. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
3. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Estimated Time Remaining: 13:09
---

## Test Case 7: Activating Crowd Pleaser Mode

### Code:

```python
print("\nActivating Crowd Pleaser Mode...")
stage.crowd_pleaser_mode()
print("\nPlaylist After Crowd Pleaser Mode:")
stage.print_playlist()
```

### Expected Output:

```txt
Playlist After Crowd Pleaser Mode:
1. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
2. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
3. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Total Time: 13:09
```

### Your Output:

[Paste your output here]
Activating Crowd Pleaser Mode...

Playlist After Crowd Pleaser Mode:
1. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
2. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
3. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Estimated Time Remaining: 13:09
---

## Test Case 8: Grouping Songs by Genre

### Code:

```python
print("\nGrouping all Hip Hop songs together...")
stage.genre_block("Hip Hop")
print("\nPlaylist After Genre Block:")
stage.print_playlist()
```

### Expected Output:

```python
Playlist After Genre Block:
1. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
2. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
3. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Total Time: 13:09
```

### Your Output:

[Paste your output here]
Grouping all Hip Hop songs together...

Playlist After Genre Block:
1. Paint The Town Red - Doja Cat (3:52) [Hip Hop] Energy: 9
2. Queencard - (G)I-DLE (2:53) [K-pop] Energy: 8
3. Milli Vanilli - Blame it on the Rain (2:25) [Hip Hop] Energy: 7
4. Calm Down - Rema & Selena Gomez (3:59) [Beats] Energy: 6
Estimated Time Remaining: 13:09
---

## Test Case 9: Calculating Estimated Time Remaining

### Code:

```python
print("\nCalculating Estimated Time Remaining...")
remaining_time = stage.estimated_time_remaining()
print(f"Estimated Time Remaining: {remaining_time // 60}:{remaining_time % 60:02}")
```

### Expected Output:

```txt
Estimated Time Remaining: 13:09
```

### Your Output:

[Paste your output here]
Calculating Estimated Time Remaining...
Estimated Time Remaining: 13:09
