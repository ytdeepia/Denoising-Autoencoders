from manim import *
from manim_voiceover import VoiceoverScene


class Scene4_1(VoiceoverScene):
    def construct(self):

        self.wait(1)

        simclr = Text("SimCLR").scale(1.5)
        simclr_2 = Text("Simple Framework for Contrastive Learning").scale(0.8)
        simclr_underline = Underline(simclr_2, buff=0.1)
        hinton_img = ImageMobject("img/hinton.jpg").scale_to_fit_width(4)
        hinton_rect = SurroundingRectangle(hinton_img, buff=0.0, color=WHITE)
        medal_svg = SVGMobject("img/medal.svg").shift(3 * RIGHT)

        self.play(Write(simclr), run_time=1.5)
        self.play(
            ShowPassingFlash(
                SurroundingRectangle(simclr, buff=0.5, color=WHITE, stroke_width=4)
            )
        )

        self.wait(0.8)

        self.play(ReplacementTransform(simclr, simclr_2))
        self.play(GrowFromEdge(simclr_underline, LEFT))

        self.play(FadeOut(simclr_2, simclr_underline, shift=0.5 * RIGHT), run_time=0.8)

        hinton_txt = Text("Geoffrey Hinton").scale(0.8).next_to(hinton_img, UP)
        self.play(FadeIn(hinton_img, hinton_rect), Write(hinton_txt))

        self.wait(0.6)


        self.play(
            Group(hinton_img, hinton_rect, hinton_txt).animate.shift(3 * LEFT)
        )

        self.play(FadeIn(medal_svg))
        self.play(
            Flash(
                medal_svg,
                line_length=0.8,
                num_lines=32,
                flash_radius=1.6,
                run_time=1.5,
            )
        )

        self.wait(0.7)

        self.play(FadeOut(*self.mobjects))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene4_1()
    scene.render()
