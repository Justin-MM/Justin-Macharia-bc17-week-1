# count the occurrence of the words/ numbers
def words(string):
  
  words_list = string.split()

# replace numbers in list with integers
  for index, item in enumerate(words_list):
    if item.isdigit() is True:
        words_list[index] = int(item)
  print(words_list)

  words_dict = {key:0 for key in words_list}
  
  for words in words_dict:
    word_count = 0
    for word in words_list:
      
      if words == word:
        word_count += 1
        words_dict[word] = word_count
        
  return words_dict

print (words("each of one 1 2 3"))
