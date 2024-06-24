v = int(input())
t = int(input())

mkad_length = 109

final_position = (v * t) % mkad_length

final_position = final_position % mkad_length

print(final_position)
