import speech_recognition
import chess
import chess.engine
from models import Stockfish

board = chess.Board()

recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()
stockfish = Stockfish()


stockfish.get_parameters()
while not board.is_stalemate() and not board.is_checkmate():
    with microphone:
        move = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=5) # шумы
        try:
            print("Say something!")
            audio = recognizer.listen(microphone, 5, 5)
        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
        try:
            print("Started recognition...")
            move = recognizer.recognize_google(audio, language='ru-RU').lower()
            move = move.split("'transcript':")[0]
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")
    
    
    
    move = move.replace('е', 'e').replace('конь', 'N').replace('слон', 'B').replace('а', 'a').replace('б',
                'b').replace('с', 'c').replace('д', 'd').replace('ф', 'f').replace('аш',
                'h').replace('эш', 'h').replace(' ', '').replace('ш', 'h').replace('жэ', 'g').replace('ж',
                'g').replace("король", "K").replace('ферзь', 'Q').replace('ладья', 'R')
    print(move)
    legal = []
    for i in board.legal_moves:
        legal.append(str(i))
    print(legal)
    stockfish.set_fen_position(board.fen())
    if stockfish.is_move_correct(board.parse_san(move)):
        #передвижение магнита под нужную шахмату
        board.push_san(move)
        #передвижение магнита на ход
        print(board)
    else:
        print("пошёл нахуй")
    print(board.parse_san(move))
    print(stockfish.get_best_move())
    board.push(chess.Move.from_uci(stockfish.get_best_move()))
    print(board)
