from datastructures.linkedlist import LinkedList
from project.festival.festivalstage import FestivalStage
from project.festival.songs import Song


class main():

    # Create the song library
    vampire = Song("Vampire", "Olivia Rodrigo", 224, "Pop Rock", 8)
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

    print("\nNow Playing: Vampire")
    stage.play_current_song()  # Automatically removes the song after it finishes
    print("\nPlaylist After Playing First Song:")
    stage.print_playlist()

    print("\nURGENT: Adding a new viral song!")
    queencard = Song("Queencard", "(G)I-DLE", 173, "K-pop", 8)
    stage.emergency_insert(queencard, 2)  # Inserting at position 2
    print("\nPlaylist After Emergency Insertion:")
    stage.print_playlist()

    print("\nRemoving song due to technical issues...")
    removed_song = stage.remove_song("Cypress Grove")
    print(f"Removed: {removed_song.title} by {removed_song.artist}")
    print("\nPlaylist After Removal:")
    stage.print_playlist()

    print("\nSwapping songs to adjust the lineup...")
    stage.swap_songs(1, 3)  # Swapping Queencard with Calm Down
    print("\nPlaylist After Swap:")
    stage.print_playlist()

    print("\nCreating an Energy Wave for a balanced playlist...")
    stage.create_energy_wave()
    print("\nPlaylist After Energy Wave:")
    stage.print_playlist()

    print("\nActivating Crowd Pleaser Mode...")
    stage.crowd_pleaser_mode()
    print("\nPlaylist After Crowd Pleaser Mode:")
    stage.print_playlist()


    print("\nGrouping all Hip Hop songs together...")
    #stage.genre_block("Hip Hop")
    print("\nPlaylist After Genre Block:")
    stage.print_playlist()

    print("\nCalculating Estimated Time Remaining...")
    remaining_time = stage.estimated_time_remaining()
    print(f"Estimated Time Remaining: {remaining_time // 60}:{remaining_time % 60:02}")

    #stage.sort()
    #sorted_list = sorted(stage)
    #print(sorted_list)

if __name__ == '__main__':
    main()