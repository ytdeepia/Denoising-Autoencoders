import numpy as np
import matplotlib.pyplot as plt
from manim import *
import numpy as np
from scipy.stats import multivariate_normal
from sklearn.neighbors import KernelDensity
import matplotlib.pyplot as plt
from manim_voiceover import VoiceoverScene

# Constants
np.random.seed(42)
data_points = np.random.multivariate_normal(
    mean=[0, 0], cov=[[1, 0.5], [0.5, 1]], size=100
)
observation = np.array([3, -1])
noise_cov = np.array([[0.5, 0], [0, 0.5]])

# Kernel density estimation for empirical prior
kde = KernelDensity(kernel="gaussian", bandwidth=0.3).fit(data_points)
x_grid, y_grid = np.meshgrid(np.linspace(-5.5, 5.5, 100), np.linspace(-5.5, 5.5, 100))
grid = np.dstack((x_grid, y_grid)).reshape(-1, 2)
prior_density = np.exp(kde.score_samples(grid)).reshape(100, 100)

# Likelihood
likelihood = multivariate_normal(mean=observation, cov=noise_cov).pdf(
    np.dstack((x_grid, y_grid))
)

# Posterior
posterior_unnormalized = prior_density * likelihood
posterior = posterior_unnormalized / posterior_unnormalized.sum()

# Compute posterior mean
x_flat = np.column_stack([x_grid.ravel(), y_grid.ravel()])
posterior_flat = posterior.ravel()
posterior_mean_coord = np.sum(x_flat.T * posterior_flat, axis=1) / posterior_flat.sum()


# Function to extract parametric contours from density data
def extract_contours(density, levels):
    """Extract parametric contours from 2D density data."""
    contours = plt.contour(x_grid, y_grid, density, levels=levels)
    parametric_contours = []
    for collection in contours.collections:
        for path in collection.get_paths():
            vertices = path.vertices
            parametric_contours.append(vertices)
    plt.close()
    return parametric_contours


# Contours for each density
prior_contours = extract_contours(
    prior_density, levels=np.linspace(1e-3, np.max(prior_density), 10)
)
likelihood_contours = extract_contours(
    likelihood, levels=np.linspace(1e-3, np.max(likelihood), 10)
)
posterior_contours = extract_contours(
    posterior, levels=np.linspace(1e-3, np.max(posterior), 10)
)


