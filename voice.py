import speech_recognition as sr
from pieces import chess


coords = chess.coords

class voise():
    def record_volume():
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as source:
            print('Listening')
            audio = r.listen(source)
        query = r.recognize_google(audio, language='ru-RU')
        answer = query.split("'transcript':")[0]
        return answer


    def get_coords(self):
        step = self.record_volume().lower()

        if step[0] == "а":
            step = f"a{step[1]}"
        elif step[0] == "е":
            step = f"e{step[1]}"

        if step[3] == "а":
            step = f"a{step[4]}"
        elif step[3] == "е":
            step = f"e{step[4]}"

        step_from = step.split(" ")[0]
        step_to = step.split(" ")[1]

        for i in range(8):
            for j in range(8):
                if coords[i][j] == step_from:
                    coords_from = i, j
        for i in range(8):
            for j in range(8):
                if coords[i][j] == step_to:
                    coords_to = i, j
        
        return (coords_from, coords_to)