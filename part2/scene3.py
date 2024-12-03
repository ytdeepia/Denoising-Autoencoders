from manim import *
from manim_voiceover import VoiceoverScene

import numpy as np


class Scene2_3(VoiceoverScene):
    def construct(self):
        self.wait(1)

        # Facenet
        self.next_section(skip_animations=False)

        title_triplet = Text("The Triplet Loss").scale(0.8)
        title_triplet_ul = Underline(title_triplet)

        paper = ImageMobject("img/facenet.jpg").scale(0.5)
        paper.shift((paper.height / 2 + config.frame_height / 2) * DOWN)
        self.add(paper)

        self.play(Write(title_triplet))
        self.play(GrowFromEdge(title_triplet_ul, LEFT))

        self.wait(0.6)

        self.play(
            VGroup(title_triplet, title_triplet_ul).animate.to_edge(UP, buff=0.2),
            paper.animate.move_to(ORIGIN),
        )

        self.wait(2)

        self.play(paper.animate.shift(3 * LEFT))

        txt = Text("30% less errors !").shift(3 * RIGHT)

        self.play(Write(txt))

        self.wait(0.8)


        self.play(FadeOut(paper, txt, shift=0.5 * RIGHT), run_time=0.8)

        # Triplet loss
        self.next_section(skip_animations=False)

        pos = Dot(ORIGIN, radius=0.1, color=GREEN)
        anchor = Dot(ORIGIN, radius=0.1, color=WHITE)
        neg = Dot(ORIGIN, radius=0.1, color=RED)

        VGroup(pos, anchor, neg).arrange(RIGHT, buff=2).move_to(ORIGIN)
        pos_label = Text("Positive", color=GREEN).scale(0.6).next_to(pos, DOWN)
        anchor_label = Text("Anchor", color=WHITE).scale(0.6).next_to(anchor, DOWN)
        neg_label = Text("Negative", color=RED).scale(0.6).next_to(neg, DOWN)

        self.play(
            LaggedStart(
                AnimationGroup(Create(pos), Write(pos_label)),
                AnimationGroup(Create(anchor), Write(anchor_label)),
                AnimationGroup(Create(neg), Write(neg_label)),
                lag_ratio=0.8,
            ),
            run_time=3,
        )

        self.wait(0.9)

        self.play(
            anchor_label.animate.move_to(DOWN),
            pos.animate.move_to(1.75 * LEFT + 0.95 * UP),
            neg.animate.move_to(3.25 * RIGHT + 2.25 * UP),
            FadeOut(pos_label, anchor_label, neg_label, shift=0.5 * DOWN),
            FadeOut(title_triplet, title_triplet_ul),
            run_time=2,
        )

        pos_label_s = (
            MathTex("P")
            .scale(0.6)
            .next_to(pos, (UP + LEFT), buff=0.1)
            .set_color(GREEN)
        )
        anchor_label_s = MathTex("A").scale(0.6).next_to(anchor, DOWN, buff=0.1)
        neg_label_s = (
            MathTex("N")
            .scale(0.6)
            .next_to(neg, (DOWN + RIGHT), buff=0.1)
            .set_color(RED)
        )

        self.play(FadeIn(pos_label_s), FadeIn(anchor_label_s), FadeIn(neg_label_s))

        anchor.set_z_index(1)
        pos.set_z_index(1)
        neg.set_z_index(1)

        dist_pos = np.linalg.norm(pos.get_center() - anchor.get_center())
        dist_neg = np.linalg.norm(neg.get_center() - anchor.get_center())
        circle_pos = Circle(radius=dist_pos, color=GREEN).move_to(
            anchor.get_center()
        )
        circle_pos = DashedVMobject(circle_pos, num_dashes=60, color=GREEN)
        circle_neg = Circle(radius=dist_neg, color=RED).move_to(anchor.get_center())
        circle_neg = DashedVMobject(circle_neg, num_dashes=60, color=RED)

        circle_neg.add_updater(
            lambda m: m.become(
                DashedVMobject(
                    Circle(
                        radius=np.linalg.norm(
                            neg.get_center() - anchor.get_center()
                        ),
                        color=RED,
                    ),
                    num_dashes=60,
                    color=RED,
                ).move_to(anchor.get_center())
            )
        )
        circle_pos.add_updater(
            lambda m: m.become(
                DashedVMobject(
                    Circle(
                        radius=np.linalg.norm(
                            pos.get_center() - anchor.get_center()
                        ),
                        color=GREEN,
                    ),
                    num_dashes=60,
                    color=GREEN,
                ).move_to(anchor.get_center())
            )
        )

        line_pos = DashedLine(
            pos.get_center(), anchor.get_center(), color=GRAY
        ).add_updater(
            lambda x: x.put_start_and_end_on(pos.get_center(), anchor.get_center())
        )
        line_neg = DashedLine(
            neg.get_center(), anchor.get_center(), color=GRAY
        ).add_updater(
            lambda x: x.put_start_and_end_on(neg.get_center(), anchor.get_center())
        )

        self.play(
            Create(circle_pos),
            Create(circle_neg),
            Create(line_pos),
            Create(line_neg),
        )

        brace_pos = BraceBetweenPoints(pos.get_center(), anchor.get_center())
        brace_pos_txt = MathTex(r"D(A, P)").scale(0.6)
        brace_pos.put_at_tip(brace_pos_txt, 0.2)
        brace_pos_txt.shift(0.25 * (RIGHT))

        brace_neg = BraceBetweenPoints(neg.get_center(), anchor.get_center())
        brace_neg_txt = MathTex(r"D(A, N)").scale(0.6)
        brace_neg.put_at_tip(brace_neg_txt, 0.2)
        brace_neg_txt.shift(0.25 * (RIGHT + UP))

        self.play(FadeIn(brace_pos, brace_pos_txt))
        self.play(FadeIn(brace_neg, brace_neg_txt))

        margin_dist = dist_pos + 0.8
        circle_margin = Circle(radius=margin_dist, color=BLUE).move_to(
            anchor.get_center()
        )
        circle_margin = DashedVMobject(circle_margin, num_dashes=60, color=BLUE)
        circle_margin.add_updater(
            lambda m: m.become(
                DashedVMobject(
                    Circle(
                        radius=np.linalg.norm(
                            pos.get_center() - anchor.get_center()
                        )
                        + 0.8,
                        color=BLUE,
                    ),
                    num_dashes=60,
                    color=BLUE,
                ).move_to(anchor.get_center())
            )
        )

        margin_label = (
            MathTex(r"D(A, P) + m", color=BLUE)
            .scale(0.6)
            .next_to(circle_margin, LEFT, buff=0.2)
        )

        self.play(Create(circle_margin))
        self.play(
            Write(margin_label),
        )

        self.wait(0.9)


        neg_dir = (neg.get_center() - anchor.get_center()) / np.linalg.norm(
            neg.get_center() - anchor.get_center()
        )
        pos_dir = (pos.get_center() - anchor.get_center()) / np.linalg.norm(
            pos.get_center() - anchor.get_center()
        )

        self.play(
            FadeOut(brace_neg_txt, brace_pos_txt, brace_pos, brace_neg, margin_label),
            VGroup(pos, pos_label_s).animate.shift(0.5 * pos_dir),
            VGroup(neg, neg_label_s).animate.shift(-2.5 * neg_dir),
            run_time=2,
        )

        self.wait(5)
        arrowpos = Arrow(pos.get_center(), anchor.get_center(), buff=0)
        arrowneg = Arrow(anchor.get_center(), neg.get_center(), buff=0)

        self.play(GrowArrow(arrowpos))
        self.play(FadeOut(arrowpos))
        self.play(GrowArrow(arrowneg))
        self.play(FadeOut(arrowneg))
        self.play(GrowArrow(arrowpos))
        self.play(FadeOut(arrowpos))
        self.play(GrowArrow(arrowneg))
        self.play(FadeOut(arrowneg))

        scheme = VGroup(
            circle_pos,
            circle_neg,
            circle_margin,
            line_pos,
            line_neg,
            anchor,
            pos,
            neg,
            pos_label_s,
            anchor_label_s,
            neg_label_s,
        )

        condition = MathTex(r"D(A, P) + m < D(A, N)").scale(0.8).shift(3 * RIGHT)

        loss = (
            MathTex(r"\mathcal{L} = D(A, P) + m - D(A, N)").scale(0.8).shift(3 * RIGHT)
        )

        self.play(scheme.animate.scale(0.6).shift(4 * LEFT))

        self.play(Write(condition))

        self.wait(0.7)

        self.play(condition.animate.shift(2 * UP), Write(loss))

        self.wait(0.8)

        loss_2 = (
            MathTex(r"\mathcal{L} = \max(0, D(A, P) - D(A, N) + m)")
            .scale(0.8)
            .move_to(loss.get_center())
        )

        self.wait(4)
        self.play(Transform(loss, loss_2))

        self.wait(0.8)

        title = Text("Triplet Loss").to_edge(UP)
        title_ul = Underline(title)

        line_neg.clear_updaters()
        line_pos.clear_updaters()
        circle_neg.clear_updaters()
        circle_pos.clear_updaters()
        circle_margin.clear_updaters()

        self.play(FadeOut(scheme), FadeOut(condition), loss.animate.move_to(ORIGIN))
        self.play(GrowFromEdge(title_ul, LEFT), Write(title))

        self.wait(0.7)

        self.play(FadeOut(*self.mobjects, shift=0.5 * DOWN))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene2_3()
    scene.render()
