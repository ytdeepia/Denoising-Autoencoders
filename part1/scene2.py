from manim import *
from manim_voiceover import VoiceoverScene


class Scene1_2(VoiceoverScene):
    def construct(self):

        # Noisy images examples
        self.next_section(skip_animations=False)

        cameraman = ImageMobject("./img/cameraman.jpg").scale_to_fit_width(3)
        cameraman.add(
            SurroundingRectangle(
                cameraman,
                color=WHITE,
                buff=0,
            )
        )
        cameraman_gaussian = ImageMobject(
            "./img/cameraman_gaussian.jpg"
        ).scale_to_fit_width(3)
        cameraman_gaussian.add(
            SurroundingRectangle(
                cameraman_gaussian,
                color=WHITE,
                buff=0,
            )
        )
        cameraman_poisson = ImageMobject(
            "./img/cameraman_poisson.jpg"
        ).scale_to_fit_width(3)
        cameraman_poisson.add(
            SurroundingRectangle(
                cameraman_poisson,
                color=WHITE,
                buff=0,
            )
        )
        cameraman_speckle = ImageMobject(
            "./img/cameraman_speckle.jpg"
        ).scale_to_fit_width(3)
        cameraman_speckle.add(
            SurroundingRectangle(
                cameraman_speckle,
                color=WHITE,
                buff=0,
            )
        )

        Group(cameraman, cameraman_gaussian, cameraman_speckle).arrange(
            RIGHT, buff=0.5
        ).move_to(ORIGIN)

        txt_ori = Text("Original Image").scale(0.5).next_to(cameraman, DOWN)
        txt_gaussian = (
            Text("Gaussian Noise").scale(0.5).next_to(cameraman_gaussian, DOWN)
        )
        txt_speckle = Text("Speckle Noise").scale(0.5).next_to(cameraman_speckle, DOWN)

        self.play(FadeIn(cameraman), Write(txt_ori), run_time=1.5)
        self.play(FadeIn(cameraman_gaussian), Write(txt_gaussian), run_time=1.5)
        self.play(FadeIn(cameraman_speckle), Write(txt_speckle), run_time=1.5)

        self.wait(0.8)

        self.play(
            FadeOut(
                cameraman,
                cameraman_gaussian,
                cameraman_speckle,
                txt_ori,
                txt_gaussian,
                txt_speckle,
            ),
            run_time=0.8,
        )

        ct_scan = ImageMobject("./img/ct_scan.jpg").scale_to_fit_width(4)
        ct_scan.add(
            SurroundingRectangle(
                ct_scan,
                color=WHITE,
                buff=0,
            )
        )
        ultrasound = ImageMobject("./img/ultrasound.png").scale_to_fit_width(4)
        ultrasound.add(
            SurroundingRectangle(
                ultrasound,
                color=WHITE,
                buff=0,
            )
        )

        Group(ultrasound, ct_scan).arrange(RIGHT, buff=1).move_to(ORIGIN)
        ct_scan.align_to(ultrasound, DOWN)

        ultrasound_txt = Text("Ultrasound").scale(0.5).next_to(ultrasound, DOWN)
        ct_scan_txt = Text("CT Scan").scale(0.5).next_to(ct_scan, DOWN)

        self.play(FadeIn(ultrasound), Write(ultrasound_txt), run_time=1.5)
        self.play(FadeIn(ct_scan), Write(ct_scan_txt), run_time=1.5)

        self.wait(0.6)

        self.play(
            FadeOut(ultrasound, ct_scan, ultrasound_txt, ct_scan_txt, shift=0.5 * DOWN),
            run_time=0.8,
        )

        # Noise approximation
        self.next_section(skip_animations=False)

        txt_gaussian = Text("Gaussian Noise").scale(0.8)
        txt_poisson = Text("Poisson Noise").scale(0.8)

        VGroup(txt_gaussian, txt_poisson).arrange(RIGHT, buff=1).move_to(ORIGIN)

        self.play(
            LaggedStart(Write(txt_gaussian), Write(txt_poisson), lag_ratio=0.3),
            run_time=2,
        )

        self.wait(0.6)

        rect = SurroundingRectangle(
            txt_gaussian,
            buff=0.2,
            color=WHITE,
        )

        self.play(Create(rect))

        self.play(
            FadeOut(txt_poisson, rect),
            txt_gaussian.animate.move_to(3 * UP),
            run_time=0.7,
        )

        gaussian_noise = MathTex(
            r"x_{noisy} = x_{clean} + \epsilon \quad \text{with} \quad \epsilon \sim",
            r"\mathcal{N}(0, \sigma)",
        ).scale(0.8)
        gaussian_noise[1].set_color(BLUE)

        gaussian_noise_2 = (
            VGroup(
                MathTex(r"x_{noisy} = x_{clean} + \epsilon"),
                Tex("with"),
                MathTex(r"\epsilon \sim", "\mathcal{N}(0, \sigma)"),
            )
            .scale(0.8)
            .arrange(DOWN, buff=0.2)
        )

        gaussian_noise_2[2][1].set_color(BLUE)
        gaussian_noise_2.to_edge(RIGHT)

        self.play(Write(gaussian_noise))

        self.wait(0.5)

        self.play(Transform(gaussian_noise, gaussian_noise_2))

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"include_tip": False},
        ).scale(0.8)

        gaussian = axes.plot(
            lambda x: (1 / (2 * 3.14) ** 0.5) * np.exp(-(x**2) / 2),
            color=BLUE,
            x_range=[-4, 4],
        )

        self.play(Create(axes))
        self.play(Create(gaussian))

        self.wait(0.7)

        plot = VGroup(axes, gaussian)

        self.play(plot.animate.scale(0.5).to_edge(LEFT))

        noisy1 = ImageMobject("./img/noisy_cameraman_1.jpg").scale_to_fit_width(3)
        noisy1.add(
            SurroundingRectangle(
                noisy1,
                color=WHITE,
                buff=0,
            )
        )
        noisy2 = ImageMobject("./img/noisy_cameraman_5.jpg").scale_to_fit_width(3)
        noisy2.add(
            SurroundingRectangle(
                noisy2,
                color=WHITE,
                buff=0,
            )
        )
        noisy3 = ImageMobject("./img/noisy_cameraman_10.jpg").scale_to_fit_width(3)
        noisy3.add(
            SurroundingRectangle(
                noisy3,
                color=WHITE,
                buff=0,
            )
        )
        noisy4 = ImageMobject("./img/noisy_cameraman_20.jpg").scale_to_fit_width(3)
        noisy4.add(
            SurroundingRectangle(
                noisy4,
                color=WHITE,
                buff=0,
            )
        )
        noisy5 = ImageMobject("./img/noisy_cameraman_50.jpg").scale_to_fit_width(3)
        noisy5.add(
            SurroundingRectangle(
                noisy5,
                color=WHITE,
                buff=0,
            )
        )

        gaussian_2 = axes.plot(
            lambda x: (1 / (2 * 3.14) ** 0.5) * np.exp(-(x**2) / (0.01 * 2)),
            color=BLUE,
            x_range=[-4, 4],
        )
        gaussian_3 = axes.plot(
            lambda x: (1 / (2 * 3.14) ** 0.5) * np.exp(-(x**2) / (0.1 * 2)),
            color=BLUE,
            x_range=[-4, 4],
        )
        gaussian_4 = axes.plot(
            lambda x: (1 / (2 * 3.14) ** 0.5) * np.exp(-(x**2) / (0.25 * 2)),
            color=BLUE,
            x_range=[-4, 4],
        )
        gaussian_5 = axes.plot(
            lambda x: (1 / (2 * 3.14) ** 0.5) * np.exp(-(x**2) / (0.5 * 2)),
            color=BLUE,
            x_range=[-4, 4],
        )
        gaussian_6 = axes.plot(
            lambda x: (1 / (2 * 3.14) ** 0.5) * np.exp(-(x**2) / (1 * 2)),
            color=BLUE,
            x_range=[-4, 4],
        )

        self.play(FadeIn(noisy1), Transform(gaussian, gaussian_2), run_time=2)

        self.wait(0.6)

        self.play(
            FadeOut(noisy1),
            FadeIn(noisy2),
            Transform(gaussian, gaussian_3),
            run_time=1.5,
        )
        self.play(
            FadeOut(noisy2),
            FadeIn(noisy3),
            Transform(gaussian, gaussian_4),
            run_time=1.5,
        )
        self.play(
            FadeOut(noisy3),
            FadeIn(noisy4),
            Transform(gaussian, gaussian_5),
            run_time=1.5,
        )
        self.play(
            FadeOut(noisy4),
            FadeIn(noisy5),
            Transform(gaussian, gaussian_6),
            run_time=1.5,
        )

        self.play(FadeOut(*self.mobjects, shift=0.5 * RIGHT), run_time=0.6)

        txt = Text("How do we remove Gaussian noise ?").scale(0.8)

        self.play(Create(txt))

        self.play(FadeOut(txt, shift=0.5 * DOWN))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene1_2()
    scene.render()
