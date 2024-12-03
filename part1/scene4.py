from manim import *
from manim_voiceover import VoiceoverScene
import numpy as np


class Scene1_4(VoiceoverScene):
    def construct(self):
        

        np.random.seed(42)  # For consistent results


        # 2D space of images
        self.next_section(skip_animations=False)

        numberplane = NumberPlane()

        self.play(FadeIn(numberplane), run_time=2)

        self.wait(1.1)

        self.wait(1)
        self.play(numberplane.animate.scale(4).set_opacity(0.0))

        img_random_1 = (
            ImageMobject("./img/random_image_1.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_random_1.add(SurroundingRectangle(img_random_1, buff=0.0, color=WHITE))
        img_random_2 = (
            ImageMobject("./img/random_image_2.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_random_2.add(SurroundingRectangle(img_random_2, buff=0.0, color=WHITE))
        img_random_3 = (
            ImageMobject("./img/random_image_3.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_random_3.add(SurroundingRectangle(img_random_3, buff=0.0, color=WHITE))
        img_square = (
            ImageMobject("./img/square.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_square.add(SurroundingRectangle(img_square, buff=0.0, color=WHITE))
        img_circle = (
            ImageMobject("./img/circle.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_circle.add(SurroundingRectangle(img_circle, buff=0.0, color=WHITE))
        img_nb_0 = (
            ImageMobject("./img/original_0.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_nb_0.add(SurroundingRectangle(img_nb_0, buff=0.0, color=WHITE))
        img_nb_1 = (
            ImageMobject("./img/original_1.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_nb_1.add(SurroundingRectangle(img_nb_1, buff=0.0, color=WHITE))
        img_nb_2 = (
            ImageMobject("./img/original_2.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_nb_2.add(SurroundingRectangle(img_nb_2, buff=0.0, color=WHITE))
        img_nb_3 = (
            ImageMobject("./img/original_3.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_nb_3.add(SurroundingRectangle(img_nb_3, buff=0.0, color=WHITE))
        img_nb_4 = (
            ImageMobject("./img/original_4.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_nb_4.add(SurroundingRectangle(img_nb_4, buff=0.0, color=WHITE))
        img_nb_5 = (
            ImageMobject("./img/original_5.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        img_nb_5.add(SurroundingRectangle(img_nb_5, buff=0.0, color=WHITE))

        dot_img_random_1 = Dot(color=RED).move_to(1.25 * UP + 3.5 * LEFT)
        img_random_1.next_to(dot_img_random_1, direction=UL, buff=0.75)
        line_img_random_1 = Line(dot_img_random_1, img_random_1, color=WHITE)

        dot_img_random_2 = Dot(color=RED).move_to(1.5 * UP + 5 * RIGHT)
        img_random_2.next_to(dot_img_random_2, direction=UL, buff=0.75)
        line_img_random_2 = Line(dot_img_random_2, img_random_2, color=WHITE)

        dot_img_random_3 = Dot(color=RED).move_to(1.5 * DOWN + 4.2 * RIGHT)
        img_random_3.next_to(dot_img_random_3, direction=DR, buff=0.75)
        line_img_random_3 = Line(dot_img_random_3, img_random_3, color=WHITE)

        dot_img_square = Dot(color=GREEN).move_to(1.2 * DOWN + 5 * LEFT)
        img_square.next_to(dot_img_square, direction=DR, buff=0.75)
        line_img_square = Line(dot_img_square, img_square, color=WHITE)

        dot_img_circle = Dot(color=GREEN).move_to(0.9 * DOWN + 2.5 * RIGHT)
        img_circle.next_to(dot_img_circle, direction=DL, buff=0.75)
        line_img_circle = Line(dot_img_circle, img_circle, color=WHITE)

        self.play(
            LaggedStart(
                Create(dot_img_random_1),
                Create(line_img_random_1),
                FadeIn(img_random_1[0]),
                Create(img_random_1[1]),
            ),
            run_time=1.5,
        )

        self.play(
            LaggedStart(
                Create(dot_img_random_2),
                Create(line_img_random_2),
                FadeIn(img_random_2[0]),
                Create(img_random_2[1]),
            ),
            run_time=1.5,
        )

        self.play(
            LaggedStart(
                Create(dot_img_random_3),
                Create(line_img_random_3),
                FadeIn(img_random_3[0]),
                Create(img_random_3[1]),
            ),
            run_time=1.5,
        )

        self.play(
            LaggedStart(
                Create(dot_img_square),
                Create(line_img_square),
                FadeIn(img_square[0]),
                Create(img_square[1]),
            ),
            run_time=1.5,
        )

        self.play(
            LaggedStart(
                Create(dot_img_circle),
                Create(line_img_circle),
                FadeIn(img_circle[0]),
                Create(img_circle[1]),
            ),
            run_time=1.5,
        )

        self.wait(0.9)


        self.play(
            FadeOut(
                dot_img_random_1,
                line_img_random_1,
                img_random_1,
                dot_img_random_2,
                line_img_random_2,
                img_random_2,
                dot_img_circle,
                line_img_circle,
                img_circle,
            )
        )

        points = []
        projections = []
        for _ in range(3):
            x = np.random.uniform(-PI, PI)
            y = 0.5 * np.sin(x) + 0.2 * x + np.random.uniform(-1, 1)
            point = Dot(point=[x, y, 0], color=BLUE_B)
            points.append(point)

            projected_y = 0.5 * np.sin(x) + 0.2 * x
            projection = Dot(point=[x, projected_y, 0], color=BLUE_B)
            projections.append(projection)

        img_nb_0.next_to(projections[0], direction=DR, buff=0.75)
        line_img_nb_0 = Line(projections[0], img_nb_0, color=WHITE)

        img_nb_1.next_to(projections[1], direction=UR, buff=0.75)
        line_img_nb_1 = Line(projections[1], img_nb_1, color=WHITE)

        img_nb_2.next_to(projections[2], direction=UL, buff=0.75)
        line_img_nb_2 = Line(projections[2], img_nb_2, color=WHITE)

        curve = ParametricFunction(
            lambda t: np.array([t, 0.5 * np.sin(t) + 0.2 * t, 0]),
            t_range=np.array([-PI, PI]),
            color=BLUE_D,
            stroke_width=4,
            z_index=-1,
        )

        self.play(
            LaggedStart(
                Create(projections[0]),
                Create(line_img_nb_0),
                FadeIn(img_nb_0[0]),
                Create(img_nb_0[1]),
            ),
            run_time=1.5,
        )

        self.play(
            LaggedStart(
                Create(projections[1]),
                Create(line_img_nb_1),
                FadeIn(img_nb_1[0]),
                Create(img_nb_1[1]),
            ),
            run_time=1.5,
        )

        self.play(
            LaggedStart(
                Create(projections[2]),
                Create(line_img_nb_2),
                FadeIn(img_nb_2[0]),
                Create(img_nb_2[1]),
            ),
            run_time=1.5,
        )

        self.wait(1)

        self.play(
            FadeOut(
                img_square,
                dot_img_square,
                line_img_square,
                img_random_3,
                dot_img_random_3,
                line_img_random_3,
            )
        )
        self.wait(1.5)

        self.play(Create(curve), run_time=2)

        txt_manifold = (
            Tex("Number Manifold", color=BLUE)
            .next_to(curve, direction=RIGHT, buff=0.2)
            .scale(0.8)
        )

        self.wait(2)

        self.play(Write(txt_manifold))

        self.wait(1)

        # Noisy data and projections
        self.next_section(skip_animations=False)

        label_nb_0 = MathTex(r"x_1", color=BLUE_B).next_to(
            projections[0], direction=UP, buff=0.3
        )
        label_nb_1 = MathTex(r"x_2", color=BLUE_B).next_to(
            projections[1], direction=UP, buff=0.3
        )
        label_nb_2 = MathTex(r"x_3", color=BLUE_B).next_to(
            projections[2], direction=DOWN, buff=0.3
        )

        self.play(
            LaggedStart(
                Create(label_nb_0),
                Create(label_nb_1),
                Create(label_nb_2),
                lag_ratio=0.5,
            ),
            run_time=1.5,
        )

        self.wait(0.8)


        projections_cp = [p.copy() for p in projections]

        self.play(
            projections[0].animate.move_to(points[0]),
            FadeOut(label_nb_0, img_nb_0, line_img_nb_0),
            run_time=1,
        )
        self.wait(0.5)
        self.play(
            projections[1].animate.move_to(points[1]),
            FadeOut(label_nb_1, img_nb_1, line_img_nb_1),
            run_time=1,
        )
        self.wait(0.5)
        self.play(
            projections[2].animate.move_to(points[2]),
            FadeOut(label_nb_2, img_nb_2, line_img_nb_2),
            run_time=1,
        )

        self.wait(0.8)


        noisy_nb_0 = (
            ImageMobject("./img/noisy_0.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        noisy_nb_0.add(SurroundingRectangle(noisy_nb_0, buff=0.0, color=WHITE))
        noisy_nb_1 = (
            ImageMobject("./img/noisy_1.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        noisy_nb_1.add(SurroundingRectangle(noisy_nb_1, buff=0.0, color=WHITE))
        noisy_nb_2 = (
            ImageMobject("./img/noisy_2.png")
            .set_resampling_algorithm(RESAMPLING_ALGORITHMS["none"])
            .scale_to_fit_width(1.5)
        )
        noisy_nb_2.add(SurroundingRectangle(noisy_nb_2, buff=0.0, color=WHITE))

        noisy_nb_0.next_to(projections[0], direction=UL, buff=0.75)
        line_noisy_nb_0 = Line(projections[0], noisy_nb_0, color=WHITE)

        noisy_nb_1.next_to(projections[1], direction=UR, buff=0.75)
        line_noisy_nb_1 = Line(projections[1], noisy_nb_1, color=WHITE)

        noisy_nb_2.next_to(projections[2], direction=DL, buff=0.75)
        line_noisy_nb_2 = Line(projections[2], noisy_nb_2, color=WHITE)

        self.play(
            LaggedStart(
                Create(line_noisy_nb_0),
                FadeIn(noisy_nb_0[0]),
                Create(noisy_nb_0[1]),
            ),
            run_time=1,
        )

        self.play(
            LaggedStart(
                Create(line_noisy_nb_1),
                FadeIn(noisy_nb_1[0]),
                Create(noisy_nb_1[1]),
            ),
            run_time=1,
        )

        self.play(
            LaggedStart(
                Create(line_noisy_nb_2),
                FadeIn(noisy_nb_2[0]),
                Create(noisy_nb_2[1]),
            ),
            run_time=1,
        )

        self.wait(0.9)

        self.play(
            projections[0].animate.move_to(projections_cp[0]),
            FadeOut(noisy_nb_0, line_noisy_nb_0),
            run_time=1,
        )

        self.play(
            projections[1].animate.move_to(projections_cp[1]),
            FadeOut(noisy_nb_1, line_noisy_nb_1),
            run_time=1,
        )

        self.play(
            projections[2].animate.move_to(projections_cp[2]),
            FadeOut(noisy_nb_2, line_noisy_nb_2),
            run_time=1,
        )

        self.wait(0.9)

        txt_projection = (
            Tex("The network approximates a projection on the image manifold")
            .scale(0.8)
            .to_edge(UP)
        )
        txt_ul = Underline(txt_projection, buff=0.1, color=WHITE)

        self.play(Write(txt_projection), GrowFromEdge(txt_ul, LEFT))

        self.wait(1)

        self.play(FadeOut(*self.mobjects))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene1_4()
    scene.render()
