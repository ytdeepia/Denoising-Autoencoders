from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.elevenlabs import ElevenLabsService


class Scene4_3(VoiceoverScene):
    def construct(self):
        self.wait(1)

        # The data augmentation pipeline
        self.next_section(skip_animations=False)

        cat_img = ImageMobject("img/cat1.jpg").scale_to_fit_width(3)
        cat_crop_img = ImageMobject("img/cat_cropped.jpg").scale_to_fit_height(
            cat_img.height
        )
        cat_jitter_img = ImageMobject(
            "img/cat_cropped_jittered.jpg"
        ).scale_to_fit_height(cat_img.height)

        dog1_img = ImageMobject("img/dog1.jpg").scale_to_fit_width(3)
        dog1_crop_img = ImageMobject("img/dog1_cropped.jpg").scale_to_fit_height(
            dog1_img.height
        )
        dog1_jitter_img = ImageMobject(
            "img/dog1_cropped_jittered.jpg"
        ).scale_to_fit_height(dog1_img.height)

        dog2_img = ImageMobject("img/dog2.jpg").scale_to_fit_width(3)
        dog2_crop_img = ImageMobject("img/dog2_cropped.jpg").scale_to_fit_height(
            dog2_img.height
        )
        dog2_jitter_img = ImageMobject(
            "img/dog2_cropped_jittered.jpg"
        ).scale_to_fit_height(dog2_img.height)

        orig_txt = Text("Original Image").scale(0.8)
        crop_txt = Text("Random Crop").scale(0.8)
        jitter_txt = Text("Color Jitter").scale(0.8)

        cat_img = Group(cat_img, SurroundingRectangle(cat_img, buff=0.0, color=WHITE))
        cat_crop_img = Group(
            cat_crop_img, SurroundingRectangle(cat_crop_img, buff=0.0, color=WHITE)
        )
        cat_jitter_img = Group(
            cat_jitter_img,
            SurroundingRectangle(cat_jitter_img, buff=0.0, color=WHITE),
        )

        dog1_img = Group(
            dog1_img, SurroundingRectangle(dog1_img, buff=0.0, color=WHITE)
        )
        dog1_crop_img = Group(
            dog1_crop_img, SurroundingRectangle(dog1_crop_img, buff=0.0, color=WHITE)
        )
        dog1_jitter_img = Group(
            dog1_jitter_img,
            SurroundingRectangle(dog1_jitter_img, buff=0.0, color=WHITE),
        )

        dog2_img = Group(
            dog2_img, SurroundingRectangle(dog2_img, buff=0.0, color=WHITE)
        )
        dog2_crop_img = Group(
            dog2_crop_img, SurroundingRectangle(dog2_crop_img, buff=0.0, color=WHITE)
        )
        dog2_jitter_img = Group(
            dog2_jitter_img,
            SurroundingRectangle(dog2_jitter_img, buff=0.0, color=WHITE),
        )

        orig_txt.next_to(dog1_img, UP, buff=1.2).scale(0.8)
        orig_txt_ul = Underline(orig_txt, buff=0.1)

        self.play(FadeIn(dog1_img), FadeIn(orig_txt), FadeIn(orig_txt_ul))

        self.wait(0.8)

        self.play(Group(dog1_img, orig_txt, orig_txt_ul).animate.shift(4 * LEFT))

        arrow_dog1_1 = Arrow(
            start=dog1_img.get_right(), end=dog1_crop_img.get_left(), buff=0.2
        )
        crop_txt.next_to(dog1_crop_img, UP, buff=1.2).scale(0.8)
        crop_txt_ul = Underline(crop_txt, buff=0.1)

        self.play(GrowArrow(arrow_dog1_1))
        self.play(FadeIn(dog1_crop_img), FadeIn(crop_txt), FadeIn(crop_txt_ul))

        self.wait(1)

        dog1_jitter_img.shift(4 * RIGHT)
        arrow_dog1_2 = Arrow(
            start=dog1_crop_img.get_right(),
            end=dog1_jitter_img.get_left(),
            buff=0.2,
        )
        jitter_txt.next_to(dog1_jitter_img, UP, buff=1.2).scale(0.8)
        jitter_txt_ul = Underline(jitter_txt, buff=0.1)

        self.play(GrowArrow(arrow_dog1_2))
        self.play(
            FadeIn(dog1_jitter_img), FadeIn(jitter_txt), FadeIn(jitter_txt_ul)
        )

        self.wait(0.7)


        self.wait(0.6)

        self.play(Group(*self.mobjects).animate.scale(0.6).shift(2 * UP), run_time=0.8)

        cat_img.scale(0.6).next_to(dog1_img, DOWN, buff=1.2)
        cat_crop_img.scale(0.6).next_to(dog1_crop_img, DOWN, buff=1.2)
        cat_jitter_img.scale(0.6).next_to(dog1_jitter_img, DOWN, buff=1.2)
        arrow_cat_1 = Arrow(
            start=cat_img.get_right(), end=cat_crop_img.get_left(), buff=0.2
        )
        arrow_cat_2 = Arrow(
            start=cat_crop_img.get_right(), end=cat_jitter_img.get_left(), buff=0.2
        )

        dog2_img.scale(0.6).next_to(cat_img, DOWN, buff=1.2)
        dog2_crop_img.scale(0.6).next_to(cat_crop_img, DOWN, buff=1.2)
        dog2_jitter_img.scale(0.6).next_to(cat_jitter_img, DOWN, buff=1.2)

        arrow_dog2_1 = Arrow(
            start=dog2_img.get_right(), end=dog2_crop_img.get_left(), buff=0.2
        )
        arrow_dog2_2 = Arrow(
            start=dog2_crop_img.get_right(), end=dog2_jitter_img.get_left(), buff=0.2
        )

        self.play(
            FadeIn(
                cat_img,
                cat_crop_img,
                cat_jitter_img,
                arrow_cat_1,
                arrow_cat_2,
            )
        )

        self.wait(0.7)

        self.play(
            FadeIn(
                dog2_img, dog2_crop_img, dog2_jitter_img, arrow_dog2_1, arrow_dog2_2
            )
        )

        self.wait(2)

        arrows = VGroup(
            arrow_dog1_1,
            arrow_dog1_2,
            arrow_cat_1,
            arrow_cat_2,
            arrow_dog2_1,
            arrow_dog2_2,
        )
        self.play(
            FadeOut(
                orig_txt,
                orig_txt_ul,
                crop_txt,
                crop_txt_ul,
                jitter_txt,
                jitter_txt_ul,
                dog1_crop_img,
                dog2_img,
                dog2_crop_img,
                cat_img,
                cat_crop_img,
                arrows,
            ),
            dog1_img.animate.move_to(3 * LEFT),
            dog1_jitter_img.animate.move_to(LEFT),
            cat_jitter_img.animate.move_to(RIGHT),
            dog2_jitter_img.animate.move_to(3 * RIGHT),
        )

        pos_brace = Brace(
            Group(dog1_img, dog1_jitter_img), UP, buff=0.2, color=GREEN
        )
        pos_txt = pos_brace.get_text("Positive").set_color(GREEN).scale(0.8)
        neg_brace = Brace(
            Group(dog1_img, cat_jitter_img), DOWN, buff=0.2, color=RED
        )
        neg_txt = neg_brace.get_text("Negative").set_color(RED).scale(0.8)

        neg_brace2 = Brace(
            Group(dog1_img, dog2_jitter_img), DOWN, buff=1.2, color=RED
        )
        neg_txt2 = neg_brace2.get_text("Negative").set_color(RED).scale(0.8)

        self.play(
            GrowFromCenter(pos_brace),
            Write(pos_txt),
        )

        self.play(
            GrowFromCenter(neg_brace),
            Write(neg_txt),
        )

        self.play(
            GrowFromCenter(neg_brace2),
            Write(neg_txt2),
        )

        self.wait(0.8)

        self.play(FadeOut(*self.mobjects), run_time=0.7)

        # Batch size
        self.next_section(skip_animations=False)

        txt_usual = (
            Text("Usual Batch Size")
            .scale(0.8)
            .to_edge(UP, buff=1)
            .shift(config.frame_width * LEFT / 4)
        )
        txt_usual_ul = Underline(txt_usual, buff=0.1)
        txt_usual_nb = Tex("64 - 256").scale(0.8).next_to(txt_usual, DOWN)

        separating_line = DashedLine(
            start=config.frame_height / 2 * UP,
            end=config.frame_height / 2 * DOWN,
            color=WHITE,
        )

        txt_simclr = (
            Text("SimCLR Batch Size")
            .scale(0.8)
            .to_edge(UP, buff=1)
            .shift(config.frame_width * RIGHT / 4)
        )
        txt_simclr_ul = Underline(txt_simclr, buff=0.1)
        txt_simclr_nb = Tex("4096-8192").scale(0.8).next_to(txt_simclr, DOWN)

        batch_usual = VGroup()
        for i in range(16):
            line = VGroup()
            for j in range(16):
                square = Square(
                    side_length=0.2,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.8,
                    stroke_width=0,
                )
                line.add(square)
            line.arrange(RIGHT, buff=0.4)
            batch_usual.add(line)

        batch_usual.arrange(DOWN, buff=0.4).scale_to_fit_width(1).move_to(
            config.frame_width * LEFT / 4 + DOWN
        )

        self.play(FadeIn(txt_usual, txt_usual_ul, txt_usual_nb))
        self.play(LaggedStartMap(FadeIn, batch_usual))
        self.play(Create(separating_line))

        batch_simclr = VGroup()
        for i in range(64):
            line = VGroup()
            for j in range(64):
                square = Square(
                    color=BLUE, fill_color=BLUE, fill_opacity=0.8, stroke_width=0
                )
                line.add(square)
            line.arrange(RIGHT, buff=0.4)
            batch_simclr.add(line)

        batch_simclr.arrange(DOWN, buff=0.4).scale_to_fit_width(4).move_to(
            config.frame_width * RIGHT / 4 + DOWN
        )

        self.play(FadeIn(txt_simclr, txt_simclr_ul, txt_simclr_nb))
        self.play(LaggedStartMap(FadeIn, batch_simclr))

        self.play(FadeOut(*self.mobjects, shift=0.5 * RIGHT))

        self.wait(1)


if __name__ == "__main__":
    scene = Scene4_3()
    scene.render()
