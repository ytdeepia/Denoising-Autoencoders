from manim import *
from manim_voiceover import VoiceoverScene


class Scene5_1(VoiceoverScene):
    def construct(self):

        self.wait(1)

        txt = Text("Let's wrap up!")
        self.play(Write(txt))
        self.wait(1)
        self.play(FadeOut(txt, shift=0.5 * RIGHT))

        supervised_txt = Tex(r"Supervised \\Learning", color=WHITE).scale(0.8)
        supervised_txt.add(
            SurroundingRectangle(supervised_txt, color=WHITE, corner_radius=0.1)
        )
        unsupervised_txt = Tex(r"Unsupervised \\Learning").scale(0.8)
        unsupervised_txt.add(
            SurroundingRectangle(unsupervised_txt, color=WHITE, corner_radius=0.1)
        )
        selfsupervised_txt = Tex(r"Self-Supervised \\Learning").scale(0.8)
        selfsupervised_txt.add(
            SurroundingRectangle(selfsupervised_txt, color=BLUE, corner_radius=0.1)
        )

        VGroup(supervised_txt, selfsupervised_txt, unsupervised_txt).arrange(
            RIGHT, buff=1
        ).move_to(ORIGIN)

        self.play(FadeIn(supervised_txt))
        self.play(FadeIn(selfsupervised_txt))
        self.play(FadeIn(unsupervised_txt))

        self.play(
            VGroup(
                supervised_txt,
                selfsupervised_txt,
                unsupervised_txt,
            ).animate.shift(UP * 2),
            run_time=0.8,
        )


        contrastive_txt = Tex(r"Contrastive\\Learning").scale(0.6)
        contrastive_txt.add(
            SurroundingRectangle(contrastive_txt, color=BLUE, corner_radius=0.1)
        )
        denoising_txt = Tex(r"Denoising").scale(0.6)
        denoising_txt.add(
            SurroundingRectangle(denoising_txt, color=WHITE, corner_radius=0.1)
        )
        masking_txt = Tex(r"Masking").scale(0.6)
        masking_txt.add(
            SurroundingRectangle(masking_txt, color=WHITE, corner_radius=0.1)
        )
        selfdistillation_txt = Tex(r"Self-Distillation").scale(0.6)
        selfdistillation_txt.add(
            SurroundingRectangle(
                selfdistillation_txt, color=WHITE, corner_radius=0.1
            )
        )

        VGroup(contrastive_txt, denoising_txt).arrange(RIGHT, buff=0.7)
        VGroup(masking_txt, selfdistillation_txt).arrange(RIGHT, buff=0.7).next_to(
            VGroup(contrastive_txt, denoising_txt), DOWN, buff=0.7
        )

        VGroup(
            contrastive_txt, denoising_txt, masking_txt, selfdistillation_txt
        ).next_to(
            VGroup(selfsupervised_txt, supervised_txt, unsupervised_txt), DOWN, 2
        )

        arrow1 = Arrow(
            selfsupervised_txt.get_bottom(),
            selfsupervised_txt.get_bottom() + DOWN * 1.5,
        )

        self.play(GrowArrow(arrow1))
        self.play(
            LaggedStart(
                FadeIn(contrastive_txt),
                FadeIn(denoising_txt),
                FadeIn(masking_txt),
                FadeIn(selfdistillation_txt),
                lag_ratio=0.5,
            ),
            run_time=3,
        )

        self.wait(1)

        techs = VGroup(
            supervised_txt,
            unsupervised_txt,
            selfsupervised_txt,
            denoising_txt,
            masking_txt,
            selfdistillation_txt,
            arrow1,
        )

        self.play(FadeOut(techs), contrastive_txt.animate.move_to(3 * UP))

        anchor = Dot(color=GRAY)
        anchor_label = Tex(r"A").scale(0.6).next_to(anchor, RIGHT)
        pos = Dot(color=GREEN).shift(1.5 * RIGHT + 0.7 * DOWN)
        pos_label = Tex(r"P").scale(0.6).next_to(pos, DOWN)
        neg = Dot(color=RED).shift(0.5 * LEFT + 1.2 * UP)
        neg_label = Tex(r"N").scale(0.6).next_to(neg, DOWN)

        brace_pos = BraceBetweenPoints(anchor.get_center(), pos.get_center())
        brace_pos_label = MathTex(r"D(A, P)", color=GREEN).scale(0.6)
        brace_pos.put_at_tip(brace_pos_label)
        brace_neg = BraceBetweenPoints(anchor.get_center(), neg.get_center())
        brace_neg_label = MathTex(r"D(A, N)", color=RED).scale(0.6)
        brace_neg.put_at_tip(brace_neg_label)

        scheme = VGroup(
            anchor,
            pos,
            neg,
            anchor_label,
            pos_label,
            neg_label,
            brace_pos,
            brace_neg,
            brace_pos_label,
            brace_neg_label,
        )

        scheme.next_to(contrastive_txt, DOWN, buff=1)

        triplet_loss = (
            MathTex(r"\mathcal{L} = \max (0, m + D(A, P) - D(A, N))")
            .scale(0.6)
            .next_to(scheme, DOWN, buff=1)
        )
        triplet_loss_rect = SurroundingRectangle(
            triplet_loss, color=WHITE, buff=0.2
        )

        self.play(FadeIn(triplet_loss))
        self.play(Create(triplet_loss_rect))
        self.play(FadeIn(anchor, anchor_label, pos, pos_label, neg, neg_label))
        self.play(GrowFromCenter(brace_pos), FadeIn(brace_pos_label))
        self.play(GrowFromCenter(brace_neg), FadeIn(brace_neg_label))

        self.wait(0.8)


        simclr = Tex(r"SimCLR").scale(0.6)
        simclr.add(SurroundingRectangle(simclr, color=BLUE, corner_radius=0.1))
        simclr.next_to(
            contrastive_txt,
            DOWN,
            buff=2,
        )
        arrow = Arrow(contrastive_txt.get_bottom(), simclr.get_top())

        self.play(FadeOut(scheme, triplet_loss, triplet_loss_rect))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(simclr))
        txt_batch_size = (
            Text("Huge Batch Sizes!").scale(0.8).next_to(simclr, DOWN, buff=1)
        )

        self.wait(0.7)

        self.play(Write(txt_batch_size))
        selfdistillation_txt.move_to(contrastive_txt)

        self.wait(0.8)

        self.play(
            FadeOut(
                simclr, arrow, txt_batch_size, contrastive_txt, shift=0.5 * DOWN
            )
        )

        txt_byol = (
            Text("Bootstrap Your Own Latent")
            .scale(0.8)
            .next_to(selfdistillation_txt, DOWN, buff=3)
        )
        txt_byol_ul = Underline(txt_byol)

        arrow = Arrow(selfdistillation_txt.get_bottom(), txt_byol.get_top())
        self.play(FadeIn(selfdistillation_txt))
        self.play(GrowArrow(arrow))
        self.play(Write(txt_byol), GrowFromEdge(txt_byol_ul, LEFT))

        self.play(FadeOut(*self.mobjects), run_time=1)

        thanks_txt = Text("Thanks for watching!").scale(1.2).shift(2 * UP)
        self.play(FadeIn(thanks_txt))

        self.wait(0.6)

        self.play(FadeOut(thanks_txt))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene5_1()
    scene.render()
