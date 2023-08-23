alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  text_list = list(text)
  end_list = []
  if direction == "decode":
      shift *= -1
  for letter in text_list:
    if letter not in alphabet:
       end_list.append(letter)
    else:       
      i = alphabet.index(letter)
      new_position = i + shift
      end_list.append(alphabet[new_position])
  return print(f"The {direction}d code is : {''.join(end_list)}")
  
cipher()


end_game = False
while end_game == False:
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  if again == "yes":
    cipher()
  else:
    end_game = True
    print("Goodbye!")
