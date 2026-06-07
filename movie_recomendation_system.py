#recommendation task based on user input on movies
movies_database={
    "action":["Die Hard","Mad Max","John Wick","RRR","Avengers:Endgame"],
    "comedy":["Jatiratnalu","3 idiots","munna bhai mbbs","pk","hera pheri","F2","Enagariniki emaindhi","superbad","The Hangover"],
    "romance":["Titanic","aashiqui 2","dilwale dulhaniya le jayenge","The notebook","Geeta Govindham"],
    "horror":["The Conjuring ","A quiet place","Annabelle","Masooda","Kanchana","Arundhati","stree"]
}
moods=["😃happy","⚡excited","💌romantic","😱thrilling"]
print("========================================") 
print("🎬MOVIE RECOMMENDATION SYSTEM 🎬")
print("========================================")
print("Welcome to the Movie Recommendation system !🍿📽️🎬")
print("📌 Instructions:Type 'exit' to quit the Movie Recommendation System." )
while True:
   print("🎭 Please select your mood from the following options:")
   for mood in moods:
      print(mood)
   user_input=input("How are you feeling today:").lower()
   if user_input=="excited":
      print()
      print("⚡⚡Here are the top action movies you might like:")
      print()
      for index,movies in enumerate(movies_database["action"],start=1):
        print(f"{index}. {movies}")
    
      print("😊 Hope you liked these recommendations!")
      print()
      print("========================================")
      print()
   elif user_input=="happy":
       print()
       print("😃😃Here are the top comedy movies that you might like :")
       print()
       for index,movies in enumerate(movies_database["comedy"],start=1):
         print(f"{index}. {movies}")
       
       print("😊 Hope you liked these recommendations!")
       print()
       print("========================================")
       print()
       
   elif user_input=="romantic":
       print()
       print("💌 Here are the top romantic movies you might like:")
       print()
       for index,movies in enumerate(movies_database["romance"],start=1):
        print(f"{index}. {movies}")
       
       print("😊 Hope you liked these recommendations!")
       print()
       print("========================================")
       print()
   
   elif user_input=="thrilling":
       print()
       print("😱😱 Here are the top horror and thriller movies you might enjoy:")
       print()
       for index,movies in enumerate(movies_database["horror"],start=1):
        print(f"{index}. {movies}")
       
       print("😊 Hope you liked these recommendations!")
       print()
       print("========================================")
       print()
   elif user_input in ["exit","quit","good bye"]:
         print()

         print("Thank you for using our Movie Recommendation System! 🍿🥤")
         print("Goodbye! Have fun! 😃🍿")
         print()
         break  
   else:
      print("❌ Sorry, that mood is not available.")
      print()
       
       
