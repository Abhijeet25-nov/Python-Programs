#get a dictonary
emoji_map_fun={
    "love": "❤️",
    "happy":"😊",
    "code":"💻",
    "tea":"☕",
    "music":"🎵",
    "food":"🍔",    
    "girl":"👧",
    "cute":"🥰"
}
#get user message
message=input("Enter your message: ")

updated_words=[] 
#process each word
for word in message.split():
    cleaned=word.lower().strip(".,!?")
    emoji=emoji_map_fun.get(cleaned,"")
    if emoji:
        updated_words.append(f" {emoji} ")
    else:
        updated_words.append(word)    
 
updated_message=" ".join(updated_words)        
print("Enhanced mesaage: ",updated_message)
# print(updated_message)