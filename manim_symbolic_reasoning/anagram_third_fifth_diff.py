from manim import *
import numpy as np

config.background_color = WHITE

class AnagramAnimation(Scene):
    def construct(self):
        # The original word
        word = "DISHWASHER"
        
        # Create and add a title
        question = "What is the difference between the position\nof the 'W' in the third word and the fifth word?\nPlease answer with just a number and no other text"
        title = Text(question, font_size=36, color=BLACK)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Create a list of Text objects for each letter in the word
        letters = [Text(letter, color=BLACK) for letter in word]
        
        # Position the letters in a line
        for i, letter in enumerate(letters):
            letter.move_to(LEFT * (len(word) / 2 - i))

        # Display the word
        self.play(*[Write(letter) for letter in letters])
        self.wait(1)

        # Shuffle the letters to create an anagram
        for _ in range(7):
            shuffled_indices = list(range(len(letters)))
            np.random.shuffle(shuffled_indices)
            shuffled_letters = [letters[i] for i in shuffled_indices]
            
            if _ == 1:
                t_word = ''.join([l.text for l in shuffled_letters])
                
            if _ == 3:
                shuffled_word = ''.join([l.text for l in shuffled_letters])
                answer = np.abs(shuffled_word.find('W') - t_word.find('W'))
                with open('combined_questions.csv', 'a+') as file:
                    file.write(f"media/videos/anagram-6-2/480p15/AnagramAnimation.mp4, {answer}, {question}\n")

            # Animate each letter along an arc to its new position
            animations = []
            for new_i, letter in enumerate(shuffled_letters):
                target_x = LEFT * (len(word) / 2 - new_i)
                current_pos = letter.get_center()
                target_pos = target_x
                arc_height = 1.5

                control_point = current_pos + UP * arc_height
                animations.append(
                    MoveAlongPath(letter, CubicBezier(current_pos, control_point, control_point, target_pos))
                )

            self.play(*animations, run_time=1)
        self.wait(1)
