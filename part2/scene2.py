from manim import *
from manim_voiceover import VoiceoverScene
import numpy as np


class Scene2_2(VoiceoverScene):
    def construct(self):

        np.random.seed(42)  # For consistent results

        mean = np.array([0, 0])  # Mean vector
        cov = np.array([[1, 0.5], [0.5, 1]])  # Covariance matrix

        def gaussian_pdf(x, mean, cov):
            size = len(mean)
            det = np.linalg.det(cov)
            norm_const = 1.0 / (np.power((2 * np.pi), size / 2) * np.sqrt(det))
            inv_cov = np.linalg.inv(cov)
            x_mu = x - mean
            result = np.exp(-0.5 * np.sum(x_mu @ inv_cov * x_mu, axis=1))
            return norm_const * result

        def gaussian_score(x, mean, cov):
            inv_cov = np.linalg.pinv(cov)
            x_mu = x - mean
            return -x_mu @ inv_cov

        samples = np.random.multivariate_normal(mean, cov, size=200)
        sample_dots = VGroup(
            *[Dot(point=[s[0], s[1], 0], color=BLUE, radius=0.025) for s in samples]
        )

        level_lines = VGroup()
        levels = np.linspace(0.1, 2, 10)  # Adjust levels for better visibility
        chol_decomp = np.linalg.cholesky(cov)

        def aux(t, level):
            x = (
                np.array(
                    [
                        np.cos(t),
                        np.sin(t),
                    ]
                )
                * level
                @ chol_decomp.T
                + mean
            )

            return (x[0], x[1], 0)

        for level in levels:
            level_lines.add(
                ParametricFunction(
                    lambda t: aux(t, level),  # Transform to ellipse
                    t_range=[0, 2 * np.pi],
                    color=BLUE_D,
                    stroke_width=2,
                    stroke_opacity=(1 - level / max(levels)),  # Decrease opacity
                )
            )

        def score_field_func(pos):
            gradient = gaussian_score(pos[:2].reshape(1, -1), mean, cov)[0]
            return np.array([gradient[0], gradient[1], 0]) * 0.4  # Scale for visibility

        # Estimating the score is easier than the PDF
        self.next_section(skip_animations=False)

        self.wait(0.8)

        distrib = MathTex(r"p(x)", color=BLUE_D).scale(0.8)

        score = MathTex(r"\nabla_x \log", r"p(x)").scale(0.8)
        score[1].set_color(BLUE_D)
        score_txt = (
            Tex("Score", color=WHITE).scale(0.8).next_to(score, UP, buff=0.5)
        )
        self.play(Write(distrib))
        self.wait(2)
        self.play(Transform(distrib, score), Write(score_txt))

        self.wait(0.7)

        self.play(FadeOut(distrib), FadeOut(score_txt))

        distrib_potential = MathTex(r"p(x)", r"= \frac{q(x)}{Z}").scale(0.8)
        distrib_potential[0].set_color(BLUE_D)
        normalizing_constant = MathTex(r"Z = \int q(x) dx").scale(0.8)

        log_distrib = MathTex(r"\log", "p(x)", r"= \log q(x) - \log (Z)").scale(0.8)
        log_distrib[1].set_color(BLUE_D)
        score = MathTex(
            r"\nabla_x \log",
            r"p(x)",
            r"= \nabla_x \log q(x)",
        ).scale(0.8)
        score[1].set_color(BLUE_D)

        self.play(Write(distrib_potential))

        self.wait(2)
        self.play(
            distrib_potential.animate.to_edge(UP, buff=1.0),
            Write(normalizing_constant),
        )

        normalizing_constant_txt = (
            Tex("Normalizing constant", color=WHITE)
            .scale(0.8)
            .next_to(normalizing_constant, UP, buff=0.5)
        )

        rect = SurroundingRectangle(
            VGroup(normalizing_constant, normalizing_constant_txt),
            color=WHITE,
            buff=0.2,
        )
        self.play(Write(normalizing_constant_txt), Create(rect))

        self.wait(0.6)

        log_distrib.next_to(distrib_potential, DOWN, buff=0.75)

        self.play(
            FadeOut(normalizing_constant, normalizing_constant_txt, rect),
        )
        self.play(Write(log_distrib))

        score.next_to(log_distrib, DOWN, buff=0.75)
        self.play(Write(score))

        self.wait(0.9)

        self.play(FadeOut(log_distrib, score, distrib_potential))

        txt = Text("Time for an example!", color=WHITE).scale(0.8)
        self.play(Write(txt))

        self.play(FadeOut(txt, shift=0.5 * RIGHT))

        # 2D Gaussian example
        self.next_section(skip_animations=False)

        score_field = ArrowVectorField(
            score_field_func, x_range=[-4, 4, 0.3], y_range=[-3, 3, 0.3]
        )

        distrib_label = (
            MathTex(r"p(x)", color=BLUE_D).scale(0.8).next_to(level_lines, UL, buff=0.5)
        )

        self.play(LaggedStartMap(Create, sample_dots), run_time=3)
        self.play(Create(level_lines), run_time=2)
        self.play(Write(distrib_label))

        self.wait(0.7)
        score_label = (
            MathTex(r"\nabla_x \log p(x)", color=RED)
            .scale(0.8)
            .next_to(score_field, RIGHT, buff=0.5)
        )

        self.play(
            FadeOut(distrib_label, sample_dots),
            level_lines.animate.set_stroke(opacity=0.4),
            run_time=2,
        )
        self.play(FadeIn(score_field), run_time=2)
        self.play(Write(score_label))

        self.wait(0.8)

        dot = Dot(np.array([2.5, -0.5, 0]), color=WHITE, radius=0.1)
        self.play(FadeIn(dot))

        dot.add_updater(score_field.get_nudge_updater())
        self.wait(6)
        dot.clear_updaters()

        self.wait(0.6)

        txt = Text("The MMSE denoiser learns a score", color=WHITE).scale(0.8)

        rect = SurroundingRectangle(txt, color=WHITE, buff=0.2)

        self.play(FadeOut(score_field, score_label, dot, level_lines))
        self.play(Write(txt))
        self.play(ShowPassingFlash(rect, time_width=0.3), run_time=1.5)

        self.wait(0.7)

        self.play(FadeOut(txt))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_2()
    scene.render()
