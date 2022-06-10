import random # Rastgele sayı üretmek için kullanılır.
from hangman_art import stages, logo # hangman_art.py dosyasındaki stages ve logo değişkenlerini kullanabilmek için import edildi.
from hangman_words import word_list # hangman_words.py dosyasındaki word_list değişkenini kullanabilmek için import edildi.

print(logo) # logo yazdırıldı.
game_is_finished = False # Oyun bitmediği için False değerini atadık.
lives = len(stages) - 1 # stages listesindeki eleman sayısının 1 eksiğiyle oyun bitmeyecek şekilde kalan can sayısını atadık.

chosen_word = random.choice(word_list) # word_list listesinden rastgele bir kelime seçildi.
word_length = len(chosen_word) # seçilen kelimenin uzunluğu atandı.

display = [] # display listesine boş bir liste atandı.
for _ in range(word_length): # word_length kadar boş bir liste atandı.
    display += "_" # display listesine "_" karakteri ekledik.

while not game_is_finished: # Oyun bitmediği sürece döngü devam eder.
    guess = input("Guess a letter: ").lower() # Kullanıcıdan bir harf girmesini istiyoruz.


    if guess in display: # Eğer girilen harf display listesinde varsa:
        print(f"You've already guessed {guess}") # Kullanıcıya bu harfi daha önce girdiği bilgisi verdik.

    for position in range(word_length): # word_length kadar döngü oluşturduk.
        letter = chosen_word[position] # seçilen kelimenin bir harfi atandı.
        if letter == guess: # Eğer girilen harf seçilen harf ile aynıysa:
            display[position] = letter # display listesindeki harf seçilen harfi ile değiştirildi.
    print(f"{' '.join(display)}") # display listesindeki harfleri birbirleriyle birleştirip yazdırdık.

    if guess not in chosen_word: # Eğer girilen harf seçilen harf ile aynı değilse:
        print(f"You guessed {guess}, that's not in the word. You lose a life.") # Kullanıcıya bu harfi daha önce girdiği bilgisi verdik.
        lives -= 1 # Can sayısı 1 azaltıldı.
        if lives == 0: # Eğer can sayısı 0 a eşitse:
            game_is_finished = True # Oyun bitmediği için True değerini atadık.
            print("You lose.") # Kullanıcıya kaybettik bilgisi verdik.
            print(f"The word was {chosen_word}.") # Kullanıcıya seçilen kelimenin oyun sonunda ne olduğunu gösterdik.
    if not "_" in display: # Eğer "_" karakteri display listesinde yoksa:
        game_is_finished = True # Oyun bittiği  için True değerini atadık.
        print("You win.") # Kullanıcıya kazandık bilgisi verdik.

    print(stages[lives]) # Can sayısına göre hangman_art.py dosyasındaki stages listesindeki bir elemanı yazdırdık.
