import iCaptur
import json

filename = input('enter filename\n')
exercise = input('enter excercise (squat,lunge, birddog, bridge or plank)\n')
with open(filename) as input_file:
        data = json.load(input_file)

iCaptur.analyze(data, exercise)