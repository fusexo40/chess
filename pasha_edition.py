import speech_recognition
import chess
import chess.engine
from models import Stockfish
import time
import serial
import pyttsx3

#кушать пешку буквагдестоит|буквакудаидет|цифракудаидет

board = chess.Board()

#ser = serial.Serial("/dev/cu.usbserial-110", 9600)
recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()
stockfish = Stockfish()
voice = pyttsx3.init()

while not board.is_stalemate() and not board.is_checkmate():
    with microphone: 
        move = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=5) # шумы
        try:
            voice.say("Скажите что-нибудь")  
            voice.runAndWait()
            print("Say something!") 
            audio = recognizer.listen(microphone, 5, 5)
        except speech_recognition.WaitTimeoutError:
            voice.say("Проверьте подключение микрофона")  
            voice.runAndWait()
            print("Can you check if your microphone is on, please?")
        try:
            voice.say("Обработка хода")  
            voice.runAndWait()
            print("Started recognition...")
            move = recognizer.recognize_google(audio, language='ru-RU').lower()
            move = move.split("'transcript':")[0]
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            voice.say("Проверьте подключение к интернету")  
            voice.runAndWait()
            print("Check your Internet Connection, please")
    
    
    move = move.replace('е', 'e').replace('конь', 'N').replace('слон', 'B').replace('а', 'a').replace('б',
                'b').replace('с', 'c').replace('д', 'd').replace('ф', 'f').replace('аш',
                'h').replace('эш', 'h').replace(' ', '').replace('ш', 'h').replace('жэ', 'g').replace('ж',
                'g').replace("король", "K").replace('ферзь', 'Q').replace('ладья', 'R').replace('икс', 'x')
    stockfish.set_fen_position(board.fen())
    print(move)
    try:
        print(board.parse_san(move))
        #move_to_c = bytes(str(board.parse_san(move)), encoding = 'utf-8')
        #ser.write(move_to_c)
        #передвижение магнита под нужную шахмату
        board.push_san(move)
        #передвижение магнита на ход
        print(board)
    except:
        voice.say("Невозможный ход")  
        voice.runAndWait()
        print("Move is not correct")
        continue
    stockfish.set_fen_position(board.fen())
    #move_to_c = bytes(str(stockfish.get_best_move()), encoding = 'utf-8')
    #ser.write(move_to_c)
    board.push(chess.Move.from_uci(stockfish.get_best_move()))
    print(board)