class Scene2_1(VoiceoverScene):
    def construct(self):

        np.random.seed(42)  # For consistent results

        # MMSE Estimator
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

        labels = []
        for i, point in enumerate(points):
            label = MathTex(rf"x_{i+1}").scale(0.7).next_to(point, UP)
            labels.append(label)
            self.add(label)

        self.play(FadeIn(curve, *points, *labels), run_time=1)

        self.wait(0.8)

        self.play(FadeOut(*self.mobjects, shift=0.5 * RIGHT), run_time=1)

        noising = MathTex(r"\tilde{x}", r"= x + \epsilon")
        noising[0].set_color(RED_C)
        noising.add(SurroundingRectangle(noising, buff=0.2, color=RED_C))
        epsilon = MathTex(r"\epsilon \sim \mathcal{N}(0, \sigma^2)")
        epsilon.add(SurroundingRectangle(epsilon, buff=0.2, color=RED_C))
        denoiser = MathTex(r"\hat{x} =", r"f_{\theta}", r"(x)")
        denoiser[1].set_color(BLUE_D)
        denoiser.add(SurroundingRectangle(denoiser, buff=0.2, color=BLUE_D))

        VGroup(noising, epsilon).arrange(RIGHT, buff=1).next_to(denoiser, UP, buff=0.75)

        label_noising = Tex("Noisy ", "Image").next_to(noising, UP).scale(0.8)
        label_noising[0].set_color(RED_C)
        label_epsilon = Tex("Gaussian Noise").next_to(epsilon, UP).scale(0.8)
        label_denoiser = Tex("Deep ", "Denoiser").next_to(denoiser, DOWN).scale(0.8)
        label_denoiser[1].set_color(BLUE_D)

        self.play(Create(noising), Write(label_noising), run_time=1)
        self.play(Create(epsilon), Write(label_epsilon), run_time=1)

        self.wait(0.7)
        self.play(Create(denoiser), Write(label_denoiser), run_time=1)

        self.wait(0.8)


        notations = VGroup(
            noising, epsilon, denoiser, label_noising, label_epsilon, label_denoiser
        )

        self.play(notations.animate.scale(0.8).to_corner(UL), run_time=1.5)

        loss = MathTex(
            r"\mathcal{L}(x, \hat{x}) = \left(x - \hat{x}\right)^2"
        ).scale(0.8)
        loss.add(SurroundingRectangle(loss, buff=0.2, color=WHITE))

        self.play(Create(loss), run_time=1)

        self.wait(0.8)

        total_loss = MathTex(
            r"\mathcal{L} = \mathbb{E} [ \left(x - \hat{x}\right)^2 ]"
        ).scale(0.8)
        total_loss.add(SurroundingRectangle(total_loss, buff=0.2, color=WHITE))

        self.play(Transform(loss, total_loss), run_time=1)

        self.wait(1)

        total_loss_objective = MathTex(
            r"\text{arg} \min_{\theta} ~ \mathbb{E} [ \left(x - ",
            r"f_{\theta}",
            r"(",
            r"\tilde{x}",
            r")\right)^2 ]",
        ).scale(0.8)
        total_loss_objective[1].set_color(BLUE_D)
        total_loss_objective[3].set_color(RED_C)

        total_loss_objective.add(
            SurroundingRectangle(total_loss_objective, buff=0.2, color=WHITE)
        )

        self.play(Transform(loss, total_loss_objective), run_time=1)

        self.wait(0.8)


        self.play(loss.animate.to_corner(UR), run_time=1)


        mmse = (
            MathTex(
                r"\hat{x}_{MMSE} = \text{arg} \min_{f} ~ \mathbb{E} [ (x - f(",
                r"\tilde{x}",
                r"))^2 ]",
            )
            .scale(0.8)
            .shift(0.2 * DOWN)
        )
        mmse[1].set_color(RED_C)
        mmse.add(SurroundingRectangle(mmse, buff=0.2, color=WHITE))

        mmse_label = Tex("MMSE Estimator").next_to(mmse, UP).scale(0.8)

        self.play(Create(mmse), run_time=1)

        self.wait(0.8)

        self.play(Write(mmse_label), run_time=1)



        self.wait(0.9)

        mmse_approx = (
            MathTex(
                r"f_{\theta}",
                r" \approx \text{arg} \min_{f} ~ \mathbb{E} [ (x - f(",
                r"\tilde{x}",
                r"))^2 ]",
            )
            .scale(0.8)
            .move_to(mmse)
        )
        mmse_approx[0].set_color(BLUE_D)
        mmse_approx[2].set_color(RED_C)
        mmse_approx.add(SurroundingRectangle(mmse_approx, buff=0.2, color=WHITE))

        self.play(Transform(mmse, mmse_approx), run_time=1)

        self.play(FadeOut(notations, loss, mmse_label), run_time=1)

        mmse_approx_txt = (
            Text("The network approximates the MMSE estimator")
            .scale(0.8)
            .to_edge(UP)
        )
        mmse_approx_txt_ul = Underline(mmse_approx_txt)

        self.play(
            Write(mmse_approx_txt),
            GrowFromEdge(mmse_approx_txt_ul, edge=LEFT),
            run_time=1,
        )

        self.wait(1)

        posterior_mean = MathTex(
            r"f_{\theta}", r"\approx", r"\mathbb{E}[X | \tilde{X}]"
        ).scale(0.8)
        posterior_mean[2].set_color(GREEN_C)
        posterior_mean[0].set_color(BLUE_D)
        posterior_mean.add(
            SurroundingRectangle(posterior_mean, buff=0.2, color=WHITE)
        )

        self.play(
            FadeOut(mmse_approx_txt, mmse_approx_txt_ul),
            Transform(mmse, posterior_mean),
            run_time=1,
        )

        self.wait(1)

        posterior_mean_txt = (
            Text("The network approximatess the posterior mean")
            .scale(0.8)
            .to_edge(UP)
        )
        posterior_mean_txt_ul = Underline(posterior_mean_txt)

        self.play(
            Write(posterior_mean_txt),
            GrowFromEdge(posterior_mean_txt_ul, edge=LEFT),
            run_time=1,
        )

        self.wait(0.9)

        self.play(FadeOut(mmse))

        # 2D example
        self.next_section(skip_animations=False)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False,
        ).shift(DOWN)

        points_group = VGroup(
            *[Dot(axes.c2p(x, y), color=BLUE_E, radius=0.025) for x, y in data_points]
        )

        def create_contour_group(contour_data, color):
            contour_group = VGroup()
            for vertices in reversed(contour_data):
                curve = ParametricFunction(
                    lambda t: axes.c2p(*vertices[int(t * (len(vertices) - 1))]),
                    t_range=[0, 1, 0.01],
                    color=color,
                    stroke_width=2,
                    stroke_opacity=1 - (len(contour_group) / len(contour_data)),
                )
                contour_group.add(curve)
            return contour_group

        prior_contour_group = create_contour_group(prior_contours, BLUE_D)
        likelihood_contour_group = create_contour_group(likelihood_contours, RED_C)
        posterior_contour_group = create_contour_group(posterior_contours, GREEN_C)

        observation_point = Dot(
            axes.c2p(*observation), color=RED_C, radius=0.075
        ).set_z_index(10)
        posterior_mean_point = Dot(
            axes.c2p(*posterior_mean_coord), color=GREEN_C, radius=0.075
        ).set_z_index(10)

        figure = VGroup(
            points_group,
            prior_contour_group,
            likelihood_contour_group,
            posterior_contour_group,
            observation_point,
            posterior_mean_point,
        ).move_to(ORIGIN)

        prior_label = MathTex(r"p(X)", color=BLUE_D).next_to(
            prior_contour_group, UP, buff=0.2
        )
        likelihood_label = MathTex(r"p(\tilde{X}|X)", color=RED_C).next_to(
            likelihood_contour_group, UR
        )
        posterior_label = MathTex(r"p(X|\tilde{X})", color=GREEN_C).next_to(
            posterior_contour_group, DOWN
        )

        posterior_mean_label = MathTex(
            r"\mathbb{E}[X|\tilde{X} = \tilde{x}]", color=GREEN_C
        ).next_to(posterior_mean_point, UR, buff=1.5)
        posterior_mean_label.add(
            SurroundingRectangle(posterior_mean_label, buff=0.2, color=GREEN_C)
        )

        line_posterior = Line(
            posterior_mean_point, posterior_mean_label, color=WHITE, buff=0.1
        )

        self.play(FadeIn(points_group))

        self.wait(0.9)

        self.play(Create(prior_contour_group), run_time=2)
        self.play(Write(prior_label))

        self.wait(1)

        self.play(FadeIn(observation_point))
        self.play(
            Indicate(observation_point), color=observation_point.color, run_time=1
        )

        self.wait(0.8)

        self.play(Create(likelihood_contour_group), run_time=2)
        self.play(Write(likelihood_label))

        self.wait(0.9)

        self.wait(tracker.duration * 0.5)
        self.play(Create(posterior_contour_group), run_time=2)
        self.play(Write(posterior_label))

        self.wait(0.9)

        self.play(Uncreate(posterior_contour_group), run_time=2)

        self.wait(0.8)

        self.play(FadeIn(posterior_mean_point))
        self.play(
            LaggedStart(
                Create(line_posterior), Write(posterior_mean_label), lag_ratio=0.7
            ),
            run_time=1.5,
        )

        self.wait(0.7)

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN), run_time=1)

        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_1()
    scene.render()
