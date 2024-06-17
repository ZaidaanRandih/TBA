class TokenRecognizer:
    def __init__(self):
        self.subjects = {"saya", "kamu", "dia", "mereka", "kami"}
        self.predicates = {"makan", "minum", "tidur", "bermain", "belajar"}
        self.objects = {"nasi", "air", "bola", "buku", "komputer"}
        self.adverbs = {"dirumah", "disekolah", "ditaman", "dengan cepat", "dengan baik"}
    
    def recognize(self, word):
        if word in self.subjects:
            return 'S'
        elif word in self.predicates:
            return 'P'
        elif word in self.objects:
            return 'O'
        elif word in self.adverbs:
            return 'K'
        else:
            return None

recognizer = TokenRecognizer()
print(recognizer.recognize("saya"))  # Output: S
print(recognizer.recognize("makan")) # Output: P

class Parser:
    def __init__(self, recognizer):
        self.recognizer = recognizer
        self.valid_structures = [
            ['S', 'P', 'O', 'K'],
            ['S', 'P', 'K'],
            ['S', 'P', 'O'],
            ['S', 'P']
        ]
    
    def parse(self, sentence):
        tokens = [self.recognizer.recognize(word) for word in sentence.split()]
        return self.is_valid_structure(tokens)
    
    def is_valid_structure(self, tokens):
        return tokens in self.valid_structures

parser = Parser(recognizer)
while True:
        sentence = input("Masukkan kalimat: ")
        if parser.parse(sentence) == True:
            print("Kalimat valid.")
        else:
            print("Kalimat tidak valid.")
        again = input("Coba lagi? (y/n): ").strip().lower()
        if again != 'y':
            break

