from manim import *
from manim_voiceover import VoiceoverScene


class Scene1_1(VoiceoverScene):
    def construct(self):
        # Diffusion models samples
        self.next_section(skip_animations=False)

        corgi1 = ImageMobject("./img/corgi_5.png").scale_to_fit_width(2)
        corgi2 = ImageMobject("./img/corgi_2.png").scale_to_fit_width(2)
        corgi3 = ImageMobject("./img/corgi_3.png").scale_to_fit_width(2)
        corgi4 = ImageMobject("./img/corgi_4.png").scale_to_fit_width(2)
        corgi5 = ImageMobject("./img/corgi_5.png").scale_to_fit_width(2)
        noisy1 = ImageMobject("./img/noisy_corgi_1.png").scale_to_fit_width(2)
        noisy2 = ImageMobject("./img/noisy_corgi_2.png").scale_to_fit_width(2)
        noisy3 = ImageMobject("./img/noisy_corgi_3.png").scale_to_fit_width(2)
        hd1 = ImageMobject("./img/hd1.png").scale_to_fit_width(3)
        hd2 = ImageMobject("./img/hd2.png").scale_to_fit_width(3)
        hd3 = ImageMobject("./img/hd3.png").scale_to_fit_width(3)
        hd4 = ImageMobject("./img/hd4.png").scale_to_fit_width(3)

        images = [
            corgi1,
            corgi2,
            corgi3,
            corgi4,
            corgi5,
            noisy1,
            noisy2,
            noisy3,
            hd1,
            hd2,
            hd3,
            hd4,
        ]
        for img in images:
            rect = SurroundingRectangle(img, color=WHITE, buff=0.0)
            img.add(rect)

        state1 = Circle(radius=0.75, color=WHITE).shift(2 * LEFT)
        state2 = Circle(radius=0.75, color=WHITE).shift(2 * RIGHT)
        state1_txt = MathTex(r"x_t").scale(0.8).move_to(state1)
        state2_txt = MathTex(r"x_{t-1}").scale(0.8).move_to(state2)

        arrow_backward = Arrow(state1.get_right(), state2.get_left(), buff=0.1)
        arrow_backward_txt = (
            MathTex(r"p_{\theta}(x_{t-1}|x_t)").scale(0.8).next_to(arrow_backward, DOWN)
        )
        arrow_forward = CurvedArrow(
            state2.get_top(),
            state1.get_top(),
        )
        arrow_forward_txt = (
            MathTex(r"q(x_t|x_{t-1})").scale(0.8).next_to(arrow_forward, UP)
        )

        rect = SurroundingRectangle(
            VGroup(
                state1,
                state2,
                arrow_backward,
                arrow_forward,
                state1_txt,
                state2_txt,
                arrow_backward_txt,
                arrow_forward_txt,
            ),
            buff=0.25,
            color=WHITE,
            corner_radius=0.05,
        )

        diff_model = (
            VGroup(
                state1,
                state2,
                arrow_backward,
                arrow_forward,
                state1_txt,
                state2_txt,
                arrow_backward_txt,
                arrow_forward_txt,
                rect,
            )
            .move_to(ORIGIN)
            .scale(0.6)
        )
        diff_model_txt = Tex("Diffusion model").next_to(diff_model, UP)

        corgi1.move_to(LEFT * (config.frame_width / 2 + corgi1.width / 2 + 0.5))
        corgi2.move_to(RIGHT * (config.frame_width / 2 + corgi2.width / 2 + 0.5))
        corgi3.move_to(UP * (config.frame_height / 2 + corgi3.height / 2 + 0.5))
        corgi4.move_to(DOWN * (config.frame_height / 2 + corgi4.height / 2 + 0.5))

        self.add(corgi1, corgi2, corgi3, corgi4)

        self.play(
            LaggedStart(
                corgi1.animate.move_to(4 * LEFT),
                corgi2.animate.move_to(4 * RIGHT),
                corgi3.animate.move_to(2 * UP),
                corgi4.animate.move_to(2 * DOWN),
                lag_ratio=0.25,
            ),
            run_time=3,
        )

        self.play(
            FadeOut(corgi3, corgi4, run_time=1),
            LaggedStart(
                Create(
                    VGroup(
                        state1,
                        state2,
                        arrow_backward,
                        arrow_forward,
                        state1_txt,
                        state2_txt,
                        arrow_backward_txt,
                        arrow_forward_txt,
                    )
                ),
                Create(rect),
                Write(diff_model_txt, run_time=1.5),
                lag_ratio=0.8,
                run_time=3,
            ),
        )

        self.wait(0.7)

        noisy1.set_z_index(-1).move_to(corgi1)
        noisy2.set_z_index(-1).move_to(corgi1)
        noisy3.set_z_index(-1).move_to(corgi1)

        self.play(FadeOut(diff_model, diff_model_txt, corgi2, run_time=1))

        self.add(noisy1, noisy2, noisy3)
        self.play(noisy1.animate.shift(2.5 * RIGHT), run_time=1)
        self.play(noisy2.animate.shift(5 * RIGHT), run_time=1)
        self.play(noisy3.animate.shift(7.5 * RIGHT), run_time=1)

        self.wait(0.8)

        x0_label = MathTex(r"x_{0}").next_to(corgi1, DOWN)
        x250_label = MathTex(r"x_{250}").next_to(noisy1, DOWN)
        x500_label = MathTex(r"x_{500}").next_to(noisy2, DOWN)
        x750_label = MathTex(r"x_{750}").next_to(noisy3, DOWN)

        self.play(
            LaggedStart(
                Write(x0_label),
                Write(x250_label),
                Write(x500_label),
                Write(x750_label),
                lag_ratio=0.5,
            ),
            run_time=2,
        )

        curved_arrow1 = CurvedArrow(
            noisy3.get_top(),
            noisy2.get_top(),
        )
        curved_arrow2 = CurvedArrow(
            noisy2.get_top(),
            noisy1.get_top(),
        )
        curved_arrow3 = CurvedArrow(
            noisy1.get_top(),
            corgi1.get_top(),
        )

        self.play(Create(curved_arrow1))
        self.play(Create(curved_arrow2))
        self.play(Create(curved_arrow3))

        self.wait(0.8)

        hd1.move_to(3 * LEFT + 2 * UP)
        hd2.move_to(3 * LEFT + 2 * DOWN)
        hd3.move_to(3 * RIGHT + 2 * UP)
        hd4.move_to(3 * RIGHT + 2 * DOWN)

        self.play(
            LaggedStart(
                GrowFromPoint(hd1, ORIGIN),
                GrowFromPoint(hd2, ORIGIN),
                GrowFromPoint(hd3, ORIGIN),
                GrowFromPoint(hd4, ORIGIN),
                lag_ratio=0.5,
            ),
            FadeOut(
                corgi1,
                noisy1,
                noisy2,
                noisy3,
                x0_label,
                x250_label,
                x500_label,
                x750_label,
                curved_arrow1,
                curved_arrow2,
                curved_arrow3,
            ),
            run_time=4,
        )

        self.wait(0.8)
        txt = Tex("What's this formula?")

        self.play(
            LaggedStart(
                FadeOut(hd1, hd2, hd3, hd4, shift=0.5 * DOWN),
                Write(txt),
                lag_ratio=0.8,
            ),
            run_time=2,
        )

        self.wait(0.8)

        txt2 = Tex("Let's find out!")

        self.play(
            LaggedStart(
                FadeOut(txt, shift=0.5 * RIGHT), Write(txt2), lag_ratio=0.8
            ),
            run_time=1.5,
        )

        self.play(
            Flash(
                txt2, line_length=1.5, num_lines=18, flash_radius=1.8, color=YELLOW
            )
        )

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN))
        self.wait(1)


if __name__ == "__main__":
    scene = Scene1_1()
    scene.render()
