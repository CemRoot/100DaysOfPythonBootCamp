alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'Grading_Program.md', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'Grading_Program.md',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # Alfabeyi ekledik


def caesar(start_text, shift_amount, cipher_direction):  # Caesar şifreleme fonksiyonu
    """

    :param start_text:  Girilen metin
    :param shift_amount:  Şifreleme sayısı
    :param cipher_direction:  Şifreleme yönü
    :return:  Şifreli metin
    """
    end_text = ""  # Şifreli metin
    if cipher_direction == "decode":  # Şifreleme yönünün kontrolü
        shift_amount *= -1  # Şifreleme sayısının -1 e çarpıp şifreleme yönünün değiştirilmesi
    for char in start_text:  # Girilen metinin her bir karakteri için döngü oluşturduk
        if char in alphabet: # Girilen metinin her bir karakteri alfabeye açık mı?
            position = alphabet.index(char)  # Karakterin alfabeye açık olduğu pozisyonu buluyoruz
            new_position = position + shift_amount  # Karakterin şifrelenmiş olduğu pozisyonu buluyoruz
            end_text += alphabet[new_position]  # Şifrelenmiş metinin eklenmesi
        else:  # Girilen metinin her bir karakteri alfabeye açık değilse
            end_text += char  # Karakterin eklenmesi
    print(f"Here's the {cipher_direction}d result: {end_text}")  # Şifrelenmiş metinin ekrana yazdırılması


from logo import logo  # logo.py dosyasının içeriğini alıyoruz

print(logo)  # logo.py dosyasının içeriğini ekrana yazdırıyoruz

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False  # Programın bitip bitmede kullanıcının girdiği değer
while not should_end:  # Programın bitip bitmede kullanıcının girdiği değer
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  # Şifreleme yönünün alınması
    text = input("Type your message:\n").lower()  # Şifrelenecek metinin alınması
    shift = int(input("Type the shift number:\n"))  # Şifreleme sayısının alınması
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift = shift % 26    # Şifreleme sayısının 26'e bölümünü alıyoruz

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)  # Caesar şifreleme fonksiyonunun çağrılması

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") # Programın tekrar çalıştırılmasını istiyor mu?
    if restart == "no":  # Eğer kullanıcı 'no' yazıyor ise
        should_end = True  # Programın bitip bitmede kullanıcının girdiği değer
        print("Goodbye")  # Programın bitip bitmede kullanıcının girdiği değer



