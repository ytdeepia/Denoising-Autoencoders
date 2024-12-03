from manim import *
from manim_voiceover import VoiceoverScene

import numpy as np


class Scene2_3(VoiceoverScene):
    def construct(self):
        

        np.random.seed(42)  # For consistent results


        txt = Text("Thanks for watching!").scale(1.2).to_edge(UP, buff=1.0)

        self.play(Write(txt))

        self.wait(3)


if __name__ == "__main__":
    scene = Scene2_3()
    scene.render()
