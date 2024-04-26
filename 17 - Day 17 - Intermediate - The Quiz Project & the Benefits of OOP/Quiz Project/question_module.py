# Question module
"""
creating class.
"""

class Question:
    def __init__(self, q_text, q_answer):
        # creating attributes
        self.text = q_text
        self.answer = q_answer


new_q = Question("How are you" , "I am FIne ")
print(f"Here is the first Q by adam : \n  {new_q.text} \n and the answer for it is as you can see \n {new_q.answer}")

