from manim import *
from manim_voiceover import VoiceoverScene

import numpy as np


class Scene2_2(VoiceoverScene):
    def construct(self):
        self.wait(1)

        # Contrative loss
        self.next_section(skip_animations=False)

        txt = Text('"The" Contrastive Loss').scale(1.5)

        self.play(Write(txt))

        self.play(FadeOut(txt, shift=0.5 * RIGHT))


        dot1 = Dot(ORIGIN, radius=0.15, color=GREEN)
        dot2 = Dot(ORIGIN, radius=0.15, color=GREEN)
        margin = MathTex(r"m", color=BLUE_C).scale(0.8)
        VGroup(dot1, dot2, margin).arrange(RIGHT, buff=2).move_to(ORIGIN)

        self.play(Create(dot1), Create(dot2), Write(margin))

        dots_brace = Brace(VGroup(dot1, dot2), direction=DOWN)
        dots_brace_text = dots_brace.get_text("Pair", buff=0.1).scale(0.6)

        margin_txt = (
            Text("Margin", color=BLUE_C)
            .scale(0.6)
            .move_to((margin.get_x(), dots_brace_text.get_y(), 0))
        )

        self.play(FadeIn(dots_brace), Write(dots_brace_text))
        self.play(Write(margin_txt))

        self.wait(0.7)


        txt_pos = Text("Positive Pair", color=WHITE).scale(0.8).to_edge(UP)
        txt_pos_ul = Underline(txt_pos)

        self.play(
            GrowFromEdge(txt_pos_ul, LEFT),
            Write(txt_pos),
            FadeOut(dots_brace_text, dots_brace, margin_txt, margin),
            run_time=0.7,
        )

        # Positive pairs
        self.next_section(skip_animations=False)


        self.play(
            dot1.animate.move_to(2 * LEFT + UP),
            dot2.animate.move_to(2 * RIGHT + DOWN),
        )

        dot1.set_z_index(1)
        dot2.set_z_index(1)

        line = DashedLine(dot1.get_center(), dot2.get_center())
        self.play(Create(line))

        mid_dot = Dot((dot1.get_center() + dot2.get_center()) / 2, radius=0.05)
        arrow1 = Arrow(dot1.get_center(), mid_dot, buff=0)
        arrow2 = Arrow(dot2.get_center(), mid_dot, buff=0)

        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(FadeOut(arrow1), FadeOut(arrow2))
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(FadeOut(arrow1), FadeOut(arrow2))

        self.wait(0.8)

        brace_dist = BraceBetweenPoints(dot1.get_center(), dot2.get_center())
        brace_dist_text = brace_dist.get_text("D", buff=0.1)

        self.play(FadeIn(brace_dist), Write(brace_dist_text))

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN), run_time=0.9)

        # Negative pairs
        self.next_section(skip_animations=False)

        txt_neg = Text("Negative Pair", color=WHITE).scale(0.8).to_edge(UP)
        txt_neg_ul = Underline(txt_neg)

        self.play(GrowFromEdge(txt_neg_ul, LEFT), Write(txt_neg))

        dot1 = Dot(ORIGIN, radius=0.1, color=RED, z_index=1).move_to(0.5 * DOWN)
        dot2 = Dot(ORIGIN, radius=0.1, color=RED, z_index=1).move_to(
            0.5 * UP + 1.2 * RIGHT
        )
        margin_circle = Circle(radius=2.5, color=BLUE_C).move_to(dot1.get_center())
        margin_circle = DashedVMobject(margin_circle, num_dashes=40, color=BLUE_C)
        margin_label = MathTex(r"m", color=BLUE_C).next_to(
            margin_circle, LEFT, buff=0.2
        )

        self.play(Create(dot1), Create(dot2))
        self.play(Create(margin_circle), Write(margin_label))

        line = DashedLine(dot1.get_center(), dot2.get_center()).add_updater(
            lambda x: x.put_start_and_end_on(dot1.get_center(), dot2.get_center())
        )

        self.play(Create(line))

        brace_d = BraceBetweenPoints(dot1.get_center(), dot2.get_center())
        brace_d.add_updater(
            lambda x: x.become(
                BraceBetweenPoints(dot1.get_center(), dot2.get_center())
            )
        )

        brace_d_text = brace_d.get_text("D", buff=0.1)

        self.play(FadeIn(brace_d), Write(brace_d_text))

        arrow1 = Arrow(dot1.get_center(), dot2.get_center(), buff=0)

        self.play(GrowArrow(arrow1))
        self.play(FadeOut(arrow1))
        self.play(GrowArrow(arrow1))
        self.play(FadeOut(arrow1))

        self.wait(0.6)
        self.play(GrowArrow(arrow1))
        self.play(FadeOut(arrow1))
        self.play(GrowArrow(arrow1))
        self.play(FadeOut(arrow1))

        self.wait(0.8)

        self.play(FadeOut(brace_d_text))

        vec_dir = dot2.get_center() - dot1.get_center()
        vec_dir = vec_dir / np.linalg.norm(vec_dir)

        self.play(dot2.animate.shift(2 * vec_dir))

        brace_d_text = MathTex(r"D > m").scale(0.8)
        brace_d.put_at_tip(brace_d_text, 0.2)

        self.play(Write(brace_d_text))

        self.wait(0.8)

        brace_d.clear_updaters()
        diag = VGroup(
            dot1, dot2, line, margin_circle, margin_label, brace_d, brace_d_text
        )

        self.play(diag.animate.scale(0.5).shift(3 * RIGHT))

        txt_formula = MathTex(
            r"\mathcal{L} = \max \left( 0, m - D \right)^2"
        ).next_to(diag, LEFT, buff=1.5)

        self.play(Write(txt_formula))

        self.play(
            FadeOut(
                txt_formula,
                margin_circle,
                margin_label,
                brace_d,
                brace_d_text,
                dot1,
                dot2,
                line,
                txt_formula,
                txt_neg,
                txt_neg_ul,
                shift=0.5 * DOWN,
            ),
            run_time=0.8,
        )

        # Putting everything together
        self.next_section(skip_animations=False)

        txt = Text('"The" Contrastive Loss').scale(1.2).to_edge(UP)
        txt_ul = Underline(txt)

        formula_complete = MathTex(
            r"\mathcal{L} = (1 - y) \cdot",
            r"D^2",
            r"+ y \cdot",
            r"\max \left( 0, m - D \right)^2",
        ).scale(1)

        formula_complete[1].set_color(GREEN)
        formula_complete[3].set_color(RED)

        self.play(
            LaggedStart(
                AnimationGroup(GrowFromEdge(txt_ul, LEFT), Write(txt)),
                Write(formula_complete),
                lag_ratio=0.8,
            ),
            run_time=2,
        )

        self.wait(0.8)

        formula_complete_origin = formula_complete.copy()
        formula_pos = MathTex(r"\mathcal{L} =", r"D^2").scale(1)
        formula_pos[1].set_color(GREEN)
        formula_neg = MathTex(
            r"\mathcal{L} =", r"\max \left( 0, m - D \right)^2"
        ).scale(1)
        formula_neg[1].set_color(RED)

        self.wait(2)
        self.play(Transform(formula_complete, formula_pos))
        self.wait(4)
        self.play(Transform(formula_complete, formula_complete_origin))

        self.wait(0.7)

        self.play(Transform(formula_complete, formula_neg))
        self.wait(4)
        self.play(Transform(formula_complete, formula_complete_origin))

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN))
        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_2()
    scene.render()
