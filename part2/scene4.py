from manim import *
from manim_voiceover import VoiceoverScene

import numpy as np


class Scene2_4(VoiceoverScene):
    def construct(self):

        np.random.seed(42)  # For consistent results

        # tweedie's formula
        self.next_section(skip_animations=False)

        tweedie_formula = MathTex(
            r"f_{\theta}",
            r"(",
            r"\tilde{x}",
            r") = ",
            r"\tilde{x}",
            r" +",
            r"\sigma \nabla \log p_{\sigma}(",
            r"\tilde{x}",
            r")",
            color=WHITE,
        ).scale(1.1)
        tweedie_formula[0].set_color(BLUE_D)
        tweedie_formula[2].set_color(RED_C)
        tweedie_formula[4].set_color(RED_C)
        tweedie_formula[7].set_color(RED_C)
        tweedie_formula_rect = SurroundingRectangle(
            tweedie_formula, color=WHITE, buff=0.2
        )

        tweedie_formula_ori = tweedie_formula.copy()
        tweedie_formula_posterior_rect_ori = tweedie_formula_rect.copy()

        tweedie_formula_posterior = MathTex(
            r"\mathbb{E}[x | ",
            r"\tilde{x}",
            r"] = ",
            r"\tilde{x}",
            r" + \sigma \nabla \log p_{\sigma}(",
            r"\tilde{x}",
            r")",
            color=WHITE,
        ).scale(1.1)
        tweedie_formula_posterior[1].set_color(RED_C)
        tweedie_formula_posterior[3].set_color(RED_C)
        tweedie_formula_posterior[5].set_color(RED_C)

        tweedie_formula_posterior_rect = SurroundingRectangle(
            tweedie_formula_posterior, color=WHITE, buff=0.2
        )

        self.wait(1.5)
        self.play(
            LaggedStart(
                Write(tweedie_formula), Create(tweedie_formula_rect), lag_ratio=0.7
            ),
            run_time=3,
        )

        self.wait(0.9)

        maurice = (
            ImageMobject("./img/maurice_tweedie.png")
            .scale_to_fit_width(2)
            .next_to(tweedie_formula, UP, buff=0.5)
        ).shift(4 * UP)

        self.play(maurice.animate.shift(4 * DOWN), run_time=2)

        maurice_txt = (
            Text("Maurice Tweedie (1919-1996)", color=WHITE)
            .scale(0.6)
            .next_to(maurice, RIGHT, buff=0.5)
        )

        self.play(Write(maurice_txt), run_time=1)

        self.wait(0.7)
        self.play(
            Transform(tweedie_formula, tweedie_formula_posterior),
            Transform(tweedie_formula_rect, tweedie_formula_posterior_rect),
            run_time=2,
        )

        self.wait(0.5)

        self.wait(2)
        self.play(
            Transform(tweedie_formula, tweedie_formula_ori),
            Transform(tweedie_formula_rect, tweedie_formula_posterior_rect_ori),
            FadeOut(maurice, maurice_txt),
            run_time=2,
        )

        self.wait(0.8)
        self.play(FadeOut(tweedie_formula, tweedie_formula_rect))

        # illustration with the score
        self.next_section(skip_animations=False)

        mean = np.array([0, 0])  # Mean vector
        cov = np.array([[1, 0.5], [0.5, 1]])  # Covariance matrix

        def gaussian_score(x, mean, cov):
            inv_cov = np.linalg.pinv(cov)
            x_mu = x - mean
            return -x_mu @ inv_cov

        def score_field_func(pos):
            gradient = gaussian_score(pos[:2].reshape(1, -1), mean, cov)[0]
            return np.array([gradient[0], gradient[1], 0]) * 0.4  # Scale for visibility

        score_field = ArrowVectorField(
            score_field_func, x_range=[-4, 4, 0.3], y_range=[-3, 3, 0.3]
        )

        self.play(FadeIn(score_field), run_time=2)

        self.play(FadeOut(score_field))

        self.play(FadeIn(tweedie_formula), run_time=1)

        rect1 = SurroundingRectangle(tweedie_formula[4], color=WHITE, buff=0.2)
        rect2 = SurroundingRectangle(
            VGroup(
                tweedie_formula[6],
                tweedie_formula[7],
                tweedie_formula[8],
            ),
            color=WHITE,
            buff=0.2,
        )

        self.wait(2)
        self.play(Create(rect1))
        self.wait(2)
        self.play(Transform(rect1, rect2))

        self.play(FadeOut(rect1), run_time=0.8)

        txt = (
            Text(
                "The denoiser move its inputs towards high density regions",
                color=WHITE,
            )
            .scale(0.7)
            .next_to(tweedie_formula, UP, buff=1)
        )

        self.play(Write(txt), run_time=1)

        self.wait(0.9)


        # Manifold hypothesis again
        self.next_section(skip_animations=False)

        curve = ParametricFunction(
            lambda t: np.array([t, 0.5 * np.sin(t) + 0.2 * t, 0]),
            t_range=np.array([-PI, PI]),
            color=BLUE_D,
            stroke_width=4,
            z_index=-1,
        )

        projections = []
        points = []
        x_values = np.linspace(-PI, PI, 5)
        for x in x_values:
            y = 0.5 * np.sin(x) + 0.2 * x + np.random.uniform(-1, 1)
            point = Dot(point=[x, y, 0], color=BLUE_B)
            points.append(point)

            projected_y = 0.5 * np.sin(x) + 0.2 * x
            projection = Dot(point=[x, projected_y, 0], color=BLUE_B)
            projections.append(projection)

        self.play(FadeOut(tweedie_formula, txt))
        self.play(Create(curve), run_time=2)
        self.play(LaggedStartMap(FadeIn, points), run_time=2)
        self.play(points[0].animate.move_to(projections[0]), run_time=1)
        self.play(points[1].animate.move_to(projections[1]), run_time=1)
        self.play(points[2].animate.move_to(projections[2]), run_time=1)
        self.play(points[3].animate.move_to(projections[3]), run_time=1)
        self.play(points[4].animate.move_to(projections[4]), run_time=1)

        self.wait(0.8)

        self.wait(0.5 * tracker.duration)
        self.play(FadeOut(curve, *points), FadeIn(tweedie_formula), run_time=1)

        self.wait(0.8)

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN), run_time=1)
        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_4()
    scene.render()
