# Quiz Project in Python using OOB.

# QUiz Project Part(1) Creating the Question class 
 - First creating the Class Question with 2 attributes  (Text & Answer)

```
    Pytoh -- OOB 
    
    class Question:
    def __init__(self, q_text, q_answer):
        # creating attributes
        self.text = q_text
        self.answer = q_answer
    new_q = Question("How are you" , "I am FIne ")
    print(f"Here is the first Q by adam : \n  
    {new_q.text} 
    \n and the answer for it is as you can see 
    \n {new_q.answer}")
```
# QUiz Project Part (2) Creating the list of Question Class.

        