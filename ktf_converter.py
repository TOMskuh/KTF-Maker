def create_ktf_file(codename):
    lyrics_file = 'input/lyrics/lyrics.txt'
    audio_file = 'input/audio/audio.mp3'  # Change the file extension if needed

    ktf_file = f'output/{codename}.ktf'

    with open(lyrics_file, 'r') as file:
        lyrics = file.read().split()

    timestamps = []
    for word in lyrics:
        print(f"Current Word: {word}")
        start_time = float(input("Enter the start time (in seconds): "))
        end_time = float(input("Enter the end time (in seconds): "))
        timestamps.append((start_time, end_time))

    ktf_lines = []
    for i, word in enumerate(lyrics):
        start_time, end_time = timestamps[i]
        ktf_line = f'[{start_time:.3f}-{end_time:.3f}] {word}'
        ktf_lines.append(ktf_line)

    with open(ktf_file, 'w') as file:
        file.write('\n'.join(ktf_lines))

    print(f"KTF file '{codename}.ktf' created successfully in 'output/' directory.")

# Usage example:
codename = input("Enter the codename: ")
create_ktf_file(codename)
