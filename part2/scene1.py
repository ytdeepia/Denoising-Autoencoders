from manim import *
from manim_voiceover import VoiceoverScene


class Scene2_1(VoiceoverScene):
    def construct(self):
        self.wait(1)

        # Family of self-supervised learning
        self.next_section(skip_animations=False)

        circle_self_supervised = Circle(
            radius=3.5,
            color=BLUE_C,
            fill_color=BLUE_C,
            fill_opacity=0.5,
        )

        text_self_supervised = (
            Text("Self-supervised Learning")
            .scale(0.5)
            .next_to(circle_self_supervised, UP, buff=-1.5)
            .set_color(BLUE)
        )

        circle_contrastive = Circle(
            radius=2,
            color=RED_D,
            fill_color=RED_D,
            fill_opacity=0.5,
        ).shift(0.8 * (LEFT + DOWN))

        text_contrastive = (
            Text("Contrastive Learning")
            .scale(0.5)
            .move_to(circle_contrastive.get_center())
            .set_color(RED)
        )

        self.play(FadeIn(circle_self_supervised, text_self_supervised))
        self.wait(1)
        self.play(FadeIn(circle_contrastive, text_contrastive))

        self.wait(0.8)

        self.play(
            FadeOut(
                circle_self_supervised,
                text_self_supervised,
                circle_contrastive,
            ),
            text_contrastive.animate.move_to(
                ORIGIN + (config.frame_height / 2 - 0.5) * UP
            )
            .set_color(WHITE)
            .scale(1.5),
        )

        text_contrastive_ul = Underline(text_contrastive)
        self.play(GrowFromEdge(text_contrastive_ul, LEFT))

        self.wait(0.6)

        # Key idea of contrastive learning
        self.next_section(skip_animations=False)

        latent_space = RoundedRectangle(
            color=BLUE,
            height=config.frame_height - 2,
            width=config.frame_width - 3,
            corner_radius=0.1,
        )

        latent_space = DashedVMobject(
            latent_space, color=latent_space.color, num_dashes=50
        ).next_to(text_contrastive, DOWN, buff=0.5)

        latent_space_title = (
            Text("Latent Space")
            .scale(0.7)
            .set_color(BLUE)
            .next_to(latent_space, DOWN, buff=-0.5)
        )

        self.play(Create(latent_space), FadeIn(latent_space_title))

        img_dog1 = ImageMobject("./img/dog1.jpg").scale_to_fit_width(1.5)
        img_dog2 = ImageMobject("./img/dog2.jpg").scale_to_fit_width(1.5)
        img_cat1 = ImageMobject("./img/cat1.jpg").scale_to_fit_width(1.5)

        dot_dog1 = Dot(color=GREEN, radius=0.1).shift(1.8 * LEFT + 0.4 * DOWN)
        dot_dog2 = Dot(color=GREEN, radius=0.1).shift(1.4 * RIGHT + 0.3 * UP)
        dot_cat = Dot(color=RED, radius=0.1).shift(0.3 * LEFT + 1.2 * DOWN)

        label_dog1 = (
            Tex("Dog")
            .scale(0.5)
            .next_to(dot_dog1, UP, buff=0.1)
            .add_updater(lambda label: label.next_to(dot_dog1, UP, buff=0.1))
        )
        label_dog2 = (
            Tex("Dog")
            .scale(0.5)
            .next_to(dot_dog2, UP, buff=0.1)
            .add_updater(lambda label: label.next_to(dot_dog2, UP, buff=0.1))
        )
        label_cat = (
            Tex("Cat")
            .scale(0.5)
            .next_to(dot_cat, UP, buff=0.1)
            .add_updater(lambda label: label.next_to(dot_cat, UP, buff=0.1))
        )

        self.play(Create(dot_dog1), FadeIn(label_dog1))
        self.play(Create(dot_dog2), FadeIn(label_dog2))
        self.play(Create(dot_cat), FadeIn(label_cat))

        img_dog1.next_to(dot_dog1, (LEFT + UP), buff=0.8)
        img_dog2.next_to(dot_dog2, (RIGHT + UP), buff=0.8)
        img_cat1.next_to(dot_cat, RIGHT, buff=1.1).shift(0.2 * DOWN)

        line_dog1 = DashedLine(dot_dog1, img_dog1).add_updater(
            lambda dl: dl.become(DashedLine(start=dot_dog1, end=img_dog1))
        )
        line_dog2 = DashedLine(dot_dog2, img_dog2).add_updater(
            lambda dl: dl.become(DashedLine(start=dot_dog2, end=img_dog2))
        )
        line_cat = DashedLine(dot_cat, img_cat1).add_updater(
            lambda dl: dl.become(DashedLine(start=dot_cat, end=img_cat1))
        )

        self.play(Create(line_dog1), GrowFromPoint(img_dog1, dot_dog1.get_center()))
        self.play(Create(line_dog2), GrowFromPoint(img_dog2, dot_dog2.get_center()))
        self.play(Create(line_cat), GrowFromPoint(img_cat1, dot_cat.get_center()))

        self.wait(0.7)


        double_arrow1 = DoubleArrow(
            start=dot_dog1, end=dot_dog2, buff=0.1, color=GREEN
        )

        double_arrow2 = DoubleArrow(
            start=dot_dog1, end=dot_cat, buff=0.1, color=RED
        )

        self.play(FadeIn(double_arrow1))
        self.play(FadeIn(double_arrow2))

        double_arrow1.add_updater(
            lambda arrow: arrow.become(
                DoubleArrow(
                    start=dot_dog1,
                    end=dot_dog2,
                    buff=0.1,
                    color=GREEN,
                )
            )
        )

        double_arrow2.add_updater(
            lambda arrow: arrow.become(
                DoubleArrow(
                    start=dot_dog1,
                    end=dot_cat,
                    buff=0.1,
                    color=RED,
                )
            )
        )

        self.wait(0.7)

        self.play(
            LaggedStart(
                AnimationGroup(
                    dot_dog1.animate.shift(RIGHT),
                    dot_dog2.animate.shift(LEFT),
                    run_time=4,
                ),
                AnimationGroup(
                    img_dog1.animate.shift(0.7 * RIGHT),
                    img_dog2.animate.shift(0.7 * LEFT),
                    run_time=4,
                ),
            )
        )

        self.play(
            LaggedStart(
                AnimationGroup(
                    dot_dog1.animate.shift(0.6 * LEFT + 0.2 * UP),
                    dot_cat.animate.shift(RIGHT + 0.2 * DOWN),
                    run_time=4,
                ),
                AnimationGroup(
                    img_dog1.animate.shift(0.4 * LEFT + 0.1 * UP),
                    img_cat1.animate.shift(0.7 * RIGHT + 0.1 * DOWN),
                    run_time=4,
                ),
            )
        )

        line_dog1.clear_updaters()
        line_dog2.clear_updaters()
        line_cat.clear_updaters()
        double_arrow1.clear_updaters()
        double_arrow2.clear_updaters()
        label_cat.clear_updaters()
        label_dog1.clear_updaters()
        label_dog2.clear_updaters()

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN), run_time=0.7)

        txt = Text("What is this loss function?")
        self.play(Write(txt))

        self.play(FadeOut(txt))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_1()
    scene.render()
