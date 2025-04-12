import nltk
from nltk.chat.util import Chat, reflections

pairs = [
        [
                 r"my name is (.*)",
                ["Hello %1, how can I help you today?",]
         [
                r"hi|hey|hellow",
                ["Hello!", "Hey there!",]
         ],
         [
                r"I am because",
                ["We are",]

         ],
         [
                r"Who is the goat of the NFL",
                ["WOOOOAAHHHHHHH THE ONE AND ONLY MYTH, THE LEGEND, JETJENNEESSS, NUMBER 18 HIMSELF, JUUUSTINNN JEFFERSON WOAHHHHHHJH",]

         ],
         [
                r"What happend a very long time ago ",
                ["A very very long time ago I was the goat at typing club",]

         ],
         [
                r"Which QB is the goat",
                ["WOAHHHHH THE GOAT THE MYTH NUMBER 1 HIMSELF, THE MAN THAT HURTZ, JALEN HURTZZZZ",]

         ],
         [
                r"WHo is the goat of Culver City High",
                ["THEE GOAT HIM SELF THE 6FT 174LB LEGEND HIMSELF MONEY MILLZZZZZZZZ/ME",]

         ],
         [
                r"quit",
                ["Goodbye! Have a nice day!",]

         ],
         [
                r".*",
                ["I'm not sure how to respond to that.",]
        ],
 ]

chatbot = Chat(pairs, reflections)

         # Function to interact with the chatbot
def chat():
    print("Hellon, I am your chatbot. How can I assist you today?")
    while True:
        user_input = input("You:")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Chatbot: ", response)
            else: 
                print("Chatbot: I'm not sure how to respond to that.")
chat()