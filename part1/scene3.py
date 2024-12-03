from manim import *
from manim_voiceover import VoiceoverScene


class Scene1_3(VoiceoverScene):
    def construct(self):

        self.wait(1)

        # Labels are expensive
        self.next_section(skip_animations=False)

        txt = Text("Why use self-supervised learning?").scale(0.9)

        self.play(Write(txt))
        self.play(
            ShowPassingFlash(
                SurroundingRectangle(txt, buff=0.2, color=WHITE), time_width=0.4
            ),
            run_time=1.5,
        )

        self.play(FadeOut(txt), run_time=0.9)

        dataset = Table(
            [
                ["1", "Male", "25", "5.8", "Engineer"],
                ["2", "Female", "30", "5.5", "Doctor"],
                ["3", "Male", "22", "6.0", "Student"],
                ["4", "Female", "28", "5.7", "Scientist"],
            ],
            col_labels=[
                Text("ID"),
                Text("Gender"),
                Text("Age"),
                Text("Height"),
                Text("Occupation"),
            ],
        ).scale(0.5)

        dataset_title = (
            Text("Labeled Dataset").scale(0.8).next_to(dataset, UP, buff=1.5)
        )
        dataset_title_ul = Underline(dataset_title)

        self.play(FadeIn(dataset))
        self.play(Write(dataset_title), GrowFromEdge(dataset_title_ul, LEFT))

        self.play(
            FadeOut(dataset, dataset_title, dataset_title_ul, shift=DOWN), run_time=0.8
        )

        img1 = ImageMobject("img/cat1.jpg").scale_to_fit_width(2)
        img1_rect = SurroundingRectangle(img1, buff=0, color=WHITE, stroke_width=2)
        img2 = ImageMobject("img/cat2.jpg").scale_to_fit_width(2)
        img2_rect = SurroundingRectangle(img2, buff=0, color=WHITE, stroke_width=2)
        img3 = ImageMobject("img/dog.png").scale_to_fit_width(2)
        img3_rect = SurroundingRectangle(img3, buff=0, color=WHITE, stroke_width=2)
        img4 = ImageMobject("img/cat3.jpg").scale_to_fit_width(2)
        img4_rect = SurroundingRectangle(img4, buff=0, color=WHITE, stroke_width=2)

        dog_title = (
            Text("Dog")
            .scale(0.8)
            .to_edge(UP, buff=1)
            .shift(config.frame_width / 3 * LEFT)
        )
        dog_title_ul = Underline(dog_title)

        cat_title = (
            Text("Cat")
            .scale(0.8)
            .to_edge(UP, buff=1)
            .shift(config.frame_width / 3 * RIGHT)
        )
        cat_title_ul = Underline(cat_title)
        line1 = DashedLine(
            start=(-config.frame_width / 6, config.frame_height / 2, 0),
            end=(-config.frame_width / 6, -config.frame_height / 2, 0),
            color=WHITE,
        )

        line2 = DashedLine(
            start=(config.frame_width / 6, config.frame_height / 2, 0),
            end=(config.frame_width / 6, -config.frame_height / 2, 0),
            color=WHITE,
        )

        self.play(Create(line1), Create(line2), run_time=2)
        self.play(FadeIn(dog_title, dog_title_ul), FadeIn(cat_title, cat_title_ul))

        Group(img1, img1_rect).shift((config.frame_height / 2 + img1.height) * UP)
        self.add(Group(img1, img1_rect))

        self.play(Group(img1, img1_rect).animate.move_to(ORIGIN))
        self.play(
            Group(img1, img1_rect).animate.shift(config.frame_width / 3 * RIGHT)
        )

        Group(img2, img2_rect).shift((config.frame_height / 2 + img2.height) * UP)
        self.add(Group(img2, img2_rect))
        self.play(Group(img2, img2_rect).animate.move_to(ORIGIN))
        self.play(
            Group(img1, img1_rect).animate.shift(2 * DOWN),
            Group(img2, img2_rect).animate.shift(config.frame_width / 3 * RIGHT),
        )

        Group(img3, img3_rect).shift((config.frame_height / 2 + img3.height) * UP)
        self.add(Group(img3, img3_rect))
        self.play(Group(img3, img3_rect).animate.move_to(ORIGIN))
        self.play(
            Group(img3, img3_rect).animate.shift(config.frame_width / 3 * LEFT),
        )

        self.play(FadeOut(*self.mobjects, shift=0.5 * RIGHT), run_time=0.9)

        # General learnt representations
        self.next_section(skip_animations=False)

        l1 = VGroup()
        l2 = VGroup()
        for i in range(3):
            l1.add(Circle(color=WHITE, radius=0.25))
            l2.add(Circle(color=WHITE, radius=0.25))

        l1.arrange(direction=DOWN, buff=0.5)
        l2.arrange(direction=DOWN, buff=0.5)
        l2.next_to(l1, RIGHT, buff=1.5)

        lines = VGroup()
        for c1 in l1:
            for c2 in l2:
                lines.add(Line(c1, c2))

        VGroup(l1, l2, lines).scale(0.7).move_to(ORIGIN)

        alg_txt = (
            Text("Backbone", color=WHITE)
            .scale(0.8)
            .next_to(VGroup(l1, l2, lines), direction=UP)
        )

        ml_alg = VGroup(l1, l2, lines, alg_txt)
        ml_alg_rect = SurroundingRectangle(
            ml_alg, buff=0.2, color=WHITE, corner_radius=0.1
        )
        VGroup(ml_alg, ml_alg_rect).scale(0.8)

        self.play(FadeIn(ml_alg), Create(ml_alg_rect))

        training_task = (
            Text("Segmentation", color=BLUE)
            .scale(0.5)
            .next_to(ml_alg_rect, DOWN, buff=0.8)
        )
        training_rect = DashedVMobject(
            SurroundingRectangle(
                VGroup(ml_alg, ml_alg_rect, training_task), color=BLUE, buff=0.5
            ),
            num_dashes=60,
        )
        training = (
            Text("Training", color=BLUE)
            .scale(0.6)
            .next_to(training_rect, UP, buff=0.6)
        )

        self.play(
            Create(training_rect), Write(training), Write(training_task), run_time=1
        )

        self.wait(0.6)


        self.play(
            VGroup(
                ml_alg, ml_alg_rect, training_task, training, training_rect
            ).animate.shift(3 * LEFT),
            run_time=0.8,
        )

        restoration = Text("Restoration", color=GREEN).scale(0.6)
        restoration_rect = SurroundingRectangle(
            restoration, color=GREEN, buff=0.2, corner_radius=0.1
        )

        inference_rect = training_rect.copy()
        inference_rect.set_color(RED).shift(6 * RIGHT)
        inference = (
            Text("Inference", color=RED)
            .scale(0.6)
            .next_to(inference_rect, UP, buff=0.6)
        )
        VGroup(restoration, restoration_rect).move_to(inference_rect)

        arrow = Arrow(
            start=training_rect.get_right(),
            end=inference_rect.get_left(),
            color=WHITE,
        )

        self.play(GrowArrow(arrow))
        self.play(
            Create(inference_rect), FadeIn(inference, restoration, restoration_rect)
        )

        self.wait(0.8)


        cross = Cross(arrow, color=RED)
        self.play(Create(cross))
        self.wait(2)
        self.play(FadeOut(arrow, cross, shift=0.5 * DOWN), run_time=0.8)

        self.wait(0.7)

        training_task_2 = (
            Text("Pretext Task", color=WHITE).scale(0.5).move_to(training_task)
        )

        self.play(
            Transform(training_task, training_task_2),
            training_rect.animate.set_color(WHITE),
            training.animate.set_color(WHITE),
            run_time=2,
        )

        classification = (
            Text("Classification", color=ORANGE)
            .scale(0.6)
            .next_to(training_rect, DOWN, buff=0.8)
        )
        classification_rect = SurroundingRectangle(
            classification, color=ORANGE, buff=0.2, corner_radius=0.1
        )
        segmentation = (
            Text("Segmentation", color=BLUE)
            .scale(0.6)
            .next_to(classification_rect, DOWN, buff=0.8)
        )
        segmentation_rect = SurroundingRectangle(
            segmentation, color=BLUE, buff=0.2, corner_radius=0.1
        )
        detection = (
            Text("Detection", color=TEAL)
            .scale(0.6)
            .next_to(segmentation_rect, DOWN, buff=0.8)
        )
        detection_rect = SurroundingRectangle(
            detection, color=TEAL, buff=0.2, corner_radius=0.1
        )

        self.wait(0.7)

        self.play(FadeOut(inference, inference_rect, restoration, restoration_rect))

        VGroup(
            VGroup(classification, classification_rect),
            VGroup(segmentation, segmentation_rect),
            VGroup(detection, detection_rect),
            VGroup(restoration, restoration_rect),
        ).arrange(direction=DOWN, buff=0.5).move_to(inference_rect)

        self.play(
            LaggedStart(
                FadeIn(classification, classification_rect, shift=0.5 * DOWN),
                FadeIn(segmentation, segmentation_rect, shift=0.5 * DOWN),
                FadeIn(detection, detection_rect, shift=0.5 * DOWN),
                FadeIn(restoration, restoration_rect, shift=0.5 * DOWN),
                lag_ratio=0.5,
            ),
            run_time=4,
        )

        self.wait(0.5)

        self.play(FadeOut(*self.mobjects), run_time=1)

        self.wait(1)


if __name__ == "__main__":
    scene = Scene1_3()
    scene.render()
