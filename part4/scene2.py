from manim import *
from manim_voiceover import VoiceoverScene


class Scene4_2(VoiceoverScene):
    def construct(self):

        self.wait(1)

        txt = Text("Which loss function is used in SimCLR?").scale(0.9)

        self.play(Write(txt))

        self.play(FadeOut(txt, shift=0.5 * DOWN), run_time=0.8)

        info_nce_math = MathTex(
            r"\mathcal{L} = - \log \frac{\exp(D_P)}{\sum_i \exp(D_{N_i})}"
        )

        info_nce = Text("InfoNCE Loss").scale(0.8)
        info_nce_ul = Underline(info_nce, buff=0.1)
        info_nce_rect = SurroundingRectangle(
            info_nce_math, buff=0.3, color=WHITE, stroke_width=4
        )

        self.play(Write(info_nce), GrowFromEdge(info_nce_ul, LEFT))
        self.play(VGroup(info_nce, info_nce_ul).animate.to_edge(UP))
        self.play(Write(info_nce_math))
        self.play(Create(info_nce_rect))

        self.wait(0.8)

        self.play(VGroup(info_nce_math, info_nce_rect).animate.to_edge(LEFT))

        anchor = Dot(color=GRAY, z_index=1)
        pos = Dot(color=GREEN, z_index=1).shift(2 * RIGHT + 0.75 * DOWN)
        neg1 = Dot(color=RED, z_index=1).shift(1.5 * LEFT + 0.5 * UP)
        neg2 = Dot(color=RED, z_index=1).shift(1.2 * LEFT + 0.5 * DOWN)
        neg3 = Dot(color=RED, z_index=1).shift(1.5 * RIGHT + 1.5 * UP)
        neg4 = Dot(color=RED, z_index=1).shift(0.75 * RIGHT + 1.75 * UP)
        neg5 = Dot(color=RED, z_index=1).shift(0.25 * LEFT + 2.5 * DOWN)
        neg6 = Dot(color=RED, z_index=1).shift(1.5 * LEFT + 2.5 * DOWN)
        neg7 = Dot(color=RED, z_index=1).shift(1.5 * RIGHT + 2.2 * DOWN)

        label_anchor = MathTex(r"A", z_index=1).scale(0.6).next_to(anchor, UP)
        label_pos = MathTex(r"P", z_index=1).scale(0.6).next_to(pos, UP)
        label_neg1 = MathTex(r"N_1", z_index=1).scale(0.6).next_to(neg1, UP)
        label_neg2 = MathTex(r"N_2", z_index=1).scale(0.6).next_to(neg2, UP)
        label_neg3 = MathTex(r"N_3", z_index=1).scale(0.6).next_to(neg3, UP)
        label_neg4 = MathTex(r"N_4", z_index=1).scale(0.6).next_to(neg4, UP)
        label_neg5 = MathTex(r"N_5", z_index=1).scale(0.6).next_to(neg5, RIGHT)
        label_neg6 = MathTex(r"N_6", z_index=1).scale(0.6).next_to(neg6, UP)
        label_neg7 = MathTex(r"N_7", z_index=1).scale(0.6).next_to(neg7, RIGHT)

        dots = VGroup(anchor, pos, neg1, neg2, neg3, neg4, neg5, neg6, neg7)
        labels = VGroup(
            label_anchor,
            label_pos,
            label_neg1,
            label_neg2,
            label_neg3,
            label_neg4,
            label_neg5,
            label_neg6,
            label_neg7,
        )
        VGroup(dots, labels).to_edge(RIGHT, buff=1)

        self.play(Create(anchor), Create(label_anchor))
        self.play(Create(pos), Create(label_pos))
        self.play(Create(neg1), Create(label_neg1))

        line_pos = DashedLine(anchor.get_center(), pos.get_center(), color=GREEN)
        line_neg1 = DashedLine(anchor.get_center(), neg1.get_center(), color=RED)
        line_neg2 = DashedLine(anchor.get_center(), neg2.get_center(), color=RED)
        line_neg3 = DashedLine(anchor.get_center(), neg3.get_center(), color=RED)
        line_neg4 = DashedLine(anchor.get_center(), neg4.get_center(), color=RED)
        line_neg5 = DashedLine(anchor.get_center(), neg5.get_center(), color=RED)
        line_neg6 = DashedLine(anchor.get_center(), neg6.get_center(), color=RED)
        line_neg7 = DashedLine(anchor.get_center(), neg7.get_center(), color=RED)

        self.play(anchor.animate.set_color(GREEN), Create(line_pos))
        self.play(Create(line_neg1))

        self.play(
            LaggedStartMap(Create, VGroup(neg2, neg3, neg4, neg5, neg6, neg7))
        )
        self.play(
            LaggedStartMap(
                Create,
                VGroup(
                    line_neg2, line_neg3, line_neg4, line_neg5, line_neg6, line_neg7
                ),
            ),
            LaggedStartMap(
                FadeIn,
                VGroup(
                    label_neg2,
                    label_neg3,
                    label_neg4,
                    label_neg5,
                    label_neg6,
                    label_neg7,
                ),
            ),
        )

        self.wait(0.7)

        self.play(FadeOut(*self.mobjects, shift=0.5 * RIGHT), run_time=0.9)

        txt = Text("How do we create the positives and negatives?").scale(0.8)

        self.play(Write(txt))

        self.play(FadeOut(txt, shift=0.5 * DOWN), run_time=1)

        self.wait(1)


if __name__ == "__main__":
    scene = Scene4_2()
    scene.render()
