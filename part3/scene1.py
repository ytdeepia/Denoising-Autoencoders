from manim import *
from manim_voiceover import VoiceoverScene

import numpy as np


class Scene3_1(VoiceoverScene):
    def construct(self):

        self.wait(1)

        # Intro
        self.next_section(skip_animations=False)

        con_loss_txt = (
            Text("Contrastive Loss")
            .scale(0.8)
            .to_edge(UP, buff=0.2)
            .shift((config.frame_width / 4) * LEFT)
        )
        con_loss_ul = Underline(con_loss_txt)

        triplet_loss_txt = (
            Text("Triplet Loss")
            .scale(0.8)
            .to_edge(UP, buff=0.2)
            .shift((config.frame_width / 4) * RIGHT)
        )
        triplet_loss_ul = Underline(triplet_loss_txt)

        con_easy = MathTex("D_{N} > m", color=WHITE).scale(0.8)
        con_easy_rect = SurroundingRectangle(con_easy, color=WHITE)
        con_null = (
            MathTex("\mathcal{L} = 0", color=RED)
            .next_to(con_easy, DOWN, buff=3)
            .scale(0.8)
        )
        con_null_rect = SurroundingRectangle(con_null, color=RED)
        arrow_con = Arrow(
            con_easy_rect.get_bottom(), con_null_rect.get_top(), color=WHITE
        )

        triplet_easy = MathTex("D(A, P) + m < D(A, N) ", color=WHITE).scale(0.8)
        triplet_easy_rect = SurroundingRectangle(triplet_easy, color=WHITE)
        triplet_null = (
            MathTex("\mathcal{L} = 0", color=RED)
            .next_to(triplet_easy, DOWN, buff=3)
            .scale(0.8)
        )
        triplet_null_rect = SurroundingRectangle(triplet_null, color=RED)
        arrow_triplet = Arrow(
            triplet_easy_rect.get_bottom(), triplet_null_rect.get_top(), color=WHITE
        )

        VGroup(con_easy, con_null, arrow_con, con_easy_rect, con_null_rect).next_to(
            con_loss_txt, DOWN, buff=1.25
        )
        VGroup(
            triplet_easy,
            triplet_null,
            arrow_triplet,
            triplet_easy_rect,
            triplet_null_rect,
        ).next_to(triplet_loss_txt, DOWN, buff=1.25)

        self.play(Write(con_loss_txt), GrowFromEdge(con_loss_ul, LEFT))
        self.play(Write(con_easy), Create(con_easy_rect))
        self.play(GrowArrow(arrow_con))
        self.play(Write(con_null), Create(con_null_rect))

        self.play(Write(triplet_loss_txt), GrowFromEdge(triplet_loss_ul, RIGHT))
        self.play(Write(triplet_easy), Create(triplet_easy_rect))
        self.play(GrowArrow(arrow_triplet))
        self.play(Write(triplet_null), Create(triplet_null_rect))

        triplet_side = VGroup(
            triplet_loss_txt,
            triplet_loss_ul,
            triplet_easy,
            triplet_easy_rect,
            triplet_null,
            triplet_null_rect,
            arrow_triplet,
        )

        con_side = VGroup(
            con_loss_txt,
            con_loss_ul,
            con_easy,
            con_easy_rect,
            con_null,
            con_null_rect,
            arrow_con,
        )

        self.play(
            FadeOut(
                triplet_side,
                shift=0.5 * RIGHT,
            )
        )

        # Contrastive loss easy examples
        self.next_section(skip_animations=False)

        dot1 = Dot(2.5 * LEFT + 0.75 * DOWN, color=RED).set_z_index(1)
        dot2 = Dot(ORIGIN, color=RED).set_z_index(1)

        brace = BraceBetweenPoints(dot1.get_center(), dot2.get_center())
        brace_text = MathTex("D_{N}", color=WHITE).scale(0.8)
        brace.put_at_tip(brace_text)

        brace.add_updater(
            lambda b: b.become(BraceBetweenPoints(dot1.get_center(), dot2.get_center()))
        )

        margin_circle = Circle(
            radius=1.6, color=BLUE_C, fill_color=BLUE_C, fill_opacity=0.5
        ).move_to(dot1.get_center())
        margin_label = MathTex(r"m", color=BLUE_C).next_to(
            margin_circle, (LEFT + DOWN), buff=0.2
        )

        scheme = VGroup(
            dot1, dot2, brace, brace_text, margin_circle, margin_label
        ).move_to(config.frame_width / 4 * RIGHT)

        self.play(Create(dot1), Create(dot2))
        self.play(Create(margin_circle), Write(margin_label))
        self.play(Create(brace), Write(brace_text))

        con_easy2 = MathTex("D_{P} < m", color=WHITE).scale(0.8).move_to(con_easy)
        con_easy2_rect = SurroundingRectangle(con_easy2, color=WHITE)

        direction = (dot1.get_center() - dot2.get_center()) / np.linalg.norm(
            dot2.get_center() - dot1.get_center()
        )

        self.wait(0.3)

        self.play(
            Transform(con_easy, con_easy2),
            Transform(con_easy_rect, con_easy2_rect),
            FadeOut(brace_text),
        )
        self.play(
            dot1.animate.set_color(GREEN),
            dot2.animate.set_color(GREEN).shift(1.4 * direction),
        )
        scheme.remove(brace_text)
        brace_text = MathTex("D_{P}", color=WHITE).scale(0.8)
        brace.put_at_tip(brace_text)

        self.play(Write(brace_text))

        self.wait(0.7)

        brace.clear_updaters()
        self.play(
            FadeOut(scheme, brace_text, shift=0.5 * RIGHT),
            FadeOut(
                con_side,
                shift=0.5 * LEFT,
            ),
        )
        self.play(FadeIn(triplet_side))

        self.wait(0.8)

        # Triplet loss easy examples
        self.next_section(skip_animations=False)

        anchor = Dot(ORIGIN, color=WHITE).set_z_index(1)
        pos = Dot(1 * RIGHT + 0.6 * DOWN, color=GREEN).set_z_index(1)
        neg = Dot(2.25 * LEFT + 1.5 * UP, color=RED).set_z_index(1)

        margin_circle = Circle(
            radius=2, color=BLUE_C, fill_color=BLUE_C, fill_opacity=0.5
        ).move_to(anchor.get_center())
        margin_label = (
            MathTex(r"D(A, P) + m", color=BLUE_C)
            .next_to(margin_circle, DOWN, buff=0.1)
            .scale(0.8)
        )

        brace_pos = BraceBetweenPoints(anchor.get_center(), pos.get_center())
        brace_neg = BraceBetweenPoints(anchor.get_center(), neg.get_center())
        brace_pos_text = MathTex("D(A, P)", color=WHITE).scale(0.8)
        brace_neg_text = MathTex("D(A, N)", color=WHITE).scale(0.8)
        brace_pos.put_at_tip(brace_pos_text)
        brace_neg.put_at_tip(brace_neg_text)

        scheme = VGroup(
            anchor,
            pos,
            neg,
            margin_circle,
            margin_label,
            brace_pos,
            brace_neg,
            brace_pos_text,
            brace_neg_text,
        ).move_to(config.frame_width / 4 * LEFT)

        self.play(Create(anchor), Create(pos), Create(neg))
        self.play(Create(margin_circle), Write(margin_label))
        self.play(Create(brace_pos), Write(brace_pos_text))
        self.play(Create(brace_neg), Write(brace_neg_text))

        self.wait(0.7)

        hard_examples_txt = Text("Hard Examples").scale(0.8).to_edge(UP, buff=0.2)
        hard_examples_ul = Underline(hard_examples_txt)

        self.play(
            FadeOut(triplet_side, shift=0.5 * RIGHT),
            scheme.animate.move_to(ORIGIN),
            FadeOut(brace_pos_text, brace_neg_text, brace_pos, brace_neg),
        )

        self.play(GrowFromEdge(hard_examples_ul, UP), Write(hard_examples_txt))

        self.wait(0.6)

        # Hard examples
        self.next_section(skip_animations=False)

        self.play(FadeOut(hard_examples_txt, hard_examples_ul))

        self.wait(0.7)

        scheme = VGroup(
            anchor,
            pos,
            neg,
            margin_circle,
            margin_label,
        )

        dog_img = (
            ImageMobject("img/dog.jpg").scale_to_fit_width(3).next_to(scheme, RIGHT)
        )
        dog_img_rect = SurroundingRectangle(dog_img, color=WHITE, buff=0)
        cat_img_easy = (
            ImageMobject("img/cat_easy.jpg")
            .scale_to_fit_width(3)
            .next_to(scheme, LEFT)
        )
        cat_img_easy_rect = SurroundingRectangle(cat_img_easy, color=WHITE, buff=0)
        cat_img_hard = (
            ImageMobject("img/cat_hard.jpg")
            .scale_to_fit_width(3)
            .next_to(scheme, LEFT)
        )
        cat_img_hard_rect = SurroundingRectangle(cat_img_hard, color=WHITE, buff=0)

        line_dog = DashedLine(anchor.get_center(), dog_img_rect)
        line_cat_easy = DashedLine(neg.get_center(), cat_img_easy_rect)

        self.play(
            LaggedStart(
                Create(line_dog), FadeIn(dog_img, dog_img_rect), lag_ratio=0.8
            ),
            run_time=2,
        )

        self.play(
            LaggedStart(
                Create(line_cat_easy),
                FadeIn(cat_img_easy, cat_img_easy_rect),
                lag_ratio=0.6,
            ),
            run_time=1.5,
        )

        self.wait(0.7)

        direction = (anchor.get_center() - neg.get_center()) / np.linalg.norm(
            neg.get_center() - anchor.get_center()
        )

        self.play(
            FadeOut(line_cat_easy, cat_img_easy, cat_img_easy_rect),
            VGroup(neg).animate.shift(1.5 * direction),
        )

        line_cat_hard = DashedLine(neg.get_center(), cat_img_hard_rect)

        self.play(
            LaggedStart(
                Create(line_cat_hard),
                FadeIn(cat_img_hard, cat_img_hard_rect),
                lag_ratio=0.6,
            ),
            run_time=1.5,
        )

        self.wait(0.9)

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN))

        txt = Text("Hard example mining").scale(1.2)
        self.play(Write(txt))

        self.play(FadeOut(txt))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene3_1()
    scene.render()
