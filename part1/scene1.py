from manim import *
from manim_voiceover import VoiceoverScene


class Scene1_1(VoiceoverScene):
    def construct(self):
        self.wait(1)
        img1 = ImageMobject("img/cat1.jpg").scale_to_fit_width(3)
        img1.add(SurroundingRectangle(img1, color=WHITE, buff=0))
        img2 = ImageMobject("img/cat2.jpg").scale_to_fit_width(3)
        img2.add(SurroundingRectangle(img2, color=WHITE, buff=0))
        img3 = ImageMobject("img/cat3.jpg").scale_to_fit_width(3)
        img3.add(SurroundingRectangle(img3, color=WHITE, buff=0))
        img4 = ImageMobject("img/dog.png").scale_to_fit_width(3)
        img4.add(SurroundingRectangle(img4, color=WHITE, buff=0))
        img5 = ImageMobject("img/dog2.jpg").scale_to_fit_width(3)
        img5.add(SurroundingRectangle(img5, color=WHITE, buff=0))
        img6 = ImageMobject("img/dog3.jpg").scale_to_fit_width(3)
        img6.add(SurroundingRectangle(img6, color=WHITE, buff=0))
        img7 = ImageMobject("img/dog4.jpg").scale_to_fit_width(3)
        img7.add(SurroundingRectangle(img7, color=WHITE, buff=0))

        img1.move_to(2.2 * DOWN + 0.8 * RIGHT)
        img2.move_to(2.5 * UP + 4.5 * LEFT)
        img3.move_to(2.3 * UP + 4.9 * RIGHT)
        img4.move_to(2.9 * DOWN + 4.4 * LEFT)
        img5.move_to(1 * DOWN + 4.6 * RIGHT)
        img6.move_to(0.3 * DOWN + 2.3 * LEFT)
        img7.move_to(1.2 * UP + 0.8 * RIGHT)

        label1 = Tex("Cat").next_to(img1, UP).scale(0.6)
        label2 = Tex("Cat").next_to(img2, UP).scale(0.6)
        label3 = Tex("Cat").next_to(img3, UP).scale(0.6)
        label4 = Tex("Dog").next_to(img4, UP).scale(0.6)
        label5 = Tex("Dog").next_to(img5, UP).scale(0.6)
        label6 = Tex("Dog").next_to(img6, UP).scale(0.6)
        label7 = Tex("Dog").next_to(img7, UP).scale(0.6)

        self.play(
            LaggedStartMap(
                GrowFromPoint,
                Group(img1, img2, img3, img4, img5, img6, img7),
                run_time=5,
                point=ORIGIN,
            )
        )

        self.wait(0.7)

        self.wait(3)
        self.play(
            LaggedStartMap(
                FadeIn,
                VGroup(label1, label2, label3, label4, label5, label6, label7),
                run_time=3,
            )
        )

        self.wait(0.8)

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene1_1()
    scene.render()
