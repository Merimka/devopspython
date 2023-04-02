"""
Using input function ask user to enter a song name.
1. Print the first charachter of given song name.
2. Print the last charachter of given song name.
3. Print the length of the given song name.
4. Print the index number of "k" in this song name.
5. Print the charachter from an index number of 3.
6. Print the song name in upper case.
7. Print the song name in lower case.
Example:
Input: Mockingbird
Output:
M
d
10
3
k
MOCKINGBIRD
mockingbird
"""
users_entered_song = input("Please, enter a song: ")
print(f"The users given songs first charachter is : {users_entered_song[0]}")
print(f"The users given songs last charachter is : {users_entered_song[-1]}")
print("The users given songs length charachter is :",len(users_entered_song))
print("The index number of 'k' in this song name: ",users_entered_song.find("k"))
print("The third charachter from song is:",users_entered_song[3])
print("The song name is:",users_entered_song.upper())
print("The song name is:",users_entered_song.lower())


