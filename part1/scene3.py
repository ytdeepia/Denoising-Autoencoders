from manim import *
from manim_voiceover import VoiceoverScene

class Scene1_3(VoiceoverScene):
    def construct(self):
        # Objective
        self.next_section(skip_animations=False)

        encoder = Polygon(
            [-1, 1, 0], [1, 0.4, 0], [1, -0.4, 0], [-1, -1, 0], color=PURPLE
        )
        encoder_txt = (
            Tex("Encoder", color=WHITE).scale(0.6).move_to(encoder.get_center())
        )

        bottleneck_txt = Tex("Bottleneck", color=WHITE).scale(0.6)
        bottleneck = SurroundingRectangle(bottleneck_txt, buff=0.3, color=BLUE)
        bottleneck_g = VGroup(bottleneck, bottleneck_txt)
        bottleneck_g.next_to(encoder, direction=RIGHT, buff=0.4)

        decoder = Polygon(
            [-1, 0.4, 0], [1, 1, 0], [1, -1, 0], [-1, -0.4, 0], color=PURPLE
        ).next_to(bottleneck, direction=RIGHT, buff=0.4)
        decoder_txt = (
            Tex("Decoder", color=WHITE).scale(0.6).move_to(decoder.get_center())
        )

        autoencoder = VGroup(
            encoder, bottleneck, decoder, encoder_txt, bottleneck_txt, decoder_txt
        )
        autoencoder.move_to(ORIGIN).scale(0.8)

        self.play(Create(encoder), Write(encoder_txt))
        self.play(Create(bottleneck_g))
        self.play(Create(decoder), Write(decoder_txt))

        self.wait(0.6)

        noisy = ImageMobject("./img/noisy_cameraman_50.jpg").scale_to_fit_width(2)
        noisy.add(SurroundingRectangle(noisy, buff=0.0, color=BLUE))

        output = ImageMobject("./img/noisy_cameraman_20.jpg").scale_to_fit_width(2)
        output.add(SurroundingRectangle(output, buff=0.0, color=RED))

        clean = ImageMobject("./img/cameraman.jpg").scale_to_fit_width(2)
        clean.add(SurroundingRectangle(clean, buff=0.0, color=GREEN))

        noisy.next_to(autoencoder, direction=LEFT, buff=1.25)
        output.next_to(autoencoder, direction=RIGHT, buff=1.25)

        input_txt = Tex("Input", color=BLUE).scale(0.6).next_to(noisy, direction=DOWN)
        output_txt = Tex("Output", color=RED).scale(0.6).next_to(output, direction=DOWN)

        arrowin = Arrow(noisy.get_right(), autoencoder.get_left(), color=WHITE)
        arrowout = Arrow(autoencoder.get_right(), output.get_left(), color=WHITE)

        self.play(
            LaggedStart(FadeIn(noisy, input_txt), GrowArrow(arrowin), lag_ratio=0.5)
        )
        self.wait(1)
        self.play(
            LaggedStart(
                GrowArrow(arrowout), FadeIn(output, output_txt), lag_ratio=0.5
            )
        )

        self.wait(0.7)


        # Training
        self.next_section(skip_animations=False)

        self.play(
            FadeOut(autoencoder, arrowin, arrowout),
            Group(noisy, input_txt).animate.move_to(2 * LEFT),
            Group(output, output_txt).animate.move_to(2 * RIGHT),
        )

        txt_mse = Tex("Mean Squared Error", color=WHITE).next_to(
            Group(noisy, output), direction=UP, buff=2
        )
        txt_mse_ul = Underline(txt_mse, buff=0.1, color=WHITE)

        self.play(Write(txt_mse), GrowFromEdge(txt_mse_ul, LEFT))

        self.wait(0.7)

        cross = Cross(noisy, color=RED, scale_factor=1.2)
        self.play(Create(cross))

        self.wait(0.8)


        clean.move_to(noisy)
        clean_txt = (
            Tex("Clean Image", color=GREEN)
            .scale(0.6)
            .next_to(clean, direction=DOWN)
        )

        self.play(FadeOut(noisy, input_txt, cross, shift=DOWN * 0.5))
        self.wait(1)
        self.play(FadeIn(clean, clean_txt))

        self.wait(0.7)


        x = MathTex("x", color=GREEN).move_to(noisy)
        x_hat = MathTex(r"\hat{x}", color=RED).move_to(output)

        self.play(LaggedStart(FadeOut(clean), FadeIn(x), lag_ratio=0.5))
        self.play(LaggedStart(FadeOut(output), FadeIn(x_hat), lag_ratio=0.5))
        self.wait(1)
        mse_formula = MathTex(
            r"\text{MSE} = ||", r"x", r"-", r"\hat{x}", r"||^2", color=WHITE
        ).scale(0.8)

        self.play(
            x.animate.move_to(mse_formula[1]),
            x_hat.animate.move_to(mse_formula[3]),
            Write(VGroup(mse_formula[0], mse_formula[2], mse_formula[4])),
            FadeOut(clean_txt, output_txt),
        )

        self.wait(0.9)

        autoencoder.move_to(2 * UP)
        noisy.next_to(autoencoder, direction=LEFT, buff=1.25)
        output.next_to(autoencoder, direction=RIGHT, buff=1.25)
        arrowin = Arrow(noisy.get_right(), autoencoder.get_left(), color=WHITE)
        arrowout = Arrow(autoencoder.get_right(), output.get_left(), color=WHITE)

        self.play(
            FadeOut(*self.mobjects),
            FadeIn(autoencoder, noisy, output, arrowin, arrowout),
        )

        self.wait(0.9)

        x_noisy = MathTex(r"x_{\text{noisy}}", color=BLUE).next_to(
            noisy, direction=DOWN, buff=2
        )
        x_hat = MathTex(r"\hat{x}", color=RED).next_to(
            output, direction=DOWN, buff=2
        )

        arrow_func = Arrow(
            x_noisy.get_right(), x_hat.get_left(), color=WHITE, buff=2
        )
        f = MathTex(r"f", color=WHITE).next_to(arrow_func, direction=DOWN, buff=0.5)

        self.play(FadeIn(x_noisy))
        self.play(LaggedStart(GrowArrow(arrow_func), FadeIn(f), lag_ratio=0.3))
        self.play(FadeIn(x_hat))

        rect_f = SurroundingRectangle(f, buff=0.2, color=WHITE)
        rect_autoencoder = SurroundingRectangle(autoencoder, buff=0.2, color=WHITE)

        self.play(ShowPassingFlash(rect_autoencoder), run_time=2)
        self.play(ShowPassingFlash(rect_f))

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene1_3()
    scene.render()
