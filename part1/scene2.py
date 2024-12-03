from manim import *
from manim_voiceover import VoiceoverScene


class Scene1_2(VoiceoverScene):
    def construct(self):

        self.wait(1)

        # Supervised learning
        self.next_section(skip_animations=False)

        input_img = ImageMobject("./img/dog.png").scale(0.06)
        input_img_rect = SurroundingRectangle(input_img, color=WHITE, buff=0)
        input_img_title = (
            Text("Input Data", color=WHITE).scale(0.8).next_to(input_img, UP, buff=1)
        )
        input_img_title_ul = Underline(input_img_title)

        label = Text("Dog", color=GREEN).scale(0.8).next_to(input_img, RIGHT, buff=1)
        label_rect = SurroundingRectangle(label, color=GREEN, corner_radius=0.1)
        label_title = (
            Text("Label", color=WHITE)
            .scale(0.8)
            .move_to((label.get_x(), input_img_title.get_y(), 0))
        )
        label_title_ul = Underline(label_title)

        Group(
            input_img,
            input_img_rect,
            input_img_title,
            input_img_title_ul,
            label,
            label_rect,
            label_title,
            label_title_ul,
        ).move_to(0.5 * UP)

        self.play(FadeIn(input_img, input_img_rect))
        self.play(Write(input_img_title), GrowFromEdge(input_img_title_ul, LEFT))
        self.play(FadeIn(label, label_rect))
        self.play(Write(label_title), GrowFromEdge(label_title_ul, LEFT))

        l1 = VGroup()
        l2 = VGroup()
        for i in range(3):
            l1.add(Circle(color=WHITE, radius=0.25))
            l2.add(Circle(color=WHITE, radius=0.25))

        l1.arrange(direction=DOWN, buff=0.5)
        l2.arrange(direction=DOWN, buff=0.5)
        l2.next_to(l1, RIGHT, buff=1.5)

        lines = VGroup()
        for c1 in l1:
            for c2 in l2:
                lines.add(Line(c1, c2))

        VGroup(l1, l2, lines).scale(0.7).move_to(ORIGIN)

        alg_txt = (
            Text("ML Algorithm", color=WHITE)
            .scale(0.8)
            .next_to(VGroup(l1, l2, lines), direction=UP)
        )

        ml_alg = VGroup(l1, l2, lines, alg_txt)
        ml_alg_rect = SurroundingRectangle(
            ml_alg, buff=0.2, color=WHITE, corner_radius=0.1
        )
        VGroup(ml_alg, ml_alg_rect).scale(0.8)

        self.play(
            FadeOut(
                input_img,
                input_img_rect,
                input_img_title,
                input_img_title_ul,
                label,
                label_rect,
                label_title,
                label_title_ul,
            ),
            run_time=0.9,
        )

        self.play(FadeIn(ml_alg, ml_alg_rect))

        Group(input_img, input_img_rect).next_to(ml_alg_rect, LEFT, buff=1)
        input_img_title.next_to(input_img, UP, buff=1.5)
        input_img_title_ul = Underline(input_img_title)

        arrowin = Arrow(
            input_img_rect.get_right(),
            ml_alg_rect.get_left(),
            color=WHITE,
            buff=0.1,
        )

        self.play(
            FadeIn(input_img, input_img_rect, input_img_title, input_img_title_ul)
        )

        output = Text("Bear", color=WHITE).scale(0.8)
        output_rect = SurroundingRectangle(output, color=WHITE, corner_radius=0.1)
        VGroup(output, output_rect).next_to(ml_alg_rect, RIGHT, buff=1)
        output_title = (
            Text("Output", color=WHITE)
            .scale(0.8)
            .move_to((output.get_x(), input_img_title.get_y(), 0))
        )
        output_title_ul = Underline(output_title)

        arrowout = Arrow(
            ml_alg_rect.get_right(), output_rect.get_left(), color=WHITE, buff=0.1
        )

        VGroup(label, label_rect).next_to(output, RIGHT, buff=1.5)
        label_title.move_to((label.get_x(), output_title.get_y(), 0))
        label_title_ul = Underline(label_title)

        self.play(GrowArrow(arrowin))

        self.play(Write(output_title), GrowFromEdge(output_title_ul, LEFT))
        self.play(GrowArrow(arrowout))
        self.play(FadeIn(output, output_rect))

        self.play(Write(label_title), GrowFromEdge(label_title_ul, LEFT))
        self.play(FadeIn(label, label_rect))

        cross = Cross(output_rect, color=RED)

        self.wait(0.6)

        self.play(Create(cross))

        self.play(ApplyWave(lines, amplitude=0.2, reverse_rate_function=True))
        self.play(
            FadeOut(
                VGroup(output, output_rect, cross),
                shift=DOWN,
            ),
            FadeOut(arrowout),
        )

        output = Text("Dog", color=GREEN).scale(0.8)
        output_rect = SurroundingRectangle(output, color=GREEN, corner_radius=0.1)
        VGroup(output, output_rect).next_to(ml_alg_rect, RIGHT, buff=1)

        self.play(GrowArrow(arrowout))
        self.play(FadeIn(output, output_rect))

        self.wait(0.7)

        self.play(FadeOut(label, label_rect, label_title, label_title_ul))

        self.wait(0.5)

        txt = Text("Yes we can!", color=WHITE).scale(1.2)

        self.play(FadeOut(*self.mobjects, shift=DOWN * 2), run_time=1.5)
        self.play(
            LaggedStart(
                Write(txt),
                Flash(
                    txt, line_length=1, num_lines=24, flash_radius=2.5, run_time=1
                ),
                lag_ratio=0.7,
            ),
            run_time=1.5,
        )

        self.play(FadeOut(txt), run_time=0.7)

        # Unsupervised learning
        self.next_section(skip_animations=False)

        dog_img1 = ImageMobject("./img/dog2.jpg").scale_to_fit_width(2)
        dog_img1_rect = SurroundingRectangle(dog_img1, color=WHITE, buff=0)
        dog_img2 = ImageMobject("./img/dog3.jpg").scale_to_fit_width(2)
        dog_img2_rect = SurroundingRectangle(dog_img2, color=WHITE, buff=0)
        dog_img3 = ImageMobject("./img/dog4.jpg").scale_to_fit_width(2)
        dog_img3_rect = SurroundingRectangle(dog_img3, color=WHITE, buff=0)
        cat_img1 = ImageMobject("./img/cat1.jpg").scale_to_fit_width(2)
        cat_img1_rect = SurroundingRectangle(cat_img1, color=WHITE, buff=0)
        cat_img2 = ImageMobject("./img/cat2.jpg").scale_to_fit_width(2)
        cat_img2_rect = SurroundingRectangle(cat_img2, color=WHITE, buff=0)
        cat_img3 = ImageMobject("./img/cat3.jpg").scale_to_fit_width(2)
        cat_img3_rect = SurroundingRectangle(cat_img3, color=WHITE, buff=0)

        Group(dog_img2, dog_img2_rect).next_to(dog_img1_rect, RIGHT, buff=0.5)
        Group(dog_img3, dog_img3_rect).next_to(
            Group(dog_img2, dog_img2_rect, dog_img1, dog_img1_rect), DOWN, buff=0.5
        )
        dogs = Group(
            dog_img1, dog_img1_rect, dog_img2, dog_img2_rect, dog_img3, dog_img3_rect
        )
        dogs.move_to(ORIGIN).shift(4 * LEFT + UP)

        self.play(GrowFromPoint(Group(dog_img1, dog_img1_rect), ORIGIN))
        self.play(GrowFromPoint(Group(dog_img2, dog_img2_rect), ORIGIN))
        self.play(GrowFromPoint(Group(dog_img3, dog_img3_rect), ORIGIN))

        Group(cat_img2, cat_img2_rect).next_to(cat_img1_rect, RIGHT, buff=0.5)
        Group(cat_img3, cat_img3_rect).next_to(
            Group(cat_img2, cat_img2_rect, cat_img1, cat_img1_rect), DOWN, buff=0.5
        )
        cats = Group(
            cat_img1,
            cat_img1_rect,
            cat_img2,
            cat_img2_rect,
            cat_img3,
            cat_img3_rect,
        )
        cats.move_to(ORIGIN).shift(4 * RIGHT + DOWN)

        self.play(GrowFromPoint(Group(cat_img1, cat_img1_rect), ORIGIN))
        self.play(GrowFromPoint(Group(cat_img2, cat_img2_rect), ORIGIN))
        self.play(GrowFromPoint(Group(cat_img3, cat_img3_rect), ORIGIN))

        self.wait(0.6)

        separating_line = DashedLine(
            (dogs.get_corner(UR)[0], config.frame_height / 2, 0),
            (cats.get_corner(DL)[0], -config.frame_height / 2, 0),
            color=WHITE,
            stroke_width=5,
        )

        self.play(Create(separating_line))

        dogs_title = (
            Text("Dogs", color=WHITE).scale(0.8).next_to(dogs, DOWN, buff=1)
        )
        dogs_title_ul = Underline(dogs_title)

        cat_title = Text("Cats", color=WHITE).scale(0.8).next_to(cats, UP, buff=1)
        cat_title_ul = Underline(cat_title)

        self.play(Write(dogs_title), GrowFromEdge(dogs_title_ul, LEFT))
        self.play(Write(cat_title), GrowFromEdge(cat_title_ul, LEFT))

        self.play(FadeOut(*self.mobjects, shift=RIGHT * 2), run_time=0.8)

        # Self-supervised learning
        self.next_section(skip_animations=False)

        unsupervised_txt = Tex(r"Unsupervised \\ Learning", color=WHITE).scale(0.8)

        unsupervised_txt_rect = SurroundingRectangle(
            unsupervised_txt, color=WHITE, buff=0.2, corner_radius=0.1
        )

        supervised_txt = Tex(r"Supervised \\ Learning", color=WHITE).scale(0.8)
        supervised_txt_rect = SurroundingRectangle(
            supervised_txt, color=WHITE, buff=0.2, corner_radius=0.1
        )

        VGroup(
            VGroup(unsupervised_txt, unsupervised_txt_rect),
            VGroup(supervised_txt, supervised_txt_rect),
        ).arrange(RIGHT, buff=1).move_to(ORIGIN)

        self.play(FadeIn(VGroup(unsupervised_txt, unsupervised_txt_rect)))
        self.play(FadeIn(VGroup(supervised_txt, supervised_txt_rect)))

        selfsupervised_txt = Tex(r"Self-supervised \\ Learning", color=BLUE).scale(
            0.8
        )
        selfsupervised_txt_rect = SurroundingRectangle(
            selfsupervised_txt, color=BLUE, buff=0.2, corner_radius=0.1
        )
        VGroup(selfsupervised_txt, selfsupervised_txt_rect).move_to(
            (config.frame_height / 2 + 0.5) * DOWN
        )
        self.add(selfsupervised_txt, selfsupervised_txt_rect)

        self.play(
            VGroup(unsupervised_txt, unsupervised_txt_rect).animate.shift(3 * LEFT),
            VGroup(supervised_txt, supervised_txt_rect).animate.shift(3 * RIGHT),
            VGroup(selfsupervised_txt, selfsupervised_txt_rect).animate.move_to(
                ORIGIN
            ),
            run_time=2,
        )

        self.wait(0.6)

        self.play(
            FadeOut(
                VGroup(unsupervised_txt, unsupervised_txt_rect),
                VGroup(supervised_txt, supervised_txt_rect),
            ),
            VGroup(selfsupervised_txt, selfsupervised_txt_rect).animate.to_edge(UP),
        )

        VGroup(ml_alg, ml_alg_rect).move_to(0.5 * DOWN)
        self.play(FadeIn(VGroup(ml_alg, ml_alg_rect)))

        input_txt = (
            Text("Input", color=RED).scale(0.8).next_to(ml_alg_rect, LEFT, buff=1.5)
        )
        input_txt_rect = SurroundingRectangle(
            input_txt, color=RED, buff=0.2, corner_radius=0.1
        )

        arrowin = Arrow(
            input_txt_rect.get_right(),
            ml_alg_rect.get_left(),
            color=WHITE,
            buff=0.1,
        )

        output_txt = (
            Text("Output", color=GREEN)
            .scale(0.8)
            .next_to(ml_alg_rect, RIGHT, buff=1.5)
        )
        output_txt_rect = SurroundingRectangle(
            output_txt, color=GREEN, buff=0.2, corner_radius=0.1
        )

        arrowout = Arrow(
            ml_alg_rect.get_right(),
            output_txt_rect.get_left(),
            color=WHITE,
            buff=0.1,
        )

        pretext_txt = (
            Text("Pretext Task", color=WHITE)
            .scale(0.8)
            .next_to(output_txt_rect, UP, buff=1.5)
        )
        pretext_txt_ul = Underline(pretext_txt)

        self.play(FadeIn(VGroup(input_txt, input_txt_rect)))
        self.play(GrowArrow(arrowin))

        self.play(Write(pretext_txt), GrowFromEdge(pretext_txt_ul, LEFT))
        self.play(GrowArrow(arrowout))
        self.play(FadeIn(VGroup(output_txt, output_txt_rect)))

        self.wait(0.7)

        self.play(
            ApplyWave(lines, amplitude=0.2, reverse_rate_function=True),
            run_time=1.5,
        )
        self.wait(1)
        self.play(
            ApplyWave(lines, amplitude=0.2, reverse_rate_function=True),
            run_time=1.5,
        )

        self.play(FadeOut(*self.mobjects))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene1_2()
    scene.render()
