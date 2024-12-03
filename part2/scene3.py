from manim import *
from manim_voiceover import VoiceoverScene

import numpy as np


class Scene2_3(VoiceoverScene):
    def construct(self):
        np.random.seed(42)  # For consistent results

        # Rigorous equivalence between gaussian noise and blurring the pdf
        self.next_section(skip_animations=False)

        circle = Arc(radius=2, angle=PI, color=YELLOW).shift(DOWN)
        tangent = Line(
            start=circle.point_from_proportion(0.5) + LEFT * 4,
            end=circle.point_from_proportion(0.5) + RIGHT * 4,
            color=RED,
        )
        self.play(Create(circle))
        self.wait(2)
        self.play(Create(tangent))

        self.play(FadeOut(circle, tangent))

        txt = Text("A classic probability theory result").scale(0.8).to_edge(UP)
        txt_ul = Underline(txt)
        self.play(Write(txt), GrowFromEdge(txt_ul, LEFT))

        self.wait(0.7)

        X = MathTex(r"X", color=BLUE_D)
        Y = MathTex(r"Y", color=RED_C)

        random_var_txt = Tex("Independant Random Variables").scale(0.8)

        VGroup(X, Y).arrange(RIGHT, buff=1.0).move_to(ORIGIN)
        random_var_txt.next_to(VGroup(X, Y), UP, buff=1.0)

        Z = MathTex(r"Z = ", r"X", r"+", r"Y")
        Z[1].set_color(BLUE_D)
        Z[3].set_color(RED_C)

        pdf_z = MathTex(
            r"p_Z(z) = \int", r"p_X(x)", "p_Y(z - x)", "dx", color=WHITE
        ).scale(0.8)
        pdf_z[1].set_color(BLUE_D)
        pdf_z[2].set_color(RED_C)
        pdf_z.add(SurroundingRectangle(pdf_z, buff=0.2, color=WHITE))

        self.play(Write(X), Write(Y))
        self.play(Write(random_var_txt))

        self.wait(0.8)

        self.play(FadeOut(X, Y, random_var_txt), Write(Z))
        self.play(Z.animate.next_to(pdf_z, UP, buff=0.75), Create(pdf_z))

        self.wait(0.9)

        z_ours = MathTex(r"\tilde{X} = ", r"X", r"+", r"\epsilon").move_to(Z)
        z_ours[1].set_color(BLUE_D)
        z_ours[3].set_color(RED_C)

        pdf_z_ours = MathTex(
            r"p_{\tilde{X}}(\tilde{x}) = \int",
            r"p_X(x)",
            r"p_{\epsilon}(\tilde{x} - x)",
            r"dx",
            color=WHITE,
        ).scale(0.8)
        pdf_z_ours[1].set_color(BLUE_D)
        pdf_z_ours[2].set_color(RED_C)
        pdf_z_ours.add(SurroundingRectangle(pdf_z_ours, buff=0.2, color=WHITE))

        self.play(Transform(Z, z_ours))
        self.play(Transform(pdf_z, pdf_z_ours))

        self.wait(0.8)

        # Example with 2D points
        self.next_section(skip_animations=False)

        self.play(FadeOut(Z, pdf_z, txt, txt_ul))

        num_points = 3
        initial_points = np.random.uniform(-2, 2, size=(num_points, 2))
        initial_dots = VGroup(
            *[
                Dot(point=(point[0], point[1], 0), color=BLUE_D)
                for point in initial_points
            ]
        )

        self.play(LaggedStartMap(FadeIn, initial_dots), run_time=2)

        noise_level = 0.3
        num_new_points = 40
        noisy_points = np.vstack(
            [
                point + np.random.normal(0, noise_level, size=(num_new_points, 2))
                for point in initial_points
            ]
        )

        noisy_dots = VGroup(
            *[
                Dot(point=(point[0], point[1], 0), color=RED_C, radius=0.05)
                for point in noisy_points
            ]
        )

        self.play(LaggedStartMap(FadeIn, noisy_dots), run_time=2)

        self.wait(0.8)

        noise_level = 0.5

        noisy_points_2 = np.vstack(
            [
                point + np.random.normal(0, noise_level, size=(num_new_points, 2))
                for point in initial_points
            ]
        )
        noisy_dots_2 = VGroup(
            *[
                Dot(point=(point[0], point[1], 0), color=RED_C, radius=0.05)
                for point in noisy_points_2
            ]
        )

        self.play(Transform(noisy_dots, noisy_dots_2), run_time=2)

        self.wait(0.8)
        for noise_level in np.arange(0.1, 1.0, 0.1):
            noisy_points = np.vstack(
                [
                    point
                    + np.random.normal(0, noise_level, size=(num_new_points, 2))
                    for point in initial_points
                ]
            )
            noisy_dots_new = VGroup(
                *[
                    Dot(point=(point[0], point[1], 0), color=RED_C, radius=0.05)
                    for point in noisy_points
                ]
            )
            self.play(Transform(noisy_dots, noisy_dots_new), run_time=1.2)

        self.play(FadeOut(*self.mobjects, shift=0.5 * RIGHT))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_3()
    scene.render()
