from manim import *
from manim_voiceover import VoiceoverScene


class Scene4_4(VoiceoverScene):
    def construct(self):
        
        num_params = [100, 200, 350]
        sup_top1_acc = [75, 77, 79]
        sup_labels = ["R50", "R50 (2x)", "R50 (4x)"]

        simclr_top1_acc = [70, 73, 75]
        simclr_labels = ["R50", "R50 (2x)", "R50 (4x)"]

        fine_tune_top1_acc = [75.5, 83, 85.8]
        fine_tune_labels = ["R50", "R50 (2x)", "R50 (4x)"]

        axes1 = Axes(
            x_range=[0, 450, 50],
            y_range=[0, 100, 10],
            x_length=5,
            y_length=5,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 24,
            },
            tips=False,
        )

        x_label = Text("Parameters (M)", font_size=24)
        x_label.next_to(axes1.x_axis, DOWN, buff=0.5)

        y_label = Text("Top 1 accuracy (%)", font_size=24)
        y_label.rotate(PI / 2)
        y_label.next_to(axes1.y_axis, LEFT, buff=0.5)

        dots_simclr = [
            Dot(axes1.c2p(num_params[i], simclr_top1_acc[i]), color=BLUE)
            for i in range(3)
        ]
        dots_sup = [
            Dot(axes1.c2p(num_params[i], sup_top1_acc[i]), color=RED) for i in range(3)
        ]
        dots_fine_tune = [
            Dot(axes1.c2p(num_params[i], fine_tune_top1_acc[i]), color=GREEN)
            for i in range(3)
        ]

        labels_sup = VGroup()
        for i, dot in enumerate(dots_sup):
            label = Text(sup_labels[i], font_size=20, color=RED)
            label.next_to(dot, UP + RIGHT, buff=0.1)
            labels_sup.add(label)

        labels_simclr = VGroup()
        for i, dot in enumerate(dots_simclr):
            label = Text(simclr_labels[i], font_size=20, color=BLUE)
            label.next_to(dot, DOWN + RIGHT, buff=0.1)
            labels_simclr.add(label)

        labels_fine_tune = VGroup()
        for i, dot in enumerate(dots_fine_tune):
            label = Text(fine_tune_labels[i], font_size=20, color=GREEN)
            label.next_to(dot, UP + LEFT, buff=0.1)
            labels_fine_tune.add(label)

        legend2 = VGroup()

        sup_legend_dot = Dot(color=RED, radius=0.1)
        sup_legend_label = Text("Supervised Models", font_size=20, color=WHITE).next_to(
            sup_legend_dot, RIGHT, buff=0.2
        )
        sup_legend = VGroup(sup_legend_dot, sup_legend_label)

        simclr_legend_dot = Dot(color=BLUE, radius=0.1)
        simclr_legend_label = Text("SimCLR", font_size=20, color=WHITE).next_to(
            simclr_legend_dot, RIGHT, buff=0.2
        )
        simclr_legend = VGroup(simclr_legend_dot, simclr_legend_label)

        fine_tune_legend = VGroup()
        fine_tune_legend_dot = Dot(color=GREEN, radius=0.1)
        fine_tune_legend_label = Text(
            "Fine-tuning \n on 1% of the labels", font_size=20, color=WHITE
        ).next_to(fine_tune_legend_dot, RIGHT, buff=0.2)
        fine_tune_legend = VGroup(fine_tune_legend_dot, fine_tune_legend_label)

        legend2.add(sup_legend, simclr_legend, fine_tune_legend).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        )
        legend2.add(SurroundingRectangle(legend2, buff=0.2, color=WHITE))
        legend2.next_to(axes1, RIGHT, buff=1)

        title_axes1 = Text("Linear Evaluation on ImageNet", font_size=24).next_to(
            axes1, UP, buff=1
        )
        title_axes1_ul = Underline(title_axes1, buff=0.1)

        plot1 = VGroup(
            axes1,
            x_label,
            y_label,
            *dots_simclr,
            *dots_sup,
            *dots_fine_tune,
            labels_simclr,
            labels_sup,
            labels_fine_tune,
            legend2,
            title_axes1,
            title_axes1_ul
        ).scale(0.9)

        # Animate the Plot

        self.play(
            Create(axes1),
            FadeIn(legend2),
            FadeIn(title_axes1, title_axes1_ul),
            run_time=2,
        )
        self.play(Write(x_label), Write(y_label), run_time=1)

        self.wait(0.7)

        self.play(
            LaggedStart(
                FadeIn(
                    dots_simclr[0], dots_sup[0], labels_sup[0], labels_simclr[0]
                ),
                FadeIn(
                    dots_simclr[1], dots_sup[1], labels_sup[1], labels_simclr[1]
                ),
                FadeIn(
                    dots_simclr[2], dots_sup[2], labels_sup[2], labels_simclr[2]
                ),
                lag_ratio=0.5,
            ),
            run_time=3,
        )

        self.wait(0.7)

        # Imagenet classification with Fine-tuning
        self.next_section(skip_animations=False)

        self.play(
            LaggedStart(
                FadeIn(dots_fine_tune[0], labels_fine_tune[0]),
                FadeIn(dots_fine_tune[1], labels_fine_tune[1]),
                FadeIn(dots_fine_tune[2], labels_fine_tune[2]),
                lag_ratio=0.5,
            ),
            run_time=3,
        )

        self.wait(0.7)


        self.play(
            plot1.animate.scale(0.8).to_edge(LEFT), FadeOut(legend2), run_time=0.7
        )

        # Batch size impact
        self.next_section(skip_animations=False)

        training_epochs = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        batch_sizes = [256, 512, 1024, 2048, 4096, 8192]

        top1_acc_data = {
            256: [58.0, 60.5, 62.0, 63.0, 64.0, 65.0, 65.5, 66.0, 66.5, 67.0],
            512: [60.0, 62.0, 64.0, 65.0, 66.0, 66.5, 67.0, 67.5, 68.0, 68.5],
            1024: [61.0, 63.5, 65.5, 66.5, 67.5, 68.0, 68.5, 69.0, 69.5, 70.0],
            2048: [62.5, 65.0, 67.0, 68.0, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5],
            4096: [63.5, 66.0, 68.0, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0],
            8192: [64.0, 66.5, 68.5, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5],
        }

        colors = [BLUE, TEAL, GREEN, ORANGE, PINK, PURPLE]

        # Axes
        axes2 = Axes(
            x_range=[0, 1000, 100],
            y_range=[50, 73, 5],
            x_length=8,
            y_length=5,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 24},
            tips=False,
        )

        x_label = Text("Training epochs", font_size=24)
        x_label.next_to(axes2.x_axis, DOWN, buff=0.5)

        y_label = Text("Top 1 accuracy (%)", font_size=24)
        y_label.rotate(PI / 2)
        y_label.next_to(axes2.y_axis, LEFT, buff=0.5)

        bars = VGroup()
        for i, epoch in enumerate(training_epochs):
            for j, batch_size in enumerate(batch_sizes):
                top1_acc = top1_acc_data[batch_size][i]
                height = axes2.c2p(0, top1_acc)[1] - axes2.c2p(0, 50)[1]
                bar = Rectangle(
                    height=height,
                    width=0.08,
                    color=colors[j],
                    fill_opacity=0.8,
                )
                bar.move_to(axes2.c2p((i + 1) * 100 + j * 10 - 25, 50)).shift(
                    height / 2 * UP
                )
                bars.add(bar)

        legend_items = VGroup()
        legend_items.add(Text("Batch size", font_size=20, color=WHITE))
        for j, batch_size in enumerate(batch_sizes):
            dot = Dot(color=colors[j])
            label = Text(str(batch_size), font_size=20, color=WHITE)
            label.next_to(dot, RIGHT, buff=0.2)
            legend_item = VGroup(dot, label)
            legend_items.add(legend_item)

        legend2 = VGroup(*legend_items).arrange(DOWN).next_to(axes2, RIGHT, buff=0.5)
        legend2.add(
            SurroundingRectangle(legend2, color=WHITE, stroke_width=2, buff=0.15)
        )

        title = Text("Influence of the batch size", font_size=28).next_to(
            axes2, UP, buff=1
        )
        title_ul = Underline(title, buff=0.1)
        plot2 = (
            VGroup(axes2, bars, x_label, y_label, legend2, title, title_ul)
            .scale(0.7)
            .to_edge(RIGHT)
        )

        self.play(
            Create(axes2), FadeIn(legend2), FadeIn(title, title_ul), run_time=2
        )
        self.play(Write(x_label), Write(y_label), run_time=1)
        self.play(LaggedStartMap(FadeIn, bars), run_time=3)

        self.wait(0.8)

        self.play(FadeOut(*self.mobjects), run_time=1)

        self.wait(1)


if __name__ == "__main__":
    scene = Scene4_4()
    scene.render()
